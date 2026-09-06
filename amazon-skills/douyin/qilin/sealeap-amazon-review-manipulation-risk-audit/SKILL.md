---
name: sealeap-amazon-review-manipulation-risk-audit
description: Audit suspicious Amazon review patterns and proposed review-growth tactics for policy risk, then replace unsafe ideas with official reporting and compliant review programs. Use when the user encounters sudden review spikes, asks about 直评突破, synchronized submissions, paid reviews, review services, or how to investigate competitor review anomalies. Do not reverse-engineer or enable manipulation.
---

# Amazon 评论操纵风险审计

## 目标

识别异常评论只是风险信号还是可验证违规，并把任何绕过式获评诉求转成合规处置与官方获评方案。

## 适用任务

- 竞品短期出现异常评论，需要做风险判断。
- 团队或服务商提出直评、批量账号、同步提交等方案。
- 需要决定是否向 Amazon 报告可疑评论。

## 开始前要拿到

- 公开可见评论变化、评论类型、变体结构和站点情况。
- 服务商方案原文、费用、承诺和要求的账号或订单动作。
- 当前 Amazon Customer Reviews policies 与官方报告入口。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 拒绝提供批量账号、同步提交、无购买评论、付费评论或规避检测的步骤。
- 异常模式不是违规定论；不得公开指认买家或竞争对手，也不得捏造证据。
- 不得以测试为名实际下单、操纵评论或访问他人账号。
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

### 1. 分类风险提议

识别是否涉及报酬、返现、控制内容、非真实变体、账号群或规避系统；命中即标为不可执行。

### 2. 记录公开信号

保存公开页面、时间范围和变化趋势，只记录可见事实，不收集或曝光无关个人信息。

### 3. 核对当前政策

优先引用 Amazon 官方评论政策和报告路径，区分明确禁止、需要更多信息和允许行为。

### 4. 建立替代方案

符合资格时考虑 Vine、Request a Review、改进产品与售后，以及不影响评价倾向的中立沟通。

### 5. 决定是否报告

只有具备具体可验证材料时才通过官方渠道提交；陈述事实和政策条款，不推断幕后主体。

### 6. 建立内部控制

记录服务商黑名单、审批要求和员工培训，防止高风险方案被重新包装。

## 判断标准

- 输出不包含任何可复现评论操纵步骤。
- 证据、推断和未知项清晰分开。
- 替代方案符合当前站点和项目资格。

## 必须交付的结果

- 评论方案风险分级。
- 公开异常信号与证据缺口。
- 官方政策核对和报告草稿。
- 合规获评替代路径。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
