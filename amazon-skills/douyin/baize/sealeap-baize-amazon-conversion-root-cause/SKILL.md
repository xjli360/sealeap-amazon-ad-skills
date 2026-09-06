---
name: sealeap-baize-amazon-conversion-root-cause
description: "Diagnose weak Amazon conversion product-first by benchmarking comparable listings, market difficulty, price-value fit, visual differentiation, keyword precision, and placement mix. Use for 产品转化差、广告不出单、价格还是图片问题、词不准还是商品页问题、商品页位置差."
---

# Amazon 商品转化根因排查

## 目标

Diagnose weak Amazon conversion product-first by benchmarking comparable listings, market difficulty, price-value fit, visual differentiation, keyword precision, and placement mix.

## 不可妥协的边界

- 当前 Amazon 官方政策、账户资格、站点字段和一方数据优先于本 Skill 的经验框架。
- 第三方数据一律标为估算或前台观测，不得写成 Amazon 一方事实。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 一次实验只改变一个主要变量，并记录基线、样本、成功、停止和回退条件。
- 不得复制来源材料或竞品表达；输出必须按当前任务重新组织并可由现有证据支撑。
- 先产品后广告是诊断顺序，不代表广告永远不是根因。
- 所有竞品和销量比较都需保留来源、站点、时间与限制。

## 先判断任务模式

1. **诊断**：读取现状、证据和缺口，不生成线上写入动作。
2. **方案草案**：输出可审核的结构、参数范围、实验和回退值。
3. **执行准备**：只生成待批准变更表或 API/控制台操作草案。
4. **已批准执行**：仅对用户在当前会话明确批准的对象和字段执行，并立即回读核验。

用户未指定时采用“诊断”。

## 开始前要拿到

- marketplace、ASIN/SKU、产品事实和当前 Listing
- 同购买意图可比竞品、价格、评论、图片和销量
- Search Term、Placement、CTR、CVR、订单、退货和利润
- VOC、Q&A、退货原因与任何页面或广告变更日志

缺失项必须标为 `NEEDS_EVIDENCE`；不得猜数字、补属性或把不同站点、ASIN、变体、币种和时间窗混在一起。

## 工作流

先读取 [references/playbook.md](references/playbook.md)，确认该方法适用于当前对象。按以下顺序执行：

1. 先建立同站点、同意图、外观价格和评论基础接近的可比组。
2. 比较本品与可比组销量，再判断所在成熟度层的市场难度。
3. 核对价格差是否有明确价值证据承接。
4. 评估主图在缩略图中是否传达真实差异，而非只看美观。
5. 产品侧无明显缺口后，再查广告词相关性、位置和搜索词。

最后做数据充分性检查，并把结论分成 `FACT / ESTIMATE / HYPOTHESIS / UNKNOWN`。若关键证据不足，状态写 `HOLD`。

## 第三方 MCP 数据

仅在自有数据不足且当前任务确实需要外部证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，再使用 `scripts/mcp_research.py`。本 Skill 的外部取数目的：获取可比竞品、评论层级、价格、关键词和自然可见度代理数据。

- 先 `doctor`，再 `search-tools` 和 `describe`；工具名及参数以实时 `tools/list` 与 `inputSchema` 为准。
- Token 只从环境变量读取。不得写入命令参数、URL、Skill、报告、日志或 Git。
- `tools/call` 或 Actor 可能计费；先展示 Provider、工具、无密钥业务参数、预计成本与输出位置，核对已有授权覆盖后才加 `--allow-cost`；该标志不是费用上限。


## 必须交付的结果

- 产品侧四层诊断
- 广告侧复核
- 首要根因
- 单变量改进实验
- 数据范围、来源、采集时间、样本与限制。
- 关键假设、待补证据、风险和不可确定项。
- 若有动作：对象、旧值、新值、预期、停止条件、回退值与审批状态。

方案状态使用 `READY FOR REVIEW / DRAFT / HOLD / STOP`；如已执行，另行记录实际结果及回读证据。未得到明确批准时，不得声称已修改线上对象。
