import asyncio
from codex_app_server import AsyncCodex

async def review_pr(repo_path: str, pr_title: str) -> dict:
    async with AsyncCodex() as codex:
        thread = await codex.thread_start(model="gpt-5.4")
        result = await thread.run(
            f"审查 {repo_path} 中的 PR「{pr_title}」，"
            "重点检查错误处理和边界条件，给出 pass/fail 结论"
        )
        return {
            "pr": pr_title,
            "result": result.final_response
        }

async def main():
    # 同时审查三个 PR
    tasks = [
        review_pr("./repo-a", "feat: 用户认证重构"),
        review_pr("./repo-b", "fix: 支付回调超时"),
        review_pr("./repo-c", "refactor: 数据库迁移脚本"),
    ]
    results = await asyncio.gather(*tasks)
    for r in results:
        print(f"\n=== {r['pr']} ===")
        print(r["result"])

asyncio.run(main())