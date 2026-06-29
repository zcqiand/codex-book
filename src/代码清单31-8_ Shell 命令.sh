
# 1. 启动 Spring Boot 应用（如未启动）
cd code/ecommerce-oms/backend
./mvnw spring-boot:run

# 2. 创建库存（先创建商品和库存）
curl -X POST "http://localhost:8080/api/inventory?productId=1&quantity=100&warehouseLocation=A区"

# 3. 创建订单（锁定库存）
curl -X POST http://localhost:8080/api/orders \
  -H "Content-Type: application/json" \
  -d '{"userId":1,"address":"测试地址","items":[{"productId":1,"quantity":3}]}'

# 4. 提交、审批、支付订单
curl -X POST http://localhost:8080/api/orders/1/submit
curl -X POST http://localhost:8080/api/orders/1/approve
curl -X POST http://localhost:8080/api/orders/1/pay

# 5. 验证库存已实扣
curl http://localhost:8080/api/inventory/product/1

# 6. 再次调用支付（测试幂等——应返回相同结果，库存不应二次扣减）
curl -X POST http://localhost:8080/api/orders/1/pay
# 第二次应返回错误：非法状态转换