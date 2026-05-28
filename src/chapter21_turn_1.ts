// 从第 21 章提取
// 来源：Codex 从入门到项目实践
const turn = await thread.run([
  { type: "text", text: "对比这两张 UI 截图与设计稿的差异，列出所有不一致之处" },
  { type: "local_image", path: "./screenshots/actual.png" },
  { type: "local_image", path: "./screenshots/design.png" },
]);