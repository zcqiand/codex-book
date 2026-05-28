# 从第 31 章提取
# 来源：Codex 从入门到项目实践

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Inventory, Product

router = APIRouter(prefix="/api/inventory", tags=["inventory"])

@router.get("/")
def list_inventory(
    low_stock_only: bool = False,
    db: Session = Depends(get_db),
):
    """库存列表：可选筛选低库存商品。"""
    q = db.query(Inventory, Product.name, Product.sku).join(
        Product, Inventory.product_id == Product.id
    ).filter(Product.is_deleted == 0)

    result = []
    for inv, name, sku in q.all():
        available = inv.current_quantity - inv.locked_quantity
        if low_stock_only and available >= inv.safety_threshold:
            continue
        result.append({
            "product_id": inv.product_id,
            "name": name,
            "sku": sku,
            "current_quantity": inv.current_quantity,
            "locked_quantity": inv.locked_quantity,
            "available_quantity": available,
            "safety_threshold": inv.safety_threshold,
            "is_low_stock": available < inv.safety_threshold,
        })
    return result

@router.patch("/{product_id}")
def adjust_inventory(
    product_id: int,
    delta: int,
    db: Session = Depends(get_db),
):
    """手动调整库存（盘点/补货用）。delta 可为正（入库）或负（出库）。"""
    if delta == 0:
        raise HTTPException(400, "调整量不能为 0")
    inv = db.query(Inventory).filter(
        Inventory.product_id == product_id
    ).with_for_update().first()
    if not inv:
        raise HTTPException(404, "库存记录不存在")

    new_qty = inv.current_quantity + delta
    if new_qty < 0:
        raise HTTPException(400, f"库存不足——当前 {inv.current_quantity}，无法扣减 {abs(delta)}")
    inv.current_quantity = new_qty
    db.commit()
    return {"product_id": product_id, "current_quantity": new_qty}