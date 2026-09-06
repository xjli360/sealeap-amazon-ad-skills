---
name: sealeap-amazon-large-keyword-portfolio
description: Design a scalable Amazon long-tail keyword portfolio with evidence-based query generation, clustering versus single-keyword isolation, portfolio budget caps, automation drafts, sample safeguards, and human approvals. Use when the user asks about hundreds of campaigns, single-keyword structures, low-bid long-tail coverage, bulk sheets, or automated bid rules. Do not create live rules or campaigns without approval.
---

# Amazon 大规模关键词组合

## 目标

扩大相关长尾覆盖的同时控制预算碎片化、自动化误杀和管理复杂度，而不是追求活动数量本身。

## 适用任务

- 候选关键词很多，需要批量建广告。
- 考虑单词单组或单活动结构。
- 希望用规则自动升价、降价、否定或暂停。

## 开始前要拿到

- 经验证的关键词主表、词根、意图和搜索量代理。
- 批量表格字段、账号限制、组合预算和命名规范。
- 历史 CPC/CVR、最小样本、止损和审批责任人。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 活动数量没有固定正确值；低流量词可按同质意图聚类，避免无意义碎片化。
- 词根组合生成的查询必须通过真实搜索或相关性证据过滤，不能把机器拼词直接投放。
- 自动规则默认只生成建议；升价、否定和暂停需样本护栏与人工批准。
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

### 1. 清洗候选词

去重并验证真实相关性、购买意图和可读性，删除仅语法成立但无消费者证据的组合词。

### 2. 决定粒度

高价值或需独立预算的词采用隔离结构；低流量同质词按词根聚类，控制活动数量。

### 3. 设置预算保护

给产品或组合设置日预算帽、累计测试损失和库存护栏，再分配到各批次。

### 4. 建立竞价阶梯

按 CPC 先验和利润从保守竞价开始，无曝光时小步上调；每次保留变更日志。

### 5. 设计安全规则

规则包含最小点击、最小时间、最大单次幅度、冷却期、累计花费和回滚条件。

### 6. 批量预检

在上传前验证实体 ID、匹配类型、预算、否定冲突和重复覆盖；输出草稿等待批准。

## 判断标准

- 关键词总数、活动总数和预估最大日花费一致。
- 所有自动规则都有样本与冷却保护。
- 批量文件不含凭证和敏感账号数据。

## 必须交付的结果

- 关键词清洗与聚类结果。
- 活动粒度和命名方案。
- 预算帽、竞价阶梯和安全规则。
- 待审核批量表格规格。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
