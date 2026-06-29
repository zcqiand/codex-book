
# 1. 创建知识图谱目录
mkdir -p knowledge/初中数学

# 2. 用 Codex 生成知识图谱 JSON
codex run -- "参考代码清单36-1的JSON格式，为初中数学'一元一次方程'章节
编写完整的 knowledge_graph.json。包含至少5个知识点，每个知识点有
id/name/grade/difficulty/prerequisites/common_errors字段。
保存到 knowledge/初中数学/knowledge_graph.json"