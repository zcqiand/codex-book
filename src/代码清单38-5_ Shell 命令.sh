
mkdir -p .codex/automations
# 将代码清单38-2保存为 .codex/automations/weekly-report.yaml
codex automation list  # 验证 Automation 已注册
codex automation run weekly-learning-report --dry-run  # 干跑验证