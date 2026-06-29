
@Transactional
public void lockInventory(Long productId, Long quantity) {
    Inventory inventory = inventoryRepository.findByProductIdWithLock(productId)
            .orElseThrow(() -> new ResourceNotFoundException("Inventory", "productId", productId));

    if (inventory.getAvailableQuantity() < quantity) {
        throw new BusinessException("INSUFFICIENT_INVENTORY",
                "Not enough inventory available for product ID: " + productId);
    }

    inventory.setLockedQuantity(inventory.getLockedQuantity() + quantity);
    inventoryRepository.save(inventory);
}