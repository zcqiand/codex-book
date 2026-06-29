
def manage_tutoring_context(messages: list[dict], max_turns: int = 10) -> list[dict]:
    """保持最近 N 轮完整对话 + 早期对话的摘要。"""
    if len(messages) <= max_turns * 2: # 每轮 = 学生消息 + Agent 回复
        return messages  # 未超限，全量保留

    # 拆分：早期对话 → 摘要；最近对话 → 完整保留
    early = messages[:-max_turns * 2]
    recent = messages[-max_turns * 2:]

    # 早期对话提取关键信息（而非丢弃）
    summary = summarize_learning_session(early)
    summary_msg = {
        "role": "system",
        "content": f"[早期对话摘要] 学生已尝试 {summary['questions_attempted']} 道题，"
                   f"正确 {summary['correct_count']} 道，"
                   f"主要错误类型：{summary['main_error_types']}，"
                   f"已掌握知识点：{summary['mastered_topics']}"
    }
    return [summary_msg] + recent


def summarize_learning_session(messages: list[dict]) -> dict:
    """从早期对话中提取结构化摘要——只保留「教学决策需要的信息」。"""
    # 提取题目和批改结果
    questions = []
    errors = []
    for msg in messages:
        if msg["role"] == "system" and "题目" in msg.get("content", ""):
            questions.append(msg["content"])
        if msg["role"] == "assistant" and "error_type" in msg.get("content", ""):
            errors.append(msg["content"])
    return {
        "questions_attempted": len(questions),
        "correct_count": len(questions) - len(errors),
        "main_error_types": list(set(errors))[:3],
        "mastered_topics": []  # 由掌握度更新逻辑填充
    }

上下文治理的核心原则是「存语义，不存原文」。丢掉早期对话的逐字记录，但保留教学决策需要的信息：做了几道题、对了几道、主要错误模式是什么。辅导 Agent 拿到摘要后，不需要回顾「第 3 道题的第 2 步追问具体说了什么」，但它需要知道「这个学生刚才在错题类型上主要是 calculation_error」——这个信息会影响下一道题的追问策略。