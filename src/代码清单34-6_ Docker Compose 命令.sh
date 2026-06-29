
# 1. 启动全部服务（postgres + backend + frontend）
docker compose up -d

# 2. 查看服务状态
docker compose ps

# 3. 查看后端日志
docker compose logs backend

# 4. 查看前端日志
docker compose logs frontend

# 5. 验证后端健康检查
curl http://localhost:8080/actuator/health

# 6. 停止全部服务
docker compose down