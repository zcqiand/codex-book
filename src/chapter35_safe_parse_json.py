# 从第 35 章提取
# 来源：Codex 从入门到项目实践

def safe_parse_json(agent_response: str, agent, retry_prompt: str = "只输出JSON，不含解释"):
    """尝试解析JSON，失败则重试一次。"""
    try:
        return json.loads(agent_response)
    except json.JSONDecodeError:
        return json.loads(await agent.send(retry_prompt))