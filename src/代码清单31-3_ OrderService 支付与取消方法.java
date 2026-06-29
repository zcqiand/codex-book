
    public Order payOrder(Long orderId) {
        Order order = getOrderById(orderId);
        if (order == null) {
            throw new IllegalArgumentException("订单不存在");
        }
        if (!order.getStatus().canTransitionTo(OrderStatus.PAID)) {
            throw new IllegalArgumentException("非法状态转换: " + order.getStatus() + " → PAID");
        }

        // 逐项实扣库存（幂等：使用 lockedQuantity 判断）
        for (OrderItem item : order.getItems()) {
            inventoryService.deductInventory(item.getProductId(), item.getQuantity());
        }

        order.setStatus(OrderStatus.PAID);
        return orderRepository.save(order);
    }

    public Order cancelOrder(Long orderId, String reason) {
        Order order = getOrderById(orderId);
        if (order == null) {
            throw new IllegalArgumentException("订单不存在");
        }
        if (!order.getStatus().canTransitionTo(OrderStatus.CANCELLED)) {
            throw new IllegalArgumentException("非法状态转换: " + order.getStatus() + " → CANCELLED");
        }

        // 取消时根据当前状态决定如何处理库存
        for (OrderItem item : order.getItems()) {
            if (order.getStatus() == OrderStatus.PAID || order.getStatus() == OrderStatus.SHIPPED) {
                // 已支付/已发货取消：退款回仓
                inventoryService.restoreInventory(item.getProductId(), item.getQuantity());
            } else {
                // 未支付取消：释放锁定库存
                inventoryService.unlockInventory(item.getProductId(), item.getQuantity());
            }
        }

        order.setStatus(OrderStatus.CANCELLED);
        return orderRepository.save(order);
    }