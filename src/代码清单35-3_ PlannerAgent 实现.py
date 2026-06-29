<!-- src:src-001,official_doc -->
class PlannerAgent:
    def __init__(self, llm_client):
        self.llm = llm_client
        self.system_prompt = """你是一个辅导系统规划员。
根据学生的当前状态，决定下一步行动：
- 如果学生刚接触新概念 → 选择 "teach"（需要先讲解）
- 如果学生已经理解基本概念 → 选择 "generate_question"（需要练习）
- 如果学生刚答完题 → 选择 "grade"（需要评分）
- 如果学生答错了 → 选择 "evaluate"（需要分析错因）或 "socratic"（需要追问引导）

输出格式：{"action": "teach|generate_question|grade|evaluate|socratic|done", "reasoning": "决策理由"}"""

    def decide(self, memory: SharedMemory) -> str:
        context = {
            "student_profile": memory.student_profile,
            "conversation_history": memory.conversation_history[-5:],
            "current_task": memory.current_task,
        }
        response = self.llm.chat([
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": f"学生状态：{context}"}
        ])
        return json.loads(response)["action"]