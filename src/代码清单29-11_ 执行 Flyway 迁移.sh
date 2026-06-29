
cd backend
mvn flyway:migrate

# 验证表已创建
psql -h localhost -U postgres -d ecommerce -c "\dt"
# 应输出: inventory  order_items  orders  products  suppliers  users