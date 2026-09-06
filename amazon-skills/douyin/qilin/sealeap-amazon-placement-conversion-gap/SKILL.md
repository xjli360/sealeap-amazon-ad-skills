---
name: sealeap-amazon-placement-conversion-gap
description: Diagnose why an Amazon keyword converts poorly at top of search but better elsewhere by analyzing placement reports, effective bids, competitor context, and controlled experiments. Use when an exact keyword gains premium placement yet underperforms, when raising bids shifts spend to the wrong placement, or when the user wants a placement test. Never claim exact page-position control.
---

# Amazon 广告位转化差异诊断

## 目标

识别同一查询在不同广告位的转化差异，用有效竞价和单变量实验找到利润更好的流量环境。

## 适用任务

- 首页顶部高消耗但低转化。
- 降低竞价后订单反而改善。
- 调整基础竞价后预算跑向非目标广告位。

## 开始前要拿到

- 按广告位拆分的曝光、点击、花费、订单、销售额和新客数据。
- 基础竞价、动态竞价策略、广告位调整和历史修改时间。
- 商品价格、评分、配送、内容与查询环境的可见竞品快照。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 广告位分类不等于固定自然页码；不能保证卡在具体位置。
- 前台竞争环境是样本，不应据单次截图下结论。
- 竞价与位置系数的改动必须计算最坏有效竞价。
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

### 1. 还原有效竞价

汇总基础竞价、动态策略和各位置系数，计算可能的有效出价范围。

### 2. 比较广告位经济性

对各位置计算 CTR、CVR、CPC、CPA、ACoS 和贡献利润，并标记样本强度。

### 3. 审视竞争环境

在标准化条件下抽样观察价格、评分、配送与卖点差异，把它作为解释线索。

### 4. 设计隔离实验

固定关键词、商品页和预算，只改变基础竞价或一个位置系数；设最小窗口和累计止损。

### 5. 调整流量组合

增加利润成立的位置权重，压低持续亏损位置；若所有位置转化差，回到 Listing 或关键词相关性。

### 6. 验证持续性

跨多个周期检查结果，防止促销、库存或竞品变化造成假胜利。

## 判断标准

- 有效竞价计算无遗漏。
- 位置对比使用相同或明确可比窗口。
- 结论区分数据事实、竞争环境推断和待验证假设。

## 必须交付的结果

- 广告位绩效和有效竞价表。
- 竞争环境假设。
- 单变量实验设计。
- 待批准位置调整与回滚条件。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
