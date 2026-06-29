<!-- src:src-001,official_doc -->
class EvaluatorAgent:
    def __init__(self, llm_client):
        self.llm = llm_client
        self.system_prompt = """你是一个严谨的学术评估员。
你的任务是判断学生的回答是否正确，并精确定位知识盲点。

评估标准：
- 答案正确 + 推理严谨 → "correct"
- 答案正确 + 推理有瑕疵 → "partial"
- 答案错误 + 是因为概念混淆 → "misconception"
- 答案错误 + 是因为计算失误 → "calculation_error"
- 答案错误 + 是因为审题不清 → "comprehension_error"

输出格式：
{"verdict": "correct|partial|misconception|calculation_error|comprehension_error",
 "analysis": "错误原因分析",
 "misconception_point": "如果错误，涉及的知识点"}"""

    def evaluate(self, memory: SharedMemory):
        student_answer = memory.read("current_answer")
        expected_answer = memory.read("expected_answer")
        # 调用 LLM 进行评估...