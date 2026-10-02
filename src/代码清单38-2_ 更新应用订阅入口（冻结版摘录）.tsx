const UPDATE_FIELDS: FieldDef[] = [
  {
    name: "status",
    label: "状态",
    type: "select",
    required: true,
    defaultValue: "1",
    options: STATUS_OPTIONS,
  },
  { name: "expireTime", label: "到期时间", placeholder: "留空=永久" },
];
// …（中略）…
  async function onUpdate(values: Record<string, unknown>) {
    if (!editTarget) return;
    try {
      await updateMut.mutateAsync({
        tenantId,
        clientId: editTarget.clientId,
        data: {
          status: Number(values.status),
          expireTime: values.expireTime ? String(values.expireTime) : undefined,
        } as UpdateTenantApplicationRequest,
      });
      setEditTarget(null);
      list.refetch();
      toast.success("订阅已更新");
    } catch (err) {
      toast.error(`更新失败：${toApiError(err).message}`);
    }
  }
// …（中略）…
                    <TableCell className="text-right space-x-1">
                      <Button
                        variant="ghost"
                        size="sm"
                        data-fn="M00.F05.I03"
                        onClick={() => setEditTarget(a)}
                      >
                        编辑
                      </Button>
// …（中略）…
      <CrudDialog
        open={Boolean(editTarget)}
        onOpenChange={(o) => !o && setEditTarget(null)}
        title="编辑订阅"
        fields={UPDATE_FIELDS}
        initialValues={
          editTarget
            ? {
                status: String(editTarget.status),
                expireTime: editTarget.expireTime ?? "",
              }
            : undefined
        }
        loading={updateMut.isPending}
        onSubmit={onUpdate}
      />