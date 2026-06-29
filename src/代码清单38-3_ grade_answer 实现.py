
def grade_answer(question: dict, student_answer: str, client: LLMClient) -> dict:
    """评判学生的答案。

    返回格式：
    {
        "correct": bool,
        "score": int,              # 0-100
        "feedback": str,           # 个性化反馈
        "step_analysis": str      # 分步解题分析
    }
    """
    model = _env_model("AI_TUTOR_MODEL_GRADER", DEFAULT_MODEL)
    tracker = CostTracker()

    system = (
        "你是评判代理。给定一道选择题的原题、正确答案，以及学生的作答，"
        "判断对错并给出分数和反馈。\n"
        "输出格式严格为：\n"
        "<correct>true 或 false</correct>\n"
        "<score>0-100 的整数</score>\n"
        "<feedback>针对学生的个性化反馈（20-50 字）</feedback>\n"
        "<step_analysis>分步解题分析</step_analysis>"
    )
    messages = [{
        "role": "user",
        "content": (
            f"题目：{question.get('question', '')}\n"
            f"选项：\n" + "\n".join(f"  {opt}" for opt in question.get('options', [])) + "\n"
            f"正确答案：{question.get('answer', '')}\n"
            f"学生答案：{student_answer}"
        ),
    }]

    response = client.create(model=model, max_tokens=512, system=system, messages=messages)
    _track_usage("grader", model, response, tracker)

    text = _extract_text(response)
    return _parse_grade(text)