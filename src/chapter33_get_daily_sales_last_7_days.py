# 从第 33 章提取
# 来源：Codex 从入门到项目实践

def get_daily_sales_last_7_days(db: Session) -> list[dict]:
    """查询近七日每日销售额——用于趋势图。"""
    results = []
    for i in range(6, -1, -1):
        day = datetime.utcnow().date() - timedelta(days=i)
        day_start = datetime(day.year, day.month, day.day)
        day_end = datetime(day.year, day.month, day.day, 23, 59, 59)

        total = db.query(func.sum(Order.total_amount)).filter(
            Order.status.in_(["paid", "shipped", "completed"]),
            Order.created_at >= day_start,
            Order.created_at <= day_end,
        ).scalar() or 0

        results.append({
            "date": day.strftime("%m-%d"),
            "amount": float(total),
        })
    return results


def get_low_stock_alerts(db: Session) -> list[dict]:
    """查询库存低于安全阈值的商品。"""
    alerts = db.query(Inventory, Product.name, Product.sku).join(
        Product, Inventory.product_id == Product.id
    ).filter(
        Product.is_deleted == 0,
        Inventory.current_quantity - Inventory.locked_quantity < Inventory.safety_threshold,
    ).all()

    return [{
        "product_id": inv.product_id,
        "name": name,
        "sku": sku,
        "available": inv.current_quantity - inv.locked_quantity,
        "threshold": inv.safety_threshold,
    } for inv, name, sku in alerts]