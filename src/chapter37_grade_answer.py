# 从第 37 章提取
# 来源：Codex 从入门到项目实践

import json
import re

def grade_answer(question: dict, student_answer: str) -> dict:
    """三层批改：(1) 数值比对 (2) 步骤推导 (3) 错误模式匹配。"""

    standard = normalize_answer(question["answer"])
    student = normalize_answer(student_answer)
    if standard == student:
        return {"is_correct": True, "error_type": "correct", "correction_hint": ""}

    if "steps" in question:
        step_result = check_steps(question["steps"], student_answer)
        if step_result["mismatch_step"]:
            return {
                "is_correct": False,
                "error_type": step_result["error_type"],
                "correction_hint": f"第{step_result['mismatch_step']}步出错：{step_result['hint']}"
            }

    # 层3：错误模式匹配（来自知识图谱 common_errors）
    for err_pattern in question.get("common_errors", []):
        if matches_error_pattern(student_answer, err_pattern):
            return {
                "is_correct": False,
                "error_type": err_pattern["error_type"],
                "correction_hint": f"你可能犯了{err_pattern['pattern']}——{get_hint(err_pattern['error_type'])}"
            }

    return {"is_correct": False, "error_type": "unknown", "correction_hint": "请展示你的解题步骤"}


def normalize_answer(ans: str) -> str:
    """标准化答案：去除空格、统一分数表示、处理 ± 符号。"""
    ans = ans.strip().replace(" ", "")
    # LaTeX 分数 \frac{num}{den} → 小数，raw string r"\\frac" 匹配字面反斜杠+fraction
    ans = re.sub(r"\\frac\{(\d+)\}\{(\d+)\}",
                  lambda m: str(round(int(m.group(1)) / int(m.group(2)), 4)), ans)
    ans = ans.replace("x=", "").replace("X=", "")
    return ans