# AGENTS.md — 项目上下文说明

# 技术栈
- React 18.3 + TypeScript 5.4
- 状态管理：Zustand 4.5
- 路由：React Router 6.23
- 测试：Vitest + React Testing Library
- 样式：Tailwind CSS 3.4

# 项目结构
- src/components/ — 通用组件，每个组件一个文件夹
- src/pages/ — 页面级组件
- src/hooks/ — 自定义 Hook
- src/api/ — API 调用封装，统一使用 axios 实例

# 命名约定
- 组件文件：PascalCase（如 UserProfile.tsx）
- Hook 文件：camelCase 以 use 开头（如 useAuth.ts）
- 测试文件：与源文件同目录，后缀 .test.tsx

# 架构约束
- 组件不能直接调用 API——必须通过 src/api/ 中的封装函数
- 全局状态只用于跨页面共享的数据
- 禁止在渲染路径中使用 any 类型

# 测试规范
- 每个组件至少覆盖基本渲染和关键交互
- API 调用使用 MSW mock，不发起真实网络请求