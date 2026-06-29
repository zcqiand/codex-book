
# 创建项目目录
mkdir ecommerce-oms
cd ecommerce-oms

# 用 Codex 生成基础设施文件（复制代码清单29-3的Prompt）
codex exec --dangerously-bypass-approvals-and-sandbox \
  "你是一个Spring Boot项目的架构师。请只生成以下文件...
  【技术约束】Spring Boot 3.3, Java 21, PostgreSQL 16, Spring Data JPA...
  【要生成的文件】1. backend/pom.xml 2. backend/src/main/resources/application.yml 3. EcommerceApplication.java 4. 六个 Entity 空类"