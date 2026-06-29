// 进程 A：创建线程并保存 ID
const thread = codex.startThread();
const threadId = thread.id;  // 把 ID 存到数据库或环境变量
await thread.run("开始分析项目结构");
// 进程退出...

// 进程 B（可能是另一次 CI 运行）：恢复线程
const savedId = process.env.CODEX_THREAD_ID!;
const resumedThread = codex.resumeThread(savedId);
await resumedThread.run("继续刚才的分析，生成报告");