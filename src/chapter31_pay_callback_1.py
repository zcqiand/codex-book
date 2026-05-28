# 从第 31 章提取
# 来源：Codex 从入门到项目实践

# 在已有 orders.py 中添加以下两个端点：

@router.post("/{order_id}/pay-callback", response_model=OrderResponse)
def pay_callback(order_id: int, db: Session = Depends(get_db)):
    """模拟支付回调——实际项目中此端点由支付网关回调触发。"""
    from app.services.inventory import pay_callback as do_pay
    try:
        order = do_pay(order_id, db)
    except ValueError as e:
        raise HTTPException(400, str(e))
    return order

@router.post("/{order_id}/cancel", response_model=OrderResponse)
def cancel_order(order_id: int, db: Session = Depends(get_db)):
    """取消订单——释放已锁定或已扣减的库存。"""
    from app.services.inventory import cancel_order as do_cancel
    try:
        order = do_cancel(order_id, db)
    except ValueError as e:
        raise HTTPException(400, str(e))
    return order