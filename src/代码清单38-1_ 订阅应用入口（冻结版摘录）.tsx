const SUBSCRIBE_FIELDS: FieldDef[] = [
  { name: "clientId", label: "Client ID", required: true, placeholder: "lab-management" },
  { name: "expireTime", label: "到期时间", placeholder: "2027-01-01T00:00:00Z（留空=永久）" },
];
// …（中略）…
  async function onSubscribe(values: Record<string, unknown>) {
    try {
      await subscribeMut.mutateAsync({
        tenantId,
        data: {
          clientId: String(values.clientId ?? "").trim(),
          expireTime: values.expireTime ? String(values.expireTime) : undefined,
        } as SubscribeTenantApplicationRequest,
      });
      setSubscribeOpen(false);
      list.refetch();
      toast.success("应用已订阅");
    } catch (err) {
      toast.error(`订阅失败：${toApiError(err).message}`);
    }
  }
// …（中略）…
      <PageHeader
        title="租户应用"
        description={`${tenantLabel} 的应用订阅`}
        actions={
          <Button data-fn="M00.F05.I02" onClick={() => setSubscribeOpen(true)}>
            订阅应用
          </Button>
        }
      />
// …（中略）…
      <CrudDialog
        open={subscribeOpen}
        onOpenChange={setSubscribeOpen}
        title="订阅应用"
        description="输入应用 Client ID 与（可选）到期时间。订阅后租户内的角色可分配菜单权限。"
        fields={SUBSCRIBE_FIELDS}
        submitText="创建"
        loading={subscribeMut.isPending}
        onSubmit={onSubscribe}
      />