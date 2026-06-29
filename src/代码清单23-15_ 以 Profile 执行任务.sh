# 提取 token 用量
codex exec --json "审查 src/ 的代码质量，给出三个改进建议" \
  | jq -s 'map(select(.type == "turn.completed") | .usage)'

# 只看最终文本回复
codex exec --json "审查 src/ 的代码质量，给出三个改进建议" \
  | jq -r 'select(.type == "item.completed" and .item.type == "agent_message") | .item.text'