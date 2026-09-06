---
name: sealeap-baize-amazon-ad-conversion-states
description: "Diagnose Amazon ad conversion that declines, stays weak, or fluctuates by separating placement expansion, price-value fit, query relevance, product-page differentiation, and market events. Use for 广告转化越来越差、一直不出单、转化忽高忽低、点击增加但订单不增. Do not use to make live campaign changes without approval."
---

# Amazon 广告转化状态诊断

## 目标

Diagnose Amazon ad conversion that declines, stays weak, or fluctuates by separating placement expansion, price-value fit, query relevance, product-page differentiation, and market events.

## 不可妥协的边界

- 当前 Amazon 官方政策、账户资格、站点字段和一方数据优先于本 Skill 的经验框架。
- 第三方数据一律标为估算或前台观测，不得写成 Amazon 一方事实。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 一次实验只改变一个主要变量，并记录基线、样本、成功、停止和回退条件。
- 不得复制来源材料或竞品表达；输出必须按当前任务重新组织并可由现有证据支撑。
- 位置靠前不必然更好；必须用本 ASIN 的位置报告验证。
- 竞品自然排名只能作为相关性线索，不能证明本品会转化。

## 先判断任务模式

1. **诊断**：读取现状、证据和缺口，不生成线上写入动作。
2. **方案草案**：输出可审核的结构、参数范围、实验和回退值。
3. **执行准备**：只生成待批准变更表或 API/控制台操作草案。
4. **已批准执行**：仅对用户在当前会话明确批准的对象和字段执行，并立即回读核验。

用户未指定时采用“诊断”。

## 开始前要拿到

- marketplace、店铺、ASIN/SKU、广告类型和目标
- 同口径的 Campaign、Targeting、Search Term、Placement 与 Advertised Product 报告
- 售价、优惠、COGS、Amazon 费用、退款与目标贡献利润
- 库存、Buy Box、Listing、评论和同期市场事件

缺失项必须标为 `NEEDS_EVIDENCE`；不得猜数字、补属性或把不同站点、ASIN、变体、币种和时间窗混在一起。

## 工作流

先读取 [references/playbook.md](references/playbook.md)，确认该方法适用于当前对象。按以下顺序执行：

1. 先把问题分成持续恶化、长期偏弱和短期波动三种状态，使用同口径时间窗比较。
2. 若点击速度上升而订单不增，先检查位置和查询是否扩展到低意向流量。
3. 若长期偏弱，依次核对价格与价值表达、关键词意图、评论基础和页面差异。
4. 若短期波动，记录竞品促销、价格、库存、Buy Box 与季节事件，不把单日变化当趋势。
5. 只选择一个主变量做小幅实验，并预先写明花费上限和恢复值。

最后做数据充分性检查，并把结论分成 `FACT / ESTIMATE / HYPOTHESIS / UNKNOWN`。若关键证据不足，状态写 `HOLD`。

## 第三方 MCP 数据

仅在自有数据不足且当前任务确实需要外部证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，再使用 `scripts/mcp_research.py`。本 Skill 的外部取数目的：补充关键词、竞品自然排名和市场价格的第三方代理证据。

- 先 `doctor`，再 `search-tools` 和 `describe`；工具名及参数以实时 `tools/list` 与 `inputSchema` 为准。
- Token 只从环境变量读取。不得写入命令参数、URL、Skill、报告、日志或 Git。
- `tools/call` 或 Actor 可能计费；先展示 Provider、工具、无密钥业务参数、预计成本与输出位置，核对已有授权覆盖后才加 `--allow-cost`；该标志不是费用上限。


## 必须交付的结果

- 三类状态判定
- 根因证据矩阵
- 单变量实验卡
- 待批准的最小调整
- 数据范围、来源、采集时间、样本与限制。
- 关键假设、待补证据、风险和不可确定项。
- 若有动作：对象、旧值、新值、预期、停止条件、回退值与审批状态。

方案状态使用 `READY FOR REVIEW / DRAFT / HOLD / STOP`；如已执行，另行记录实际结果及回读证据。未得到明确批准时，不得声称已修改线上对象。
