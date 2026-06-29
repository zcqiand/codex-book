
@Transactional
public Order submitOrder(Long orderId) {
    Order order = getOrderById(orderId);

    if (order.getStatus() != OrderStatus.DRAFT) {
        throw new BusinessException("INVALID_ORDER_STATUS",
                "Order can only be submitted from DRAFT status");
    }

    order.setStatus(OrderStatus.SUBMITTED);
    order.setSubmittedAt(LocalDateTime.now());
    return orderRepository.save(order);
}