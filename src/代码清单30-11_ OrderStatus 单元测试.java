
@Test
void testTerminalStatesHaveNoExits() {
    assertFalse(OrderStatus.COMPLETED.canTransitionTo(OrderStatus.DRAFT));
    assertFalse(OrderStatus.COMPLETED.canTransitionTo(OrderStatus.PAID));
    assertFalse(OrderStatus.REJECTED.canTransitionTo(OrderStatus.APPROVED));
    assertFalse(OrderStatus.CANCELLED.canTransitionTo(OrderStatus.PAID));
}

@Test
void testNonTerminalStatesHaveAtLeastOneExit() {
    assertTrue(OrderStatus.DRAFT.canTransitionTo(OrderStatus.SUBMITTED));
    assertTrue(OrderStatus.SUBMITTED.canTransitionTo(OrderStatus.APPROVED)
            || OrderStatus.SUBMITTED.canTransitionTo(OrderStatus.REJECTED));
    assertTrue(OrderStatus.APPROVED.canTransitionTo(OrderStatus.PAID)
            || OrderStatus.APPROVED.canTransitionTo(OrderStatus.CANCELLED));
    assertTrue(OrderStatus.PAID.canTransitionTo(OrderStatus.SHIPPED)
            || OrderStatus.PAID.canTransitionTo(OrderStatus.CANCELLED));
    assertTrue(OrderStatus.SHIPPED.canTransitionTo(OrderStatus.COMPLETED));
}