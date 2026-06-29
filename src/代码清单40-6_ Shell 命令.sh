
mkdir -p .codex/automations
# 将代码清单40-3保存为 .codex/automations/parent-report.yaml
codex automation list  # 确认 parent-weekly-report 已注册
codex automation run parent-weekly-report --dry-run  # 干跑验证