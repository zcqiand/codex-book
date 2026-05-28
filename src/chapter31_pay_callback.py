# 从第 31 章提取
# 来源：Codex 从入门到项目实践

from sqlalchemy.orm import Session
from app.models import Order, Inventory

def pay_callback(order_id: int, db: Session) -> Order:
    """支付成功回调：已支付→实扣库存。幂等——重复调用不会重复扣减。"""
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise ValueError(f"订单 {order_id} 不存在")

    if order.status != "pending_payment":
        return order  # 已处理过，幂等返回

    for item in order.items:
        inv = db.query(Inventory).filter(
            Inventory.product_id == item.product_id
        ).with_for_update().first()

        if not inv or inv.locked_quantity < item.quantity:
            raise ValueError(f"商品 {item.product_id} 锁定库存不足——数据不一致")

        inv.locked_quantity -= item.quantity   # 释放锁定
        inv.current_quantity -= item.quantity  # 实际扣减

        if inv.current_quantity < inv.safety_threshold:
            _trigger_low_stock_alert(inv)

    order.status = "paid"
    db.commit()
    db.refresh(order)
    return order


def cancel_order(order_id: int, db: Session) -> Order:
    """取消订单：释放锁定库存。"""
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise ValueError(f"订单 {order_id} 不存在")

    if order.status == "cancelled":
        return order  # 幂等

    if order.status == "completed":
        raise ValueError("已完成订单不可取消")

    # 如果已支付（paid/shipped），释放当前库存（退款场景）
    already_paid = order.status in ("paid", "shipped")
    for item in order.items:
        inv = db.query(Inventory).filter(
            Inventory.product_id == item.product_id
        ).with_for_update().first()
        if inv:
            if already_paid:
                inv.current_quantity += item.quantity  # 退款回仓
            else:
                inv.locked_quantity = max(0, inv.locked_quantity - item.quantity)

    order.status = "cancelled"
    db.commit()
    db.refresh(order)
    return order


def _trigger_low_stock_alert(inv: Inventory):
    """库存低于安全阈值时打印告警（生产环境应接入通知系统）。"""
    print(f"[库存告警] 商品ID={inv.product_id} "
          f"当前库存={inv.current_quantity} "
          f"安全阈值={inv.safety_threshold}")