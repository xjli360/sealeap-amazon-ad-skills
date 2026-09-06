---
name: sealeap-amazon-white-hat-product-ranking
description: Plan an ad-intensive but policy-compliant Amazon launch that expands indexed and converting keyword coverage while preserving profitability and inventory guardrails. Use when the user asks for a pure white-hat launch, broad keyword coverage, when to move terms into exact campaigns, or how to combine auto, broad, product targeting, and eligible promotions. No review manipulation or ranking guarantees.
---

# Amazon 合规关键词覆盖扩张

## 目标

通过分层广告和真实转化扩大有效关键词覆盖，把主要出单词变成可独立管理的资产，并在成熟后收缩无效花费。

## 适用任务

- Listing 已具备竞争力且预算相对充足的新品。
- 希望同时扩大词量并精细管理主力词。
- 需要把促销纳入广告节奏但保持官方资格和利润边界。

## 开始前要拿到

- 关键词全集及头部、中部、长尾和词根分类。
- Listing readiness、库存、价格、Vine 或其他官方项目资格。
- 广告预算、促销成本、贡献利润和停止线。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 评论只能来自真实客户或符合资格的官方项目；不得安排直评、测评或评论合并。
- 不得用大规模广告数量替代相关性和预算控制。
- 促销必须符合当前官方资格与价格规则，并先核算促销后贡献利润。
- 当前 Amazon 官方政策、帮助页、账户资格和后台实际字段优先于本 Skill 中的经验框架；规则可能变化时先核验。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不输出原素材的创作者身份、账号、链接、视频编号或可反查线索；当前业务证据的官方来源、采集时间和口径仍需保留。

## 第三方 MCP 数据

只有在本任务确实需要外部市场、竞品、关键词或公开网页证据时，才读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，并使用 scripts/mcp_research.py。

- 先动态执行 tools/list、search-tools 和 describe，依据实时 inputSchema 构造参数，不照搬历史工具名。
- 凭证只从环境变量读取，不放进命令参数、URL、Skill、结果文件或 Git。
- tools/call 可能计费。调用前展示 Provider、工具名、无密钥参数、预计成本与输出位置，核对已有授权覆盖后才加 --allow-cost；该标志不是费用上限。
- 第三方数据标为估算或代理证据，记录 Provider、工具、无密钥参数、查询时间和原始结果位置；失败一次后记录缺口，不反复消耗额度。
- 脱敏结果用 --output 写到 Skill 包之外的任务私有目录；不假设安装位置受仓库 .gitignore 保护，不把运行结果写入 Skill 包。

## 工作流

### 1. 确认可承接

检查商品信息、价格、库存、配送、合规和真实评价基础，未达标时先修 Listing 或产品。

### 2. 扩展收录入口

建立受控自动、相关词根广泛和高相似商品投放，分别定义探索对象和预算。

### 3. 保护转化

首轮不直接无差别冲头部词，优先覆盖中部词和高意图词根；不相关词根提前审慎否定。

### 4. 精准承接

当某词达到相关性、样本和利润门槛且在探索层预算不稳时，迁移到独立精准广告。

### 5. 分层放量

随着稳定词增多，再逐步扩展头部或更泛流量；符合资格时用官方促销做独立实验，避免同时改变过多变量。

### 6. 成熟收敛

按增量利润保留主力词，降低重复探索和低效广告，并持续监控库存与自然侧。

## 判断标准

- 广告数量由业务问题决定，不设人为数量目标。
- 每个迁移词有报告证据和去重方案。
- 放量后总利润、退货和库存仍在护栏内。

## 必须交付的结果

- 覆盖层、承接层和放量层架构。
- 关键词迁移与否定表。
- 促销实验和库存保护方案。
- 成熟期广告收敛计划。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
