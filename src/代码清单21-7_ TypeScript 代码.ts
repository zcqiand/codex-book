const schema = {
  type: "object",
  properties: {
    summary: { type: "string" },
    status: { type: "string", enum: ["ok", "action_required"] },
    issues: {
      type: "array",
      items: {
        type: "object",
        properties: {
          file: { type: "string" },
          severity: { type: "string", enum: ["error", "warning"] },
          description: { type: "string" },
        },
        required: ["file", "severity", "description"],
      },
    },
  },
  required: ["summary", "status"],
  additionalProperties: false,
} as const;

const turn = await thread.run("审查 src/ 下所有文件的错误处理是否完整", {
  outputSchema: schema,
});

const report = JSON.parse(turn.finalResponse);
// report.status: "ok" | "action_required"
// report.issues: Array<{file, severity, description}>