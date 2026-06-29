
# 获取所有库存记录，验证 quantity - lockedQuantity = 所有未完成订单的待发货数量之和
curl http://localhost:8080/api/inventory/

# 获取所有 PAID/SHIPPED 状态的订单
curl "http://localhost:8080/api/orders/?status=PAID"

# 手动对账：验证公式
# 初始 quantity = 100
# 订单1下单 3 件：lockedQuantity = 3，可用 = 97
# 订单1支付：quantity = 97，lockedQuantity = 0，可用 = 97
# 理论上：quantity(97) - lockedQuantity(0) = 97 = 所有未完成订单待发货量(0)