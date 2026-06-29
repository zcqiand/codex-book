
def socratic_tutor(topic: str, student_question: str, client: LLMClient) -> str:
    """苏格拉底式辅导：针对学生的提问返回引导式回复。

    参数：
        topic: 当前学习主题（如 "导数"、"力学"）
        student_question: 学生提出的具体问题
        client: LLM client

    返回：
        引导式回复（不直接给答案，通过提问或类比引导思考）
    """
    model = _env_model("AI_TUTOR_MODEL_SOCRATIC", DEFAULT_MODEL)
    tracker = CostTracker()

    system = (
        "你是一位苏格拉底式辅导老师。你不会直接回答学生的问题，"
        "而是通过追问、类比、举例的方式引导学生自己思考出答案。\n"
        "回复要求：\n"
        "1. 不直接给出答案或结论\n"
        "2. 用 1-2 个递进式问题引导\n"
        "3. 可用生活中的类比帮助理解\n"
        "4. 回复简洁，50-100 字为宜\n"
        "5. 用中文回复"
    )
    messages = [{
        "role": "user",
        "content": (
            f"当前学习主题：{topic}\n"
            f"学生提问：{student_question}"
        ),
    }]

    response = client.create(
        model=model,
        max_tokens=512,
        system=system,
        messages=messages,
    )
    _track_usage("socratic_tutor", model, response, tracker)

    return _extract_text(response)