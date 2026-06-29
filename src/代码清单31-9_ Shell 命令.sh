
# 创建供应商
curl -X POST http://localhost:8080/api/suppliers \
  -H "Content-Type: application/json" \
  -d '{"name":"深圳电子科技","contactPerson":"张三","phone":"13800138000"}'

# 查询所有供应商
curl http://localhost:8080/api/suppliers/

# 查询单个供应商
curl http://localhost:8080/api/suppliers/1

# 更新供应商
curl -X PUT http://localhost:8080/api/suppliers/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"深圳电子科技（更新）","contactPerson":"李四","phone":"13900139000"}'

# 删除供应商
curl -X DELETE http://localhost:8080/api/suppliers/1