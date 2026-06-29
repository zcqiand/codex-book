cat > ci_review.sh << 'SCRIPT'
#!/usr/bin/env bash
set -euo pipefail
REPO_PATH="${1:-.}"

RESULT=$(codex exec --cd "$REPO_PATH" \
  --sandbox read-only \
  --json \
  --ephemeral \
  "审查代码中的安全漏洞。如果发现严重问题，请在回复中明确写出 CRITICAL_FOUND: yes")

if echo "$RESULT" | grep -q "CRITICAL_FOUND: yes"; then
  echo "发现严重问题，CI 检查不通过"
  exit 1
else
  echo "安全检查通过"
  exit 0
fi
SCRIPT

chmod +x ci_review.sh
./ci_review.sh ./project-a