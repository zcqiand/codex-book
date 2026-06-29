const turn = await thread.run("诊断测试失败原因并提出修复方案");
console.log(turn.finalResponse);  // Codex 的最终文本回复
console.log(turn.items);          // 本轮所有交换项（工具调用、消息、文件变更）