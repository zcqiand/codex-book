export default function ConsoleLayout({ children }: { children: React.ReactNode }) {
  const router = useRouter();
  const { token } = useAuth();
  const [hydrated, setHydrated] = useState(false);

  useEffect(() => {
    setHydrated(true);
  }, []);
  useEffect(() => {
    if (hydrated && !token) router.replace("/login");
  }, [hydrated, token, router]);

  // hydrate 完成前 token 是 null（避免 SSR/CSR mismatch）
  // hydrate 完成前 token 是 null（避免 SSR/CSR mismatch）
  // @entry M01.F04.I02 — 路由守卫：未登录（无 token）→ router.replace(/login) + 守卫占位 UI（hydrate 完成前的中间态）
  if (!hydrated || !token) {
    return (
      <main
        data-fn="M01.F04.I02"
        data-testid="console-layout-guard"
        className="min-h-screen flex items-center justify-center text-sm text-slate-500"
      >
        未登录，跳 /login 中...
      </main>
    );
  }

  return (
    <Suspense fallback={null}>
      <AppShell>{children}</AppShell>
    </Suspense>
  );