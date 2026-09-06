---
name: sealeap-xiezhi-amazon-cpc-cvr-opportunity-gate
description: "Run a fast Amazon opportunity gate using precise-query CPC, defensible conversion scenarios, visible differentiation, and unit economics. Use when deciding whether a product deserves deeper research before spending on samples or inventory."
---

# Amazon CPC-CVR 机会快判

## 目标

用精准流量成本和可达转化区间淘汰明显无法盈利的候选，把深研资源留给有证据的方向。

## 适用任务

- 几分钟内判断候选是否值得深研。
- 计算保本 CPC、CVR 和 CPA。
- 检查差异化是否足以支撑转化假设。

## 开始前要拿到

- 候选产品事实、售价与完整变动成本。
- 最匹配的直接竞品和精准属性/场景词。
- 一组实时竞价代理值。
- 保守、基准和乐观 CVR 证据。

缺少字段时列出证据缺口，并把相关结论标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`；不要补造数据。

## 不可妥协的边界

- 第三方数据均为估算或代理证据；Amazon 一方报告、后台实时字段和产品事实优先。
- 经验阈值只能作为可调起点，必须展示敏感性分析，不能写成 Amazon 官方规则。
- 不得捏造销量、搜索量、CPC、CVR、成本、认证、产品属性或消费者需求。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不输出或保存素材来源身份、账号、链接、作品编号、互动数据、原始话术或其他可反查来源的线索。
- 不得以单个建议竞价或单个竞品决定市场。
- 快判通过不替代 IP、合规、产品安全和供应链闸门。

## 工作流

### 1. 找精准词

从最匹配直接竞品提取自然排名靠前且搜索结果一致的属性、对象和场景词。

### 2. 取保守 CPC

收集多个精准词的建议竞价与可比实际 CPC，记录策略、匹配方式和查询时间。建议竞价不等于实际 CPC；新品情景须标为假设，并以小额验证结果更新。

### 3. 评估可达 CVR

结合低评论竞品、市场一方数据、产品差异和页面表达建立三档 CVR，而非直接套固定值。

### 4. 计算盈亏

计算广告前贡献、CPA、保本 CPC/CVR/ACoS，并对价格、CPC 和 CVR 做敏感性分析。

### 5. 作快速决策

明显无法覆盖广告则 NO-GO；接近边界或证据不足则 HOLD；通过后才进入 IP、合规、供应和库存深研。

## 判断标准

- CPA = CPC / 订单 CVR；保本 CPC = 广告前每单贡献毛利 × 订单 CVR。订单 CVR = 同口径归因订单 / 点击，以小数代入；多件订单先汇总每单收入和成本。
- 5%–7% CVR 可作为某些非标品的压力测试，不得作为真实基准。
- 即便保守情景略亏，也只能进入 HOLD 深研，不能直接写 GO。

## 第三方 MCP 数据

需要外部关键词、竞品、评论或公开网页证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，并使用 `scripts/mcp_research.py`。

- 先动态执行 `tools/list`、`search-tools` 和 `describe`，依据实时 `inputSchema` 构造参数。
- 凭证只从环境变量读取，不进入参数、URL、Skill、终端输出或 Git。
- 可能计费的 `tools/call` 先展示 Provider、工具、无密钥参数、预计成本与输出位置，核对已有授权；仅在授权覆盖本次范围时使用 `--allow-cost`，该标志不是费用上限。
- 脱敏结果用 `--output` 写入 Skill 包之外的任务私有目录；不假设安装位置受仓库 `.gitignore` 保护。第三方数据标为估算或代理证据。
- 失败一次后记录缺口，不以重复付费重试掩盖不可用状态。

## 必须交付的结果

- 精准词证据
- CPC 分布
- CVR 依据与区间
- 盈亏敏感性
- NO-GO/HOLD/深研结论

结尾列出站点、数据窗口、证据来源、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行细节、证据字段和质量检查见 [references/playbook.md](references/playbook.md)。
