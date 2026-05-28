# 从第 20 章提取
# 来源：Codex 从入门到项目实践
import asyncio
from codex_app_server import AsyncCodex

async def main():
    async with AsyncCodex() as codex:
        thread = await codex.thread_start(model="gpt-5.4")
        result = await thread.run("实现一个快速排序函数")
        print(result.final_response)

asyncio.run(main())