export async function GET(request: Request) {
  const sub = subFromBearer(request.headers.get("authorization"));
  if (sub === null) {
    // ADR-0019：无 Bearer = 401，不再 fallback "USER-A" 走 demo 路径。
    return NextResponse.json(
      { code: "UNAUTHORIZED", message: "Bearer token required (ADR-0019)" },
      { status: 401 },
    );
  }
  const snapshot = getMenuSnapshot(sub);
  if (!snapshot) {
    // 2026-09-04 自愈：部署重启后快照清空，浏览器持旧 token 用户刷新会撞 miss。
    // 对齐 login route serviceLogin 链同步重拉；拉到（含空树）→ 200；拉不到 → 503。
    const saasToken = await serviceLogin();
    if (saasToken) {
      await cacheMenuSnapshot(sub, saasToken, SAAS_BASE_URL());
      const recovered = getMenuSnapshot(sub);
      if (recovered) return NextResponse.json(recovered);
    } else {
      console.warn(
        `[menus] self-heal: service-account login unreachable for user ${sub}`,
      );
    }
    // demo 兜底删除（2026-08-27）：miss 如实报错，可恢复态（重登/refresh 重建快照）
    return NextResponse.json(
      {
        code: "MENUS_UNAVAILABLE",
        message: `menu snapshot unavailable for user ${sub}; re-login to refresh`,
      },
      { status: 503 },
    );
  }
  return NextResponse.json(snapshot);
}