
const calculateTotal = (): number => {
  return orderItems.reduce((total, item) => {
    const product = products.find((p) => p.id === item.productId);
    return total + (product ? product.price * item.quantity : 0);
  }, 0);
};

return (
  <div style={{ marginBottom: '24px', padding: '16px', backgroundColor: '#f5f5f5', borderRadius: '4px' }}>
    <strong>订单总额: ¥{calculateTotal().toFixed(2)}</strong>
    <br />
    <small style={{ color: '#666' }}>
      {calculateTotal() >= 1000
        ? '需要二级审批（部门经理 + 财务总监）'
        : '需要一级审批（直属经理）'}
    </small>
  </div>
);