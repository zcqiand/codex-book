# 从文件读取 prompt
cat review-prompt.txt | codex exec -

# 用脚本动态组装 prompt
echo "审查 $(git diff --name-only HEAD~1) 中的变更，重点关注安全漏洞" | codex exec -