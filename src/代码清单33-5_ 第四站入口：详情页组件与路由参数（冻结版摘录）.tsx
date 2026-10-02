// @entry M03.F09.I01
export function ReceiptDetailPage() {
  const { id } = useParams<{ id: string }>();
  const [receipt, setReceipt] = useState<SampleReceipt | null>(null);
  const [parameters, setParameters] = useState<TestParameter[]>([]);
  const [reportNames, setReportNames] = useState<InspectionReportName[]>([]);
  const [standards, setStandards] = useState<InspectionStandard[]>([]);
  // B6 加载态：首屏即视为加载中（首帧不渲染详情壳；refetch 时详情保持旧数据）
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [previewOpen, setPreviewOpen] = useState(false);