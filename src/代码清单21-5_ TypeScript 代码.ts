const { events } = await thread.runStreamed(
  "诊断测试失败原因并提出修复方案"
);

for await (const event of events) {
  switch (event.type) {
    case "item.completed":
      console.log("[完成]", event.item);
      break;
    case "turn.completed":
      console.log("[轮次结束]", "token 用量:", event.usage);
      break;
    default:
      console.log("[事件]", event.type);
  }
}