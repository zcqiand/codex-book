
const handleDelete = async (id: number) => {
  if (!confirm('Are you sure you want to delete this product?')) {
    return;
  }
  try {
    await api.products.delete(id);
    await loadProducts(); // 删除成功后刷新列表
  } catch (err) {
    setError(err instanceof Error ? err.message : 'Failed to delete product');
  }
};