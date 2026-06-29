// 接续上面的 thread——Codex 记得之前的上下文
const result2 = await thread.run(
  "在 README 中补充一个「本地开发」节，包含安装和运行步骤"
);
console.log(result2);