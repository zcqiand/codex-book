
# 运行全部测试（单元测试 + 集成测试）
mvn test

# 完整验证：编译 + 测试 + 打包（CI 中使用这个）
mvn verify

# 生成测试覆盖率报告（需 jacoco 插件）
mvn test jacoco:report