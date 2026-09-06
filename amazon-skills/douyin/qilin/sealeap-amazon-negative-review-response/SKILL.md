---
name: sealeap-amazon-negative-review-response
description: Triage negative Amazon reviews into policy violations, suspected abuse, and genuine product feedback, then prepare factual official reports and product-remediation actions. Use when the user asks whether a review can be removed, how to report abusive content, or how to respond to a rating decline. Never fabricate evidence, contact reviewers off-platform, or incentivize review changes.
---

# Amazon 差评合规处置

## 目标

只对明确违反社区准则的内容走官方报告，对真实差评回到产品和售后修复，并保留完整证据链。

## 适用任务

- 判断某条差评是否符合删除或报告条件。
- 怀疑恶意攻击但证据不足。
- 建立差评预警、分流和产品闭环。

## 开始前要拿到

- 评论原文、公开页面、时间、关联 ASIN 和可见上下文。
- 当前 Amazon Community Guidelines 与官方报告入口。
- 退货原因、客服工单、批次和质量记录。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 不得捏造职业差评师、竞争对手攻击或买家身份；相似表达只算线索。
- 不得站外联系评论者、施压、补偿换改评或委托服务商磨掉差评。
- 真实且合规的负面体验不能因影响评分而要求删除。
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

### 1. 保存原始证据

记录完整评论、页面、时间和 ASIN，不截取会改变语义的片段，也不扩散个人信息。

### 2. 按准则分类

逐条比对辱骂、个人信息、促销内容、非商品反馈等当前规则，列出匹配条款和不确定点。

### 3. 评估异常模式

查看公开可验证的重复、集中时间或跨商品模式，但把它标为风险信号而非主体归因。

### 4. 选择官方路径

违规内容通过官方报告或支持渠道提交；用事实、链接和条款写简洁材料，不夸大。

### 5. 处理真实差评

把问题映射到设计、包装、说明、质检、变体或售后，确定负责人和验证指标。

### 6. 建立闭环

按主题跟踪差评率、退货率和修复后变化，重复问题升级为批次或产品决策。

## 判断标准

- 每条删除请求都有具体政策依据。
- 报告材料区分事实、推断和未知。
- 真实问题有产品或服务纠正措施。

## 必须交付的结果

- 评论合规分类表。
- 官方报告草稿与证据附件清单。
- 不可删除评论的产品修复计划。
- 差评主题预警看板字段。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
