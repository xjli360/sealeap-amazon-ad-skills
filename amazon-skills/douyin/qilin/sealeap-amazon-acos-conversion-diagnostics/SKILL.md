---
name: sealeap-amazon-acos-conversion-diagnostics
description: Diagnose high Amazon Ads ACoS by decomposing CPC, conversion rate, price, query mix, placement mix, and sample sufficiency. Use when the user asks why ACoS is high, whether a keyword has enough clicks, how to estimate CPA or break-even CPC, or whether to move, pause, or continue a target. Return evidence-ranked actions and keep live changes behind approval.
---

# Amazon ACoS 转化驱动诊断

## 目标

把笼统的高 ACoS 问题拆成 CPC、转化率、售价、流量结构和样本量问题，优先处理最能改变利润的驱动项。

## 适用任务

- 广告高消耗低出单的根因诊断。
- 判断关键词样本是否足以暂停、降价或继续观察。
- 按查询和广告位重新分配预算。

## 开始前要拿到

- 搜索词、投放、广告位、已购商品和业务报告。
- 售价、优惠、退款、Amazon 费用、COGS 和目标贡献利润。
- 历史转化率、自有品牌分析基准或明确标注的第三方估算。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 第三方类目转化率只能做先验参考，不能冒充目标 ASIN 的真实转化率。
- 不能用固定点击数作为所有词的裁决线；应结合预期转化、花费风险和置信度。
- 新品期可以容忍阶段性高 ACoS，但仍必须设置累计亏损和库存止损。
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

### 1. 统一经济口径

计算盈亏平衡 ACoS、盈亏平衡 CPA 和盈亏平衡 CPC；说明是否按销售额、净售价或贡献毛利计算。

### 2. 定位花费去向

按搜索词、目标、广告活动和广告位排序花费，识别预算是否被低相关查询或低效位置吸收。

### 3. 建立转化基准

优先使用本 ASIN 历史数据，其次同产品组，再次类目代理值；为每个基准写明时间窗和可信度。

### 4. 判断样本强度

根据预期转化率估算一次转化所需点击，并结合贝叶斯或区间思路标记数据充分、偏弱或不足。

### 5. 选择动作

高 CPC 且转化正常时降竞价或换位置；流量不相关时否定；转化显著不足时检查商品页后再暂停；数据不足时延长窗口但不突破止损。

### 6. 安排复测

每次只改变一个主要变量，记录前后 CPC、CVR、CPA、ACoS、订单和利润。

## 判断标准

- ACoS = CPC /（平均归因每单销售额 × 订单 CVR）；订单 CVR 使用归因订单 / 点击的小数值。每单一件且价格一致时，才可用单件售价近似。
- 报告中分开商品页问题、流量问题和竞价问题。
- 任何暂停建议都附样本、损失上限和恢复条件。

## 必须交付的结果

- ACoS 驱动树。
- 关键词与广告位样本强度表。
- 继续、降价、迁移、否定、暂停建议。
- 待批准的最小变更集与复测窗口。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
