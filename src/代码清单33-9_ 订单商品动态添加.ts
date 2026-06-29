
const [orderItems, setOrderItems] = useState<OrderItemInput[]>([
  { productId: 0, quantity: 1 },
]);

const handleAddItem = () => {
  setOrderItems([...orderItems, { productId: 0, quantity: 1 }]);
};

const handleRemoveItem = (index: number) => {
  if (orderItems.length === 1) {
    alert('至少需要一个商品');
    return;
  }
  const newItems = orderItems.filter((_, i) => i !== index);
  setOrderItems(newItems);
};

const handleItemChange = (
  index: number,
  field: 'productId' | 'quantity',
  value: number
) => {
  const newItems = [...orderItems];
  newItems[index] = { ...newItems[index], [field]: value };
  setOrderItems(newItems);
};