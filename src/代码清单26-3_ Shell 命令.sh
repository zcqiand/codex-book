git checkout -b test-codex-review
# 故意引入一个问题后提交
git add . && git commit -m "test: trigger codex review"
git push origin test-codex-review
# 在 GitHub 上创建 PR，观察 Actions 标签页