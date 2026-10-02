                <td className="px-4 py-2 text-xs whitespace-nowrap align-top">
                  <button
                    type="button"
                    onClick={() => setEditing(item)}
                    data-fn={FN_CREATE[key]}
                    aria-label={`编辑 ${(item as { code: string }).code}`}
                    className="text-blue-600 hover:underline disabled:opacity-40 mr-3"
                  >
                    编辑
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      setDeleting(item);
                      setDeleteError(null);
                    }}
                    data-fn={FN_DELETE[key]}
                    aria-label={`删除 ${(item as { code: string }).code}`}
                    disabled={isOfficialRow(key, item)}
                    className="text-red-600 hover:underline disabled:opacity-40"
                  >
                    删除
                  </button>
                </td>