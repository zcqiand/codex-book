
    public Map<String, Object> getAvailableStockWithSupplier(Long productId, Long requiredQuantity) {
        Map<String, Object> result = new HashMap<>();
        Inventory selfInventory = getInventoryByProductId(productId);
        Long selfAvailable = selfInventory != null ? selfInventory.getAvailableQuantity() : 0L;
        result.put("selfStock", selfAvailable);
        result.put("selfStockEnough", selfAvailable >= requiredQuantity);

        if (selfAvailable < requiredQuantity) {
            // 查询供应商库存（实际实现需调用外部 API）
            List<Map<String, Object>> supplierStock = querySupplierStock(productId, requiredQuantity - selfAvailable);
            result.put("supplierStock", supplierStock);
            result.put("canFulfill", !supplierStock.isEmpty());
        } else {
            result.put("supplierStock", Collections.emptyList());
            result.put("canFulfill", true);
        }
        return result;
    }

    private List<Map<String, Object>> querySupplierStock(Long productId, Long deficitQuantity) {
        // 实际实现：调用供应商 API 查询可用库存和交期
        // 此处为示例返回值
        List<Map<String, Object>> suppliers = new ArrayList<>();
        // 模拟数据
        Map<String, Object> supplier1 = new HashMap<>();
        supplier1.put("supplierId", "SUP-A-001");
        supplier1.put("availableQuantity", 500L);
        supplier1.put("leadTimeDays", 3);
        suppliers.add(supplier1);
        return suppliers;
    }
}