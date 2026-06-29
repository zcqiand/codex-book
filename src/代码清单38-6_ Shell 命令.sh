
mkdir -p math-tutor-plugin/.codex/{skills,agents,automations}
mkdir -p math-tutor-plugin/knowledge/初中数学
# 将代码清单38-3保存为 math-tutor-plugin/plugin.toml
# 复制前几章的 Skills/Agents/Automations 到对应目录
codex plugin install ./math-tutor-plugin
codex plugin list  # 确认 math-tutor 已安装