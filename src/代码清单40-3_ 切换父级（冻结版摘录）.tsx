  async function onMove(values: Record<string, unknown>) {
    if (!moveTarget) return;
    const parentId =
      values.parentId && values.parentId !== "" ? String(values.parentId) : undefined;
    try {
      await moveMut.mutateAsync({
        clientId: selectedAppId,
        menuId: moveTarget.id,
        data: { parentId },
      });
      setMoveTarget(null);
      menusQ.refetch();
      toast.success("父级已切换");
    } catch (err) {
      toast.error(`移动失败：${toApiError(err).message}`);
    }
  }
// …（中略）…
                      <Button
                        variant="ghost"
                        size="sm"
                        data-fn="M04.F04.I07"
                        onClick={() => setMoveTarget(r)}
                      >
                        移动
                      </Button>