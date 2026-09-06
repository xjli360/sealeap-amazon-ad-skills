---
name: sealeap-amazon-keyword-selection-and-campaign-mapping
description: Turn an Amazon keyword universe into a clean taxonomy and campaign map using relevance, intent, roots, negatives, and evidence from authorized reports. Use when the user asks how to collect keywords, perform word-root analysis, choose auto versus broad versus exact targeting, or prevent broad campaigns from drifting. Produce a draft architecture and never apply ad changes without explicit approval.
---

# Amazon 关键词选取与广告映射

## 目标

把杂乱的关键词集合转成可执行的分类、否定和投放结构，使探索范围与高转化目标同时可控。

## 适用任务

- 竞品反查后词太多、重复多、不知道如何下手。
- 需要为新品搭建自动、广泛、词组、精准和商品投放的职责分工。
- 广泛流量跑偏，需要建立词根级前置否定。

## 开始前要拿到

- 产品事实表：品名、材质、功能、兼容性、尺寸、人群、场景和明确不适用项。
- 授权来源的竞品关键词、Amazon 搜索词报告、品牌分析或其他可追溯数据。
- 搜索量或代理指标、CPC、转化、订单和自然排名数据。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 竞品词不等于本品词；每个关键词必须通过产品事实和相关性复核。
- 不得购买、抓取或使用无权访问的竞品机密广告数据。
- 否定词先检查歧义和变体，避免一次词根否定误伤有效查询。
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

### 1. 合并与去重

统一大小写、单复数和常见拼写，保留原始来源字段，删除重复项但不丢失证据链。

### 2. 建立词根 taxonomy

至少区分高意图属性词根、覆盖型高频词根、通用词、品牌词、竞品词和不相关词根。

### 3. 评分排序

按事实相关性、购买意图、流量、竞争、预估转化和利润空间评分；缺失数据不伪造，降级为待验证。

### 4. 映射广告职责

自动用于受控发现，广泛或词组用于词根扩展，精准用于已验证词，商品投放用于相似详情页或类目机会。

### 5. 建立否定逻辑

明确哪些词做精准否定、哪些词根可做词组否定，并记录否定原因和复核人。

### 6. 持续迁移

按固定窗口把出单搜索词迁移、把高耗无转化词降级或否定，并同步检查广告间的重复覆盖。

## 判断标准

- 词库每行至少包含关键词、相关性、意图、词根、证据来源、建议投放和状态。
- 高转化只是预测时必须明确标为假设。
- 广告结构能回答每一组的探索对象、预算职责和迁移出口。

## 必须交付的结果

- 去重后的关键词主表。
- 词根分类、优先级和不相关词表。
- 关键词到广告类型的映射表。
- 迁移、否定和复核节奏。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
