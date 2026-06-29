# 调用示例：生成 alg-7-02（一元一次方程解法）的自适应练习题
kp = {
    'id': 'alg-7-02',
    'name': '一元一次方程的解法',
    'prerequisites': ['alg-7-01', 'num-7-01'],
    'common_errors': [
        {'pattern': '移项不变号', 'error_type': 'calculation_error'},
        {'pattern': '去括号忘变号', 'error_type': 'concept_confusion'}
    ]
}
prompt = build_question_prompt(kp, student_mastery=0.6, question_type='choice', count=3)
# 将 prompt 发送给 Codex 出题 Agent，即可得到 3 道自适应难度的选择题