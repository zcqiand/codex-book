
def generate_learning_curve_chart(student_id: str, kp_ids: list[str]) -> str:
    """构建 $imagegen 调用 prompt，生成学习曲线图。"""
    kp_labels = ", ".join(kp_ids)
    return f"""
$imagegen 生成一张学习曲线折线图，规格如下：

【数据来源】
从 Memory 读取学生 {student_id} 的知识点 {kp_labels} 的掌握度历史。
每个知识点取最近 30 天的每日掌握度快照。

【图表规格】
- 类型：多线折线图（multi-line chart）
- X 轴：日期（最近 30 天，格式 MM-DD）
- Y 轴：掌握度（范围 0.0-1.0，刻度 0.1）
- 每条线一个知识点，用不同颜色区分，图例标注知识点名称
- 标题：{student_id} 最近30天学习曲线
- 风格：简洁商务风，白色背景，网格线浅灰色

【关键标注】
- 在掌握度首次超过 0.7 的日期点标注 "掌握"
- 在掌握度单日涨幅超过 0.2 的点标注 "突破"
"""


def generate_radar_chart(student_id: str) -> str:
    """构建雷达图生成 prompt。"""
    return f"""
$imagegen 生成一张能力雷达图，规格如下：

【数据来源】
从 Memory 读取学生 {student_id} 的掌握度，按能力维度聚合：
- 代数运算：alg-* 知识点的平均掌握度
- 几何直观：geo-* 知识点的平均掌握度
- 方程建模：eq-* 知识点的平均掌握度
- 逻辑推理：logic-* 知识点的平均掌握度
- 运算准确度：所有知识点做题正确率

【图表规格】
- 类型：雷达图（radar chart）
- 5 个维度，范围 0-100（百分比）
- 填充区域半透明蓝色
- 标题：{student_id} 能力结构图
- 风格：简洁商务风

【诊断标注】
- 掌握度低于 40 的维度标注红色 "需加强"
- 掌握度高于 80 的维度标注绿色 "优势"
"""