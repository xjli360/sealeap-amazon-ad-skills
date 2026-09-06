---
name: sealeap-baize-amazon-breakout-case-audit
description: "Reverse-engineer an Amazon breakout case by testing competing explanations across product innovation, brand, keyword breadth, organic visibility, timing, variants, promotions, returns, and compliance. Use for 爆款案例复盘、为什么突然增长、是不是站外、能不能复制、成功因素拆解."
---

# Amazon 爆款案例因果审计

## 目标

Reverse-engineer an Amazon breakout case by testing competing explanations across product innovation, brand, keyword breadth, organic visibility, timing, variants, promotions, returns, and compliance.

## 不可妥协的边界

- 当前 Amazon 官方政策、账户资格、站点字段和一方数据优先于本 Skill 的经验框架。
- 第三方数据一律标为估算或前台观测，不得写成 Amazon 一方事实。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 一次实验只改变一个主要变量，并记录基线、样本、成功、停止和回退条件。
- 不得复制来源材料或竞品表达；输出必须按当前任务重新组织并可由现有证据支撑。
- 不模仿评论合并、变体滥用、刷单或其他人为干预。
- 第三方历史数据不能证明后台真实操作或违规行为。

## 先判断任务模式

1. **诊断**：读取现状、证据和缺口，不生成线上写入动作。
2. **方案草案**：输出可审核的结构、参数范围、实验和回退值。
3. **执行准备**：只生成待批准变更表或 API/控制台操作草案。
4. **已批准执行**：仅对用户在当前会话明确批准的对象和字段执行，并立即回读核验。

用户未指定时采用“诊断”。

## 开始前要拿到

- 目标 marketplace 与案例 ASIN 的明确时间范围
- 销量、评论、价格、促销、变体和上架时间线
- 关键词自然/广告可见度、品牌与站外流量代理证据
- 可复核来源、数据口径、缺失项和替代解释

缺失项必须标为 `NEEDS_EVIDENCE`；不得猜数字、补属性或把不同站点、ASIN、变体、币种和时间窗混在一起。

## 工作流

先读取 [references/playbook.md](references/playbook.md)，确认该方法适用于当前对象。按以下顺序执行：

1. 先列出功能、品牌、价格、流量、时机、变体和促销等互斥或并存解释。
2. 用关键词自然覆盖、销量评论时间线和市场需求逐项证伪。
3. 区分相关事件与可归因因素，不从结果倒推唯一原因。
4. 识别不可复制条件、合规风险和幸存者偏差。
5. 将可迁移部分转成产品、页面、选词和位置实验。

最后做数据充分性检查，并把结论分成 `FACT / ESTIMATE / HYPOTHESIS / UNKNOWN`。若关键证据不足，状态写 `HOLD`。

## 第三方 MCP 数据

仅在自有数据不足且当前任务确实需要外部证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，再使用 `scripts/mcp_research.py`。本 Skill 的外部取数目的：补充关键词历史、销量评论变化、上架时间、促销和市场趋势代理数据。

- 先 `doctor`，再 `search-tools` 和 `describe`；工具名及参数以实时 `tools/list` 与 `inputSchema` 为准。
- Token 只从环境变量读取。不得写入命令参数、URL、Skill、报告、日志或 Git。
- `tools/call` 或 Actor 可能计费；先展示 Provider、工具、无密钥业务参数、预计成本与输出位置，核对已有授权覆盖后才加 `--allow-cost`；该标志不是费用上限。


## 必须交付的结果

- 候选因果树
- 证据与反证
- 可复制与不可复制项
- 合规实验
- 数据范围、来源、采集时间、样本与限制。
- 关键假设、待补证据、风险和不可确定项。
- 若有动作：对象、旧值、新值、预期、停止条件、回退值与审批状态。

方案状态使用 `READY FOR REVIEW / DRAFT / HOLD / STOP`；如已执行，另行记录实际结果及回读证据。未得到明确批准时，不得声称已修改线上对象。
