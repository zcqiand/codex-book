
def test_parse_question():
    """_parse_question 能正确解析 LLM 输出的 XML 标签。"""
    text = (
        "<question>链式法则求导：若 y = sin(x²)，则 dy/dx = ？</question>\n"
        "<optionA>A. cos(x²)</optionA>\n"
        "<optionB>B. 2x·cos(x²)</optionB>\n"
        "<optionC>C. x²·cos(x²)</optionC>\n"
        "<optionD>D. 2cos(x²)</optionD>\n"
        "<answer>B</answer>\n"
        "<explanation>复合函数求导：外层 sin 的导数为 cos，内层 x² 的导数为 2x，故结果为 2x·cos(x²)。</explanation>"
    )
    result = _parse_question(text)

    assert "链式法则" in result["question"]
    assert len(result["options"]) == 4
    assert result["answer"] == "B"
    assert "复合函数" in result["explanation"]