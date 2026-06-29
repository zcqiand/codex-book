
# 使用 Codex 生成订单相关 Java 文件：
# 1. OrderService.java - 订单业务逻辑（含 createOrder, submitOrder, approveOrder, rejectOrder, payOrder, shipOrder, completeOrder, cancelOrder）
# 2. OrderController.java - REST API 端点
# 3. CreateOrderRequest.java - 请求 DTO（含 @Valid 校验注解）
# 4. OrderStatus.java - 状态枚举（含 canTransitionTo 方法）

# 要求：
# - 金额用 BigDecimal
# - 创建订单时快照 unitPrice
# - 订单号格式 yyyyMMddHHmmss + 6位随机数
# - 使用 @Autowired 注入依赖
# - 使用 @Transactional 管理事务