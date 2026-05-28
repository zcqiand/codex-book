# 从第 36 章提取
# 来源：Codex 从入门到项目实践

from codex import Codex

def record_wrong_answer(student_id: str, question_id: str,
                        knowledge_point_id: str, error_type: str):
    """批改 Agent 发现错题后，记录到学生 Memory。"""
    client = Codex()
    memory = client.memory(f"student:{student_id}:wrong_answers")
    existing = memory.get(default=[])
    existing.append({
        "question_id": question_id,
        "knowledge_point_id": knowledge_point_id,
        "error_type": error_type,
        "timestamp": "2026-05-06T10:30:00Z",
    })
    memory.set(existing)


def get_weak_points(student_id: str, top_n: int = 3) -> list[str]:
    """分析学生最薄弱的知识点（错题最多的 top N）。"""
    client = Codex()
    memory = client.memory(f"student:{student_id}:wrong_answers")
    wrong_records = memory.get(default=[])
    from collections import Counter
    kp_counter = Counter(r["knowledge_point_id"] for r in wrong_records)
    return [kp_id for kp_id, _ in kp_counter.most_common(top_n)]


def update_mastery(student_id: str, knowledge_point_id: str,
                   mastery_level: float):
    """更新某个知识点的掌握度（0.0 = 完全不掌握，1.0 = 完全掌握）。"""
    client = Codex()
    memory = client.memory(f"student:{student_id}:mastery")
    mastery = memory.get(default={})
    mastery[knowledge_point_id] = mastery_level
    memory.set(mastery)