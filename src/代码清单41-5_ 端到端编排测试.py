
def test_run_full_session_with_fake_client():
    """用 fake client 跑完整三代理流程，验证编排顺序与成本累计。"""
    # planner(1) + tutor(2 步) + evaluator(1) = 4 次调用
    client = FakeClient([
        # planner
        "<rationale>递进</rationale><step>定义</step><step>法则</step>",
        # tutor step 1
        "<content>定义讲解</content><keypoints>要点 A；要点 B</keypoints>",
        # tutor step 2
        "<content>法则讲解</content><keypoints>要点 C；要点 D</keypoints>",
        # evaluator
        "<score>90</score><strengths>清晰</strengths><gaps>缺练习</gaps>"
        "<recommendation>加练习</recommendation>",
    ])
    tracker = CostTracker(budget_usd=1.0)

    memory = run_full_session("导数", client, tracker, max_steps=2)

    assert memory.plan is not None
    assert len(memory.lessons) == 2
    assert memory.evaluation is not None
    assert memory.evaluation.understanding_score == 90
    # 4 次调用：planner + 2 tutor + evaluator
    assert len(tracker.records) == 4
    agents_called = [r.agent for r in tracker.records]
    assert agents_called == ["planner", "tutor", "tutor", "evaluator"]