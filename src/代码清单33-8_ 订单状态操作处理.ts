
const handleStatusAction = async (
  id: number,
  action: 'submit' | 'pay' | 'ship' | 'complete' | 'cancel',
  reason?: string
) => {
  try {
    switch (action) {
      case 'submit':
        await api.orders.submit(id);
        break;
      case 'pay':
        await api.orders.pay(id);
        break;
      case 'ship':
        await api.orders.ship(id);
        break;
      case 'complete':
        await api.orders.complete(id);
        break;
      case 'cancel':
        await api.orders.cancel(id, reason);
        break;
    }
    await loadOrders(); // 操作成功后刷新列表
  } catch (err) {
    setError(err instanceof Error ? err.message : `Failed to ${action} order`);
  }
};