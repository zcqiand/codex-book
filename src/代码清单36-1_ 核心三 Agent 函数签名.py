
# planner：根据用户问题制定学习路径
def run_planner(memory: SharedMemory, client: LLMClient, tracker: CostTracker) -> LearningPlan:
    """planner：根据用户问题制定学习路径。"""
    # 输出格式：<rationale>...</rationale><step>步骤1</step><step>步骤2</step>...
    ...

# tutor：讲解学习路径中的某一步
def run_tutor_step(
    step: str,
    memory: SharedMemory,
    client: LLMClient,
    tracker: CostTracker,
) -> Lesson:
    """tutor：讲解学习路径中的某一步。"""
    # 输出格式：<content>讲解正文（markdown）</content><keypoints>要点1；要点2</keypoints>
    ...

# evaluator：评估本次学习的效果
def run_evaluator(memory: SharedMemory, client: LLMClient, tracker: CostTracker) -> Evaluation:
    """evaluator：评估本次学习的效果。"""
    # 输出格式：<score>0-100</score><strengths>优点1；优点2</strengths><gaps>不足1</gaps><recommendation>建议</recommendation>
    ...