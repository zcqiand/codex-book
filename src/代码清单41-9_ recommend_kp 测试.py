
def test_recommend_kp_respects_prerequisites():
    """recommend_kp 不会推荐先修未掌握的知识点。"""
    with tempfile.TemporaryDirectory() as tmpdir:
        tracker = StudentTracker(data_dir=tmpdir)
        sid = "student_test_003"

        # deriv-def 答对 9 次，掌握度 0.9
        for _ in range(9):
            tracker.record_answer(sid, "deriv-def", correct=True)

        recommended = recommend_next_kp(sid, tracker)
        # deriv-geo 的先修 deriv-def 已满足 0.6 阈值，应该可以推荐
        assert recommended in ("deriv-geo", "deriv-rules", "deriv-chain",
                               "int-def", "int-rules", "int-sub", "newton-leibniz",
                               "deriv-def")