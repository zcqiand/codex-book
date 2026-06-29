
# question_maker.py — 出题 Agent
def make_question(kp_id: str, difficulty: int, client: LLMClient) -> dict:
    """根据知识点 ID 和难度生成一道选择题。
    返回：{"question": str, "options": list[str], "answer": str, "explanation": str}
    """
    ...

# grader.py — 批改 Agent
def grade_answer(question: dict, student_answer: str, client: LLMClient) -> dict:
    """评判学生答案。
    参数 question：make_question 产出的 dict
    返回：{"correct": bool, "score": int, "feedback": str, "step_analysis": str}
    """
    ...