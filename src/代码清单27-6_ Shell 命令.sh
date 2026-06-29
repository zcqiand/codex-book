#!/bin/bash
# audit.sh ——将每次工具调用记录到审计日志
echo "[$(date -Iseconds)] Tool: $1 | Args: $2" >> /opt/codex-managed/audit.log
echo '{"decision": "allow"}'