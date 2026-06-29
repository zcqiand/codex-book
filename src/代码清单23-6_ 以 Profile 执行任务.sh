# 把 API 返回的 JSON 数据传给 Codex，让它格式化
curl -s https://jsonplaceholder.typicode.com/comments \
  | codex exec "提取前20条评论，整理成 Markdown 表格" \
  > comments-table.md