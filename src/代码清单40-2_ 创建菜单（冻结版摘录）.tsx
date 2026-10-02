  async function onCreate(values: Record<string, unknown>) {
    const parentId =
      values.parentId && values.parentId !== "" ? String(values.parentId) : undefined;
    try {
      await createMut.mutateAsync({
        clientId: selectedAppId,
        data: {
          clientId: selectedAppId,
          code: String(values.code ?? "").trim(),
          name: String(values.name ?? "").trim(),
          path: (values.path as string) || undefined,
          type: values.type as "group" | "page" | "action",
          parentId,
          sortOrder: Number(values.sortOrder ?? 0),
          status: Number(values.status ?? 1),
        } as unknown as CreateSysMenuRequest,
      });
      setCreateOpen(false);
      menusQ.refetch();
      toast.success("菜单已创建");
    } catch (err) {
      toast.error(`创建失败：${toApiError(err).message}`);
    }
  }
// …（中略）…
            <Button data-fn="M04.F04.I02" onClick={() => setCreateOpen(true)}>
              新建菜单
            </Button>