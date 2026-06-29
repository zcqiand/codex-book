
@Transactional
public void deductInventory(Long productId, Long quantity) {
    Inventory inventory = inventoryRepository.findByProductIdWithLock(productId)
            .orElseThrow(() -> new ResourceNotFoundException("Inventory", "productId", productId));

    if (inventory.getQuantity() < quantity) {
        throw new BusinessException("INSUFFICIENT_INVENTORY",
                "Not enough inventory for product ID: " + productId);
    }

    inventory.setQuantity(inventory.getQuantity() - quantity);
    inventory.setLockedQuantity(Math.max(0, inventory.getLockedQuantity() - quantity));
    inventoryRepository.save(inventory);
}