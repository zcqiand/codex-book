const codex = new Codex({
  env: { MY_CUSTOM_VAR: "value" },    // 注入额外环境变量
  baseUrl: "https://custom-api.example.com",  // 自定义 API 端点
  config: {                            // 任意 CLI 配置项
    show_raw_agent_reasoning: true,
    sandbox_workspace_write: { network_access: true },
  },
});