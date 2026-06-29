<!-- src:src-001,official_doc -->
class FakeClient:
    """测试用 LLM 客户端：注入预定义响应，不调用真实 API"""
    def __init__(self, responses: dict[str, str]):
        self.responses = responses
        self.call_history = []

    def chat(self, messages: list[dict]) -> str:
        key = self._get_key(messages)
        self.call_history.append({"key": key, "messages": messages})
        return self.responses.get(key, '{"action": "done"}')

    def _get_key(self, messages: list[dict]) -> str:
        # 简化：取最后一条用户消息的哈希作为 key
        return hash(str(messages[-1])) % 10000