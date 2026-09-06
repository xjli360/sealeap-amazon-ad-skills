---
name: sealeap-xiezhi-amazon-product-test-decision-tree
description: "Choose a compliant Amazon validation method based on whether the uncertainty is concept acceptance, marketplace conversion, or paid-traffic economics. Use when deciding whether to test an original design, a differentiated mature product, or a proven-market candidate."
---

# Amazon 产品测款决策树

## 目标

只验证尚未被证据回答的最大不确定性，并用真实可履约库存、最小样本和明确止损控制测试成本。

## 适用任务

- 判断产品是否需要测款。
- 选择概念测试、FBM 或小批 FBA 验证。
- 定义测试指标、样本和退出条件。

## 开始前要拿到

- 产品创新程度及可比商品集合。
- 需要验证的具体假设。
- 真实可履约库存、配送时效和售后能力。
- CPC、CVR、毛利、首批量、测试预算与时间窗口。

缺少字段时列出证据缺口，并把相关结论标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`；不要补造数据。

## 不可妥协的边界

- 第三方数据均为估算或代理证据；Amazon 一方报告、后台实时字段和产品事实优先。
- 经验阈值只能作为可调起点，必须展示敏感性分析，不能写成 Amazon 官方规则。
- 不得捏造销量、搜索量、CPC、CVR、成本、认证、产品属性或消费者需求。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不输出或保存素材来源身份、账号、链接、作品编号、互动数据、原始话术或其他可反查来源的线索。
- 禁止创建无库存、不可履约或计划取消订单的虚假 FBM Listing。
- 不得通过虚假订单、评价或变体操纵测试结果。

## 工作流

### 1. 识别未知项

区分需求是否存在、设计是否被接受、FBA 条件下的真实转化、CPC 和市场份额上限。

### 2. 选择方法

纯概念先做访谈/落地页/样品研究；有真实 FBM 库存时可测购买意向；成熟市场微创新用小批 FBA 测真实履约条件。

### 3. 定义成功

在测试前写明 CTR、CVR、CPC、订单、退款、评价和库存周转的目标区间与最低样本。

### 4. 限制暴露

只投入足以回答假设的真实库存和广告预算，并预先设累计亏损、时长和清货条件。

### 5. 决策复盘

将结果与先验区间比较，选择扩大、迭代、延长或停止；记录无法归因的混杂因素。

## 判断标准

- 已有可比市场和历史证据时，优先用单位经济与小批实销验证，不重复验证已知需求。
- FBM 与 FBA 的配送承诺不同，结果不能直接等同；方法必须匹配待验证问题。
- 测试不是追求几单，而是用最小成本降低最大不确定性。

## 第三方 MCP 数据

需要外部关键词、竞品、评论或公开网页证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，并使用 `scripts/mcp_research.py`。

- 先动态执行 `tools/list`、`search-tools` 和 `describe`，依据实时 `inputSchema` 构造参数。
- 凭证只从环境变量读取，不进入参数、URL、Skill、终端输出或 Git。
- 可能计费的 `tools/call` 先展示 Provider、工具、无密钥参数、预计成本与输出位置，核对已有授权；仅在授权覆盖本次范围时使用 `--allow-cost`，该标志不是费用上限。
- 脱敏结果用 `--output` 写入 Skill 包之外的任务私有目录；不假设安装位置受仓库 `.gitignore` 保护。第三方数据标为估算或代理证据。
- 失败一次后记录缺口，不以重复付费重试掩盖不可用状态。

## 必须交付的结果

- 不确定性清单
- 方法选择树
- 测试方案与样本门槛
- 预算/库存止损
- 扩大或停止结论

结尾列出站点、数据窗口、证据来源、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行细节、证据字段和质量检查见 [references/playbook.md](references/playbook.md)。
