# 保存为 ~/.codex/hooks/security_gate.py
import json, sys, re

BLOCKED_PATTERNS = [
    r'\brm\s+(-[rRf]+\s+)*[/~]',    # rm 作用于根目录或 home
    r'\bsudo\b',                       # sudo 提权
    r'\bchmod\s+777\b',               # 过度放宽权限
    r'/etc/',                          # 操作系统配置目录
    r'>\s*/dev/[a-z]+[0-9]*\b',       # 直接写入设备文件
]

def main():
    data = json.load(sys.stdin)
    command = data.get("tool_input", {}).get("command", "")

    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, command):
            result = {
                "continue": True,
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason":
                        f"安全策略拦截：命令匹配危险模式 '{pattern}'"
                }
            }
            json.dump(result, sys.stdout)
            return

    # 未匹配危险模式——放行（不输出 = 批准）
    json.dump({"continue": True}, sys.stdout)

if __name__ == "__main__":
    main()