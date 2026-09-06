---
name: sealeap-baize-amazon-keyword-weight-model
description: "Build testable hypotheses for Amazon keyword relevance and ranking from conversion, clicks, orders, add-to-cart signals, listing semantics, and related-query behavior without claiming a proprietary ranking formula. Use for 关键词权重、精准小词和大词关系、为什么出单后曝光增加、自然排名机制假设."
---

# Amazon 关键词权重假设

## 目标

Build testable hypotheses for Amazon keyword relevance and ranking from conversion, clicks, orders, add-to-cart signals, listing semantics, and related-query behavior without claiming a proprietary ranking formula.

## 不可妥协的边界

- 当前 Amazon 官方政策、账户资格、站点字段和一方数据优先于本 Skill 的经验框架。
- 第三方数据一律标为估算或前台观测，不得写成 Amazon 一方事实。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 一次实验只改变一个主要变量，并记录基线、样本、成功、停止和回退条件。
- 不得复制来源材料或竞品表达；输出必须按当前任务重新组织并可由现有证据支撑。
- 任何指标权重排序和间接加权机制都不是公开公式。
- 排名抓取可能受地点、登录态、变体和个性化影响。

## 先判断任务模式

1. **诊断**：读取现状、证据和缺口，不生成线上写入动作。
2. **方案草案**：输出可审核的结构、参数范围、实验和回退值。
3. **执行准备**：只生成待批准变更表或 API/控制台操作草案。
4. **已批准执行**：仅对用户在当前会话明确批准的对象和字段执行，并立即回读核验。

用户未指定时采用“诊断”。

## 开始前要拿到

- marketplace、产品事实、ASIN/SKU 与目标购买意图
- 本品和可比竞品的关键词、自然位置、广告可见度与采样时间
- 搜索词报告、转化、CPC、订单、利润和 Listing 当前覆盖
- 站点语言、变体、价格、库存与同期促销记录

缺失项必须标为 `NEEDS_EVIDENCE`；不得猜数字、补属性或把不同站点、ASIN、变体、币种和时间窗混在一起。

## 工作流

先读取 [references/playbook.md](references/playbook.md)，确认该方法适用于当前对象。按以下顺序执行：

1. 把直接词表现与相关词联动拆成不同假设。
2. 记录出单前后曝光、点击、转化和自然位置，但控制价格、促销与库存。
3. 用产品事实和搜索结果验证词根相近是否也代表购买意图相近。
4. 为每条可能的词间关系设置可证伪观察窗。
5. 只把观测结果写成账户内证据，不外推为平台算法。

最后做数据充分性检查，并把结论分成 `FACT / ESTIMATE / HYPOTHESIS / UNKNOWN`。若关键证据不足，状态写 `HOLD`。

## 第三方 MCP 数据

仅在自有数据不足且当前任务确实需要外部证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，再使用 `scripts/mcp_research.py`。本 Skill 的外部取数目的：获取关键词自然位置、需求、相关词和历史趋势的代理观测。

- 先 `doctor`，再 `search-tools` 和 `describe`；工具名及参数以实时 `tools/list` 与 `inputSchema` 为准。
- Token 只从环境变量读取。不得写入命令参数、URL、Skill、报告、日志或 Git。
- `tools/call` 或 Actor 可能计费；先展示 Provider、工具、无密钥业务参数、预计成本与输出位置，核对已有授权覆盖后才加 `--allow-cost`；该标志不是费用上限。


## 必须交付的结果

- 关键词假设图
- 观测变量
- 证伪条件
- 账户内结论
- 数据范围、来源、采集时间、样本与限制。
- 关键假设、待补证据、风险和不可确定项。
- 若有动作：对象、旧值、新值、预期、停止条件、回退值与审批状态。

方案状态使用 `READY FOR REVIEW / DRAFT / HOLD / STOP`；如已执行，另行记录实际结果及回读证据。未得到明确批准时，不得声称已修改线上对象。
