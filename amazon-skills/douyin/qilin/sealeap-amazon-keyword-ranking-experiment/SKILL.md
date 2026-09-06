---
name: sealeap-amazon-keyword-ranking-experiment
description: Design Amazon keyword-ranking experiments that identify promising terms from relevance, conversion, current organic visibility, and placement performance, then sequence long-tail, mid-tail, and head-term tests. Use when the user asks which keywords to push, what an ad position may reveal about order potential, or why organic rank stalls despite paid orders. Do not equate sponsored placement with organic rank or guarantee movement.
---

# Amazon 关键词排名实验

## 目标

用广告实验筛选与商品最匹配、在合理位置能产生利润的关键词，再按证据逐级扩大，而不是把排名当作可直接购买的结果。

## 适用任务

- 从已收录词中选择优先推进对象。
- 估算某查询在不同广告位的订单潜力。
- 广告有订单但自然位置停滞。

## 开始前要拿到

- 关键词相关性、查询报告、自然位置历史和广告位表现。
- CTR、CVR、CPC、CPA、价格、库存和贡献利润。
- 竞品环境、促销和 Listing 变化时间线。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- Sponsored 位置与 organic 位置的曝光和点击机制不同，不能直接等同。
- 自然排名由 Amazon 系统决定；不承诺固定订单量或固定时间换取位置。
- 不得使用分时出价、广告或其他方法配合虚假订单和人为转化。
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

### 1. 筛选候选词

从真实相关、已有转化、自然可见度较好或广告效率较高的词中建立候选集，不只按当前名次。

### 2. 设定实验位置假设

选择一个或多个广告位类别，固定商品页、价格和预算，明确不是精确页码控制。

### 3. 估算订单潜力

比较各位置的曝光、CTR、CVR、CPA 和贡献利润，形成区间而非把广告订单直接当作未来自然订单。

### 4. 先推高把握词

优先给高意图长尾或中部词稳定预算；达到利润和样本门槛后才扩大。

### 5. 诊断自然停滞

检查相对转化、点击、库存、价格、竞争和词根相关性；不要仅靠更高竞价追自然位。

### 6. 迭代到核心词

当多个相关词形成稳定基本盘后，小规模测试核心词，并保留止损和退出路径。

## 判断标准

- 订单潜力以区间和假设呈现。
- 广告与自然数据分别展示。
- 候选词排序同时考虑利润和相关性。

## 必须交付的结果

- 候选词评分表。
- 广告位实验与预算护栏。
- 长尾、中部、核心词的推进顺序。
- 自然停滞诊断和下一步建议。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
