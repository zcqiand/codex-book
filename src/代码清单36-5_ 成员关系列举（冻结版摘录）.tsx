// TenantSwitcher — 顶部栏右侧 Dropdown，切换当前用户可访问的租户。
// M00.F02.I03 / M01.F03.I02（2026-09-11 接真 API，E2E REQ-2026-004）：
// @entry M01.F03.I01 — 列出我的租户成员关系（GET /me/tenants 渲染切换菜单）
// 成员关系 GET /me/tenants（TenantMember[]，契约无租户名）；
// 显示名 join 平台租户列表（管理控制台自身页面数据源，复用同一 query key 缓存）；
// 切换 POST /me/tenants/:id/switch → 新 token 落 session → 进该租户工作区。
// …（中略）…
  const membershipsQ = useQuery({
    queryKey: ["meListMyTenants"],
    queryFn: async () => (await meListMyTenants({ clientId: "" })).data,
  });
  const tenantsQ = useQuery({
    queryKey: ["adminTenantsListTenants"],
    queryFn: async () => (await adminTenantsListTenants()).data.items,
  });

  const memberships = membershipsQ.data ?? [];
  const nameById = new Map((tenantsQ.data ?? []).map((t) => [t.id, t.name]));