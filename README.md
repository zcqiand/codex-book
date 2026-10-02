# Codex 从入门到项目实践 - 代码清单

## 关于本书

本书是一本系统讲解 OpenAI Codex 的实战入门书。Codex 不是「补全式」的代码提示工具，而是能直接操作文件系统、运行命令、管理 Git 的代理式编码助手——本书把它的配置体系、扩展机制与安全边界一次讲透，帮助开发者真正把 AI 编程整合进日常工程流程。

全书以「应用目标驱动」组织：每一章开头都明确「学完这章你能交付什么」，且交付目标全部是真实可用的工程成果，而非「了解某个概念」。卷一至卷三打牢 CLI、配置、扩展与协作基础，卷四、卷五以两个完整生产级项目（建筑工程实验室管理系统、SaaS 多租户统一身份管理平台）把能力落到真实业务。适合想从「会用补全」进阶到「会调度代理」的开发者、技术负责人，以及评估 AI 编程工具落地的团队。

## 本书特点

**第一，应用目标驱动。** 每章从可交付成果出发倒讲功能，学完即可在工作中复用，不做参数手册式的罗列。

**第二，两个完整生产级项目。** 卷四、卷五绑定两个真实可跑的 Next.js 15 全栈项目（实验室管理系统、SaaS 身份平台），从需求到部署完整走一遍代理式开发流程。

**第三，配置与安全边界讲透。** 多层配置管理、AGENTS.md 规则体系、审批与沙箱模式——不只讲「怎么配」，更讲「什么时候用、不用会怎样」。

**第四，版本基线最新。** 全书基于 2026 年 5 月的 Codex CLI / App / IDE 扩展与 GPT-5.4 模型基线写作，SDK 覆盖 TypeScript 与 Python 双语言。

## 案例仓库

| 仓库名 | 说明 |
| :--- | :--- |
| [lab-management-system-nextjs](https://github.com/zcqiand/lab-management-system-nextjs) @ v0.3.86-20260926 | 基于 Next.js 15 (App Router) / React 19 / TypeScript 5.7 strict / Drizzle ORM 的建筑工程实验室管理系统实战项目，覆盖检测样本、检测项目目录与报表流程等业务模块 |
| [saas-identity-platform-nextjs](https://github.com/zcqiand/saas-identity-platform-nextjs) @ v0.7.69-20260926 | 基于 Next.js 15 (App Router) / React 19 / TypeScript 5.7 strict / Drizzle ORM 的 SaaS 多租户统一身份管理平台实战项目，覆盖多租户、JWT 认证、OAuth 令牌与审计拦截 |

> 配套案例仓库为独立可跑工程，已冻结 tag，含完整测试与 CI，clone 即跑。

## 代码清单说明

本书所有代码清单均收录于本目录，对应书稿中「代码清单 N-M」标题块。

### 运行环境

```bash
# 环境要求：Node.js 18+（CLI 经 npm 分发；TypeScript SDK 依赖 Node.js 运行时），Python SDK 示例需 Python 3.10+
npm install -g @openai/codex
codex --version
# 项目实战章节（卷四/卷五）依赖案例仓库：clone 后切到冻结 tag，进入项目目录安装依赖
npm install
```

### 目录结构

```
src/
├── 代码清单2-* … 代码清单41-*   # 第 2-41 章，共 176 个清单文件（命名「代码清单N-M_ 描述.扩展名」）
└── extracted_code_manifest.json   # 全部清单索引（title/lang/chapter_file/line/extracted_file/source）
```
