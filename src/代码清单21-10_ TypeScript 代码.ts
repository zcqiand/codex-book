const diagnosis = await thread.run([
  { type: "text", text: `E2E 测试失败。日志如下：\n${testLogs}\n\n请判断失败原因并给出修复建议。` },
  { type: "local_image", path: "./test-output/screenshot.png" },
]);