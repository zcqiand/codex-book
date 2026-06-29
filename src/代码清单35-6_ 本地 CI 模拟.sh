
# 1. 模拟 backend Job（Maven verify with PostgreSQL）
# 先确保本地有 PostgreSQL，或者使用 Docker 启动
docker run -d --name test-postgres \
  -e POSTGRES_DB=ecommerce \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -p 5432:5432 \
  postgres:16-alpine

# 等待健康检查
sleep 5

# 运行 Maven verify
cd backend
mvn clean verify \
  -Dspring.datasource.url=jdbc:postgresql://localhost:5432/ecommerce \
  -Dspring.datasource.username=postgres \
  -Dspring.datasource.password=postgres

# 清理
docker stop test-postgres && docker rm test-postgres