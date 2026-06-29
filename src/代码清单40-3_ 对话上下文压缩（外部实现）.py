
def manage_tutoring_context(messages: list[dict], max_turns: int = 10) -> list[dict]:
    """保持最近 N 轮完整对话 + 早期对话的摘要。"""
    if len(messages) <= max_turns * 2:  # 每轮 = 学生消息 + Agent 回复
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
                   f"主要错误类型：{summary['main_error_types']}"
    }
    return [summary_msg] + recent