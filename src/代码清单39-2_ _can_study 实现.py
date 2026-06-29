
def _can_study(kp_id: str, tracker: StudentTracker, student_id: str) -> bool:
    """判断学生是否可以学习该知识点（所有先修都已掌握 >= 0.6）。"""
    for prereq in _get_prerequisites(kp_id):
        if tracker.get_mastery(student_id, prereq) < 0.6:
            return False
    return True