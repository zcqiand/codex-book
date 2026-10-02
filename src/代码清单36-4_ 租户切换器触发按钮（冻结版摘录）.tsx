  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button
          variant="outline"
          size="sm"
          className="gap-2"
          data-testid="tenant-switcher"
          data-fn="M00.F02.I03"
        >
          <Building2 className="h-4 w-4 text-slate-500" />
          <span className="font-medium">
            {current ? (nameById.get(current.tenantId) ?? "…") : "选择租户"}
          </span>
          <ChevronsUpDown className="h-3.5 w-3.5 text-slate-400" />
        </Button>
      </DropdownMenuTrigger>