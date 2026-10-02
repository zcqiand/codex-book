  const save = async () => {
    setError(null);
    // 新建路径三段复合键必填（PUT 路径键取自 editRow 行内原值，不经 form）
    const objectCode = form.inspectionObjectCode ?? "";
    const paramCode = form.inspectionParameterCode ?? "";
    const stdCode = form.judgmentStandardCode ?? "";
    if (!editRow && (!objectCode || !paramCode || !stdCode)) {
      setError("检测项目、检测参数与检测依据为必填");
      return;
    }