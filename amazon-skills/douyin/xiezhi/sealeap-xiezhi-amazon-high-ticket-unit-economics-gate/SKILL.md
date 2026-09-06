---
name: sealeap-xiezhi-amazon-high-ticket-unit-economics-gate
description: "Evaluate whether a higher-priced Amazon offer creates enough contribution margin to absorb paid traffic and operational risk. Use when comparing low-ticket and bundled or higher-value product concepts."
---

# Amazon 高客单单位经济闸门

## 目标

不把高价当作机会本身，而用实际成本、CPC 与 CVR 验证更高售价是否带来足够的广告和清货容错。

## 适用任务

- 比较低客单与高客单方案。
- 验证数量组合或高货值产品的毛利空间。
- 设置上市前价格与利润底线。

## 开始前要拿到

- 含包装、贴标、物流、FBA、佣金、退款和折扣的落地成本。
- 候选售价与可比产品价格带。
- 精准词 CPC 分布和 CVR 情景。
- 首批库存、清货折扣和现金周转要求。

缺少字段时列出证据缺口，并把相关结论标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`；不要补造数据。

## 不可妥协的边界

- 第三方数据均为估算或代理证据；Amazon 一方报告、后台实时字段和产品事实优先。
- 经验阈值只能作为可调起点，必须展示敏感性分析，不能写成 Amazon 官方规则。
- 不得捏造销量、搜索量、CPC、CVR、成本、认证、产品属性或消费者需求。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不输出或保存素材来源身份、账号、链接、作品编号、互动数据、原始话术或其他可反查来源的线索。
- 不得通过虚构功能、数量、认证或场景制造溢价。
- 不能忽略大件、易碎、高退货或售后产品的尾部损失。

## 工作流

### 1. 还原净售价

从标价扣除优惠、税费处理和退款影响，统一到每单净销售额。

### 2. 计算广告前毛利

扣除采购、包装、头程、FBA、佣金和其他变动成本，明确是否包含退货准备金。

### 3. 叠加流量情景

用多关键词 CPC 与保守/基准/乐观 CVR 计算 CPA 和贡献利润。

### 4. 验证溢价理由

检查数量、组合、材质、功能或场景是否让目标消费者感知到更高价值。

### 5. 测试清货韧性

模拟降价、CPC 上升、CVR 下滑与滞销情况下的现金回收和最大损失。

## 判断标准

- 30 美元售价、10 美元广告前毛利等只能作为特定模式的探索基线。
- 高客单价降低所需订单量，但可能提高决策周期、退货损失和库存占用。
- CPA = CPC / CVR；任何方案都要展示 CVR 变化下的盈亏交点。

## 第三方 MCP 数据

需要外部关键词、竞品、评论或公开网页证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，并使用 `scripts/mcp_research.py`。

- 先动态执行 `tools/list`、`search-tools` 和 `describe`，依据实时 `inputSchema` 构造参数。
- 凭证只从环境变量读取，不进入参数、URL、Skill、终端输出或 Git。
- 可能计费的 `tools/call` 先展示 Provider、工具、无密钥参数、预计成本与输出位置，核对已有授权；仅在授权覆盖本次范围时使用 `--allow-cost`，该标志不是费用上限。
- 脱敏结果用 `--output` 写入 Skill 包之外的任务私有目录；不假设安装位置受仓库 `.gitignore` 保护。第三方数据标为估算或代理证据。
- 失败一次后记录缺口，不以重复付费重试掩盖不可用状态。

## 必须交付的结果

- 全成本单位经济表
- 价格/CPC/CVR 敏感性矩阵
- 溢价证据
- 清货压力测试
- 价格与立项闸门

结尾列出站点、数据窗口、证据来源、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行细节、证据字段和质量检查见 [references/playbook.md](references/playbook.md)。
