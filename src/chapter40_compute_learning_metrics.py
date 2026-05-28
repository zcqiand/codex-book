# 从第 40 章提取
# 来源：Codex 从入门到项目实践

from codex import Memory
from datetime import datetime, timedelta
from collections import defaultdict


def compute_learning_metrics(student_id: str, domain: str = "初中数学") -> dict:
    """从 Memory 原始数据中计算三个核心学情指标。"""
    mastery_mem = Memory(f"student:{student_id}:mastery")
    wrong_mem = Memory(f"student:{student_id}:wrong_answers")
    mastery = mastery_mem.get(default={})
    wrong_records = wrong_mem.get(default=[])

    if mastery:
        overall_mastery = round(sum(mastery.values()) / len(mastery), 2)
    else:
        overall_mastery = 0.0

    now = datetime.utcnow()
    week_ago = now - timedelta(days=7)
    recent_wrong = [
        r for r in wrong_records
        if datetime.fromisoformat(r["timestamp"]) > week_ago
    ]
    older_wrong = [
        r for r in wrong_records
        if datetime.fromisoformat(r["timestamp"]) <= week_ago
    ]
    total_recent = len(recent_wrong) + len([r for r in wrong_records
        if datetime.fromisoformat(r["timestamp"]) > week_ago and r.get("is_correct")])
    if len(wrong_records) > 0:
        recent_error_rate = len(recent_wrong) / max(len(wrong_records), 1)
        progress_rate = round(1 - recent_error_rate, 2)  # 越高越好
    else:
        progress_rate = 0.0

    # 指标3：薄弱点 Top 3（错题最多的知识点）
    kp_errors = defaultdict(int)
    for r in wrong_records:
        kp_errors[r["knowledge_point_id"]] += 1
    weak_points = sorted(kp_errors.items(), key=lambda x: x[1], reverse=True)[:3]

    return {
        "student_id": student_id,
        "domain": domain,
        "overall_mastery": overall_mastery,
        "progress_rate": progress_rate,
        "weak_points": [
            {"kp_id": kp, "error_count": cnt}
            for kp, cnt in weak_points
        ],
        "generated_at": now.isoformat()
    }