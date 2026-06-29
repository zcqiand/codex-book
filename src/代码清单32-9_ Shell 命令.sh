
# 1. 启动服务
docker compose up -d

# 2. 创建草稿订单（通过前端或 API）
# POST /api/orders with items

# 3. 提交订单（草稿 → 已提交）
# POST /api/orders/{id}/submit

# 4. 审批通过（已提交 → 已批准）
# POST /api/orders/{id}/approve

# 5. 支付（已批准 → 已支付）
# POST /api/orders/{id}/pay

# 6. 发货（已支付 → 已发货）
# POST /api/orders/{id}/ship

# 7. 完成（已发货 → 已完成）
# POST /api/orders/{id}/complete

# 8. 验证每一步的状态和时间戳
# GET /api/orders/{id}