
class SharedMemory:
    user_question: str
    plan: LearningPlan | None = None
    lessons: list[Lesson] = field(default_factory=list)
    evaluation: Evaluation | None = None

    def freeze_plan(self) -> LearningPlan:
        """返回不可变快照，供下游代理只读。若 plan 未生成则抛 ValueError。"""
        if self.plan is None:
            raise ValueError("plan 尚未生成")
        return self.plan

    def lessons_summary(self) -> str:
        """给 evaluator 看的已讲解内容摘要。"""
        if not self.lessons:
            return "(尚未讲解)"
        return "\n\n".join(
            f"【{l.step}】\n{l.content}\n关键要点：{', '.join(l.key_points)}"
            for l in self.lessons
        )