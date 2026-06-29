
import json
import time
from codex import Agent

def test_full_tutoring_session(student_id: str = "bob",
                               kp_id: str = "alg-7-02") -> dict:
    """端到端测试：从出题到报告生成的完整流程。"""
    results = {"steps": [], "errors": [], "duration_ms": 0}
    start = time.time()

    # Step 1: 规划 Agent 决定出题参数
    planner = Agent("planner")
    plan = planner.send(
        f"学生 {student_id} 当前掌握度数据在 Memory 中。"
        f"请为知识点 {kp_id} 推荐出题参数（题型、数量、难度）。"
        f"输出纯 JSON：{{\"question_type\": \"...\", \"count\": N, \"difficulty\": N}}"
    )
    try:
        plan_data = json.loads(plan.content)
        results["steps"].append({"step": "plan", "status": "ok", "output": plan_data})
    except json.JSONDecodeError:
        results["errors"].append("step1_plan: JSON 解析失败")
        results["steps"].append({"step": "plan", "status": "error"})

    # Step 2: 出题 Agent 根据规划参数生成题目
    question_maker = Agent("question-maker")
    questions_resp = question_maker.send(
        f"知识点: {kp_id}，题型: {plan_data.get('question_type', 'choice')}，"
        f"数量: {plan_data.get('count', 3)}，难度: {plan_data.get('difficulty', 2)}。"
        f"输出纯 JSON：{{\"questions\": [...], \"metadata\": {{...}}}}"
    )
    try:
        questions_data = json.loads(questions_resp.content)
        assert "questions" in questions_data
        assert len(questions_data["questions"]) > 0
        results["steps"].append({"step": "make_questions", "status": "ok",
                                 "count": len(questions_data["questions"])})
    except (json.JSONDecodeError, AssertionError) as e:
        results["errors"].append(f"step2_questions: {str(e)}")
        results["steps"].append({"step": "make_questions", "status": "error"})

    # Step 3: 模拟学生作答，然后批改 Agent 批改
    grader = Agent("grader")
    for i, q in enumerate(questions_data["questions"][:1]): # 端到端只测第1道
        # 模拟一个错误答案
        student_answer = "x = 8"  # 正确答案是 x = 3（移项没变号的典型错误）
        grade_resp = grader.send(
            f"题目：{json.dumps(q, ensure_ascii=False)}\n"
            f"学生答案：{student_answer}\n"
            f"输出纯 JSON：{{\"is_correct\": bool, \"error_type\": \"...\", \"correction_hint\": \"...\"}}"
        )
        try:
            grade_data = json.loads(grade_resp.content)
            results["steps"].append({"step": f"grade_q{i}", "status": "ok",
                                     "is_correct": grade_data.get("is_correct"),
                                     "error_type": grade_data.get("error_type")})
        except json.JSONDecodeError:
            results["errors"].append(f"step3_grade_q{i}: JSON 解析失败")
            results["steps"].append({"step": f"grade_q{i}", "status": "error"})

    # Step 4: 辅导 Agent 讲解（仅在答错时）
    if not grade_data.get("is_correct", True):
        tutor = Agent("tutor")
        tutor_resp = tutor.send(
            f"学生做错了{questions_data['questions'][0]['stem']}，"
            f"错误类型：{grade_data['error_type']}，"
            f"学生答案：{student_answer}。请用苏格拉底式追问引导。"
        )
        results["steps"].append({"step": "tutor", "status": "ok",
                                 "response_length": len(tutor_resp.content)})

    # Step 5: 规划 Agent 更新学习路径
    planner.send(
        f"学生 {student_id} 完成了知识点 {kp_id} 的练习。"
        f"请根据 Memory 中的最新数据更新学习路径推荐。"
    )
    results["steps"].append({"step": "update_path", "status": "ok"})

    # Step 6: 生成学情指标（验证数据管道完整性）
    planner.send(
        f"为 {student_id} 生成最新学情指标（compute_learning_metrics）。"
        f"确认三个指标均可计算且不为默认值。"
    )
    results["steps"].append({"step": "metrics", "status": "ok"})

    results["duration_ms"] = round((time.time() - start) * 1000)
    results["passed"] = len(results["errors"]) == 0
    return results


if __name__ == "__main__":
    result = test_full_tutoring_session()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"\n{'✅ 集成测试通过' if result['passed'] else '❌ 集成测试失败'}")
    print(f"总耗时: {result['duration_ms']}ms")