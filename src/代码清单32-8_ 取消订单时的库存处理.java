
@Transactional
public Order cancelOrder(Long orderId, String reason) {
    Order order = getOrderById(orderId);

    if (order.getStatus() == OrderStatus.COMPLETED || order.getStatus() == OrderStatus.SHIPPED) {
        throw new BusinessException("INVALID_ORDER_STATUS",
                "Cannot cancel order in status: " + order.getStatus());
    }

    if (order.getStatus() == OrderStatus.PAID) {
        // 已支付的订单取消：恢复实际扣减的库存（退款场景）
        for (OrderItem item : order.getItems()) {
            inventoryService.restoreInventory(item.getProduct().getId(), item.getQuantity());
        }
    } else {
        // 未支付的订单取消：释放锁定的库存
        for (OrderItem item : order.getItems()) {
            inventoryService.unlockInventory(item.getProduct().getId(), item.getQuantity());
        }
    }

    order.setStatus(OrderStatus.CANCELLED);
    order.setCancelledAt(LocalDateTime.now());
    order.setCancellationReason(reason);
    return orderRepository.save(order);
}