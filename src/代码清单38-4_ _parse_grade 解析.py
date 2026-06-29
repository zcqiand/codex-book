
def _parse_grade(text: str) -> dict:
    """从 LLM 输出解析评判结果。"""
    def grab(tag: str) -> str:
        m = re.search(rf"<{tag}>(.*?)</{tag}>", text, re.DOTALL)
        return m.group(1).strip() if m else ""

    correct_raw = grab("correct").lower()
    correct = correct_raw == "true"

    score_match = re.search(r"<score>(\d+)</score>", text)
    score = int(score_match.group(1)) if score_match else (100 if correct else 0)

    feedback = grab("feedback")
    step_analysis = grab("step_analysis")

    return {
        "correct": correct,
        "score": max(0, min(100, score)),
        "feedback": feedback or ("回答正确！" if correct else "答案有误，请查看解析。"),
        "step_analysis": step_analysis or "",
    }