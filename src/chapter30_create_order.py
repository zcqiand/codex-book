# 从第 30 章提取
# 来源：Codex 从入门到项目实践

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Order, OrderItem, Product, Inventory
from app.schemas import OrderCreate, OrderStatusUpdate, OrderResponse, OrderListResponse, OrderItemResponse
from decimal import Decimal
from datetime import datetime
import uuid

router = APIRouter(prefix="/api/orders", tags=["orders"])

@router.post("/", response_model=OrderResponse, status_code=201)
def create_order(payload: OrderCreate, db: Session = Depends(get_db)):
    """创建订单：校验商品状态 → 计算总金额 → 创建订单和明细 → 锁定库存。"""
    product_ids = [item.product_id for item in payload.items]
    products = db.query(Product).filter(
        Product.id.in_(product_ids),
        Product.is_deleted == 0
    ).all()
    if len(products) != len(set(product_ids)):
        raise HTTPException(400, "部分商品不存在或已下架")
    product_map = {p.id: p for p in products}

    total = Decimal("0")
    for item in payload.items:
        product = product_map[item.product_id]
        inventory = db.query(Inventory).filter(
            Inventory.product_id == item.product_id
        ).with_for_update().first()
        if not inventory or inventory.current_quantity - inventory.locked_quantity < item.quantity:
            raise HTTPException(400, f"商品 {product.name} 库存不足")
        total += product.unit_price * item.quantity
        inventory.locked_quantity += item.quantity

    order = Order(
        order_no=datetime.now().strftime("%Y%m%d%H%M%S") + uuid.uuid4().hex[:6].upper(),
        user_id=payload.user_id,
        status="pending_payment",
        total_amount=total,
        address=payload.address,
    )
    db.add(order)
    db.flush()  # 获取 order.id

    for item in payload.items:
        product = product_map[item.product_id]
        db.add(OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            unit_price_snapshot=product.unit_price,  # 快照
        ))

    db.commit()
    db.refresh(order)
    return order