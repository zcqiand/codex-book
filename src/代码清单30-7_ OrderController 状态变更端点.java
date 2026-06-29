
    @PostMapping("/{id}/submit")
    public ApiResponse<Order> submitOrder(@PathVariable Long id) {
        try {
            Order order = orderService.submitOrder(id);
            return ApiResponse.success("订单已提交", order);
        } catch (IllegalArgumentException e) {
            return ApiResponse.error(400, e.getMessage());
        }
    }

    @PostMapping("/{id}/approve")
    public ApiResponse<Order> approveOrder(@PathVariable Long id,
                                          @RequestParam(required = false) String notes) {
        try {
            Order order = orderService.approveOrder(id, notes);
            return ApiResponse.success("订单已审批通过", order);
        } catch (IllegalArgumentException e) {
            return ApiResponse.error(400, e.getMessage());
        }
    }

    @PostMapping("/{id}/reject")
    public ApiResponse<Order> rejectOrder(@PathVariable Long id,
                                          @RequestParam String reason) {
        try {
            Order order = orderService.rejectOrder(id, reason);
            return ApiResponse.success("订单已拒绝", order);
        } catch (IllegalArgumentException e) {
            return ApiResponse.error(400, e.getMessage());
        }
    }

    @PostMapping("/{id}/pay")
    public ApiResponse<Order> payOrder(@PathVariable Long id) {
        try {
            Order order = orderService.payOrder(id);
            return ApiResponse.success("支付成功", order);
        } catch (IllegalArgumentException e) {
            return ApiResponse.error(400, e.getMessage());
        }
    }

    @PostMapping("/{id}/ship")
    public ApiResponse<Order> shipOrder(@PathVariable Long id) {
        try {
            Order order = orderService.shipOrder(id);
            return ApiResponse.success("订单已发货", order);
        } catch (IllegalArgumentException e) {
            return ApiResponse.error(400, e.getMessage());
        }
    }

    @PostMapping("/{id}/complete")
    public ApiResponse<Order> completeOrder(@PathVariable Long id) {
        try {
            Order order = orderService.completeOrder(id);
            return ApiResponse.success("订单已完成", order);
        } catch (IllegalArgumentException e) {
            return ApiResponse.error(400, e.getMessage());
        }
    }

    @PostMapping("/{id}/cancel")
    public ApiResponse<Order> cancelOrder(@PathVariable Long id,
                                          @RequestParam(required = false) String reason) {
        try {
            Order order = orderService.cancelOrder(id, reason);
            return ApiResponse.success("订单已取消", order);
        } catch (IllegalArgumentException e) {
            return ApiResponse.error(400, e.getMessage());
        }
    }