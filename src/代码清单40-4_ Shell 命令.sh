
python -c "
# 模拟 Memory 数据，测试三个指标的计算逻辑
# 假设学生 bob 有 5 个知识点，掌握度分别为 0.3/0.5/0.7/0.6/0.4
mastery = {'alg-7-01': 0.3, 'alg-7-02': 0.5, 'alg-7-03': 0.7, 'geo-7-01': 0.6, 'alg-7-04': 0.4}
overall = sum(mastery.values()) / len(mastery)
print(f'整体掌握度: {overall:.2f}')  # 期望: 0.50

# 模拟薄弱点：按错题数排序
from collections import Counter
wrong = [{'kp_id': 'alg-7-02'}, {'kp_id': 'alg-7-02'}, {'kp_id': 'alg-7-01'}, {'kp_id': 'alg-7-02'}, {'kp_id': 'alg-7-03'}]
kp_count = Counter(r['kp_id'] for r in wrong)
print(f'薄弱点: {kp_count.most_common(3)}')  # 期望: alg-7-02 排第一
"