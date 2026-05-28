# 从第 31 章提取
# 来源：Codex 从入门到项目实践

from mcp.server import Server, stdio_server
from mcp.types import Tool, TextContent

MOCK_SUPPLIER_INVENTORY = {
    "SUP-A-001": {"name": "蓝牙耳机", "stock": 500, "lead_time_days": 3},
    "SUP-A-002": {"name": "USB-C 数据线", "stock": 1200, "lead_time_days": 2},
    "SUP-B-001": {"name": "手机壳", "stock": 80, "lead_time_days": 5},
}

server = Server("supplier-inventory")

@server.tool()
async def check_stock(supplier_id: str, sku: str) -> str:
    """查询指定供应商的指定商品库存和交货周期。

    Args:
        supplier_id: 供应商编号，如 SUP-A-001
        sku: 商品 SKU
    """
    key = f"{supplier_id}-{sku}"
    item = MOCK_SUPPLIER_INVENTORY.get(key)
    if not item:
        return f"供应商 {supplier_id} 未提供 SKU={sku} 的商品"
    return (
        f"供应商: {supplier_id}\n"
        f"商品: {item['name']}\n"
        f"可用库存: {item['stock']} 件\n"
        f"交货周期: {item['lead_time_days']} 天"
    )

@server.tool()
async def place_supplier_order(supplier_id: str, sku: str, quantity: int) -> str:
    """向供应商下单采购（模拟）。

    Args:
        supplier_id: 供应商编号
        sku: 商品 SKU
        quantity: 采购数量
    """
    key = f"{supplier_id}-{sku}"
    item = MOCK_SUPPLIER_INVENTORY.get(key)
    if not item:
        return f"错误: 供应商 {supplier_id} 无此商品"
    if quantity > item["stock"]:
        return f"错误: 需求量 {quantity} 超过供应商库存 {item['stock']}"
    item["stock"] -= quantity
    return f"采购单已创建: {supplier_id} × {item['name']} × {quantity}件, 预计 {item['lead_time_days']} 天后到货"

if __name__ == "__main__":
    import asyncio
    asyncio.run(stdio_server(server))