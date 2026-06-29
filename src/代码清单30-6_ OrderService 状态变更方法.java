
    public Order submitOrder(Long orderId) {
        Order order = getOrderById(orderId);
        if (order == null) {
            throw new IllegalArgumentException("订单不存在");
        }
        if (!order.getStatus().canTransitionTo(OrderStatus.SUBMITTED)) {
            throw new IllegalArgumentException("非法状态转换: " + order.getStatus() + " → SUBMITTED");
        }
        order.setStatus(OrderStatus.SUBMITTED);
        return orderRepository.save(order);
    }

    public Order approveOrder(Long orderId, String notes) {
        Order order = getOrderById(orderId);
        if (order == null) {
            throw new IllegalArgumentException("订单不存在");
        }
        if (!order.getStatus().canTransitionTo(OrderStatus.APPROVED)) {
            throw new IllegalArgumentException("非法状态转换: " + order.getStatus() + " → APPROVED");
        }
        order.setStatus(OrderStatus.APPROVED);
        return orderRepository.save(order);
    }

    public Order rejectOrder(Long orderId, String reason) {
        Order order = getOrderById(orderId);
        if (order == null) {
            throw new IllegalArgumentException("订单不存在");
        }
        if (!order.getStatus().canTransitionTo(OrderStatus.REJECTED)) {
            throw new IllegalArgumentException("非法状态转换: " + order.getStatus() + " → REJECTED");
        }
        // 审批拒绝时释放库存
        for (OrderItem item : order.getItems()) {
            inventoryService.unlockInventory(item.getProductId(), item.getQuantity());
        }
        order.setStatus(OrderStatus.REJECTED);
        return orderRepository.save(order);
    }

    public Order payOrder(Long orderId) {
        Order order = getOrderById(orderId);
        if (order == null) {
            throw new IllegalArgumentException("订单不存在");
        }
        if (!order.getStatus().canTransitionTo(OrderStatus.PAID)) {
            throw new IllegalArgumentException("非法状态转换: " + order.getStatus() + " → PAID");
        }
        // 支付成功：锁定库存转为实际扣减
        for (OrderItem item : order.getItems()) {
            inventoryService.deductInventory(item.getProductId(), item.getQuantity());
        }
        order.setStatus(OrderStatus.PAID);
        return orderRepository.save(order);
    }

    public Order shipOrder(Long orderId) {
        Order order = getOrderById(orderId);
        if (order == null) {
            throw new IllegalArgumentException("订单不存在");
        }
        if (!order.getStatus().canTransitionTo(OrderStatus.SHIPPED)) {
            throw new IllegalArgumentException("非法状态转换: " + order.getStatus() + " → SHIPPED");
        }
        order.setStatus(OrderStatus.SHIPPED);
        return orderRepository.save(order);
    }

    public Order completeOrder(Long orderId) {
        Order order = getOrderById(orderId);
        if (order == null) {
            throw new IllegalArgumentException("订单不存在");
        }
        if (!order.getStatus().canTransitionTo(OrderStatus.COMPLETED)) {
            throw new IllegalArgumentException("非法状态转换: " + order.getStatus() + " → COMPLETED");
        }
        order.setStatus(OrderStatus.COMPLETED);
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