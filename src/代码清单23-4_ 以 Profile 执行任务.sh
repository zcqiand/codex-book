# 第一阶段：分析
codex exec "检查 src/ 目录中的竞态条件"

# 第二阶段：用 --last 继续最近一次 session
codex exec resume --last "修复你发现的竞态条件"

# 或者指定 session ID 继续
codex exec resume 0199a213-81c0-7800-8aa1-bbab2a035a53 "补充单元测试"