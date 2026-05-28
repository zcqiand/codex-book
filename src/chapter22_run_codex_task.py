# 从第 22 章提取
# 来源：Codex 从入门到项目实践
# 封装示例：把 SDK 调用集中在一个函数中，方便未来迁移
from codex_app_server import Codex

def run_codex_task(prompt: str, model: str = "gpt-5.4") -> str | None:
    """执行一次 Codex 任务并返回最终回复。"""
    with Codex() as codex:
        thread = codex.thread_start(model=model)
        result = thread.run(prompt)
        return result.final_response