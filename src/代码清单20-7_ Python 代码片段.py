from codex_app_server import Codex

with Codex() as codex:
    thread = codex.thread_start(model="gpt-5.4")
    result = thread.run("分析当前项目的目录结构，生成一份 README.md 草稿")
    print(result.final_response)