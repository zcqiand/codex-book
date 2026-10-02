# 前置：本地 dev server 已启动，巡检任务在只读档位下通过只读接口取数，不做任何修改
mkdir -p reports

# 单条任务完整形态：巡检清单第 1 项，租户详情核对（8 个核对点）
codex exec \
  --cd ./saas-identity-platform-nextjs \
  --sandbox read-only \
  --ephemeral \
  --output-schema ./inspection-schema.json \
  --output-last-message ./reports/tenant-detail.json \
  "按巡检清单第 1 项核对租户详情：acme-dev 与 acme-prod 的名称、状态、成员数、建档时间，逐点回报核对值与判定，只读核对，不做任何修改"

# 批量形态：四个报告文件对应清单第 1、2-3、4、5-7 项的分组
declare -A PROMPTS=(
  [tenant-detail]="按巡检清单第 1 项核对租户详情：acme-dev 与 acme-prod 的名称、状态、成员数、建档时间，逐点回报核对值与判定，只读核对"
  [tenant-apps]="按巡检清单第 2-3 项核对租户应用列表：订阅行数对账、到期显示格式、订阅到期日在档、临期 30 天标记，只读核对"
  [client-meta]="按巡检清单第 4 项核对公共 client 元数据：4 个在册 client 逐个核对元数据可读、名称一致、回调域在册，只读核对"
  [menu-order]="按巡检清单第 5-7 项核对：菜单同级序号连续且无重复、租户状态在 0/1/2 允许集内、订阅状态与台账一致，只读核对"
)
for task in tenant-detail tenant-apps client-meta menu-order; do
  codex exec --cd ./saas-identity-platform-nextjs \
    --sandbox read-only --ephemeral \
    --output-schema ./inspection-schema.json \
    --output-last-message "./reports/${task}.json" \
    "${PROMPTS[$task]}"
done

# 审批策略边界（第 9 章口径）：read-only 档位下写动作由沙箱直接拒绝；
# 无头任务遇需审批动作（on-request 默认策略下写文件/执行命令/访问网络）会挂起等待，
# 无人应答即停——无头不等于无界