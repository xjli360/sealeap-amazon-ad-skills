---
name: sealeap-amazon-asin-targeting-strategy
description: Plan Amazon ASIN product-targeting campaigns by scoring product similarity, demand, truthful conversion advantages, placement hypotheses, budget isolation, and downstream search-term harvesting. Use when the user asks whether a new product can start with ASIN targeting, how to choose competitor ASINs, or when to move discovered queries into exact campaigns. Avoid review manipulation and ranking guarantees.
---

# Amazon ASIN 商品投放策略

## 目标

用少量高匹配商品目标验证详情页与搜索环境机会，并把被报告证实的查询或目标迁移到独立结构。

## 适用任务

- 新品希望用商品投放启动。
- 从大量竞品 ASIN 中筛选少量高价值目标。
- 商品投放有订单但预算与目标混杂。

## 开始前要拿到

- 候选 ASIN 的品类、规格、用途、价格、评分、配送和销量代理。
- 本品真实差异化、价格、评分、库存和内容承接力。
- 商品投放、搜索词和广告位报告。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 所谓转化优势必须来自真实价格、功能、内容或服务，不得来自虚假评论或人为参考价。
- 商品投放不能保证复制对方关键词，也不能精确承诺出现在某个自然页码。
- 不得使用无授权的竞品私密数据。
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

### 1. 建立目标评分

按品类相关性、功能相似度、受众重合、需求、价格区间和本品真实优势筛选。

### 2. 控制初始范围

优先单目标或小同质组，关闭不必要的扩展，确保每个结果可归因。

### 3. 提出位置假设

根据广告位报告区分商品页面与搜索位置表现；调整基础竞价和位置系数前先计算有效出价。

### 4. 运行验证

记录点击、CVR、CPA、已购商品、搜索词和利润；无订单时先判断样本和相关性。

### 5. 迁移赢家

稳定商品目标独立管理；报告中出现且证据充分的高转化查询可迁移到精准关键词广告。

### 6. 扩大边界

只有首批结果成立后才增加更广目标，并持续检查内部重复与库存。

## 判断标准

- 每个候选 ASIN 都有入选或排除理由。
- 位置结论来自报告，不由主观前台观察单独决定。
- 迁移查询有实际报告证据。

## 必须交付的结果

- ASIN 目标评分与批次。
- 商品投放结构和竞价假设。
- 目标或查询迁移规则。
- 扩量与停止条件。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
