      <InspectionCapabilityFormModal
        resource={key}
        open={createOpen}
        onClose={() => setCreateOpen(false)}
        onSaved={() => load()}
      />
      <InspectionCapabilityFormModal
        resource={key}
        open={editing !== null}
        editing={editing ? { id: rowId(editing), ...(editing as object) } : null}
        onClose={() => setEditing(null)}
        onSaved={() => {
          setEditing(null);
          load();
        }}
      />