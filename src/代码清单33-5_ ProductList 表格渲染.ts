
return (
  <div>
    <table style={{ width: '100%', borderCollapse: 'collapse', backgroundColor: 'white' }}>
      <thead>
        <tr style={{ backgroundColor: '#f5f5f5' }}>
          <th style={thStyle}>ID</th>
          <th style={thStyle}>SKU</th>
          <th style={thStyle}>名称</th>
          <th style={thStyle}>价格</th>
          <th style={thStyle}>分类</th>
          <th style={thStyle}>操作</th>
        </tr>
      </thead>
      <tbody>
        {products.map((product) => (
          <tr key={product.id} style={{ borderBottom: '1px solid #eee' }}>
            <td style={tdStyle}>{product.id}</td>
            <td style={tdStyle}>{product.sku}</td>
            <td style={tdStyle}>{product.name}</td>
            <td style={tdStyle}>¥{product.price.toFixed(2)}</td>
            <td style={tdStyle}>{product.category || '-'}</td>
            <td style={tdStyle}>
              <button onClick={() => handleDelete(product.id)} ...>
                删除
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);