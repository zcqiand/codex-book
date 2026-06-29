
const handleSubmit = async (e: React.FormEvent) => {
  e.preventDefault();

  const validItems = orderItems.filter(
    (item) => item.productId > 0 && item.quantity > 0
  );
  if (validItems.length === 0) {
    setError('请至少选择一个商品');
    return;
  }

  const request: CreateOrderRequest = {
    userId,
    items: validItems.map((item) => ({
      productId: item.productId,
      quantity: item.quantity,
    })),
  };

  try {
    setSubmitting(true);
    setError(null);
    await api.orders.create(request);
    navigate('/orders'); // 创建成功后跳转到订单列表
  } catch (err) {
    setError(err instanceof Error ? err.message : 'Failed to create order');
  } finally {
    setSubmitting(false);
  }
};