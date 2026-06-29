
codex run --agent planner -- \
  "为学生 bob 生成学情图表：
  1. 从 Memory 读取 bob 最近 30 天的掌握度数据
  2. 用 \$imagegen 生成一张多线学习曲线图（包含 alg-7-02 和 alg-7-03 两个知识点）
  3. 用 \$imagegen 生成一张能力雷达图（5 个维度）
  4. 保存图片 URL 到 Memory: student:bob:dashboard_images"
# 观察 $imagegen 的返回格式和图片 URL 的有效期