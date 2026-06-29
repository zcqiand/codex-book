
def recommend_next_kp(student_id: str, tracker: StudentTracker) -> str:
    """自适应推荐下一个最合适的知识点 ID。

    优先级：
    1. 弱项中可学的（薄弱且前置已满足）
    2. 未学过的先修知识点（前置已满足但未练习）
    3. 已掌握知识点的进阶（前置已满足）
    """
    weak = tracker.get_weak_points(student_id)   # 掌握度 < 0.6 的知识点
    studied = set(tracker.all_kp_ids(student_id)) # 已练习过的知识点
    all_ids = _all_kp_ids()                       # 知识图谱中所有知识点

    # 优先从弱项中选择可学的
    for kp_id in weak:
        if kp_id in studied and _can_study(kp_id, tracker, student_id):
            return kp_id

    # 寻找未学过的知识点（前置已满足）
    for kp_id in all_ids:
        if kp_id not in studied and _can_study(kp_id, tracker, student_id):
            return kp_id

    # 从弱项中放宽条件（前置不满足也推荐，但提示前置未掌握）
    if weak:
        return weak[0]

    # 全都掌握或无数据，返回第一个知识点作为兜底
    return all_ids[0] if all_ids else "deriv-def"