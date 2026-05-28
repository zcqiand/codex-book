# 从第 33 章提取
# 来源：Codex 从入门到项目实践

from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Order, OrderItem, Inventory, Product
from datetime import datetime, timedelta

def compute_dashboard_metrics(db: Session) -> dict:
    """计算三个核心指标：GMV、客单价、库存周转率。"""
    now = datetime.utcnow()
    this_month_start = now.replace(day=1, hour=0, minute=0, second=0)

    # 1. GMV（Gross Merchandise Volume）：本月已完成订单的总销售额
    gmv = db.query(func.sum(Order.total_amount)).filter(
        Order.status.in_(["paid", "shipped", "completed"]),
        Order.created_at >= this_month_start,
    ).scalar() or 0

    completed_count = db.query(func.count(Order.id)).filter(
        Order.status.in_(["paid", "shipped", "completed"]),
        Order.created_at >= this_month_start,
    ).scalar() or 1
    avg_order_value = round(float(gmv) / completed_count, 2)

    sold_qty = db.query(func.sum(OrderItem.quantity)).join(
        Order, OrderItem.order_id == Order.id
    ).filter(
        Order.status.in_(["paid", "shipped", "completed"]),
        Order.created_at >= this_month_start,
    ).scalar() or 0

    avg_inventory = db.query(func.avg(Inventory.current_quantity)).scalar() or 1
    turnover_rate = round(float(sold_qty) / float(avg_inventory), 2)

    return {
        "gmv": float(gmv),
        "avg_order_value": avg_order_value,
        "inventory_turnover_rate": turnover_rate,
        "completed_orders": completed_count,
        "total_sold_quantity": int(sold_qty),
        "period": f"{this_month_start.strftime('%Y-%m-%d')} ~ {now.strftime('%Y-%m-%d')}",
    }