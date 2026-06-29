
@Service
@Transactional
public class OrderService {

    @Autowired
    private OrderRepository orderRepository;
    @Autowired
    private ProductService productService;
    @Autowired
    private InventoryService inventoryService;

    public Order createOrder(CreateOrderRequest request) {
        // 1. 校验所有商品存在且未删除，库存充足
        List<Long> productIds = request.getItems().stream()
                .map(OrderItemRequest::getProductId)
                .collect(Collectors.toList());

        // 2. 计算总金额并锁定库存
        BigDecimal total = BigDecimal.ZERO;
        for (OrderItemRequest item : request.getItems()) {
            Product product = productService.getProductById(item.getProductId());
            if (product == null || product.getIsDeleted() != 0) {
                throw new IllegalArgumentException("商品不存在或已下架");
            }
            Inventory inventory = inventoryService.getInventoryByProductId(item.getProductId());
            if (inventory == null || inventory.getAvailableQuantity() < item.getQuantity()) {
                throw new IllegalArgumentException("商品 " + product.getName() + " 库存不足");
            }
            total = total.add(product.getUnitPrice().multiply(BigDecimal.valueOf(item.getQuantity())));
            inventoryService.lockInventory(item.getProductId(), item.getQuantity());
        }

        // 3. 创建订单
        Order order = new Order();
        order.setOrderNo(generateOrderNumber());
        order.setUserId(request.getUserId());
        order.setStatus(OrderStatus.DRAFT);
        order.setTotalAmount(total);
        order.setAddress(request.getAddress());
        order = orderRepository.save(order);

        // 4. 创建订单明细
        for (OrderItemRequest item : request.getItems()) {
            Product product = productService.getProductById(item.getProductId());
            OrderItem orderItem = new OrderItem();
            orderItem.setOrderId(order.getId());
            orderItem.setProductId(item.getProductId());
            orderItem.setQuantity(item.getQuantity());
            orderItem.setUnitPriceSnapshot(product.getUnitPrice()); // 快照
            orderItemRepository.save(orderItem);
        }

        return order;
    }

    private String generateOrderNumber() {
        return LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyyMMddHHmmss"))
                + String.format("%06d", new Random().nextInt(999999));
    }

    public Order getOrderById(Long id) {
        return orderRepository.findById(id).orElse(null);
    }

    public Order getOrderByNumber(String orderNumber) {
        return orderRepository.findByOrderNumber(orderNumber);
    }

    public List<Order> getAllOrders() {
        return orderRepository.findAll();
    }
}