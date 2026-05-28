# 从第 34 章提取
# 来源：Codex 从入门到项目实践

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.models import User, Product, Inventory, Order, OrderItem
from app.services.order_state import apply_transition
from app.services.inventory import pay_callback, cancel_order
from decimal import Decimal

@pytest.fixture
def db():
    """创建测试专用数据库——每次测试前重建表结构。"""
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(username="testuser", email="test@example.com")
    session.add(user)
    product = Product(name="测试商品", sku="TST-001", unit_price=Decimal("99.00"))
    session.add(product)
    session.flush()
    inv = Inventory(product_id=product.id, current_quantity=100, safety_threshold=10)
    session.add(inv)
    session.commit()
    yield session
    session.close()

def create_test_order(db, status="pending_payment"):
    """辅助函数：创建一个含 2 件商品的测试订单。"""
    product = db.query(Product).first()
    inv = db.query(Inventory).filter(Inventory.product_id == product.id).first()
    inv.locked_quantity += 2
    order = Order(
        user_id=1,
        total_amount=Decimal("198.00"),
        status=status,
        address="测试地址",
    )
    db.add(order)
    db.flush()
    item = OrderItem(
        order_id=order.id,
        product_id=product.id,
        product_name=product.name,
        product_sku=product.sku,
        unit_price=product.unit_price,
        quantity=2,
    )
    db.add(item)
    db.commit()
    db.refresh(order)
    return order


class TestOrderStateMachine:
    """订单状态机——合法转换与非法拦截。"""

    def test_pending_payment_to_paid(self, db):
        """pending_payment → paid：支付回调触发实扣库存。"""
        order = create_test_order(db, "pending_payment")
        pay_callback(order.id, db)
        db.refresh(order)
        assert order.status == "paid"

    def test_paid_to_shipped(self, db):
        """paid → shipped：已支付订单可以发货。"""
        order = create_test_order(db, "paid")
        apply_transition(order, "shipped", db)
        assert order.status == "shipped"

    def test_pending_payment_to_shipped_rejected(self, db):
        """pending_payment → shipped：未支付不能直接发货。"""
        order = create_test_order(db, "pending_payment")
        with pytest.raises(ValueError, match="非法状态转换"):
            apply_transition(order, "shipped", db)

    def test_completed_to_cancelled_rejected(self, db):
        """completed → cancelled：已完成订单不可取消。"""
        order = create_test_order(db, "completed")
        with pytest.raises(ValueError):
            cancel_order(order.id, db)

    def test_pay_callback_idempotent(self, db):
        """支付回调幂等：重复调用不重复扣库存。"""
        order = create_test_order(db, "pending_payment")
        pay_callback(order.id, db)
        pay_callback(order.id, db)  # 第二次调用
        db.refresh(order)
        inv = db.query(Inventory).first()
        assert inv.current_quantity == 98
        assert inv.locked_quantity == 0


class TestInventoryLifecycle:
    """库存三段式：预占 → 实扣 → 释放。"""

    def test_order_creates_lock(self, db):
        """下单时锁定库存——locked_quantity 增加，current_quantity 不变。"""
        order = create_test_order(db, "pending_payment")
        inv = db.query(Inventory).first()
        assert inv.locked_quantity == 2
        assert inv.current_quantity == 100  # 实物未动

    def test_pay_reduces_both(self, db):
        """支付成功：locked_quantity 和 current_quantity 都减少。"""
        order = create_test_order(db, "pending_payment")
        pay_callback(order.id, db)
        inv = db.query(Inventory).first()
        assert inv.locked_quantity == 0
        assert inv.current_quantity == 98

    def test_cancel_before_pay_releases_lock(self, db):
        """支付前取消：只释放锁定，不退实货。"""
        order = create_test_order(db, "pending_payment")
        cancel_order(order.id, db)
        inv = db.query(Inventory).first()
        assert inv.locked_quantity == 0
        assert inv.current_quantity == 100  # 实物未动

    def test_cancel_after_pay_returns_stock(self, db):
        """支付后取消（退款）：实物退回仓库。"""
        order = create_test_order(db, "pending_payment")
        pay_callback(order.id, db)
        cancel_order(order.id, db)
        inv = db.query(Inventory).first()
        assert inv.current_quantity == 100  # 退回仓库
        assert inv.locked_quantity == 0


class TestShipmentSubStates:
    """发货子状态：picking → packed → in_transit → delivered。"""

    def test_full_shipment_lifecycle(self, db):
        """完整的发货子状态流转路径。"""
        from app.models import Shipment
        from app.services.shipment import advance_shipment

        order = create_test_order(db, "paid")
        shipment = Shipment(order_id=order.id, status="picking")
        db.add(shipment)
        db.commit()

        # picking → packed
        advance_shipment(shipment, "packed", db)
        assert shipment.status == "packed"
        assert shipment.packed_at is not None

        # packed → in_transit
        advance_shipment(shipment, "in_transit", db,
                         tracking_number="SF1234567890", carrier="顺丰")
        assert shipment.status == "in_transit"
        assert shipment.tracking_number == "SF1234567890"

        # in_transit → delivered（联动订单→completed）
        advance_shipment(shipment, "delivered", db)
        assert shipment.status == "delivered"
        db.refresh(order)
        assert order.status == "completed"

    def test_in_transit_without_tracking_rejected(self, db):
        """进入运输状态必须提供物流单号。"""
        from app.models import Shipment
        from app.services.shipment import advance_shipment

        order = create_test_order(db, "paid")
        shipment = Shipment(order_id=order.id, status="packed")
        db.add(shipment)
        db.commit()

        with pytest.raises(ValueError, match="必须提供物流单号"):
            advance_shipment(shipment, "in_transit", db)