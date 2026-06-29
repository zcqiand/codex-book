# 提取 token 用量
codex exec --json "分析代码库的复杂度" \
  | jq -s '[.[] | select(.type == "turn.completed") | .usage]'

# 提取所有 agent 文本回复（合并多轮）
codex exec --json "逐文件审查错误处理" \
  | jq -r 'select(.type == "item.completed" and .item.type == "agent_message") | .item.text'