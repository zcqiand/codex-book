function AssignButton({
  receipt,
  onAssign,
  refresh,
}: {
  receipt: SampleReceipt;
  onAssign: (r: SampleReceipt, refresh: () => Promise<void>) => void;
  refresh: () => Promise<void>;
}) {
  return (
    <button
      onClick={() => onAssign(receipt, refresh)}
      data-fn="M03.F02.I01"
      className="px-2 py-1 text-purple-600 hover:underline"
    >
      安排
    </button>
  );
}