
QUESTION_TEMPLATES = {
    "choice": {
        "format": "4选项选择题",
        "output_schema": {
            "stem": "题目题干（一行）",
            "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
            "answer": "正确选项字母",
            "distractor_logic": "每个错误选项对应的典型错误（移项不变号/去括号忘变号/...）"
        },
        "difficulty_modifiers": {
            1: "数字为整数，一步运算",
            2: "数字含小数或分数，两步运算",
            3: "含括号或需要先化简，三步运算",
            4: "含参数或需要逆向思维",
            5: "多知识点综合，需要识别隐含条件"
        }
    },
    "fill_in": {
        "format": "填空题",
        "output_schema": {
            "stem": "题目题干（含一个 __ 空）",
            "answer": "标准答案",
            "acceptable_variants": ["可接受的答案变体"]
        },
        "difficulty_modifiers": {
            1: "直接代入公式即可得答案",
            2: "需要一步变形后代入",
            3: "需要两步推导",
            4: "需要建立方程再求解",
            5: "需要画图或列表辅助理解题意"
        }
    }
}


def build_question_prompt(knowledge_point: dict, student_mastery: float,
                          question_type: str = "choice",
                          count: int = 3) -> str:
    """根据知识点、学生掌握度和题型构建出题 Prompt。"""
    template = QUESTION_TEMPLATES[question_type]
    # 难度自适应：比当前掌握度高 1 级（保持挑战性但不打击信心）
    target_difficulty = min(int(student_mastery * 5) + 1, 5)
    modifier = template["difficulty_modifiers"][target_difficulty]

    return f"""
请生成 {count} 道初中数学{knowledge_point['name']}的{template['format']}。

【知识点约束】
- 前置知识点：{knowledge_point.get('prerequisites', [])}（学生已掌握）
- 常见错误模式（请在干扰项中体现）：{knowledge_point.get('common_errors', [])}

【难度控制】
目标难度 {target_difficulty}/5：{modifier}

【输出格式】
严格输出 JSON，格式为：
{json.dumps(template['output_schema'], ensure_ascii=False, indent=2)}
每道题额外包含 "knowledge_point_id": "{knowledge_point['id']}"
"""