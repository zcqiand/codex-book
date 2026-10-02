interface Props {
  /** 码表实体：/models /specifications /grades /brands */
  endpoint: "/models" | "/specifications" | "/grades" | "/brands";
  title: string;
  hint?: string;
  /** 功能 ID（用于 data-fn 入口标记），格式 Mxx.Fyy.Izz */
  dataFn?: string;
  /** 新建按钮 data-fn */
  createDataFn?: string;
  /** 编辑按钮 data-fn */
  editDataFn?: string;
  /** 删除按钮 data-fn */
  deleteDataFn?: string;
}

// @entry M04.F06.I01
// @entry M04.F07.I01
// @entry M04.F08.I01
// @entry M04.F09.I01
/**
 * 4 码表通用页（M04.F06/F07/F08/F09 I01）：
 * 左侧检测项目树（一级）+ 右侧可拖拽排序的列表。
 * 拖拽行后 PUT 持久化 sortOrder；新建项 sortOrder 自动续号。
 * 移植自 REF lab-management-system src/features/dicts/CategoryDictList.tsx。
 */
export function CategoryDictList({
  endpoint,
  title,
  hint,
  dataFn,
  createDataFn,
  editDataFn,
  deleteDataFn,
}: Props) {