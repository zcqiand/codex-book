
def _parse_question(text: str) -> dict:
    """从 LLM 输出解析题目结构。"""
    def grab(tag: str) -> str:
        m = re.search(rf"<{tag}>(.*?)</{tag}>", text, re.DOTALL)
        return m.group(1).strip() if m else ""

    question = grab("question")
    answer_raw = grab("answer").upper()
    if answer_raw not in ("A", "B", "C", "D"):
        answer_raw = "A"

    options = []
    for tag in ("optionA", "optionB", "optionC", "optionD"):
        content = grab(tag)
        if content:
            options.append(content)

    explanation = grab("explanation")

    return {
        "question": question or text[:200],
        "options": options if options else ["A. 对", "B. 错", "C. 不确定", "D. 以上都不对"],
        "answer": answer_raw,
        "explanation": explanation,
    }