
def test_parse_grade_correct():
    """_parse_grade 解析正确答案返回 correct=True。"""
    text = (
        "<correct>true</correct>\n"
        "<score>100</score>\n"
        "<feedback>回答正确！掌握链式法则的核心。</feedback>\n"
        "<step_analysis>先求外层导数 cos(x²)，再乘内层导数 2x。</step_analysis>"
    )
    result = _parse_grade(text)

    assert result["correct"] is True
    assert result["score"] == 100
    assert "正确" in result["feedback"]