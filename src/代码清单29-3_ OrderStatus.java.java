
package com.zcqiand.ecommerce.entity;

public enum OrderStatus {
    DRAFT,       // 草稿
    SUBMITTED,   // 已提交
    APPROVED,    // 已审批
    REJECTED,    // 已拒绝
    PAID,        // 已支付
    SHIPPED,     // 已发货
    COMPLETED,   // 已完成
    CANCELLED    // 已取消
}