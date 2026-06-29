
def test_tutor_parses_lesson_content_and_keypoints():
    memory = SharedMemory(user_question="导数")
    tracker = CostTracker()
    client = FakeClient([
        "<content>导数描述瞬时变化率。</content>"
        "<keypoints>瞬时变化率；切线斜率；极限定义</keypoints>"
    ])

    lesson = run_tutor_step("导数定义", memory, client, tracker)

    assert lesson.step == "导数定义"
    assert "瞬时变化率" in lesson.content
    assert lesson.key_points == ("瞬时变化率", "切线斜率", "极限定义")
    assert lesson in memory.lessons