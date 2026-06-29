
def make_question(kp_id: str, difficulty: int, client: LLMClient) -> dict:
    """根据知识点 ID 和难度生成一道选择题。

    返回格式：
    {
        "question": str,        # 题目正文
        "options": list[str],    # 选项列表，通常 4 个
        "answer": str,          # 正确答案（A/B/C/D 之一）
        "explanation": str      # 解析
    }
    """
    model = _env_model("AI_TUTOR_MODEL_QUESTION_MAKER", DEFAULT_MODEL)

    difficulty_labels = {1: "基础", 2: "中等", 3: "进阶"}
    diff_label = difficulty_labels.get(difficulty, "中等")

    system = (
        "你是出题代理。根据给定的知识点和难度，生成一道高中数学选择题。\n"
        "输出格式严格为：\n"
        "<question>题目正文</question>\n"
        "<optionA>A. 选项内容</optionA>\n"
        "<optionB>B. 选项内容</optionB>\n"
        "<optionC>C. 选项内容</optionC>\n"
        "<optionD>D. 选项内容</optionD>\n"
        "<answer>A</answer>\n"
        "<explanation>解析内容</explanation>\n"
        "选项应为 4 个，答案只能是 A/B/C/D 之一。"
    )
    messages = [{
        "role": "user",
        "content": f"知识点 ID：{kp_id}\n难度：{diff_label}（1=基础，2=中等，3=进阶）",
    }]

    response = client.create(model=model, max_tokens=1024, system=system, messages=messages)
    _track_usage("question_maker", model, response, tracker)

    text = _extract_text(response)
    return _parse_question(text)