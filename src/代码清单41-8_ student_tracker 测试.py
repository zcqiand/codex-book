
def test_record_answer_updates_mastery():
    """record_answer 答对增加掌握度，答错降低。"""
    with tempfile.TemporaryDirectory() as tmpdir:
        tracker = StudentTracker(data_dir=tmpdir)
        sid = "student_test_001"

        # 第一次答错：0.0 - 0.05 = -0.05 → clamp to 0.0
        tracker.record_answer(sid, "deriv-def", correct=False, question="q1", student_answer="A")
        assert tracker.get_mastery(sid, "deriv-def") == 0.0

        # 第二次答对：0.0 + 0.1 = 0.1
        tracker.record_answer(sid, "deriv-def", correct=True, question="q2", student_answer="B")
        assert tracker.get_mastery(sid, "deriv-def") == 0.1

        # 第三次答对：0.1 + 0.1 = 0.2
        tracker.record_answer(sid, "deriv-def", correct=True, question="q3", student_answer="C")
        assert tracker.get_mastery(sid, "deriv-def") == 0.2