<!-- src:src-001,official_doc -->
class TutorAgent:
    def __init__(self, llm_client):
        self.llm = llm_client
        self.system_prompt = """你是一个耐心、有同理心的辅导老师。
你的任务是根据学生的理解程度，调整讲解的深度和方式。

讲解原则：
1. 从学生已知的知识出发，引出新概念（类比驱动）
2. 每讲完一个步骤，确认学生是否跟上（交互式）
3. 避免使用专业术语的堆砌，用生活化类比解释复杂概念
4. 如果学生表示困惑，换一种方式讲解，不要重复同样的表述

输出格式：
- explanation: 讲解内容（Markdown，支持代码块和公式）
- confirm_question: 确认学生是否理解的跟进问题"""

    def teach(self, memory: SharedMemory):
        knowledge_point = memory.read("current_knowledge_point")
        student_level = memory.student_profile.get("level", "beginner")

        prompt = f"知识点：{knowledge_point}\n学生水平：{student_level}"
        response = self.llm.chat([...])  # 简化表示
        memory.write("tutor_output", response)