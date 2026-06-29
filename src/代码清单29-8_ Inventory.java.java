
package com.zcqiand.ecommerce.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "inventory")
public class Inventory {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "product_id", unique = true, nullable = false)
    private Product product;

    @Column(nullable = false)
    private Long quantity = 0L;

    @Column(nullable = false)
    private Long lockedQuantity = 0L;

    @Column(length = 100)
    private String warehouseLocation;

    /**
     * 计算可用库存：实际库存 - 锁定库存
     */
    public Long getAvailableQuantity() {
        return quantity - lockedQuantity;
    }

    // getters and setters
}