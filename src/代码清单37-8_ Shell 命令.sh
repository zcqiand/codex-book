
python -c "
# 层1: 数值比对
print(normalize_answer('x=3'))      # 期望: 3
print(normalize_answer('x = 3.0'))  # 期望: 3.0
print(normalize_answer('X=6/2'))    # 期望: 3.0 (需完善)

# 层3: 错误模式匹配
# 2x+5=11, 正确答案 x=3
# 常见错误: 移项不变号 → x=8 (2x=16)
# 常见错误: 去括号忘变号 → x=6
print('模拟批改 2x+5=11, 学生答案 x=8, 类型: 移项不变号')
"