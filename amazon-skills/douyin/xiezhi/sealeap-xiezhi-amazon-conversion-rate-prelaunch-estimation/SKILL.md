---
name: sealeap-xiezhi-amazon-conversion-rate-prelaunch-estimation
description: "Estimate a defensible pre-launch conversion range from Amazon first-party opportunity data, competitor traffic proxies, and unit economics. Use when a product appears profitable only under an assumed CVR and the team needs a risk-aware launch gate."
---

# Amazon 上市前转化率估算

## 目标

用头部链接和细分市场两种口径交叉估算转化率，再判断保本 CVR 是否现实。

## 适用任务

- 测算候选产品的保本转化率。
- 用单 ASIN 与市场整体数据交叉验证。
- 识别长决策、低转化且广告难盈利的市场。

## 开始前要拿到

- 售价、落地成本、Amazon 费用、优惠和目标利润。
- 精准词 CPC 区间。
- 竞品销量与搜索点击代理数据。
- Amazon 商机探测器或其他一方市场购买率数据。

缺少字段时列出证据缺口，并把相关结论标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`；不要补造数据。

## 不可妥协的边界

- 第三方数据均为估算或代理证据；Amazon 一方报告、后台实时字段和产品事实优先。
- 经验阈值只能作为可调起点，必须展示敏感性分析，不能写成 Amazon 官方规则。
- 不得捏造销量、搜索量、CPC、CVR、成本、认证、产品属性或消费者需求。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不输出或保存素材来源身份、账号、链接、作品编号、互动数据、原始话术或其他可反查来源的线索。
- 不得把销量估算与点击估算的比值写成真实转化率。
- 当前 Amazon 一方字段定义优先于任何历史方法。

## 工作流

### 1. 统一单位经济

计算广告前贡献毛利、盈亏平衡 CPA、ACoS 和所需 CVR，并明确税费、退款和优惠口径。

### 2. 估单品 CVR

只有订单与点击来自相同流量范围、对象、时间窗和归因口径时才估算订单 CVR。全渠道销量除以搜索点击只能标为需求比例代理，不能作为 CVR 或直接代入 CPA；缺少可比样本时用明确标注的假设区间并保留 HOLD。

### 3. 估市场 CVR

读取细分市场购买率、转化购买率或等价一方指标，解释访客、点击、归因窗差异。

### 4. 形成区间

不机械取单点，使用保守/基准/乐观三档并剔除口径不可比样本。

### 5. 做立项闸门

若头部或市场基准仍低于保本 CVR，则 HOLD；只有差异化能被证据支持时才建立例外情景。

## 判断标准

- CPA = CPC / 订单 CVR；保本订单 CVR = CPC / 广告前每单贡献毛利。贡献毛利非正、分母为零或所需 CVR 超过 100% 时，标为当前经济模型不可行。
- 搜索点击口径通常不能代表全部流量，单 ASIN 结果必须标注偏差方向。
- 购买率与转化购买率定义可能随报表变化，必须记录当前官方字段说明。
- 头部转化差时，新品默认不能假设显著优于头部。

## 第三方 MCP 数据

需要外部关键词、竞品、评论或公开网页证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，并使用 `scripts/mcp_research.py`。

- 先动态执行 `tools/list`、`search-tools` 和 `describe`，依据实时 `inputSchema` 构造参数。
- 凭证只从环境变量读取，不进入参数、URL、Skill、终端输出或 Git。
- 可能计费的 `tools/call` 先展示 Provider、工具、无密钥参数、预计成本与输出位置，核对已有授权；仅在授权覆盖本次范围时使用 `--allow-cost`，该标志不是费用上限。
- 脱敏结果用 `--output` 写入 Skill 包之外的任务私有目录；不假设安装位置受仓库 `.gitignore` 保护。第三方数据标为估算或代理证据。
- 失败一次后记录缺口，不以重复付费重试掩盖不可用状态。

## 必须交付的结果

- 单位经济表
- 单 ASIN CVR 区间
- 市场 CVR 区间
- 保本敏感性矩阵
- GO/HOLD/NO-GO 及证据缺口

结尾列出站点、数据窗口、证据来源、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行细节、证据字段和质量检查见 [references/playbook.md](references/playbook.md)。
