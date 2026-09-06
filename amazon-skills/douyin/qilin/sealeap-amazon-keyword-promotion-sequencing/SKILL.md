---
name: sealeap-amazon-keyword-promotion-sequencing
description: Sequence Amazon keyword promotion from high-intent long-tail terms to mid-volume and head terms using stage gates, mixed ad formats, profitability checks, and exact harvesting. Use when the user asks which keywords to launch first, why competitor head terms do not convert for a new ASIN, or how to expand traffic without losing relevance. No ranking promises or artificial orders.
---

# Amazon 关键词推广顺序

## 目标

先用最容易验证真实转化的查询建立基本盘，再按证据扩大到中部与核心词。

## 适用任务

- 新品直接打大词转化差。
- 需要规划长尾、中部和核心词的先后顺序。
- 在不同阶段组合 SP、商品投放和品牌视频。

## 开始前要拿到

- 关键词相关性、意图、搜索量代理、CPC、预估转化和词根关系。
- 广告类型资格、视频素材权利和预算。
- 商品转化、库存、利润和自然位置趋势。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 搜索量分段不是跨类目固定阈值，应按当前市场分位数定义。
- 品牌视频或促销仅在账号有资格且素材合规时使用。
- 自然位置是观测结果，不以固定订单承诺排名。
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

### 1. 阶段零准备

完成 Listing、库存、利润和词库检查，为每个词标注意图与当前证据。

### 2. 阶段一验证长尾

用精准广告和受控发现覆盖最贴合卖点的长尾主题，优先验证 CVR 与 CPA。

### 3. 阶段二扩展中部词

把同词根中部词分批放入词组或其他合适匹配，按样本淘汰并保留表现者。

### 4. 阶段三精准承接

把通过门槛的中部词迁移到精准层，增加预算前检查与原活动重叠。

### 5. 阶段四测试核心词

在基本盘、库存和利润足够后，小规模测试核心词及商品投放，不一次性重押。

### 6. 持续收敛

把预算流向增量利润成立的层级，缩减无效泛词并观察自然侧变化。

## 判断标准

- 每个阶段有进入、毕业和停止条件。
- 词从一层迁移到下一层有报告证据。
- 广告类型选择与资格、素材和预算相匹配。

## 必须交付的结果

- 关键词分层与阶段顺序。
- 每阶段广告组合和预算职责。
- 迁移、否定与停止规则。
- 自然侧与利润监控方案。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
