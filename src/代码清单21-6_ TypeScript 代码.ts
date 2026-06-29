import { Codex } from "@openai/codex-sdk";

async function diagnoseCI() {
  const codex = new Codex();
  const thread = codex.startThread({ skipGitRepoCheck: true });

  const { events } = await thread.runStreamed(
    "分析最近的 CI 失败日志，找出根因并生成修复 PR 描述"
  );

  let completedSteps = 0;
  for await (const event of events) {
    if (event.type === "item.completed") {
      completedSteps++;
      console.log(`[步骤 ${completedSteps}] 完成:`, event.item);
    } else if (event.type === "turn.completed") {
      console.log(`\n执行完成，共 ${completedSteps} 个步骤`);
      console.log("Token 用量:", event.usage);
    }
  }
}

diagnoseCI().catch(console.error);