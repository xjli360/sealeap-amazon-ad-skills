---
name: sealeap-amazon-new-product-conversion-readiness
description: Diagnose why an Amazon new product cannot gain traction by separating retail-readiness, traffic relevance, click-through, conversion, economics, and feedback quality. Use when a new ASIN is not launching, ads are not converting, or the team is tempted to use fake reviews, inflated reference prices, or artificial orders. Replace unsafe tactics with compliant conversion and advertising work.
---

# Amazon 新品转化就绪诊断

## 目标

找出新品推不动是可售、点击、转化、流量还是经济性问题，并先修承接短板再扩大流量。

## 适用任务

- 新品有曝光或点击但没有订单。
- 团队把评论数量当作唯一启动条件。
- 需要建立商品页与广告的联合排查顺序。

## 开始前要拿到

- 可售状态、库存、Buy Box、价格、优惠和配送承诺。
- 主图、标题、五点、A+、视频、属性、合规评价和退货反馈。
- 查询级曝光、CTR、CVR、CPA 与竞品可比数据。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 拒绝虚假订单、免评单、测评、付费好评、评论合并和人为操纵参考价。
- 评论数量少不等于必须暂停推广；用真实转化障碍判断。
- 不得把广告带来的短期变化宣称为平台认可或排名因果。
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

### 1. 检查可售漏斗

从抑制、库存、配送、Featured Offer 和价格开始，先排除根本无法顺畅下单的问题。

### 2. 诊断点击

对比同一查询环境下的主图、价格、优惠、评分和标题相关性，找出 CTR 短板。

### 3. 诊断转化

检查内容证据、功能表达、变体选择、风险消除、真实评价主题和售后信息。

### 4. 审查流量

确认广告查询与商品事实匹配，集中预算到高意图主题，否定明确无关流量。

### 5. 建立合规反馈基础

使用符合资格的 Vine、Request a Review 和中立售后；把差评主题转为产品或说明改进。

### 6. 设置验证门槛

每个改动设前后窗口、目标指标和止损，承接仍弱时回到产品决策而不是继续烧钱。

## 判断标准

- 漏斗各层使用对应指标，不用评论数解释所有问题。
- 商品页改动有事实依据，不制造虚假稀缺、折扣或证明。
- 广告预算只在承接达标后扩大。

## 必须交付的结果

- 新品漏斗诊断。
- 商品页优先修复清单。
- 合规评价与售后计划。
- 精准流量验证方案和停止条件。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
