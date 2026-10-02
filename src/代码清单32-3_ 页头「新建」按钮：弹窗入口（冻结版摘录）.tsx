          <button
            type="button"
            onClick={() => setCreateOpen(true)}
            data-fn={FN_CREATE[key]}
            className="px-3 py-1.5 text-sm bg-blue-600 text-white rounded hover:bg-blue-700"
          >
            {CREATE_LABELS[key]}
          </button>