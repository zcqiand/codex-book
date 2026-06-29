
export type OrderStatus =
  | 'DRAFT'
  | 'SUBMITTED'
  | 'APPROVED'
  | 'REJECTED'
  | 'PAID'
  | 'SHIPPED'
  | 'COMPLETED'
  | 'CANCELLED';

export interface Product {
  id: number;
  sku: string;
  name: string;
  price: number;
  category: string | null;
}

export interface Order {
  id: number;
  orderNumber: string;
  userId: number;
  status: OrderStatus;
  totalAmount: number;
  approvalLevel: number;
  approvalNotes: string | null;
  createdAt: string;
  submittedAt: string | null;
  paidAt: string | null;
  shippedAt: string | null;
  completedAt: string | null;
  cancelledAt: string | null;
  cancellationReason: string | null;
  items: OrderItem[];
}

export interface OrderItem {
  id: number;
  productId: number;
  productName: string;
  quantity: number;
  price: number;
  subtotal: number;
}

export interface CreateOrderRequest {
  userId: number;
  items: { productId: number; quantity: number }[];
}

// API 对象：封装所有与后端的 HTTP 通信
export const api = {
  products: { getAll, delete },
  orders: { getAll, create, submit, approve, pay, ship, complete, cancel },
};