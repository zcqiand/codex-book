
@RestController
@RequestMapping("/api/inventory")
public class InventoryController {

    @Autowired
    private InventoryService inventoryService;

    @GetMapping("/")
    public ApiResponse<List<Inventory>> listInventory(
            @RequestParam(required = false) Boolean lowStockOnly) {
        List<Inventory> inventories = inventoryService.getAllInventory();
        if (Boolean.TRUE.equals(lowStockOnly)) {
            inventories = inventories.stream()
                    .filter(inv -> inv.getAvailableQuantity() < 10) // 安全阈值
                    .collect(Collectors.toList());
        }
        return ApiResponse.success(inventories);
    }

    @GetMapping("/product/{productId}")
    public ApiResponse<Inventory> getInventory(@PathVariable Long productId) {
        Inventory inventory = inventoryService.getInventoryByProductId(productId);
        if (inventory == null) {
            return ApiResponse.error(404, "库存记录不存在");
        }
        return ApiResponse.success(inventory);
    }

    @PostMapping("/")
    public ApiResponse<Inventory> createInventory(
            @RequestParam Long productId,
            @RequestParam Long quantity,
            @RequestParam(required = false) String warehouseLocation) {
        try {
            Inventory inventory = inventoryService.createInventory(productId, quantity, warehouseLocation);
            return ApiResponse.success("库存创建成功", inventory);
        } catch (Exception e) {
            return ApiResponse.error(400, e.getMessage());
        }
    }

    @PutMapping("/product/{productId}")
    public ApiResponse<Inventory> updateInventory(
            @PathVariable Long productId,
            @RequestParam Long quantity,
            @RequestParam(required = false) String warehouseLocation) {
        try {
            Inventory inventory = inventoryService.updateInventory(productId, quantity, warehouseLocation);
            return ApiResponse.success("库存更新成功", inventory);
        } catch (IllegalArgumentException e) {
            return ApiResponse.error(404, e.getMessage());
        }
    }

    @PostMapping("/lock")
    public ApiResponse<Void> lockInventory(
            @RequestParam Long productId,
            @RequestParam Long quantity) {
        try {
            inventoryService.lockInventory(productId, quantity);
            return ApiResponse.success("库存锁定成功", null);
        } catch (IllegalArgumentException e) {
            return ApiResponse.error(400, e.getMessage());
        }
    }

    @PostMapping("/unlock")
    public ApiResponse<Void> unlockInventory(
            @RequestParam Long productId,
            @RequestParam Long quantity) {
        try {
            inventoryService.unlockInventory(productId, quantity);
            return ApiResponse.success("库存释放成功", null);
        } catch (IllegalArgumentException e) {
            return ApiResponse.error(400, e.getMessage());
        }
    }
}