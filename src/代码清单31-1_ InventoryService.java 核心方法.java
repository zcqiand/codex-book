
@Service
@Transactional
public class InventoryService {

    @Autowired
    private InventoryRepository inventoryRepository;

    public void lockInventory(Long productId, Long quantity) {
        Inventory inventory = getInventoryByProductId(productId);
        if (inventory == null) {
            throw new IllegalArgumentException("库存记录不存在");
        }
        if (inventory.getAvailableQuantity() < quantity) {
            throw new IllegalArgumentException("商品 " + productId + " 可用库存不足");
        }
        inventory.setLockedQuantity(inventory.getLockedQuantity() + quantity);
        inventoryRepository.save(inventory);
    }

    public void unlockInventory(Long productId, Long quantity) {
        Inventory inventory = getInventoryByProductId(productId);
        if (inventory == null) {
            throw new IllegalArgumentException("库存记录不存在");
        }
        inventory.setLockedQuantity(Math.max(0, inventory.getLockedQuantity() - quantity));
        inventoryRepository.save(inventory);
    }

    public void deductInventory(Long productId, Long quantity) {
        Inventory inventory = getInventoryByProductId(productId);
        if (inventory == null) {
            throw new IllegalArgumentException("库存记录不存在");
        }
        if (inventory.getLockedQuantity() < quantity) {
            throw new IllegalArgumentException("商品 " + productId + " 锁定库存不足——数据不一致");
        }
        inventory.setLockedQuantity(inventory.getLockedQuantity() - quantity);
        inventory.setQuantity(inventory.getQuantity() - quantity);
        inventoryRepository.save(inventory);

        // 低库存预警
        if (inventory.getAvailableQuantity() < getSafetyThreshold(productId)) {
            triggerLowStockAlert(inventory);
        }
    }

    public void restoreInventory(Long productId, Long quantity) {
        Inventory inventory = getInventoryByProductId(productId);
        if (inventory == null) {
            throw new IllegalArgumentException("库存记录不存在");
        }
        inventory.setQuantity(inventory.getQuantity() + quantity);
        inventoryRepository.save(inventory);
    }

    public Inventory getInventoryByProductId(Long productId) {
        return inventoryRepository.findByProductId(productId);
    }

    public List<Inventory> getAllInventory() {
        return inventoryRepository.findAll();
    }

    public Inventory createInventory(Long productId, Long quantity, String warehouseLocation) {
        Inventory inventory = new Inventory();
        inventory.setProductId(productId);
        inventory.setQuantity(quantity);
        inventory.setLockedQuantity(0L);
        inventory.setWarehouseLocation(warehouseLocation);
        return inventoryRepository.save(inventory);
    }

    public Inventory updateInventory(Long productId, Long quantity, String warehouseLocation) {
        Inventory inventory = getInventoryByProductId(productId);
        if (inventory == null) {
            throw new IllegalArgumentException("库存记录不存在");
        }
        inventory.setQuantity(quantity);
        inventory.setWarehouseLocation(warehouseLocation);
        return inventoryRepository.save(inventory);
    }

    private Long getSafetyThreshold(Long productId) {
        // 实际实现应从配置或 Product 实体获取
        return 10L;
    }

    private void triggerLowStockAlert(Inventory inventory) {
        // 低库存告警（生产环境应接入通知系统，如发邮件、短信、钉钉通知）
        System.out.println("[库存告警] 商品ID=" + inventory.getProductId()
                + " 当前可用库存=" + inventory.getAvailableQuantity()
                + " 安全阈值=" + getSafetyThreshold(inventory.getProductId()));
    }
}