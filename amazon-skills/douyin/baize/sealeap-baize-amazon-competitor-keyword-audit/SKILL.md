---
name: sealeap-baize-amazon-competitor-keyword-audit
description: "Infer competitor keyword coverage from observable organic and sponsored positions, shared attributes, query patterns, and product relevance without claiming access to a competitor account. Use for 竞品广告词分析、反查竞品关键词、判断精准词与探索词、找防守或捡漏词. Do not claim unseen campaign settings as facts."
---

# Amazon 竞品关键词结构审计

## 目标

Infer competitor keyword coverage from observable organic and sponsored positions, shared attributes, query patterns, and product relevance without claiming access to a competitor account.

## 不可妥协的边界

- 当前 Amazon 官方政策、账户资格、站点字段和一方数据优先于本 Skill 的经验框架。
- 第三方数据一律标为估算或前台观测，不得写成 Amazon 一方事实。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 一次实验只改变一个主要变量，并记录基线、样本、成功、停止和回退条件。
- 不得复制来源材料或竞品表达；输出必须按当前任务重新组织并可由现有证据支撑。
- 前台观测不能反推出竞品后台匹配类型、竞价或预算。
- 自然排名高也可能来自品牌、历史或变体因素，必须核对本品适配。

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

1. 选择功能、外观、价格和评价基础足够接近的竞品。
2. 分开记录自然可见度、广告可见度、词义相关性和采样时间。
3. 重复属性词可作为词组或广泛策略线索；杂乱查询只作为自动流量假设。
4. 优先找自然表现强、语义匹配但广告覆盖弱的候选词。
5. 对自然靠后或无自然证据的广告词做低相关风险复核，而非自动否定。

最后做数据充分性检查，并把结论分成 `FACT / ESTIMATE / HYPOTHESIS / UNKNOWN`。若关键证据不足，状态写 `HOLD`。

## 第三方 MCP 数据

仅在自有数据不足且当前任务确实需要外部证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，再使用 `scripts/mcp_research.py`。本 Skill 的外部取数目的：获取竞品流量词、自然位置、广告覆盖与搜索需求代理数据。

- 先 `doctor`，再 `search-tools` 和 `describe`；工具名及参数以实时 `tools/list` 与 `inputSchema` 为准。
- Token 只从环境变量读取。不得写入命令参数、URL、Skill、报告、日志或 Git。
- `tools/call` 或 Actor 可能计费；先展示 Provider、工具、无密钥业务参数、预计成本与输出位置，核对已有授权覆盖后才加 `--allow-cost`；该标志不是费用上限。


## 必须交付的结果

- 竞品词证据表
- 结构假设与置信度
- 捡漏候选
- 本品验证计划
- 数据范围、来源、采集时间、样本与限制。
- 关键假设、待补证据、风险和不可确定项。
- 若有动作：对象、旧值、新值、预期、停止条件、回退值与审批状态。

方案状态使用 `READY FOR REVIEW / DRAFT / HOLD / STOP`；如已执行，另行记录实际结果及回读证据。未得到明确批准时，不得声称已修改线上对象。
