  const roleAssignMut = useTenantMembersAssignTenantMemberRoles();
// …（中略）…
                      <Button
                        variant="ghost"
                        size="sm"
                        data-fn="M01.F02.I01"
                        onClick={() => setRoleTarget(u)}
                      >
                        分配角色
                      </Button>
// …（中略）…
      <CrudDialog
        open={Boolean(roleTarget)}
        onOpenChange={(o) => !o && setRoleTarget(null)}
        title={`分配角色：${roleTarget?.username ?? ""}`}
        fields={[
          {
            name: "roleIds",
            label: "角色（多选）",
            type: "select",
            options: roles.map((r) => ({ value: r.id, label: `${r.roleCode} · ${r.roleName}` })),
          },
        ]}
        submitText="保存角色"
        loading={roleAssignMut.isPending}
        initialValues={roleTarget ? { roleIds: roleTarget.roleIds ?? [] } : undefined}
// …（中略）…
        onSubmit={onAssignRoles}
      />