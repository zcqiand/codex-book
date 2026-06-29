
class CostTracker:
    """记录每次 LLM 调用的 Token 消耗。"""

    def __init__(self, budget_usd: float = 0.50):
        self.budget_usd = budget_usd
        self.records: list[CostRecord] = []

    def track(self, agent: str, model: str,
              input_tokens: int, output_tokens: int) -> None:
        """记录一次调用，若超预算则抛 BudgetExceededError。"""
        record = CostRecord(...)
        self.records.append(record)
        if self.total_cost > self.budget_usd:
            raise BudgetExceededError(...)

    def format_summary(self) -> str:
        """输出格式化消耗报告。"""
        ...