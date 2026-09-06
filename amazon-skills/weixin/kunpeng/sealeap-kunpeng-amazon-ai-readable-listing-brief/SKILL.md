---
name: sealeap-kunpeng-amazon-ai-readable-listing-brief
description: "Create an evidence-backed Amazon listing brief that clearly answers buyer discovery, comparison, compatibility, and decision questions for both people and AI shopping interfaces. Use before drafting or testing listing content in an AI-assisted shopping environment."
---

# Amazon AI 可读 Listing 简报

## 目标

把真实产品证据组织成清晰、可扫描、可比较的购买信息，同时保持关键词相关性和政策合规，不追逐未经验证的生成式排名公式。

## 适用任务

- 做当前状态的只读诊断。
- 形成有证据、可审批、可回退的计划或单变量实验。
- 判断信息不足时应继续验证、暂停还是保持 `HOLD`。

## 开始前要拿到

- 站点、product type、产品规格、测试报告、适配范围和限制。
- 买家问题、退货原因、评论主题、搜索词和竞品信息缺口。
- 现有标题、五点、描述、A+、图片和可用实验工具。

缺少字段时明确标为 `UNKNOWN` 或 `NEEDS_EVIDENCE`，不要补造数据。

## 不可妥协的边界

- Amazon 当前官方规则、账户实时状态和一方业务报告优先；公开内容与第三方数据只能作为待验证启发或代理证据。
- 数值、政策、因果与执行状态分别标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`。
- 不捏造销量、搜索量、成本、产品属性、合规状态、评论、广告结果或平台机制。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不保存或输出素材来源身份、账号、链接、文章编号、发布日期、阅读量、原始话术或其他可反查线索。
- 平台界面、功能、费率、资格和规则会变化；执行前必须在目标站点复核。

## 工作流

1. 按发现、比较、适配、使用、风险和售后阶段整理买家问题。
2. 为每个回答绑定产品事实与证据，无法证明的数值和绝对化词语标记删除。
3. 建立属性词、自然问句、同义表达与页面字段的覆盖矩阵。
4. 起草标题、五点、A+ 和附图信息层级，优先清晰事实而非关键词密度。
5. 进行政策、类目、可读性和跨字段一致性审查。
6. 每次只测试一个信息结构变量，以业务指标判断，不用 AI 单次回答代替效果。

## 判断规则

- 问答完整度是内容质量目标，不是平台推荐保证。
- 不得复制竞品受版权保护的文案、图像或无法验证的参数。
- 技术术语需给消费者可理解的解释，但不能改变真实含义。

## 必须交付的结果

- 买家问题地图
- 事实与证据矩阵
- Listing 内容简报
- 单变量实验与验收标准

结尾列出站点、数据窗口、口径、证据、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行表、指标和质量检查见 [references/playbook.md](references/playbook.md)。

