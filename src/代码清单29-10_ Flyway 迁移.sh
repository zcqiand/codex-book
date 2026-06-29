
# 确认 PostgreSQL 已启动
docker-compose up -d postgres

# 执行 Flyway 迁移
cd backend
mvn flyway:migrate

# 【关键】打开 src/main/resources/db/migration/V1__init_schema.sql
# 逐段审查 CREATE TABLE 语句，确认所有表结构和约束正确

# 验证
psql -h localhost -U postgres -d ecommerce -c "\dt"
# 应输出: inventory  order_items  orders  products  suppliers  users