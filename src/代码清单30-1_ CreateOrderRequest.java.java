
package com.zcqiand.ecommerce.dto;

import jakarta.validation.constraints.*;
import lombok.Data;
import java.util.List;

@Data
public class CreateOrderRequest {
    @NotNull(message = "用户ID不能为空")
    @Positive(message = "用户ID必须为正数")
    private Long userId;

    @NotBlank(message = "收货地址不能为空")
    @Size(min = 1, max = 500, message = "收货地址长度必须在1到500之间")
    private String address;

    @NotEmpty(message = "订单商品不能为空")
    @Size(min = 1, max = 50, message = "订单商品数量必须在1到50之间")
    private List<OrderItemRequest> items;
}

@Data
class OrderItemRequest {
    @NotNull(message = "商品ID不能为空")
    @Positive(message = "商品ID必须为正数")
    private Long productId;

    @NotNull(message = "数量不能为空")
    @Positive(message = "数量必须为正数")
    @Max(value = 9999, message = "数量不能超过9999")
    private Long quantity;
}