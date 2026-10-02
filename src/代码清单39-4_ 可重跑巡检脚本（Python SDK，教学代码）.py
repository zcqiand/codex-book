# 教学代码，非案例仓源码；巡检全走只读侧，不写任何产品数据。
import asyncio
import subprocess
import sys
from pathlib import Path

from codex_app_server import AsyncCodex

MAX_CONCURRENT = 5  # 第 22 章口径：每个线程独占一条 App Server 连接，并发上限 5
MODEL = "gpt-5.4"   # 第 22 章口径：Python SDK 无默认模型，必须显式指定
REPORT_DIR = Path("./reports")

# 巡检清单：4 条任务覆盖全部 7 项清单 40 个核对点，任务分组与代码清单 39-2 一致
INSPECTIONS = [
    {"name": "tenant-detail", "prompt": "巡检清单第 1 项：核对 acme-dev 与 acme-prod 的名称、状态、成员数、建档时间，逐点回报核对值与 pass/fail 判定，只读核对不做修改"},
    {"name": "tenant-apps", "prompt": "巡检清单第 2-3 项：核对两租户应用列表订阅行数对账与到期显示格式，扫描订阅到期日在档并标记临期 30 天，只读核对不做修改"},
    {"name": "client-meta", "prompt": "巡检清单第 4 项：核对 4 个在册 client 元数据可读、名称一致、回调域在册，逐点回报判定，只读核对不做修改"},
    {"name": "menu-order", "prompt": "巡检清单第 5-7 项：核对菜单同级序号连续且无重复、租户状态在 0/1/2 允许集内、订阅状态与台账一致，只读核对不做修改"},
]


def ensure_app_server() -> None:
    # 实验性 SDK 的务实策略，见第 22 章：SDK 与 App Server 版本不匹配会产生静默错误，
    # 启动时先确认可用：宁可启动失败，不要跑一半才发现连不上
    try:
        subprocess.run(["codex", "--version"], check=True, capture_output=True)
    except (OSError, subprocess.CalledProcessError) as exc:
        sys.exit(f"App Server 不可用，终止巡检：{exc}")


async def run_one(codex, item) -> dict:
    try:
        thread = await codex.thread_start(model=MODEL)
        result = await thread.run(item["prompt"])
        # 防御性检查（第 22 章口径）：final_response 为空按该任务失败计，记录后继续
        if not result.final_response:
            return {"name": item["name"], "ok": False, "path": "-"}
        path = REPORT_DIR / f"{item['name']}.json"
        path.write_text(result.final_response, encoding="utf-8")
        return {"name": item["name"], "ok": True, "path": str(path)}
    except Exception as exc:  # 单任务异常只记录不扩散，保证整批收齐结果
        return {"name": item["name"], "ok": False, "path": f"error: {exc}"}


async def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    async with AsyncCodex() as codex:
        # 通用分批（第 22 章口径）：并发超过上限时按批 gather，批与批之间串行
        for i in range(0, len(INSPECTIONS), MAX_CONCURRENT):
            batch = INSPECTIONS[i:i + MAX_CONCURRENT]
            results.extend(await asyncio.gather(*(run_one(codex, t) for t in batch)))
    for r in results:
        verdict = "成功" if r["ok"] else "失败"
        print(f"[{verdict}] {r['name']} -> {r['path']}")


if __name__ == "__main__":
    ensure_app_server()
    asyncio.run(main())