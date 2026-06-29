
    public void linkProductToSupplier(Long supplierId, Long productId) {
        Supplier supplier = getSupplierById(supplierId);
        Product product = productService.getProductById(productId);
        if (supplier == null || product == null) {
            throw new IllegalArgumentException("供应商或商品不存在");
        }
        // 检查是否已关联
        if (supplier.getProducts().contains(product)) {
            throw new IllegalArgumentException("该商品已关联此供应商");
        }
        supplier.getProducts().add(product);
        supplierRepository.save(supplier);
    }

    public void unlinkProductFromSupplier(Long supplierId, Long productId) {
        Supplier supplier = getSupplierById(supplierId);
        Product product = productService.getProductById(productId);
        if (supplier == null) {
            throw new IllegalArgumentException("供应商不存在");
        }
        if (product == null || !supplier.getProducts().contains(product)) {
            throw new IllegalArgumentException("关联不存在");
        }
        supplier.getProducts().remove(product);
        supplierRepository.save(supplier);
    }

    public List<Product> getSupplierProducts(Long supplierId) {
        Supplier supplier = getSupplierById(supplierId);
        if (supplier == null) {
            throw new IllegalArgumentException("供应商不存在");
        }
        return supplier.getProducts().stream()
                .filter(p -> p.getIsDeleted() == 0)
                .collect(Collectors.toList());
    }