cat > risk-schema.json << 'EOF'
{
  "type": "object",
  "properties": {
    "risks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "file": {"type": "string"},
          "severity": {"enum": ["low", "medium", "high", "critical"]},
          "description": {"type": "string"}
        },
        "required": ["file", "severity", "description"]
      }
    }
  },
  "required": ["risks"]
}
EOF

codex exec "扫描 src/ 目录的安全风险" \
  --output-schema ./risk-schema.json \
  -o ./risks.json