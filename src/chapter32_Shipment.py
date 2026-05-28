# 从第 32 章提取
# 来源：Codex 从入门到项目实践

class Shipment(Base):
    __tablename__ = 'shipments'
    __table_args__ = (
        CheckConstraint(
            "status IN ('picking','packed','in_transit','delivered','failed')",
            name='ck_shipment_status'
        ),
    )
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), unique=True, nullable=False)
    tracking_number = Column(String(50), default='')  # in_transit 后必填
    carrier = Column(String(50), default='')
    status = Column(String(20), default='picking')
    picked_at = Column(DateTime, nullable=True)       # 拣货完成时间
    packed_at = Column(DateTime, nullable=True)       # 打包出库时间
    shipped_at = Column(DateTime, nullable=True)       # 交付快递时间
    delivered_at = Column(DateTime, nullable=True)     # 签收时间

    order = relationship('Order', back_populates='shipment', uselist=False)