<!-- src:src-001,official_doc -->
class SharedMemory:
    """所有 Agent 共享的上下文容器"""
    def __init__(self):
        self.student_profile = {}      # 学生画像：年级、学科、薄弱点
        self.conversation_history = [] # 对话历史
        self.current_task = None       # 当前任务
        self.evaluation_result = None  # 最近一次评估结果
        self.generated_questions = []  # 已生成的练习题
        self.grading_result = None     # 最近一次评分结果

    def write(self, key, value):
        setattr(self, key, value)

    def read(self, key):
        return getattr(self, key, None)