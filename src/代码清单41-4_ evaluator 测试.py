
def test_evaluator_parses_score_and_recommendation():
    from ai_tutoring.shared_memory import LearningPlan, Lesson
    memory = SharedMemory(user_question="导数")
    memory.plan = LearningPlan(topic="导数", steps=("定义",), rationale="r")
    memory.lessons.append(Lesson(step="定义", content="讲解", key_points=("a",)))

    client = FakeClient([
        "<score>85</score>"
        "<strengths>讲解清晰；例子贴切</strengths>"
        "<gaps>缺少练习题</gaps>"
        "<recommendation>下次加练习</recommendation>"
    ])
    tracker = CostTracker()

    ev = run_evaluator(memory, client, tracker)

    assert ev.understanding_score == 85
    assert ev.strengths == ("讲解清晰", "例子贴切")
    assert ev.gaps == ("缺少练习题",)
    assert ev.recommendation == "下次加练习"