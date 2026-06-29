<!-- src:src-001,official_doc -->
def test_multi_agent_workflow():
    # 1. 准备 FakeClient（注入所有 Agent 的响应）
    fake_client = FakeClient({
        "planner_decide": '{"action": "teach", "reasoning": "学生是新手，需要先讲解"}',
        "tutor_explain": '{"explanation": "一元二次方程是指...", "confirm_question": "你理解了吗？"}',
        "evaluator_result": '{"verdict": "partial", "analysis": "公式记忆有误", "misconception_point": "求根公式"}',
        "question_generate": '{"question": "求 x^2 - 5x + 6 = 0 的根", "answer": "x=2 或 x=3"}',
        "grader_score": '{"score": 3, "max_score": 5, "feedback": "公式用错了", "next_action": "socratic"}',
        "socratic_questions": '{"questions": ["求根公式是什么？", "你记得公式的符号吗？"], "hint": "公式是 (-b ± √(b²-4ac)) / 2a", "expected_breakthrough": "学生应纠正符号错误"}',
    })

    # 2. 初始化 SharedMemory 和所有 Agent
    memory = SharedMemory()
    memory.student_profile = {"name": "小明", "level": "beginner"}
    memory.current_knowledge_point = "一元二次方程求根公式"

    planner = PlannerAgent(fake_client)
    tutor = TutorAgent(fake_client)
    evaluator = EvaluatorAgent(fake_client)
    question_maker = QuestionMakerAgent(fake_client)
    grader = GraderAgent(fake_client)
    socratic_tutor = SocraticTutorAgent(fake_client)

    # 3. 运行 Agent Loop
    result = agent_loop(
        memory,
        agents=[planner, tutor, evaluator, question_maker, grader, socratic_tutor],
        max_iterations=10
    )

    # 4. 验证结果
    assert result["status"] == "completed"
    assert len(fake_client.call_history) <= 10  # 不超过最大迭代次数
    assert memory.grading_result["score"] == 3