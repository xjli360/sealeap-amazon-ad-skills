---
name: sealeap-amazon-new-product-ad-recovery
description: Recover an underperforming Amazon new-product advertising program by diagnosing traffic concentration, sample sufficiency, placement mix, retail readiness, and unit economics in a fixed order. Use when a new ASIN has run for days or weeks with few orders, scattered clicks, or unclear next steps. Build controlled tests and do not increase budget or change live ads without approval.
---

# Amazon 新品广告恢复诊断

## 目标

用固定诊断顺序替代空泛焦虑，确定是预算被分散、样本不足、广告位不利还是商品竞争力不足。

## 适用任务

- 新品多个活动各点几次但没有结论。
- 精准词预算太少，长期无法形成样本。
- 查询相关但广告位或商品页转化差。

## 开始前要拿到

- 新品上线日期和所有广告活动、查询、目标、广告位报告。
- 预算、竞价修改史、价格、优惠、库存和 Listing 版本。
- 预估或历史 CVR、CPC、贡献利润和最大测试损失。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 不能为了达到点击样本无限增加预算；累计花费止损优先。
- 第三方预估只作先验，最终以本 ASIN 数据修正。
- 若商品承接明显不合格，应暂停扩量并修产品页。
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

### 1. 检查流量集中度

把花费按搜索意图和词根汇总，识别预算是否碎片化；保留最相关的一至数个主题形成可判断样本。

### 2. 检查样本充分性

根据预期转化率、CPC 和止损计算需要的观察窗口；预算有限时延长时间，不同时扩太多目标。

### 3. 检查广告位

比较顶部、其余搜索位置和商品页面的 CVR、CPA 与利润，确认预算是否流向低效位置。

### 4. 检查商品承接

审查主图、价格、评分、配送、卖点、变体和竞品环境，确定是否值得继续购买流量。

### 5. 设计修复实验

每轮只改变目标集中度、竞价或商品页中的一个主要变量，保留基准和回滚线。

### 6. 作继续或退出决定

连续实验仍低于最低转化和利润门槛时，缩量、重做商品或退出，而不是永久烧钱。

## 判断标准

- 诊断按集中度、样本、位置、商品力顺序完成。
- 每个测试有预算上限和足够但不过量的样本目标。
- 最终结论允许退出。

## 必须交付的结果

- 新品广告故障树。
- 预算碎片化与样本分析。
- 广告位和商品页修复实验。
- 继续、返工或退出建议。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
