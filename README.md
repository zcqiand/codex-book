# Codex 从入门到项目实践 - 代码清单

> **本书配套代码示例库** — 从章节中提取的完整可运行代码

## 关于本书

2025 年秋天，我在一个创业公司担任技术顾问。团队决定全面引入 AI 编程工具来提升开发效率，他们试过 GitHub Copilot，也试过让工程师在 ChatGPT 网页版上调试代码，但效果都不理想——Copilot 只能补全零散代码片段，ChatGPT 需要手动复制粘贴，每次都得重新解释项目上下文。后来他们发现了 OpenAI Codex，一个能直接操作文件系统、运行命令、管理 Git 的代理式编码工具。短短两个月，团队的开发效率提升了 40%，但那段摸索配置、扩展机制、安全边界的经历充满了弯路。

这本书就是那段经历的系统化总结——我希望其他开发者不需要重复那些踩坑的过程。

## 本书特点

**第一，应用目标驱动。** 每一章开头都明确说明「学完这章你能交付什么」，并且这些目标都是真实的可交付成果——不是「了解配置体系」，而是「能用多层配置管理不同项目的规则」。

**第二，两个完整生产级项目。** 卷四和卷五分别实现了电商订单库存系统和 AI 学习辅导多智能体系统两个端到端项目，覆盖需求分析、数据建模、核心业务、集成测试、部署上线全流程。

**第三，扩展机制的实战组合。** 斜杠命令、Hooks、MCP 协议、插件市场、技能系统、子代理——本书通过大量对比表格和决策框架帮你建立选择直觉。

## 谁应该读这本书

如果你是一名有一年及以上编程经验的开发者，熟悉 Python、JavaScript、Go、Java 等任意一门主流语言，希望将 AI 编程能力融入日常工作，这本书适合你。你可能是：

- 在互联网公司工作的后端/前端/全栈工程师，希望用 AI 减少重复编码工作
- 独立开发者或小团队成员，需要一个人完成从需求到部署的全流程
- 对 AI 编程感兴趣的技术爱好者，想了解「代理式编码」的本质边界

## 代码清单说明

本目录包含从书籍章节中提取的 **274 个**代码示例文件，涵盖第 2-41 章的核心知识点。

### 📊 代码统计

- **总文件数**: 274 个
- **涉及章节**: 第 2-41 章（全覆盖）
- **两个完整案例**: 电商订单系统（卷四）+ AI 辅导多智能体（卷五）

### 📋 按编程语言分类

| 语言       | 文件数 | 说明                        |
| ---------- | ------ | --------------------------- |
| Bash/Shell | 102    | CLI 命令、安装脚本          |
| Python     | 47     | 后端脚本、SDK 示例、数据处理 |
| TOML       | 38     | 配置文件（config.toml）     |
| Java       | 31     | 电商案例后端代码            |
| TypeScript | 25     | SDK 使用、类型定义          |
| YAML       | 12     | CI/CD 配置、工作流、Agent 定义 |
| JSON       | 7      | 数据结构、API 响应          |
| Markdown   | 4      | 文档示例、SKILL.md 模板     |
| 其他       | 8      | text/plaintext/sql/jsonc    |

### 📂 章节覆盖

| 章节范围 | 内容主题                          |
| -------- | -------------------------------- |
| 第 2-5 章 | 环境安装与快速上手               |
| 第 6-9 章 | 核心概念（配置、规则、记忆、权限）|
| 第 10-19 章 | 扩展与集成（斜杠命令、Hooks、MCP、插件）|
| 第 20-27 章 | SDK 与自动化                     |
| 第 28-35 章 | **电商订单与库存管理系统案例**（Spring Boot + React）|
| 第 36-41 章 | **AI 学习辅导多智能体系统案例**（Python Agent SDK）|

### 文件命名规范

```text
代码清单{章节号}-{序号}_ {描述}.{扩展名}
```

示例：

- `代码清单06-8_ Codex config.toml 配置.txt` - 第 6 章第 8 个代码块，config.toml 配置
- `代码清单20-1_ npm 全局安装 Codex CLI.sh` - 第 20 章安装脚本
- `代码清单29-5_ User 类定义.py` - 第 29 章 Python 类

每个文件内的来源注释标明原始章节：

```python
# 摘自：output/xr-know-003/chapters/chapter-29.md
# 书籍：Codex 从入门到项目实践
```

## 完整案例仓库

书中卷四、卷五的两个完整可运行项目托管在独立仓库中，代码清单中的片段均可在对应仓库中找到完整实现：

### 🛒 电商订单与库存管理系统（卷四 · 第 28-35 章）

> **仓库**：[https://github.com/zcqiand/ecommerce-oms](https://github.com/zcqiand/ecommerce-oms)
>
> **技术栈**：Spring Boot 3.3 + Java 21 LTS + PostgreSQL 16 + React 18 + Vite 5 + Docker Compose
>
> **内容**：需求分析、ER 图、数据库迁移、RESTful API、库存锁定/扣减/释放、审批流、多级审核、供应商管理、前端页面、CI/CD 端到端部署
>
> **运行**：
> ```bash
> cd code/ecommerce-oms
> docker compose up -d
> # 后端：http://localhost:8080
> # 前端：http://localhost:3000
> ```

### 🎓 AI 学习辅导多智能体系统（卷五 · 第 36-41 章）

> **仓库**：[https://github.com/zcqiand/ai-tutoring-multi-agent](https://github.com/zcqiand/ai-tutoring-multi-agent)
>
> **技术栈**：Python 3.10+ + Claude Agent SDK
>
> **内容**：三代理架构（Planner/Tutor/Evaluator）、知识库建模、出题与批改、自适应学习路径、辅导对话管理、端到端集成测试
>
> **运行**：
> ```bash
> cd code/ai-tutoring-multi-agent
> pip install -e .
> python run_demo.py
> ```

### 本书主仓库（代码片段索引）

> **仓库**：[https://github.com/zcqiand/codex-book](https://github.com/zcqiand/codex-book)
>
> 本仓库（`codex-book`）为书中代码片段的索引库，按章组织，仅供查阅对照。两个完整案例的详细代码请参考上述对应仓库。

## 配套资源

- **书籍主仓库**：[https://github.com/zcqiand/codex-book](https://github.com/zcqiand/codex-book)
- **勘误页面**：[https://github.com/zcqiand/codex-book/issues](https://github.com/zcqiand/codex-book/issues)
- **读者交流**：1282301776@qq.com
- **电子书籍网址**：[亚马逊](https://www.amazon.com/dp/B0H3781RB9)

## ⚠️ 注意事项

1. **代码版本**：代码基于 2026 年 5 月的 Codex 版本编写，API 可能有更新
2. **依赖安装**：某些代码可能需要额外依赖包（参见对应章节说明）
3. **安全审查**：生产环境使用前请审查代码，特别是涉及认证和权限的部分
4. **环境差异**：部分代码可能需要根据实际环境调整

---

**最后更新**：2026年6月27日
**书籍版本**：1.0（案例完整对接版）
**代码来源**：[../../output/xr-know-003/chapters](../../output/xr-know-003/chapters/)