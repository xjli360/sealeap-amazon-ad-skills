---
name: sealeap-xiezhi-amazon-market-acos-feasibility
description: "Determine whether an Amazon product can economically tolerate the market's CPC and conversion environment before trying to optimize ACoS. Use when ads remain expensive, volume falls after bid cuts, or a team needs a launch feasibility gate."
---

# Amazon 市场 ACoS 可承受性

## 目标

把 ACoS 拆回 CPC、CVR、售价、贡献毛利和复购价值，先判断商业模型能否承受市场，再选择广告动作。

## 适用任务

- 判断高 ACoS 是流量错误还是赛道经济问题。
- 计算单次订单和生命周期价值可承受获客成本。
- 为产品定位、流量和规模设盈利边界。

## 开始前要拿到

- 售价、折扣、退款、平台费、履约费、COGS 和贡献毛利。
- 查询级 CPC、CVR、ACoS、订单与广告位。
- 复购率、毛利留存和客户生命周期数据；没有则标缺口。
- 直接竞品与低评论新品的转化/销量代理值。

缺少字段时列出证据缺口，并把相关结论标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`；不要补造数据。

## 不可妥协的边界

- 第三方数据均为估算或代理证据；Amazon 一方报告、后台实时字段和产品事实优先。
- 经验阈值只能作为可调起点，必须展示敏感性分析，不能写成 Amazon 官方规则。
- 不得捏造销量、搜索量、CPC、CVR、成本、认证、产品属性或消费者需求。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不输出或保存素材来源身份、账号、链接、作品编号、互动数据、原始话术或其他可反查来源的线索。
- 不得为了降低 ACoS 隐藏销量、利润或库存恶化。
- 不得用未经验证的未来复购为当前亏损辩护。

## 工作流

### 1. 计算边界

计算保本 CPA、ACoS、CPC 与所需 CVR，并给出单次订单和生命周期两种口径。

### 2. 审计流量

排查宽泛或不相关查询、广告位和人群是否拉低转化；明显错投先修正。

### 3. 审计产品力

比较精准痛点、差异可见性、主图、定价、评分、变体和页面承接。

### 4. 评估赛道

比较低评论样本与头部样本的表现，判断新品在正常运营下是否有可达转化区间。

### 5. 选择经营策略

可承受则守住盈利区间并单变量优化；不可承受则改定位、提高客单/复购价值或退出。

## 判断标准

- ACoS = CPC /（平均归因每单销售额 × 订单 CVR），各项须来自同范围、同归因窗；仅在每单一件且价格口径一致时才可用单件售价替代每单销售额。
- 保本 ACoS = 归因订单的广告前贡献 / 同口径归因销售额；贡献包含退款和可变成本，分母保持广告报告销售额定义，不能随意替换为净收入。
- 生命周期价值只有在真实复购数据与毛利留存支持时才能抵消首单亏损。
- 低评论组/头部组销量比仅是市场友好度代理，不是转化率本身。

## 第三方 MCP 数据

需要外部关键词、竞品、评论或公开网页证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，并使用 `scripts/mcp_research.py`。

- 先动态执行 `tools/list`、`search-tools` 和 `describe`，依据实时 `inputSchema` 构造参数。
- 凭证只从环境变量读取，不进入参数、URL、Skill、终端输出或 Git。
- 可能计费的 `tools/call` 先展示 Provider、工具、无密钥参数、预计成本与输出位置，核对已有授权；仅在授权覆盖本次范围时使用 `--allow-cost`，该标志不是费用上限。
- 脱敏结果用 `--output` 写入 Skill 包之外的任务私有目录；不假设安装位置受仓库 `.gitignore` 保护。第三方数据标为估算或代理证据。
- 失败一次后记录缺口，不以重复付费重试掩盖不可用状态。

## 必须交付的结果

- ACoS 驱动树
- 盈亏敏感性矩阵
- 流量与产品根因表
- 可承受规模区间
- 优化、重定位或退出建议

结尾列出站点、数据窗口、证据来源、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行细节、证据字段和质量检查见 [references/playbook.md](references/playbook.md)。
