---
name: sealeap-xiezhi-amazon-first-product-low-risk-screen
description: "Screen a beginner's first Amazon product for a small, low-review niche with defensible paid-traffic economics. Use when the goal is to learn the FBA loop while protecting capital rather than chasing a large launch."
---

# Amazon 首款产品低风险筛选

## 目标

为首款产品建立需求、竞争、精准词、广告成本和供应链风险的最小可行闸门。

## 适用任务

- 为新卖家选择首个低风险方向。
- 判断低评论细分市场是否适合正常广告启动。
- 在发货前估算 CPC、CPA 和最低毛利。

## 开始前要拿到

- 可用资金、亏损上限和学习目标。
- 价格、销量、评论、上架时间与直接竞品数据。
- 精准词与建议竞价代理值。
- 采购、物流、FBA 费用、MOQ、合规与 IP 信息。

缺少字段时列出证据缺口，并把相关结论标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`；不要补造数据。

## 不可妥协的边界

- 第三方数据均为估算或代理证据；Amazon 一方报告、后台实时字段和产品事实优先。
- 经验阈值只能作为可调起点，必须展示敏感性分析，不能写成 Amazon 官方规则。
- 不得捏造销量、搜索量、CPC、CVR、成本、认证、产品属性或消费者需求。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不输出或保存素材来源身份、账号、链接、作品编号、互动数据、原始话术或其他可反查来源的线索。
- 不得把低评论产品等同于低竞争。
- 未完成合规、IP 和产品事实核验前不得采购或发布。

## 工作流

### 1. 控制初筛范围

从常规且合规负担可控的类目开始，用中小销量、低评论和较高售价寻找候选。

### 2. 验证运营难度

通过精准词搜索比较低评论与头部链接的销量/转化代理值，并检查尾部新品是否只是烧广告。

### 3. 估算流量成本

用一组精准词的 CPC 区间和保守 CVR 计算 CPA，不使用单一关键词或单一时点。

### 4. 核对盈利

在不假设自然流量的情景下计算贡献利润和止损；不能覆盖 CPA 的候选不进入首批。

### 5. 完成采购前闸门

再做差异化、专利版权、产品安全、供应商 MOQ 和首批库存核查。

## 判断标准

- 月销量约 300、评论约 100、售价约 35 美元只能作为起始筛选值。
- 5% CVR 等保守假设必须做区间，不得冒充真实转化。
- 流程学习不是接受必然亏损的理由；首款应有明确止损和清货路径。

## 第三方 MCP 数据

需要外部关键词、竞品、评论或公开网页证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，并使用 `scripts/mcp_research.py`。

- 先动态执行 `tools/list`、`search-tools` 和 `describe`，依据实时 `inputSchema` 构造参数。
- 凭证只从环境变量读取，不进入参数、URL、Skill、终端输出或 Git。
- 可能计费的 `tools/call` 先展示 Provider、工具、无密钥参数、预计成本与输出位置，核对已有授权；仅在授权覆盖本次范围时使用 `--allow-cost`，该标志不是费用上限。
- 脱敏结果用 `--output` 写入 Skill 包之外的任务私有目录；不假设安装位置受仓库 `.gitignore` 保护。第三方数据标为估算或代理证据。
- 失败一次后记录缺口，不以重复付费重试掩盖不可用状态。

## 必须交付的结果

- 首款候选评分卡
- 精准词与竞品核验
- 三档单位经济
- 合规/IP/供应链缺口
- 首批与止损建议

结尾列出站点、数据窗口、证据来源、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行细节、证据字段和质量检查见 [references/playbook.md](references/playbook.md)。
