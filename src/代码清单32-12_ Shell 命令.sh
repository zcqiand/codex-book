
# 1. 尝试对已完成的订单再次发货
# POST /api/orders/{id}/ship
# 预期: 400 错误，INVALID_ORDER_STATUS

# 2. 尝试取消已发货的订单
# POST /api/orders/{id}/cancel
# 预期: 400 错误，INVALID_ORDER_STATUS

# 3. 尝试对草稿状态订单直接支付
# POST /api/orders/{id}/pay
# 预期: 400 错误，INVALID_ORDER_STATUS