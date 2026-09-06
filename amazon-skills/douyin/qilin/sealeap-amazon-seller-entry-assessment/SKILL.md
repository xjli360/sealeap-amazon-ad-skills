---
name: sealeap-amazon-seller-entry-assessment
description: Assess whether a team should enter or expand on Amazon using unit economics, cash runway, product-market fit, operational capability, compliance, and staged validation. Use when the user asks whether Amazon is still worth doing, whether a new seller or factory should enter, what product-price band to choose, or how to make a GO/NO-GO decision. Do not promise returns or treat anecdotes as benchmarks.
---

# Amazon 卖家入场可行性评估

## 目标

把“还能不能做”转化为团队自身条件、商品经济性和可验证市场假设的决策，而不是用个别成功案例代替分析。

## 适用任务

- 新卖家、工厂或运营团队准备进入 Amazon。
- 比较高低客单、精品与精铺、小团队与扩张模式。
- 评估当前资金是否足以度过开发、生产、运输和验证周期。

## 开始前要拿到

- 团队经验、可投入时间、供应链能力、合规能力和失败承受度。
- 产品售价、成本、费用、退货、广告 CPC/CVR 和库存周转假设。
- 市场规模、竞争、差异化、知识产权和资质门槛。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 高客单并非天然更优；必须同时验证转化、退货、资本占用和售后成本。
- 不把低价、朋友成功或工厂供货优势单独当作进入理由。
- 不建议借贷或投入不可承受资金，也不提供收益保证。
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

### 1. 评估创始条件

列出可迁移能力、缺口、时间投入和关键人依赖，区分运营经验与经营全盘能力。

### 2. 建立单位经济模型

从净售价扣除平台费、物流、广告、退货、税费和 COGS，计算贡献利润和盈亏平衡指标。

### 3. 测现金周期

覆盖备货、海运或空运、入仓、推广、回款和补货，计算基准与压力情景下的资金峰值。

### 4. 验证市场匹配

用多个可比产品、需求趋势和消费者痛点验证差异化，不照抄单一竞品。

### 5. 设计小规模试点

用少量 SKU、明确验证期和停止线先完成从零到一；成功后再复制，不提前扩团队和固定成本。

### 6. 形成决策

按产品、资金、能力、合规和时机分别评分，输出 GO、CONDITIONAL GO 或 NO-GO。

## 判断标准

- 利润和现金流同时为正才算健康，不用销售额替代。
- 关键假设都有验证方法和失败退出路径。
- 模式选择与团队真实优势相匹配。

## 必须交付的结果

- 入场能力与缺口表。
- 单位经济和现金流压力测试。
- 最小验证方案。
- 带前置条件的决策结论。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
