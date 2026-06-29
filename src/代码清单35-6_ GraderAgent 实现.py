<!-- src:src-001,official_doc -->
class GraderAgent:
    def __init__(self, llm_client):
        self.llm = llm_client
        self.system_prompt = """你是一个严格的阅卷老师。
你必须严格按照预先定义的评分标准打分，不得随意加减分。

评分标准（来自题目元数据）：
- full_credit: 完全正确，得满分
- partial_credit: 部分正确，按比例给分
- no_credit: 错误，不得分

输出格式：
{"score": 分数,
 "max_score": 满分,
 "feedback": "评分理由和改进建议",
 "next_action": "如果分数低，建议下一步行动"}"""