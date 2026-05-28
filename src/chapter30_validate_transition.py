# 从第 30 章提取
# 来源：Codex 从入门到项目实践

ALLOWED_TRANSITIONS = {
    "pending_payment": {"paid", "cancelled"},
    "paid": {"shipped", "cancelled"},
    "shipped": {"completed"},
    "completed": set(),       # 终态，不可转换
    "cancelled": set(),       # 终态，不可转换
}

def validate_transition(current: str, target: str) -> bool:
    """检查从 current 状态转换到 target 状态是否合法。"""
    if target not in ALLOWED_TRANSITIONS.get(current, set()):
        raise ValueError(
            f"非法状态转换: {current} → {target}。"
            f"允许的目标状态: {ALLOWED_TRANSITIONS.get(current, set())}"
        )
    return True

def apply_transition(order, target: str, db):
    """校验状态转换合法性，通过后更新订单状态并提交。"""
    validate_transition(order.status, target)
    order.status = target
    if target == "cancelled":
        from app.models import Inventory
        for item in order.items:
            inv = db.query(Inventory).filter(
                Inventory.product_id == item.product_id
            ).with_for_update().first()
            if inv:
                inv.locked_quantity = max(0, inv.locked_quantity - item.quantity)
    db.commit()
    db.refresh(order)
    return order