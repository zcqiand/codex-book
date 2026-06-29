<!-- src:src-001,official_doc -->
def agent_loop(memory: SharedMemory, max_iterations=10):
    """Agent 循环：直到任务完成或达到最大迭代次数"""
    iteration = 0
    while iteration < max_iterations:
        # 1. Planner 决定下一步
        next_action = planner.decide(memory)

        if next_action == "teach":
            tutor.teach(memory)
        elif next_action == "generate_question":
            question_maker.generate(memory)
        elif next_action == "grade":
            grader.grade(memory)
        elif next_action == "evaluate":
            evaluator.evaluate(memory)
        elif next_action == "done":
            break  # 任务完成

        iteration += 1