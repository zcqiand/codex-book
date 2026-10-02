  /** 功能 ID（用于 data-fn 入口标记），格式 Mxx.Fyy.Izz */
  dataFn?: string;
  /** 三态过滤器的 data-fn ID，如 M03.F01.I06 */
  filterDataFn?: string;
  /** 行级「查看详情」按钮的 data-fn ID，如 M03.F05.I02 */
  viewDataFn?: string;
  /** 行级「提交/退回」按钮的 data-fn ID，如 M03.F05.I07（审核通过/批准/发放/归档等共用） */
  actionDataFn?: string;
  /** 下一阶段的自定义标签（用于「提交后进入」文案覆盖，如 issuance→已归档） */
  nextStageLabel?: string;
}