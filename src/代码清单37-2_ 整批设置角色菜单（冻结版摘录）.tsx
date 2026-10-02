  async function save() {
    try {
      await saveMut.mutateAsync({
        tenantId,
        roleId,
        data: { menuIds: Array.from(granted) },
        params: { clientId: "" } as never,
      });
      grantQ.refetch();
      toast.success("菜单授权已保存");
    } catch (err) {
      toast.error(`保存失败：${toApiError(err).message}`);
    }
  }
// …（中略）…
            <Button data-fn="M00.F04.I03" disabled={saveMut.isPending} onClick={save}>
              {saveMut.isPending ? "保存中…" : `保存 (${granted.size})`}
            </Button>