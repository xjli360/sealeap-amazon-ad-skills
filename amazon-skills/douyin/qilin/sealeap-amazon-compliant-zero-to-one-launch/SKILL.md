---
name: sealeap-amazon-compliant-zero-to-one-launch
description: Design a compliant precision-first Amazon launch that starts with high-intent long-tail demand, validates conversion, and expands toward broader terms without fake orders or review manipulation. Use when the user asks for 白帽 0-1 推新品, a universal launch sequence, keyword-root grouping, or a limited-risk launch framework. Produce a staged plan and require approval before ad changes.
---

# Amazon 合规从零到一推广

## 目标

先把流量送到最有转化把握的查询，再由精准到宽泛逐级扩展，以真实订单验证商品竞争力。

## 适用任务

- 预算有限且希望降低新品早期低转化信号。
- 非标品有多组属性词根，需要分组推进。
- 标品词少，但仍要组合不同合法广告入口。

## 开始前要拿到

- 产品事实、差异化卖点、价格、库存和完整 Listing。
- 关键词全集、词根分类、搜索量代理、相关性和预估转化。
- 广告预算、盈亏平衡 CPC、阶段目标和最长验证期。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 仅使用真实客户订单和 Amazon 允许的评论项目；拒绝刷单、返现、测评和评论操纵。
- 长尾词也必须有真实相关性，不能为扩词拼接消费者不会使用的查询。
- 不以排名为保证，阶段升级必须由转化、利润和样本共同触发。
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

### 1. 找全并筛词

从自有报告和授权竞品数据建立词库，按属性或场景词根分组，并标记不相关词根。

### 2. 选择首发词

每组优先选购买意图最明确、与商品事实最匹配的长尾词；流量过小时可组合多个同类词，但不混合不同意图。

### 3. 搭建探索与精准层

用受控自动和商品投放补充发现，用精准广告承接首发词，用低风险广泛覆盖同词根的其他查询。

### 4. 验证承接能力

对每组比较 CTR、CVR、CPA、退货和利润。转化不足先排查价格、内容、评价质量和产品匹配，不盲目加价。

### 5. 逐级扩展

首发词稳定后扩展到更短的中部词，再到核心词；每层有独立预算和进入门槛。

### 6. 收敛与防守

迁移赢家、否定无关词、保留低成本探索，并按库存和利润调整规模。

## 判断标准

- 每一层关键词都有事实相关性证据。
- 广告入口之间职责明确，不重复堆预算。
- 任何扩量都不突破现金、库存和合规护栏。

## 必须交付的结果

- 词根分层和首发词清单。
- 从长尾到核心词的阶段路线。
- 广告职责、预算与否定方案。
- 升级、暂停和商品页返工条件。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
