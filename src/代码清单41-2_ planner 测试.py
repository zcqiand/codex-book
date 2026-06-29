
def test_planner_parses_steps_and_rationale():
    memory = SharedMemory(user_question="请教我导数")
    client = FakeClient([
        "<rationale>从定义到应用递进</rationale>"
        "<step>导数定义</step>"
        "<step>几何意义</step>"
        "<step>求导法则</step>"
    ])
    tracker = CostTracker()

    plan = run_planner(memory, client, tracker)

    assert plan.topic == "请教我导数"
    assert plan.rationale == "从定义到应用递进"
    assert plan.steps == ("导数定义", "几何意义", "求导法则")
    assert memory.plan is plan
    assert len(tracker.records) == 1
    assert tracker.records[0].agent == "planner"