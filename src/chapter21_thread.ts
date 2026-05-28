// 从第 21 章提取
// 来源：Codex 从入门到项目实践
const thread = codex.startThread({
  workingDirectory: "/path/to/project",  // 指定工作目录，默认 process.cwd()
  skipGitRepoCheck: true,                // 跳过 Git 仓库检查
});