
def test_socratic_tutor_does_not_give_direct_answer():
    """回复不应包含直接答案的关键词。"""
    client = FakeClient([
        "试着想想：sin(u) 的导数是 cos(u)，那么 u 应该是什么？"
    ])
    result = socratic_tutor("导数", "sin(x²) 的导数是什么？", client)

    # 苏格拉底式回复不应直接给出"2x·cos(x²)"
    assert "2x" not in result or "cos" not in result