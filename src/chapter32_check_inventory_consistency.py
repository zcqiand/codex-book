# 从第 32 章提取
# 来源：Codex 从入门到项目实践

"""PreToolUse Hook：在调用发货 API 之前校验库存一致性。

Codex 在准备调用 POST /api/shipments 时执行此脚本。
如果库存数据异常（locked > current），返回非 0 拦截操作。
"""

import sys
import json
import sqlite3

def check_inventory_consistency():
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    # 检查是否有 locked_quantity > current_quantity 的异常记录
    cursor.execute("""
        SELECT i.product_id, p.name, p.sku,
               i.current_quantity, i.locked_quantity,
               i.current_quantity - i.locked_quantity AS available
        FROM inventory i
        JOIN products p ON i.product_id = p.id
        WHERE i.locked_quantity > i.current_quantity
    """)
    anomalies = cursor.fetchall()
    conn.close()

    if anomalies:
        print("❌ 库存数据异常——locked_quantity > current_quantity：")
        for row in anomalies:
            print(f"  商品ID={row[0]} {row[1]}({row[2]}) "
                  f"当前={row[3]} 锁定={row[4]} 可用={row[5]}")
        print("请先修复以上数据异常再执行发货操作。")
        sys.exit(1)  # 非 0 退出码 → Codex 拦截操作
    else:
        print("✅ 库存数据一致性检查通过")
        sys.exit(0)

if __name__ == "__main__":
    check_inventory_consistency()