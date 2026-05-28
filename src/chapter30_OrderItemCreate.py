# 从第 30 章提取
# 来源：Codex 从入门到项目实践

from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import datetime
from typing import Optional, List

class OrderItemCreate(BaseModel):
    product_id: int = Field(..., gt=0, description="商品ID")
    quantity: int = Field(..., gt=0, le=9999, description="数量")

class OrderItemResponse(BaseModel):
    id: int
    product_id: int
    product_name: str = ""  # 关联查询填充
    quantity: int
    unit_price_snapshot: Decimal

    class Config:
        from_attributes = True

# ── 订单 ──
class OrderCreate(BaseModel):
    user_id: int = Field(..., gt=0, description="用户ID")
    address: str = Field(..., min_length=1, max_length=500, description="收货地址")
    items: List[OrderItemCreate] = Field(..., min_length=1, max_length=50)

class OrderStatusUpdate(BaseModel):
    status: str = Field(..., description="目标状态")

class OrderResponse(BaseModel):
    id: int
    order_no: str
    user_id: int
    status: str
    total_amount: Decimal
    address: str
    created_at: datetime
    items: List[OrderItemResponse] = []

    class Config:
        from_attributes = True

class OrderListResponse(BaseModel):
    total: int
    page: int
    page_size: int
    orders: List[OrderResponse]