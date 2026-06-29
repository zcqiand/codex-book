
# 1. 运行全部测试
cd backend
mvn test

# 2. 生成覆盖率报告（需在 pom.xml 中添加 jacoco 插件）
mvn test jacoco:report

# 3. 查看覆盖率报告
# target/site/jacoco/index.html

# 4. 观察哪些方法未被覆盖——这些是未来补测试的优先级列表
# 重点关注：cancelOrder 中 PAID 状态的库存恢复分支