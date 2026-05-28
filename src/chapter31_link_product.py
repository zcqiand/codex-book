# 从第 31 章提取
# 来源：Codex 从入门到项目实践

@router.post("/{supplier_id}/products/{product_id}")
def link_product(supplier_id: int, product_id: int,
                  db: Session = Depends(get_db)):
    """将商品关联到供应商——表示该供应商可供应此商品。"""
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    product = db.query(Product).filter(Product.id == product_id, Product.is_deleted == 0).first()
    if not supplier or not product:
        raise HTTPException(404, "供应商或商品不存在")
    if product in supplier.products:
        raise HTTPException(400, "该商品已关联此供应商")
    supplier.products.append(product)
    db.commit()
    return {"supplier_id": supplier_id, "product_id": product_id, "linked": True}

@router.delete("/{supplier_id}/products/{product_id}")
def unlink_product(supplier_id: int, product_id: int,
                    db: Session = Depends(get_db)):
    """解除商品与供应商的关联。"""
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if not supplier:
        raise HTTPException(404, "供应商不存在")
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product or product not in supplier.products:
        raise HTTPException(404, "关联不存在")
    supplier.products.remove(product)
    db.commit()
    return {"linked": False}

@router.get("/{supplier_id}/products")
def list_supplier_products(supplier_id: int, db: Session = Depends(get_db)):
    """查询供应商可提供的所有商品。"""
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if not supplier:
        raise HTTPException(404, "供应商不存在")
    return [{"id": p.id, "name": p.name, "sku": p.sku, "unit_price": str(p.unit_price)}
            for p in supplier.products if p.is_deleted == 0]