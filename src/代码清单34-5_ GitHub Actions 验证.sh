
# 1. 确保 .github/workflows/ci.yml 存在
ls -la .github/workflows/

# 2. 在本地模拟 CI 的 Maven verify（使用 H2 内存数据库）
cd backend
mvn clean verify -Dspring.profiles.active=test

# 3. 查看 GitHub Actions 日志（push 后）
# https://github.com/<owner>/<repo>/actions

# 4. 常见失败原因：
#    - 数据库迁移文件（V1__init_schema.sql）有语法错误
#    - 实体类字段与数据库列不匹配（Flyway 迁移未同步）
#    - 缺少环境变量（SPRING_DATASOURCE_*）