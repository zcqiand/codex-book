/** 数据录入——流程线第三环节（flowStatus='data_entry'）。
 * 列表用 FlowStagePage；点「录入结果」打开双栏弹窗：左样品 / 右该样品全部检测参数平铺。
 * 录入检测结果 + 人工单项评定（verdict），POST/PUT /test-records。 */
function EntryRowAction({
  receipt,
  onEntry,
}: {
  receipt: SampleReceipt;
  onEntry: (r: SampleReceipt) => void;
}) {
  return (
    <button
      onClick={() => onEntry(receipt)}
      data-fn="M03.F03.I03"
      className="px-2 py-1 text-blue-600 hover:underline"
    >
      录入结果
    </button>
  );
}