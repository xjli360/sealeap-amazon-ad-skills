---
name: sealeap-xiezhi-amazon-product-selection-eight-gates
description: "Run an eight-gate Amazon product selection audit covering discoverability, operating difficulty, economics, differentiation, timing, seasonality, compliance, and inventory. Use when a candidate needs a complete pre-purchase decision review."
---

# Amazon 选品八道闸门

## 目标

用八个相互独立的门槛把候选从有趣方向推进到可审计立项，任何关键证据缺失都保持 HOLD。

## 适用任务

- 对候选做完整立项审查。
- 建立高成功率选品 SOP。
- 定位候选卡在哪个环节。

## 开始前要拿到

- 产品事实、目标站点和精准词。
- 直接竞品、评论层级、销量、广告与历史趋势。
- 单位经济、供应链、MOQ、差异化和变体方案。
- IP、产品安全、认证、政策和库存时效证据。

缺少字段时列出证据缺口，并把相关结论标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`；不要补造数据。

## 不可妥协的边界

- 第三方数据均为估算或代理证据；Amazon 一方报告、后台实时字段和产品事实优先。
- 经验阈值只能作为可调起点，必须展示敏感性分析，不能写成 Amazon 官方规则。
- 不得捏造销量、搜索量、CPC、CVR、成本、认证、产品属性或消费者需求。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不输出或保存素材来源身份、账号、链接、作品编号、互动数据、原始话术或其他可反查来源的线索。
- 不得跳过 IP、产品安全或认证闸。
- 不得用异常竞品、违规增长或不可比口径美化评分。

## 工作流

### 1. 精准流量闸

必须有能锁定直接竞品和购物意图的属性/对象/场景词。

### 2. 运营难度闸

比较低评论正常样本与头部样本，判断新品是否可在合规条件下获得转化。

### 3. 经济效率闸

核算广告前贡献、CPA、ACoS、资金占用和周转，不用模糊投产比。

### 4. 差异与供应闸

差异有需求证据、搜索页可见且供应商能按质量、成本和 MOQ 实现。

### 5. 时间与周期闸

旺季、活动和上架窗口与生产物流倒排一致，并有历史周期证据。

### 6. 合规与 IP 闸

完成专利、商标、版权、产品安全、认证、类目和宣传声明核查。

### 7. 库存与变体闸

以可达份额、销售窗和变体需求分配首批库存，设置补货和退出条件。

### 8. 总决策

汇总每闸证据、置信度与失败成本，只有关键闸均通过才给条件式 GO。

## 判断标准

- 低评论/头部销量比、投产比 120%、未来三到五个月等都属于可调代理指标。
- 任何一个关键闸为 UNKNOWN 时，总结论最多为 HOLD。
- 成功率必须用真实立项的后验结果计算，不能用筛选通过率替代。

## 第三方 MCP 数据

需要外部关键词、竞品、评论或公开网页证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，并使用 `scripts/mcp_research.py`。

- 先动态执行 `tools/list`、`search-tools` 和 `describe`，依据实时 `inputSchema` 构造参数。
- 凭证只从环境变量读取，不进入参数、URL、Skill、终端输出或 Git。
- 可能计费的 `tools/call` 先展示 Provider、工具、无密钥参数、预计成本与输出位置，核对已有授权；仅在授权覆盖本次范围时使用 `--allow-cost`，该标志不是费用上限。
- 脱敏结果用 `--output` 写入 Skill 包之外的任务私有目录；不假设安装位置受仓库 `.gitignore` 保护。第三方数据标为估算或代理证据。
- 失败一次后记录缺口，不以重复付费重试掩盖不可用状态。

## 必须交付的结果

- 八闸评分卡
- 证据与缺口台账
- 单位经济敏感性
- 库存/时间倒排
- GO/HOLD/NO-GO 决策书

结尾列出站点、数据窗口、证据来源、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行细节、证据字段和质量检查见 [references/playbook.md](references/playbook.md)。
