
class FakeClient:
    """按预设脚本返回响应的 fake client。

    responses 是 list[str]，按调用顺序依次返回。
    让测试能精确控制每个 Agent 看到什么输入。
    """

    def __init__(self, responses: list[str]):
        self.responses = list(responses)
        self.calls: list[dict] = []

    def create(self, *, model, max_tokens, system, messages):
        self.calls.append({"model": model, "system": system, "messages": messages})
        text = self.responses.pop(0)
        return FakeResponse(
            content=[FakeBlock(text=text)],
            usage=FakeUsage(input_tokens=100, output_tokens=len(text) // 4),
        )