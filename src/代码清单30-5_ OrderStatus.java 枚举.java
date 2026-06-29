
package com.zcqiand.ecommerce.entity;

public enum OrderStatus {
    DRAFT,       // 草稿
    SUBMITTED,   // 已提交待审批
    APPROVED,    // 审批通过
    REJECTED,    // 审批拒绝
    PAID,        // 已支付
    SHIPPED,     // 已发货
    COMPLETED,   // 已完成
    CANCELLED;   // 已取消

    // 合法转换映射
    public boolean canTransitionTo(OrderStatus target) {
        return switch (this) {
            case DRAFT -> target == SUBMITTED;
            case SUBMITTED -> target == APPROVED || target == REJECTED;
            case APPROVED -> target == PAID || target == CANCELLED;
            case PAID -> target == SHIPPED || target == CANCELLED;
            case SHIPPED -> target == COMPLETED;
            case COMPLETED, REJECTED, CANCELLED -> false; // 终态，不可转换
        };
    }
}