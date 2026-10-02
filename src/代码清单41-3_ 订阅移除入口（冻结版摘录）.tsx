  const subscribeMut = useTenantApplicationsSubscribeTenantApplication();
  const updateMut = useTenantApplicationsUpdateTenantApplication();
  const removeMut = useTenantApplicationsRemoveTenantApplication();

  const [subscribeOpen, setSubscribeOpen] = useState(false);
  const [editTarget, setEditTarget] = useState<TenantApplication | null>(null);
  const [removeTarget, setRemoveTarget] = useState<TenantApplication | null>(null);

  const apps = (list.data?.data?.items ?? []) as TenantApplication[];
// …（中略）…
  async function confirmRemove() {
    if (!removeTarget) return;
    try {
      await removeMut.mutateAsync({ tenantId, clientId: removeTarget.clientId });
      setRemoveTarget(null);
      list.refetch();
      toast.success("订阅已取消");
    } catch (err) {
      toast.error(`取消失败：${toApiError(err).message}`);
    }
  }
// …（中略）…
                      <Button
                        variant="ghost"
                        size="sm"
                        data-fn="M00.F05.I04"
                        className="text-red-600 hover:text-red-700"
                        onClick={() => setRemoveTarget(a)}
                      >
                        取消订阅
                      </Button>
// …（中略）…
      <ConfirmDialog
        open={Boolean(removeTarget)}
        onOpenChange={(o) => !o && setRemoveTarget(null)}
        title={`取消订阅「${removeTarget ? appName(removeTarget.clientId) : ""}」？`}
        description="租户下该应用的所有角色菜单授权将一并清除。不可撤销。"
        confirmText="取消订阅"
        destructive
        loading={removeMut.isPending}
        onConfirm={confirmRemove}
      />