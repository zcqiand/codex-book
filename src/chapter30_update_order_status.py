# 从第 30 章提取
# 来源：Codex 从入门到项目实践

@router.patch("/{order_id}/status", response_model=OrderResponse)
def update_order_status(
    order_id: int,
    payload: OrderStatusUpdate,
    db: Session = Depends(get_db),
):
    """更新订单状态：校验状态转换合法性后执行。"""
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(404, "订单不存在")

    from app.services.order_state import apply_transition
    try:
        apply_transition(order, payload.status, db)
    except ValueError as e:
        raise HTTPException(400, str(e))

    return order