// 从第 20 章提取
// 来源：Codex 从入门到项目实践
import { Codex } from "@openai/codex-sdk";

async function main() {
  // 1. 创建 Codex 实例
  const codex = new Codex();

  // 2. 启动一个新线程
  const thread = codex.startThread();

  // 3. 发送提示词，等待执行完成
  const result = await thread.run(
    "分析当前项目的目录结构，生成一份 README.md 草稿"
  );

  // 4. 输出最终结果
  console.log("=== Codex 输出 ===");
  console.log(result);
  console.log("=== 完成 ===");
}

main().catch(console.error);