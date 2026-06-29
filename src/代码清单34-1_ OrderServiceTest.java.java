
package com.zcqiand.ecommerce.service;

import com.zcqiand.ecommerce.entity.*;
import com.zcqiand.ecommerce.repository.*;
import org.junit.jupiter.api.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
@Transactional
class OrderServiceTest {

    @Autowired
    OrderService orderService;

    @Autowired
    ProductService productService;

    @Autowired
    InventoryService inventoryService;

    @Autowired
    UserRepository userRepository;

    @Autowired
    ProductRepository productRepository;

    @Autowired
    InventoryRepository inventoryRepository;

    private User testUser;
    private Product testProduct;

    @BeforeEach
    void setUp() {
        testUser = new User();
        testUser.setUsername("testuser");
        testUser.setEmail("test@example.com");
        userRepository.save(testUser);

        testProduct = new Product();
        testProduct.setName("测试商品");
        testProduct.setSku("TST-001");
        testProduct.setPrice(new BigDecimal("99.00"));
        productRepository.save(testProduct);

        Inventory inv = new Inventory();
        inv.setProduct(testProduct);
        inv.setCurrentQuantity(100);
        inv.setLockedQuantity(0);
        inventoryRepository.save(inv);
    }

    @Test
    void testDraftToSubmitted() {
        // DRAFT → SUBMITTED：提交订单
        Order order = createTestOrder(OrderStatus.DRAFT);
        Order result = orderService.submitOrder(order.getId());
        assertEquals(OrderStatus.SUBMITTED, result.getStatus());
        assertNotNull(result.getSubmittedAt());
    }

    @Test
    void testSubmittedToApproved() {
        // SUBMITTED → APPROVED：审批通过
        Order order = createTestOrder(OrderStatus.SUBMITTED);
        Order result = orderService.approveOrder(order.getId(), "同意");
        assertEquals(OrderStatus.APPROVED, result.getStatus());
        assertEquals("同意", result.getApprovalNotes());
    }

    @Test
    void testSubmittedToRejected() {
        // SUBMITTED → REJECTED：审批拒绝
        Order order = createTestOrder(OrderStatus.SUBMITTED);
        Order result = orderService.rejectOrder(order.getId(), "库存不足");
        assertEquals(OrderStatus.REJECTED, result.getStatus());
        assertEquals("库存不足", result.getCancellationReason());
    }

    @Test
    void testApprovedToPaid() {
        // APPROVED → PAID：支付成功，扣减库存
        Order order = createTestOrder(OrderStatus.APPROVED);
        int beforeQty = inventoryService.getByProductId(testProduct.getId()).getCurrentQuantity();

        Order result = orderService.payOrder(order.getId());
        assertEquals(OrderStatus.PAID, result.getStatus());
        assertNotNull(result.getPaidAt());

        int afterQty = inventoryService.getByProductId(testProduct.getId()).getCurrentQuantity();
        assertEquals(beforeQty - 2, afterQty); // 扣了 2 件
    }

    @Test
    void testPaidToShipped() {
        // PAID → SHIPPED：已支付订单可以发货
        Order order = createTestOrder(OrderStatus.PAID);
        Order result = orderService.shipOrder(order.getId());
        assertEquals(OrderStatus.SHIPPED, result.getStatus());
        assertNotNull(result.getShippedAt());
    }

    @Test
    void testShippedToCompleted() {
        // SHIPPED → COMPLETED：完成收货
        Order order = createTestOrder(OrderStatus.SHIPPED);
        Order result = orderService.completeOrder(order.getId());
        assertEquals(OrderStatus.COMPLETED, result.getStatus());
        assertNotNull(result.getCompletedAt());
    }

    @Test
    void testCannotCancelShippedOrCompleted() {
        // SHIPPED 和 COMPLETED 状态不可取消
        Order shippedOrder = createTestOrder(OrderStatus.SHIPPED);
        assertThrows(Exception.class, () -> orderService.cancelOrder(shippedOrder.getId(), "用户反悔"));

        Order completedOrder = createTestOrder(OrderStatus.COMPLETED);
        assertThrows(Exception.class, () -> orderService.cancelOrder(completedOrder.getId(), "用户反悔"));
    }

    @Test
    void testCancelPaidOrderRestoresInventory() {
        // PAID 状态取消：实物退回仓库
        Order order = createTestOrder(OrderStatus.APPROVED);
        orderService.payOrder(order.getId()); // 先支付，扣了库存

        int qtyBeforeCancel = inventoryService.getByProductId(testProduct.getId()).getCurrentQuantity();
        orderService.cancelOrder(order.getId(), "重复下单");
        int qtyAfterCancel = inventoryService.getByProductId(testProduct.getId()).getCurrentQuantity();

        assertEquals(qtyBeforeCancel + 2, qtyAfterCancel); // 退回了 2 件
    }

    @Test
    void testCancelBeforePayUnlocksInventory() {
        // APPROVED（未支付）状态取消：只释放锁定，不退实货
        Order order = createTestOrder(OrderStatus.APPROVED);
        int qtyBeforeCancel = inventoryService.getByProductId(testProduct.getId()).getCurrentQuantity();
        orderService.cancelOrder(order.getId(), "用户取消");
        int qtyAfterCancel = inventoryService.getByProductId(testProduct.getId()).getCurrentQuantity();

        assertEquals(qtyBeforeCancel, qtyAfterCancel); // 实物未动
    }

    @Test
    void testOrderNumberIsGenerated() {
        Order order = createTestOrder(OrderStatus.DRAFT);
        assertNotNull(order.getOrderNumber());
        assertTrue(order.getOrderNumber().startsWith("ORD-"));
    }

    private Order createTestOrder(OrderStatus status) {
        CreateOrderRequest request = new CreateOrderRequest();
        request.setUserId(testUser.getId());
        request.setItems(List.of(
            new CreateOrderRequest.OrderItemRequest(testProduct.getId(), 2)
        ));
        Order order = orderService.createOrder(request);
        // 强制刷新获取最新状态
        order = orderService.getOrderById(order.getId());

        // 根据目标状态跳转
        switch (status) {
            case DRAFT -> { return order; }
            case SUBMITTED -> { return orderService.submitOrder(order.getId()); }
            case APPROVED -> {
                orderService.submitOrder(order.getId());
                return orderService.approveOrder(order.getId(), "同意");
            }
            case REJECTED -> {
                orderService.submitOrder(order.getId());
                return orderService.rejectOrder(order.getId(), "拒绝");
            }
            case PAID -> {
                orderService.submitOrder(order.getId());
                orderService.approveOrder(order.getId(), "同意");
                return orderService.payOrder(order.getId());
            }
            case SHIPPED -> {
                orderService.submitOrder(order.getId());
                orderService.approveOrder(order.getId(), "同意");
                orderService.payOrder(order.getId());
                return orderService.shipOrder(order.getId());
            }
            case COMPLETED -> {
                orderService.submitOrder(order.getId());
                orderService.approveOrder(order.getId(), "同意");
                orderService.payOrder(order.getId());
                orderService.shipOrder(order.getId());
                return orderService.completeOrder(order.getId());
            }
            default -> { return order; }
        }
    }
}