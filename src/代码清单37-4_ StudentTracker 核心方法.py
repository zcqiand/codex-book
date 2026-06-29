
class StudentTracker:
    """学生追踪器，支持内存操作和 JSON 持久化。"""

    def record_answer(
        self,
        student_id: str,
        kp_id: str,
        correct: bool,
        *,
        question: str = "",
        student_answer: str = "",
    ) -> None:
        """记录一次作答，更新掌握度和错题本。
        答对 +0.1（上限 1.0），答错 -0.05（下限 0.0）。
        """

    def get_weak_points(self, student_id: str) -> list[str]:
        """返回掌握度低于 0.6 的知识点 ID 列表，按掌握度升序。"""

    def get_mastery(self, student_id: str, kp_id: str) -> float:
        """查询指定知识点的掌握度，未练习过返回 0.0。"""

    def all_kp_ids(self, student_id: str) -> list[str]:
        """返回该学生已练习过的所有知识点 ID。"""