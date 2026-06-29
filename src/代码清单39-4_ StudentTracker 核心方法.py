
class StudentTracker:
    def record_answer(self, student_id, kp_id, correct, *, question="", student_answer="") -> None:
        """记录作答，答对+0.1，答错-0.05，更新错题本。"""

    def get_weak_points(self, student_id: str) -> list[str]:
        """返回掌握度 < 0.6 的知识点列表，按掌握度升序。"""
        record = self._load(student_id)
        weak = [
            (kp_id, data.get("mastery", 0.0))
            for kp_id, data in record.knowledge_points.items()
            if data.get("mastery", 1.0) < 0.6
        ]
        weak.sort(key=lambda x: x[1])
        return [kp_id for kp_id, _ in weak]

    def get_mastery(self, student_id: str, kp_id: str) -> float:
        """查询掌握度，未练习过返回 0.0。"""
        record = self._load(student_id)
        return record.knowledge_points.get(kp_id, {}).get("mastery", 0.0)

    def all_kp_ids(self, student_id: str) -> list[str]:
        """返回该学生已练习过的所有知识点 ID。"""
        record = self._load(student_id)
        return list(record.knowledge_points.keys())

    def get_wrong_answers(self, student_id: str, kp_id: str | None = None) -> list[dict]:
        """获取错题本，可按 kp_id 过滤。"""