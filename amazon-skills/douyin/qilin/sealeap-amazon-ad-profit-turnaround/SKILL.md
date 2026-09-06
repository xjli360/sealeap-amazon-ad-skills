---
name: sealeap-amazon-ad-profit-turnaround
description: Rebuild an unprofitable Amazon ad account by replacing head-term dependence with a verified keyword universe, root-based broad tests, pre-emptive negatives, exact harvesting, and portfolio-level profit controls. Use when ACoS is extreme, lowering ads kills sales, or a product needs a structured turnaround. Do not promise a fixed turnaround period.
---

# Amazon 广告利润重建

## 目标

在不依赖高价大词硬扛的情况下，重新找到可盈利查询组合并恢复可控订单。

## 适用任务

- 核心大词 CPC 高、自然侧也没有改善。
- 关广告没单、开广告亏损。
- 需要从现有账户迁移到新结构而不一次性断流。

## 开始前要拿到

- 完整搜索词和投放历史、否定词、广告位与预算。
- 产品词库、词根分类和明确不相关属性。
- 售价、贡献毛利、库存与最大重建损失。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 不宣称固定周期扭亏；结果取决于商品竞争力和市场。
- 不把无转化点击一律视为关键词收录价值，必须受预算约束。
- 否定词先复核歧义，旧结构分阶段降载而不是盲目全关。
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

### 1. 建立损失地图

按查询、目标、广告位和活动找出亏损来源，计算关闭风险与可保留的订单。

### 2. 重建词库

合并自有查询和授权研究，按高相关词根、次级词根、不相关词根和核心词分类。

### 3. 部署受控覆盖

用紧密自动和词根级广泛测试，先加入经过复核的不相关词根否定，并设置组合预算帽。

### 4. 逐批验证

预算有限时从最相关词根开始；比较 CVR、CPA、利润和样本，不追求一次覆盖全部词。

### 5. 精准收割

稳定出单词迁移到精准广告，单独管理预算；探索层用去重规则继续发现。

### 6. 平滑切换

新结构达到订单与利润门槛后才逐步降低旧大词依赖，并监控总销量、TACoS 和库存。

## 判断标准

- 重建前后口径一致。
- 每个词根批次有预算和退出门槛。
- 账户级利润改善而非单一活动美化。

## 必须交付的结果

- 现有亏损地图。
- 词根批次和否定词方案。
- 新旧结构迁移计划。
- 利润、订单和库存护栏。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
