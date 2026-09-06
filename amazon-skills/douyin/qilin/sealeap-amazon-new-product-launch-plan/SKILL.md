---
name: sealeap-amazon-new-product-launch-plan
description: Create a quantified Amazon new-product launch plan by translating a sales target into comparable-product benchmarks, keyword economics, budget scenarios, milestones, and stop-loss rules. Use when the user asks for a 新品推广计划, target-order reverse planning, competitor-based launch budget, or GO/NO-GO assessment before launch. Keep competitor estimates labeled and do not execute campaigns without approval.
---

# Amazon 新品推广成本倒推

## 目标

从目标销量反推需要争取的流量、关键词订单、广告成本和现金需求，在上架前判断项目是否值得推进。

## 适用任务

- 为目标日单量或月销量制定推广预算。
- 选择可比竞品并拆解其可能的流量和关键词结构。
- 在预算、利润和成功概率之间形成 GO、CONDITIONAL GO 或 NO-GO。

## 开始前要拿到

- 目标销量、售价、贡献毛利、库存、补货周期和最长验证期。
- 多个可比竞品的产品规格、价格、历史表现和可追溯流量代理数据。
- 关键词 CPC、预估转化率、订单贡献、自然与广告位置快照。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 竞品销量、广告单占比和转化率通常是估算值，不能写成已知事实。
- 不得把竞品可疑评论或灰色操作转成自己的执行方案。
- 不承诺在固定天数、固定订单量后进入首页；排名只作为情景变量。
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

### 1. 定义商业目标

把目标销量转换为收入、贡献利润、库存周转和类目位置的情景，不把类目排名当成唯一成功标准。

### 2. 建立可比组

选择多款规格、价格、受众和生命周期接近的产品，避免用单一竞品代表市场。

### 3. 拆解需求结构

估算自然与广告订单区间、主要查询的订单贡献和可见位置，并为每项标注来源与置信度。

### 4. 计算关键词经济性

使用 CPA 约等于 CPC 除以转化率，进一步计算每个词的盈亏平衡 CPC、所需点击、预算区间和利润敏感性。

### 5. 形成阶段计划

按准备、验证、扩大和收敛阶段列出目标词、预算、数据门槛、库存条件和复盘节点。

### 6. 做压力测试

至少模拟基准、转化下降、CPC 上升和补货延迟情景，给出资金峰值与停止条件。

## 判断标准

- 所有货币单位、税费、Amazon 费用和时间窗口一致。
- 计划能追溯到具体关键词或商品目标，而不是只给总预算。
- 最坏情景不突破现金和库存护栏。

## 必须交付的结果

- 目标与可比竞品表。
- 关键词级 CPA 和预算模型。
- 阶段里程碑、止损线和现金需求。
- GO、CONDITIONAL GO 或 NO-GO 结论。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
