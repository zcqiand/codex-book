
# 将代码清单36-3的函数定义保存为 knowledge_memory.py，然后在 Python 中测试：
python -c "
from knowledge_memory import record_wrong_answer, get_weak_points, update_mastery

# 模拟：学生 bob 做了 5 道题
record_wrong_answer('bob', 'q001', 'alg-7-02', 'calculation_error')
record_wrong_answer('bob', 'q002', 'alg-7-02', 'concept_confusion')
record_wrong_answer('bob', 'q003', 'alg-7-01', 'calculation_error')

# 查询薄弱点（应返回 alg-7-02 排第一）
weak = get_weak_points('bob')
print(f'薄弱知识点: {weak}')

# 更新掌握度
update_mastery('bob', 'alg-7-02', 0.6)
print('掌握度已更新')
"