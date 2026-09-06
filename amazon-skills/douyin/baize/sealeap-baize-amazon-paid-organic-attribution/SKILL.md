---
name: sealeap-baize-amazon-paid-organic-attribution
description: "Assess paid-versus-organic Amazon order contribution with whole-ASIN economics, cannibalization tests, query relevance, and time-window controls instead of subtracting attributed ad orders mechanically. Use for 广告单挤占自然单、关广告会不会掉单、哪些词可停、自然订单怎么算、整体广告盈利."
---

# Amazon 广告与自然订单归因

## 目标

Assess paid-versus-organic Amazon order contribution with whole-ASIN economics, cannibalization tests, query relevance, and time-window controls instead of subtracting attributed ad orders mechanically.

## 不可妥协的边界

- 当前 Amazon 官方政策、账户资格、站点字段和一方数据优先于本 Skill 的经验框架。
- 第三方数据一律标为估算或前台观测，不得写成 Amazon 一方事实。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 一次实验只改变一个主要变量，并记录基线、样本、成功、停止和回退条件。
- 不得复制来源材料或竞品表达；输出必须按当前任务重新组织并可由现有证据支撑。
- 自然订单不能简单等同于会话订单减广告订单，报表口径和归因窗可能不同。
- 第三方关键词数据之间可能口径冲突，保留各来源而非强行合并。

## 先判断任务模式

1. **诊断**：读取现状、证据和缺口，不生成线上写入动作。
2. **方案草案**：输出可审核的结构、参数范围、实验和回退值。
3. **执行准备**：只生成待批准变更表或 API/控制台操作草案。
4. **已批准执行**：仅对用户在当前会话明确批准的对象和字段执行，并立即回读核验。

用户未指定时采用“诊断”。

## 开始前要拿到

- marketplace、ASIN/SKU、广告归因窗与业务报告时间窗
- 广告订单、总订单、会话、自然位置、TACOS 与贡献利润
- 价格、优惠、库存、Buy Box、Listing 和评论变更日志
- 查询、广告位和投放对象的相关性证据

缺失项必须标为 `NEEDS_EVIDENCE`；不得猜数字、补属性或把不同站点、ASIN、变体、币种和时间窗混在一起。

## 工作流

先读取 [references/playbook.md](references/playbook.md)，确认该方法适用于当前对象。按以下顺序执行：

1. 统一 ASIN、站点、归因窗和业务报告日期，先看总订单与贡献利润。
2. 记录广告点击带来的详情页曝光和后续非直接归因影响，但标为假设。
3. 仅在自然位、价格、库存和页面稳定时做阶梯降价或停投实验。
4. 比较广告订单下降后自然订单是否补回、总单是否稳定、利润是否改善。
5. 不因某词短期未归因订单就自动否定；先检查相关性和样本。

最后做数据充分性检查，并把结论分成 `FACT / ESTIMATE / HYPOTHESIS / UNKNOWN`。若关键证据不足，状态写 `HOLD`。

## 第三方 MCP 数据

仅在自有数据不足且当前任务确实需要外部证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，再使用 `scripts/mcp_research.py`。本 Skill 的外部取数目的：补充自然排名与关键词相关性；归因结论仍以 Amazon 一方报告和实验为主。

- 先 `doctor`，再 `search-tools` 和 `describe`；工具名及参数以实时 `tools/list` 与 `inputSchema` 为准。
- Token 只从环境变量读取。不得写入命令参数、URL、Skill、报告、日志或 Git。
- `tools/call` 或 Actor 可能计费；先展示 Provider、工具、无密钥业务参数、预计成本与输出位置，核对已有授权覆盖后才加 `--allow-cost`；该标志不是费用上限。


## 必须交付的结果

- 口径对齐表
- 增量性实验
- 词级保留与暂停理由
- 利润变化
- 数据范围、来源、采集时间、样本与限制。
- 关键假设、待补证据、风险和不可确定项。
- 若有动作：对象、旧值、新值、预期、停止条件、回退值与审批状态。

方案状态使用 `READY FOR REVIEW / DRAFT / HOLD / STOP`；如已执行，另行记录实际结果及回读证据。未得到明确批准时，不得声称已修改线上对象。
