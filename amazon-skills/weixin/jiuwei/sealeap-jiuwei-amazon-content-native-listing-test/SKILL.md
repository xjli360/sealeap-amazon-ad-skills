---
name: sealeap-jiuwei-amazon-content-native-listing-test
description: "Translate familiar content patterns into compliant Amazon secondary-image or A+ experiments without copying social interfaces, fabricating testimonials, or changing the main-image rules. Use when listing creative feels generic and needs a controlled engagement test."
---

# Amazon 内容原生化 Listing 测试

## 目标

将对话、场景和人物视角转译为清楚的电商信息结构，以真实买家问题和产品事实做单变量创意测试。

## 适用任务

- 做当前状态的只读诊断。
- 形成有证据、可审批、可回退的计划或单变量实验。
- 判断信息不足时应继续验证、暂停还是保持 `HOLD`。

## 开始前要拿到

- 站点、类目规则、现有主图/附图/A+ 和移动端预览。
- 买家问题、退货原因、使用场景、真实产品证据和品牌规范。
- 基线 CTR、CVR、会话、退货与实验窗口。

缺少字段时明确标为 `UNKNOWN` 或 `NEEDS_EVIDENCE`，不要补造数据。

## 不可妥协的边界

- Amazon 当前官方规则、账户实时状态和一方业务报告优先；公开内容与第三方数据只能作为待验证启发或代理证据。
- 数值、政策、因果与执行状态分别标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`。
- 不捏造销量、搜索量、成本、产品属性、合规状态、评论、广告结果或平台机制。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不保存或输出素材来源身份、账号、链接、文章编号、发布日期、阅读量、原始话术或其他可反查线索。
- 平台界面、功能、费率、资格和规则会变化；执行前必须在目标站点复核。

## 工作流

1. 先审计当前素材，定位是信息缺失、理解成本还是视觉同质化。
2. 从真实问题中选一个内容结构：问答、第一视角、步骤或前后场景。
3. 将结构用于附图或 A+；主图继续遵守当前类目硬性要求。
4. 去除虚构头像、点赞数、评论数、平台按钮和可能被误认成真实评价的元素。
5. 做移动端可读性、事实、版权和政策复核后，只改变一个创意变量。
6. 用 CTR、CVR、净贡献和退货原因判断；没有足够样本时保持 INCONCLUSIVE。

## 判断规则

- 熟悉感来自信息结构，不是复制第三方平台 UI。
- 不得把未经证实的算法、停留或转化提升比例当作预期结果。
- 不得通过卡片、二维码或文案把顾客引向站外，除非当前政策和页面类型明确允许。

## 必须交付的结果

- 创意问题诊断
- 合规内容结构简报
- 单变量素材测试
- 结果、局限与下一轮建议

结尾列出站点、数据窗口、口径、证据、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行表、指标和质量检查见 [references/playbook.md](references/playbook.md)。

