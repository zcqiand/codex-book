
# 1. 在 Codex 会话中执行审查：
#    /review src/main/java/com/zcqiand/ecommerce/controller/OrderController.java
#       src/main/java/com/zcqiand/ecommerce/service/OrderService.java
#       src/main/java/com/zcqiand/ecommerce/entity/OrderStatus.java

# 2. 启动 Spring Boot 应用：
cd code/ecommerce-oms/backend
./mvnw spring-boot:run

# 3. 创建商品和库存数据（通过 JPA 自动建表后）：
#    POST /api/products 创建商品
#    POST /api/inventory?productId=xxx&quantity=xxx 创建库存

# 4. 用 curl 测试下单：
curl -X POST http://localhost:8080/api/orders \
  -H "Content-Type: application/json" \
  -d '{"userId":1,"address":"测试地址","items":[{"productId":1,"quantity":2}]}'

# 5. 测试状态转换：
curl -X POST http://localhost:8080/api/orders/1/submit
curl -X POST http://localhost:8080/api/orders/1/approve
curl -X POST http://localhost:8080/api/orders/1/pay

# 6. 测试非法转换（应返回 400）：
curl -X POST http://localhost:8080/api/orders/1/complete
# completed 前必须先 shipped，不能从 paid 直接完成