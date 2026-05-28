# 从第 32 章提取
# 来源：Codex 从入门到项目实践

router = APIRouter(prefix="/api/shipments", tags=["shipments"])

@router.post("/", status_code=201)
def create_shipment(order_id: int, db: Session = Depends(get_db)):
    """为已支付订单创建发货记录——进入 picking 状态。"""
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(404, "订单不存在")
    if order.status != "paid":
        raise HTTPException(400, f"订单状态为 {order.status}，只有已支付订单可发货")

    existing = db.query(Shipment).filter(Shipment.order_id == order_id).first()
    if existing:
        raise HTTPException(400, f"已有发货记录，当前状态: {existing.status}")

    shipment = Shipment(order_id=order_id, status="picking")
    db.add(shipment)
    # 订单状态进入 shipped 阶段
    from app.services.order_state import apply_transition
    apply_transition(order, "shipped", db)
    db.commit()
    db.refresh(shipment)
    return shipment

@router.patch("/{shipment_id}/advance")
def advance(shipment_id: int, target: str, tracking_number: str = "",
            carrier: str = "", db: Session = Depends(get_db)):
    """推进发货子状态到下一个阶段。"""
    shipment = db.query(Shipment).filter(Shipment.id == shipment_id).first()
    if not shipment:
        raise HTTPException(404, "发货记录不存在")
    try:
        advance_shipment(shipment, target, db,
                         tracking_number=tracking_number, carrier=carrier)
    except ValueError as e:
        raise HTTPException(400, str(e))
    return shipment