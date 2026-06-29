
python -c "
# 模拟不同掌握度下的目标难度
for mastery in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]:
    target = min(int(mastery * 5) + 1, 5)
    print(f'掌握度 {mastery} → 目标难度 {target}')
# 预期输出：0.0→1, 0.2→2, 0.4→3, 0.6→4, 0.8→5, 1.0→5(封顶)
"