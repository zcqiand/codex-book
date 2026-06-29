
# 1. 构建开发版本
VITE_API_URL=http://localhost:8080 npm run build

# 2. 检查构建产物中的 API 地址
grep -r "localhost:8080" dist/

# 3. 清理并构建生产版本
rm -rf dist
VITE_API_URL=https://api.production.com npm run build

# 4. 再次检查构建产物
grep -r "api.production.com" dist/