
class StudentTracker:
    """学生追踪器，支持内存操作和 JSON 持久化。"""

    DEFAULT_DIR = "data/student_tracker"

    def __init__(self, data_dir: str | None = None):
        self._data_dir = data_dir or self.DEFAULT_DIR
        self._cache: dict[str, StudentRecord] = {}
        self._ensure_dir()

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
        record = self._load(student_id)
        now = StudentRecord._now_iso()

        kp_data = record.knowledge_points.get(kp_id, {
            "mastery": 0.0, "wrong_count": 0, "last_practiced": now,
        })
        delta = 0.1 if correct else -0.05
        new_mastery = max(0.0, min(1.0, kp_data.get("mastery", 0.0) + delta))

        record.knowledge_points[kp_id] = {
            "mastery": new_mastery,
            "wrong_count": kp_data.get("wrong_count", 0) + (0 if correct else 1),
            "last_practiced": now,
        }

        if not correct and question:
            record.wrong_answers.append({
                "kp_id": kp_id, "question": question,
                "student_answer": student_answer,
                "correct": False, "timestamp": now,
            })

        self._save(record)

    def get_weak_points(self, student_id: str) -> list[str]:
        """返回掌握度低于 0.6 的知识点 ID 列表，按掌握度升序。"""
        ...

    def get_mastery(self, student_id: str, kp_id: str) -> float:
        """查询指定知识点的掌握度，未练习过返回 0.0。"""
        ...