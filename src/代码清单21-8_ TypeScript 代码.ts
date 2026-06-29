import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const ReviewSchema = z.object({
  summary: z.string(),
  status: z.enum(["ok", "action_required"]),
  issues: z.array(z.object({
    file: z.string(),
    severity: z.enum(["error", "warning"]),
    description: z.string(),
  })),
});

const turn = await thread.run("审查 src/ 下的错误处理", {
  outputSchema: zodToJsonSchema(ReviewSchema, { target: "openAi" }),
});