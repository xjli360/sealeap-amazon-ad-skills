---
name: sealeap-xiezhi-amazon-ad-relevance-weight-bootstrap
description: "Create a guarded Amazon Ads launch plan that prioritizes query relevance, listing alignment, conversion evidence, and capped learning spend. Use when a new product has little history and the team wants to improve auction eligibility without assuming a hidden fixed weight score."
---

# Amazon 广告相关性启动

## 目标

用精准购物意图、页面一致性和受控学习预算积累可解释的点击与转化信号，而不是依赖未经证实的权重公式。

## 适用任务

- 为新品设计前几天的广告学习计划。
- 诊断相同出价但曝光差异。
- 在提高竞价前检查关键词和 Listing 相关性。

## 开始前要拿到

- 目标 ASIN/SKU、站点和产品事实。
- 精准词、搜索结果相关性和 Listing 字段覆盖。
- 建议竞价、广告位、预算、盈亏 CPC 与止损。
- CTR、CVR、CPC、订单和归因窗口基线。

缺少字段时列出证据缺口，并把相关结论标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`；不要补造数据。

## 不可妥协的边界

- 第三方数据均为估算或代理证据；Amazon 一方报告、后台实时字段和产品事实优先。
- 经验阈值只能作为可调起点，必须展示敏感性分析，不能写成 Amazon 官方规则。
- 不得捏造销量、搜索量、CPC、CVR、成本、认证、产品属性或消费者需求。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不输出或保存素材来源身份、账号、链接、作品编号、互动数据、原始话术或其他可反查来源的线索。
- 广告写操作须在用户明确授权的对象、动作与预算范围内，并保留回退值；已有授权覆盖时不重复索取。
- 不得把经验性拍卖解释或短期相关性写成 Amazon 官方公式。

## 工作流

### 1. 建立相关性地图

将产品核心属性、对象和场景与搜索词、Listing 标题/要点和目标页面逐项对齐。

### 2. 选择启动词

优先购买意图明确且搜索结果高度一致的词，排除大而泛、与产品弱相关的流量。

### 3. 设置学习护栏

以建议竞价区间为参考制定小范围测试，预先限定日预算、累计花费、最低样本和停止条件。

### 4. 观察分层信号

分别看曝光、CTR、CVR、CPC、广告位和搜索词；先判断资格/相关性，再判断商品页和价格。

### 5. 逐步调整

一次只改变主要变量；只有转化证据支持时扩大预算或竞价，表现恶化则回退。

## 判断标准

- 广告排序受出价、相关性、预计效果和竞争环境共同影响；不存在可直接读取的固定单一权重分。
- 新品可进行受控学习，但不得无上限高价抢位或把前三天当作必然起量窗口。
- 盈亏 CPC = 广告前每单贡献毛利 × 订单 CVR；订单 CVR 按归因订单 / 点击，以小数代入。出价与实际 CPC 分开，并检查动态竞价和位置调整后的风险。

## 第三方 MCP 数据

需要外部关键词、竞品、评论或公开网页证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，并使用 `scripts/mcp_research.py`。

- 先动态执行 `tools/list`、`search-tools` 和 `describe`，依据实时 `inputSchema` 构造参数。
- 凭证只从环境变量读取，不进入参数、URL、Skill、终端输出或 Git。
- 可能计费的 `tools/call` 先展示 Provider、工具、无密钥参数、预计成本与输出位置，核对已有授权；仅在授权覆盖本次范围时使用 `--allow-cost`，该标志不是费用上限。
- 脱敏结果用 `--output` 写入 Skill 包之外的任务私有目录；不假设安装位置受仓库 `.gitignore` 保护。第三方数据标为估算或代理证据。
- 失败一次后记录缺口，不以重复付费重试掩盖不可用状态。

## 必须交付的结果

- 关键词—页面相关性矩阵
- 启动广告草案
- 预算与累计止损
- 学习期监控表
- 待批准最小变更集

结尾列出站点、数据窗口、证据来源、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行细节、证据字段和质量检查见 [references/playbook.md](references/playbook.md)。
