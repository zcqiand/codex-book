
const statusLabels: Record<OrderStatus, string> = {
  DRAFT: '草稿',
  SUBMITTED: '已提交',
  APPROVED: '已批准',
  REJECTED: '已拒绝',
  PAID: '已支付',
  SHIPPED: '已发货',
  COMPLETED: '已完成',
  CANCELLED: '已取消',
};

const statusColors: Record<OrderStatus, string> = {
  DRAFT: '#9e9e9e',       // 灰色-草稿
  SUBMITTED: '#ff9800',   // 橙色-待处理
  APPROVED: '#4caf50',    // 绿色-通过
  REJECTED: '#f44336',    // 红色-拒绝
  PAID: '#2196f3',        // 蓝色-已支付
  SHIPPED: '#9c27b0',    // 紫色-已发货
  COMPLETED: '#4caf50',  // 绿色-完成
  CANCELLED: '#f44336',  // 红色-取消
};