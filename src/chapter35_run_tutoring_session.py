# 从第 35 章提取
# 来源：Codex 从入门到项目实践

from codex import Codex
import json

async def run_tutoring_session(student_request: str, student_profile: dict):
    """一次完整的辅导会话：规划→出题→批改→辅导。"""
    async with Codex() as codex:
        # 1. 规划 Agent：分析请求，决定需要哪些 Agent
        planner = codex.spawn("planner")
        plan = await planner.send(
            f"学生请求：{student_request}\n"
            f"学生画像：{json.dumps(student_profile)}\n"
            f"分析需要哪些 Agent，输出 JSON 格式任务分配。"
        )
        plan_result = json.loads(plan.text)

        # 2. 根据规划结果创建子 Agent
        sub_agents = {}
        results = {}
        for task in plan_result["tasks"]:
            match task["agent"]:
                case "question_maker":
                    sub = codex.spawn("question_maker")
                    results["questions"] = await sub.send(json.dumps(task["params"]))
                    sub_agents["question_maker"] = sub
                case "grader":
                    sub_agents["grader"] = codex.spawn("grader")
                case "tutor":
                    sub_agents["tutor"] = codex.spawn("tutor")

        if "student_answers" in plan_result and "grader" in sub_agents:
            grader = sub_agents["grader"]
            results["grading"] = await grader.send(json.dumps({
                "questions": results.get("questions"),
                "student_answers": plan_result["student_answers"],
            }))
            grading = json.loads(results["grading"].text)
            wrong = [r for r in grading.get("results", []) if not r["is_correct"]]
            if wrong and "tutor" in sub_agents:
                results["tutoring"] = await sub_agents["tutor"].send(json.dumps({
                    "wrong_questions": wrong, "student_profile": student_profile,
                }))

        # 4. 清理：关闭所有子 Agent
        for agent in sub_agents.values():
            agent.close()

        return {"plan": plan_result, "results": {k: v.text for k, v in results.items()}}