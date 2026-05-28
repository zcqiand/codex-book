# 从第 32 章提取
# 来源：Codex 从入门到项目实践

ALLOWED_SHIPMENT_TRANSITIONS = {
    "picking": {"packed"},
    "packed": {"in_transit"},
    "in_transit": {"delivered", "failed"},
    "delivered": set(),
    "failed": set(),
}

def advance_shipment(shipment, target: str, db, **kwargs):
    """推进发货子状态——校验合法性后更新状态和时间戳。"""
    if target not in ALLOWED_SHIPMENT_TRANSITIONS.get(shipment.status, set()):
        raise ValueError(
            f"非法发货状态转换: {shipment.status} → {target}。"
            f"允许的目标: {ALLOWED_SHIPMENT_TRANSITIONS.get(shipment.status, set())}"
        )
    shipment.status = target
    now = datetime.utcnow()
    if target == "packed":
        shipment.packed_at = now
    elif target == "in_transit":
        if not kwargs.get("tracking_number"):
            raise ValueError("进入运输状态必须提供物流单号")
        shipment.tracking_number = kwargs["tracking_number"]
        shipment.carrier = kwargs.get("carrier", "")
        shipment.shipped_at = now
    elif target == "delivered":
        shipment.delivered_at = now
        # 联动：更新订单状态为 completed
        from app.services.order_state import apply_transition
        apply_transition(shipment.order, "completed", db)
    db.commit()
    return shipment