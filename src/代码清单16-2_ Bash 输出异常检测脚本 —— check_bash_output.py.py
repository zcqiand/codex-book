import sys, json

data = json.loads(sys.stdin.read())
output = data.get("tool_output", "")

ERROR_SIGNALS = [
    "Traceback (most recent call last)",
    "Error:",
    "FATAL:",
    "Segmentation fault",
    "command not found",
    "ModuleNotFoundError",
    "Cannot find module"
]

for signal in ERROR_SIGNALS:
    if signal in output:
        print(json.dumps({
            "decision": "block",
            "reason": f"检测到错误信号: {signal}",
            "explanation": "Bash 输出包含错误信息，建议先检查输出再继续。"
        }))
        sys.exit(0)

print(json.dumps({"decision": "allow"}))