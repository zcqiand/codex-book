
from typing import Optional

def recommend_next_kp(student_id: str, knowledge_graph: dict) -> Optional[str]:
    """推荐学生下一步应该学习/练习的知识点。三个规则按优先级排列。"""
    mastery = get_student_mastery(student_id)  # {kp_id: 0.0-1.0}
    
    # 规则1（最高优先级）：巩固临界点
    # 掌握度在 0.4-0.6 之间的知识点——"似懂非懂"状态，最需要练习
    critical = [
        kp for kp, m in mastery.items()
        if 0.4 <= m <= 0.6
    ]
    if critical:
        return min(critical, key=lambda kp: mastery[kp])  # 最弱的优先
    
    # 规则2（次优先级）：推进已解锁的前沿
    # 前置条件已满足但尚未学习的知识点
    unlocked = []
    for kp in knowledge_graph["knowledge_points"]:
        if kp["id"] in mastery and mastery[kp["id"]] >= 0.7:
            continue  # 已掌握，跳过
        prereqs_met = all(
            mastery.get(pr, 0) >= 0.7
            for pr in kp.get("prerequisites", [])
        )
        if prereqs_met:
            unlocked.append(kp["id"])
    if unlocked:
        return min(unlocked, key=lambda kp_id: knowledge_graph["knowledge_points"][kp_id]["difficulty"])
    
    # 规则3（兜底）：复习最早学的最弱知识点
    weakest = min(mastery.items(), key=lambda x: x[1])
    return weakest[0]