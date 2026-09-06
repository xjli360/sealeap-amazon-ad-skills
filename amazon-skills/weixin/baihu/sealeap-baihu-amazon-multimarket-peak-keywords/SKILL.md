---
name: sealeap-baihu-amazon-multimarket-peak-keywords
description: "Build localized, evidence-backed Amazon keyword plans for seasonal peaks across multiple marketplaces. Use when preparing listings and ads for an event while preventing literal translation, shared-budget assumptions, and cross-market data leakage."
---

# Amazon 多站点旺季关键词

## 目标

以每个站点的真实搜索表达、季节窗口和单位经济独立建词库，使 Listing 承接与广告测试在旺季前有节奏地验证。

## 适用任务

- 做当前状态的只读诊断。
- 形成有证据、可审批、可回退的计划或单变量实验。
- 判断信息不足时应继续验证、暂停还是保持 `HOLD`。

## 开始前要拿到

- 目标站点、语言、活动日期、补货截止和预算。
- ABA、搜索词报告、自动广告、竞品公开词及其站点和窗口。
- 本地化 Listing、产品事实、禁限词、CPC/CVR 与毛利。

缺少字段时明确标为 `UNKNOWN` 或 `NEEDS_EVIDENCE`，不要补造数据。

## 不可妥协的边界

- Amazon 当前官方规则、账户实时状态和一方业务报告优先；公开内容与第三方数据只能作为待验证启发或代理证据。
- 数值、政策、因果与执行状态分别标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`。
- 不捏造销量、搜索量、成本、产品属性、合规状态、评论、广告结果或平台机制。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不保存或输出素材来源身份、账号、链接、文章编号、发布日期、阅读量、原始话术或其他可反查线索。
- 平台界面、功能、费率、资格和规则会变化；执行前必须在目标站点复核。

## 工作流

1. 为每个站点分别定义购买场景、活动时间轴和本地消费者表达。
2. 合并一方搜索词、ABA 和竞品候选词，保留来源、窗口与匹配意图。
3. 由母语或本地化审核区分直译词、自然表达、歧义词、拼写变体和禁限词。
4. 按核心、长尾、场景、季节和否定词分层，并检查 Listing 是否真实承接。
5. 在各站点独立设置小规模广告测试、预算和停止线，不共享结论。
6. 按搜索词、转化、净贡献、库存与时间衰减周更，淘汰无效表达。

## 判断规则

- 一个站点有效的词不得直接复制为另一个站点的事实。
- 第三方搜索量和竞品词为估算或公开代理，Amazon 一方报告优先。
- 旺季热度不能弥补低相关性、页面不承接或不可盈利。

## 必须交付的结果

- 分站点关键词证据表
- 本地化审核清单
- Listing 与广告词路由
- 旺季测试日历及停止条件

结尾列出站点、数据窗口、口径、证据、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行表、指标和质量检查见 [references/playbook.md](references/playbook.md)。

