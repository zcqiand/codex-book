# 从第 22 章提取
# 来源：Codex 从入门到项目实践
from codex_app_server import Codex

with Codex() as codex:
    thread = codex.thread_start(model="gpt-5.4")
    result = thread.run("列出当前项目的目录结构，总结每个目录的用途")
    print(result.final_response)