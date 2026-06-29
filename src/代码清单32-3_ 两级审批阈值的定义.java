
private static final BigDecimal TWO_LEVEL_APPROVAL_THRESHOLD = new BigDecimal("1000");

@Transactional
public Order createOrder(CreateOrderRequest request) {
    // ... 创建订单逻辑 ...

    order.calculateTotalAmount();

    // 根据订单金额决定审批级别
    if (order.getTotalAmount().compareTo(TWO_LEVEL_APPROVAL_THRESHOLD) >= 0) {
        order.setApprovalLevel(2); // >= 1000元: 部门经理 + 财务总监两级审批
    } else {
        order.setApprovalLevel(1); // < 1000元: 直属经理一级审批
    }

    // 下单时锁定库存
    for (OrderItem item : order.getItems()) {
        inventoryService.lockInventory(item.getProduct().getId(), item.getQuantity());
    }

    return orderRepository.save(order);
}