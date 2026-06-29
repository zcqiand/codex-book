
python -c "
# 模拟：学生有 3 个知识点，掌握度分别为 0.5(临界)、0.3(弱)、0.8(已掌握)
# 规则1应优先选 0.5
mastery = {'alg-7-01': 0.3, 'alg-7-02': 0.5, 'alg-7-03': 0.8}
critical = [kp for kp,m in mastery.items() if 0.4 <= m <= 0.6]
print(f'临界点: {critical}')
print(f'推荐: {min(critical, key=lambda kp: mastery[kp])}')
# 预期：推荐 alg-7-02（临界且最弱）
"