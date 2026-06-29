
cat > test_with_timeout.py << 'EOF'
import concurrent.futures
import time

def agent_call_with_timeout(agent_func, timeout=30):
    """为 Agent 调用添加超时控制。"""
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(agent_func)
        try:
            result = future.result(timeout=timeout)
            return {"status": "ok", "result": result}
        except concurrent.futures.TimeoutError:
            return {"status": "timeout", "error": f"Agent 调用超时（{timeout}秒）"}

# 测试超时处理
def slow_agent():
    time.sleep(35)  # 模拟一个耗时 35 秒的 Agent 调用
    return "完成"

result = agent_call_with_timeout(slow_agent, timeout=30)
print(f"测试结果: {result}")
EOF

python test_with_timeout.py