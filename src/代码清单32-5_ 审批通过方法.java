
@Transactional
public Order approveOrder(Long orderId, String notes) {
    Order order = getOrderById(orderId);

    if (order.getStatus() != OrderStatus.SUBMITTED) {
        throw new BusinessException("INVALID_ORDER_STATUS",
                "Order can only be approved from SUBMITTED status");
    }

    order.setStatus(OrderStatus.APPROVED);
    order.setApprovalNotes(notes);
    return orderRepository.save(order);
}