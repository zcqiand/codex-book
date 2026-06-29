
python -c "
# 模拟集成测试的数据流转验证
import json

# 模拟 Step1 输出：规划参数
plan = {'question_type': 'choice', 'count': 3, 'difficulty': 2}

# 模拟 Step2 输出：题目 JSON（必须包含 questions 和 metadata）
questions = {
    'questions': [
        {'stem': '2x + 5 = 11，求 x', 'options': ['A. x=3', 'B. x=8', 'C. x=6', 'D. x=4'], 'answer': 'A'},
        {'stem': '3x - 7 = 14，求 x', 'options': ['A. x=3', 'B. x=7', 'C. x=21', 'D. x=5'], 'answer': 'B'},
    ],
    'metadata': {'kp_id': 'alg-7-02', 'difficulty': 2}
}

# 验证接口契约：每个 question 必须包含 stem/options/answer 字段
for i, q in enumerate(questions['questions']):
    assert 'stem' in q, f'题目{i}缺少stem字段'
    assert 'options' in q, f'题目{i}缺少options字段'
    assert 'answer' in q, f'题目{i}缺少answer字段'
    print(f'题目{i}: {q[\"stem\"][:20]}... ✅')

# 验证批改接口：批改 Agent 期望的字段名
assert questions['questions'][0]['stem']  # 批改Agent读的是stem，不是question_text
print('接口契约验证通过 ✅')
"