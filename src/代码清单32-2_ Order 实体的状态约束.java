
@Enumerated(EnumType.STRING)
@Column(nullable = false)
private OrderStatus status;

// 状态转换的前置条件在 OrderService 中实现
// 以下是各转换的业务含义说明

// submitOrder: DRAFT → SUBMITTED
//   前置条件：当前状态必须是 DRAFT
//   副作用：设置 submittedAt 时间戳

// approveOrder: SUBMITTED → APPROVED
//   前置条件：当前状态必须是 SUBMITTED
//   副作用：设置 approvalNotes 审批备注

// rejectOrder: SUBMITTED → REJECTED
//   前置条件：当前状态必须是 SUBMITTED
//   副作用：解锁已锁定的库存，设置 cancellationReason

// payOrder: APPROVED → PAID
//   前置条件：当前状态必须是 APPROVED
//   副作用：扣减库存（从 locked 转入实际扣减），设置 paidAt

// shipOrder: PAID → SHIPPED
//   前置条件：当前状态必须是 PAID
//   副作用：设置 shippedAt

// completeOrder: SHIPPED → COMPLETED
//   前置条件：当前状态必须是 SHIPPED
//   副作用：设置 completedAt

// cancelOrder: 多个状态 → CANCELLED
//   前置条件：当前状态不是 COMPLETED 或 SHIPPED
//   副作用：根据当前状态决定是恢复库存还是释放锁定库存