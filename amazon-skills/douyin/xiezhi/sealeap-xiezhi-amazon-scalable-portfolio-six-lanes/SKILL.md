---
name: sealeap-xiezhi-amazon-scalable-portfolio-six-lanes
description: "Route Amazon product research across six portfolio lanes: niche demand, extensible variations, bulky high-value items, regulated or high-barrier products, seasonal events, and higher-ticket bundles. Use when building a diversified product pipeline around operational fit."
---

# Amazon 可复制组合六赛道

## 目标

按团队能力把候选分入六种结构性机会赛道，每种赛道使用独立证据和风险门槛。

## 适用任务

- 建立多赛道选品雷达。
- 选择与供应链和团队能力匹配的方向。
- 避免把低评论或多 SKU 简化为铺货。

## 开始前要拿到

- 团队资金、供应链、认证、物流、海外仓和设计能力。
- 各赛道的需求、竞品、评论、价格和关键词证据。
- 当前可接受的库存、退货和合规风险。
- 多 SKU 管理、素材和广告容量。

缺少字段时列出证据缺口，并把相关结论标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`；不要补造数据。

## 不可妥协的边界

- 第三方数据均为估算或代理证据；Amazon 一方报告、后台实时字段和产品事实优先。
- 经验阈值只能作为可调起点，必须展示敏感性分析，不能写成 Amazon 官方规则。
- 不得捏造销量、搜索量、CPC、CVR、成本、认证、产品属性或消费者需求。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不输出或保存素材来源身份、账号、链接、作品编号、互动数据、原始话术或其他可反查来源的线索。
- 不得把政策、认证、物流困难视为可以规避的竞争壁垒。
- 所有变体、评论和流量策略必须保持合规。

## 工作流

### 1. 冷门细分

寻找精准需求、竞品较少且低评论正常出单的中小市场。

### 2. 可扩变体

选择真实可按图案、颜色、规格或主题扩展且符合 variation policy 的产品。

### 3. 大件高货值

只有具备物流、配送、退货翻新和现金能力时，才评估天然高门槛大件。

### 4. 高门槛产品

仅在认证、开发、质量体系和授权已具备时评估，不把监管复杂性当作轻易红利。

### 5. 季节与活动

用历史周期和提前布局寻找阶段需求，并以保守库存管理季末风险。

### 6. 高客单与套装

通过真实价值、便利和单位经济提升客单，不以虚假组合制造价格。

### 7. 组合配置

对每条赛道计算能力匹配、风险、资本占用和预期贡献，设年度配置上限。

## 判断标准

- 六赛道是机会分类，不是每个团队都应覆盖全部。
- 低评论正常出单是共同线索，但必须结合精准词、单位经济和异常排除。
- 高认证和大件产品的损失尾部更大，缺少能力时直接 NO-GO。

## 第三方 MCP 数据

需要外部关键词、竞品、评论或公开网页证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，并使用 `scripts/mcp_research.py`。

- 先动态执行 `tools/list`、`search-tools` 和 `describe`，依据实时 `inputSchema` 构造参数。
- 凭证只从环境变量读取，不进入参数、URL、Skill、终端输出或 Git。
- 可能计费的 `tools/call` 先展示 Provider、工具、无密钥参数、预计成本与输出位置，核对已有授权；仅在授权覆盖本次范围时使用 `--allow-cost`，该标志不是费用上限。
- 脱敏结果用 `--output` 写入 Skill 包之外的任务私有目录；不假设安装位置受仓库 `.gitignore` 保护。第三方数据标为估算或代理证据。
- 失败一次后记录缺口，不以重复付费重试掩盖不可用状态。

## 必须交付的结果

- 六赛道能力矩阵
- 候选路由清单
- 资本/风险配置
- 每赛道验证门槛
- 季度产品管线

结尾列出站点、数据窗口、证据来源、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行细节、证据字段和质量检查见 [references/playbook.md](references/playbook.md)。
