
def recommend_next_kp(student_id: str, tracker: StudentTracker) -> str:
    """自适应推荐下一个最合适的知识点 ID。"""
    weak = tracker.get_weak_points(student_id)    # 掌握度 < 0.6，按升序排列
    studied = set(tracker.all_kp_ids(student_id)) # 已练习过的知识点
    all_ids = _all_kp_ids()                       # 知识图谱中所有知识点

    # 段1（最高优先级）：弱项中可学的
    for kp_id in weak:
        if kp_id in studied and _can_study(kp_id, tracker, student_id):
            return kp_id

    # 段2（次优先级）：未学过的先修知识点
    for kp_id in all_ids:
        if kp_id not in studied and _can_study(kp_id, tracker, student_id):
            return kp_id

    # 段3（兜底）：弱项中前置不满足也推荐
    if weak:
        return weak[0]

    # 全都掌握或无数据：返回第一个知识点
    return all_ids[0] if all_ids else "deriv-def"