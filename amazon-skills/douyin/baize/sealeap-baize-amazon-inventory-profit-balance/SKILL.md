---
name: sealeap-baize-amazon-inventory-profit-balance
description: "Set Amazon per-SKU inventory and advertising boundaries from realistic sales capacity, cash turnover, conversion, break-even acquisition cost, and portfolio risk. Use for 首批发多少、库存临界点、精铺盈利逻辑、广告花费怎么控、多产品组合风险."
---

# Amazon 库存与利润平衡

## 目标

Set Amazon per-SKU inventory and advertising boundaries from realistic sales capacity, cash turnover, conversion, break-even acquisition cost, and portfolio risk.

## 不可妥协的边界

- 当前 Amazon 官方政策、账户资格、站点字段和一方数据优先于本 Skill 的经验框架。
- 第三方数据一律标为估算或前台观测，不得写成 Amazon 一方事实。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 一次实验只改变一个主要变量，并记录基线、样本、成功、停止和回退条件。
- 不得复制来源材料或竞品表达；输出必须按当前任务重新组织并可由现有证据支撑。
- 不存在可验证的固定店铺订单上限时，不用该假设限制组合。
- 固定广告占比是经验值，应按产品毛利、退货和目标利润重算。

## 先判断任务模式

1. **诊断**：读取现状、证据和缺口，不生成线上写入动作。
2. **方案草案**：输出可审核的结构、参数范围、实验和回退值。
3. **执行准备**：只生成待批准变更表或 API/控制台操作草案。
4. **已批准执行**：仅对用户在当前会话明确批准的对象和字段执行，并立即回读核验。

用户未指定时采用“诊断”。

## 开始前要拿到

- marketplace、ASIN/SKU、库存阶段、补货与到仓时间
- 断货或备货前后的销量、流量、广告、自然位置和转化基线
- COGS、头程、仓储、平台费、退货和清仓成本
- 可比产品的成熟度、销量区间和需求趋势

缺失项必须标为 `NEEDS_EVIDENCE`；不得猜数字、补属性或把不同站点、ASIN、变体、币种和时间窗混在一起。

## 工作流

先读取 [references/playbook.md](references/playbook.md)，确认该方法适用于当前对象。按以下顺序执行：

1. 用低成熟度可比产品估算销量区间，而不是直接采用头部销量。
2. 计算不同备货量下的现金占用、仓储、广告和清仓损失。
3. 用单位贡献利润反推最大广告获客成本。
4. 在单 SKU 和组合层分别设置补货、减投和退出触发器。
5. 滚动更新实际销量与转化，逐批增加而非一次压货。

最后做数据充分性检查，并把结论分成 `FACT / ESTIMATE / HYPOTHESIS / UNKNOWN`。若关键证据不足，状态写 `HOLD`。

## 第三方 MCP 数据

仅在自有数据不足且当前任务确实需要外部证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，再使用 `scripts/mcp_research.py`。本 Skill 的外部取数目的：获取历史趋势、可比销量、评论成熟度和关键词需求代理数据。

- 先 `doctor`，再 `search-tools` 和 `describe`；工具名及参数以实时 `tools/list` 与 `inputSchema` 为准。
- Token 只从环境变量读取。不得写入命令参数、URL、Skill、报告、日志或 Git。
- `tools/call` 或 Actor 可能计费；先展示 Provider、工具、无密钥业务参数、预计成本与输出位置，核对已有授权覆盖后才加 `--allow-cost`；该标志不是费用上限。


## 必须交付的结果

- 销量区间
- 库存情景表
- 获客成本上限
- 组合风险与触发器
- 数据范围、来源、采集时间、样本与限制。
- 关键假设、待补证据、风险和不可确定项。
- 若有动作：对象、旧值、新值、预期、停止条件、回退值与审批状态。

方案状态使用 `READY FOR REVIEW / DRAFT / HOLD / STOP`；如已执行，另行记录实际结果及回读证据。未得到明确批准时，不得声称已修改线上对象。
