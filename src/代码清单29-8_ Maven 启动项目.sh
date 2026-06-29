
# 启动 PostgreSQL（使用 Docker Compose）
docker-compose up -d postgres

# 编译并启动 Spring Boot 应用
cd backend
mvn spring-boot:run

# 在浏览器中打开 http://localhost:8080/swagger-ui.html
# 看到 Swagger UI 即验证通过