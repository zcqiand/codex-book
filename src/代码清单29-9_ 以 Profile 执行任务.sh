
# 让 Codex 基于你的 ER 设计生成完整 Entity 类
# 把表29-1的列设计粘贴进Prompt作为上下文
codex exec --dangerously-bypass-approvals-and-sandbox \
  "基于以下ER设计生成 JPA Entity 类:
  （粘贴你的ER设计）
  要求: 使用 Jakarta Persistence 注解，每个字段类型和约束正确，
  relationship 使用 @ManyToOne/@OneToOne/@OneToMany，Enum 类型使用 @Enumerated(EnumType.STRING)。"