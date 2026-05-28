# 从第 30 章提取
# 来源：Codex 从入门到项目实践

@router.get("/", response_model=OrderListResponse)
def list_orders(
    status: str = Query(None, description="按状态筛选"),
    user_id: int = Query(None, description="按用户筛选"),
    date_from: str = Query(None, description="起始日期 YYYY-MM-DD"),
    date_to: str = Query(None, description="截止日期 YYYY-MM-DD"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    """订单列表：支持多条件组合筛选和分页。"""
    q = db.query(Order)
    if status:
        q = q.filter(Order.status == status)
    if user_id:
        q = q.filter(Order.user_id == user_id)
    if date_from:
        q = q.filter(Order.created_at >= f"{date_from} 00:00:00")
    if date_to:
        q = q.filter(Order.created_at <= f"{date_to} 23:59:59")

    total = q.count()
    orders = q.order_by(Order.created_at.desc()).offset(
        (page - 1) * page_size
    ).limit(page_size).all()

    return OrderListResponse(total=total, page=page, page_size=page_size, orders=orders)


@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    """订单详情：含订单明细和商品名称。"""
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(404, "订单不存在")
    return order