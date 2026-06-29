
# 1. 启动全部服务
docker compose up -d

# 2. 查看服务状态
docker compose ps

# 3. 查看后端健康检查
curl http://localhost:8080/actuator/health
# 期望输出：{"status":"UP"}

# 4. 查看前端
open http://localhost:3000

# 5. 查看日志
docker compose logs -f backend

# 6. 停止服务（保留数据卷）
docker compose down

# 7. 停止服务并删除数据卷（危险！数据会丢失）
docker compose down -v