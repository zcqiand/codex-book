
<td style={tdStyle}>
  <div style={{ display: 'flex', gap: '4px', flexWrap: 'wrap' }}>
    {order.status === 'DRAFT' && (
      <button onClick={() => handleStatusAction(order.id, 'submit')} ...>
        提交
      </button>
    )}
    {order.status === 'APPROVED' && (
      <button onClick={() => handleStatusAction(order.id, 'pay')} ...>
        支付
      </button>
    )}
    {order.status === 'PAID' && (
      <button onClick={() => handleStatusAction(order.id, 'ship')} ...>
        发货
      </button>
    )}
    {order.status === 'SHIPPED' && (
      <button onClick={() => handleStatusAction(order.id, 'complete')} ...>
        完成
      </button>
    )}
    {['DRAFT', 'SUBMITTED', 'APPROVED'].includes(order.status) && (
      <button onClick={() => {
        const reason = prompt('请输入取消原因:');
        if (reason) handleStatusAction(order.id, 'cancel', reason);
      }} ...>
        取消
      </button>
    )}
  </div>
</td>