result = thread.run("删除所有临时文件")
if result.final_response:
    print("Codex 回复:", result.final_response)
else:
    print("Codex 已完成操作（无文本回复）")
    # 可以通过其他方式验证操作结果，例如 os.listdir()