---
name: sealeap-jiuwei-amazon-main-image-distinctiveness-test
description: "Design a category-compliant Amazon main-image distinctiveness experiment based on shopper recognition and click-through evidence. Use when competing listings look interchangeable or a visual-similarity feature creates an unverified optimization hypothesis."
---

# Amazon 主图可识别差异测试

## 目标

在主图政策和类目识别不变的前提下，用一个可解释的视觉变量测试点击差异，不声称能操纵视觉推荐池。

## 适用任务

- 做当前状态的只读诊断。
- 形成有证据、可审批、可回退的计划或单变量实验。
- 判断信息不足时应继续验证、暂停还是保持 `HOLD`。

## 开始前要拿到

- 站点、product type、当前类目主图规则和后台状态。
- 自身与直接竞品在同一设备、关键词、日期的主图样本。
- 可合法展示的实物角度、颜色、包装状态和基线 CTR/CVR。

缺少字段时明确标为 `UNKNOWN` 或 `NEEDS_EVIDENCE`，不要补造数据。

## 不可妥协的边界

- Amazon 当前官方规则、账户实时状态和一方业务报告优先；公开内容与第三方数据只能作为待验证启发或代理证据。
- 数值、政策、因果与执行状态分别标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`。
- 不捏造销量、搜索量、成本、产品属性、合规状态、评论、广告结果或平台机制。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不保存或输出素材来源身份、账号、链接、文章编号、发布日期、阅读量、原始话术或其他可反查线索。
- 平台界面、功能、费率、资格和规则会变化；执行前必须在目标站点复核。

## 工作流

1. 先做合规审计，任何硬性违规先修复，不进入创意实验。
2. 建立竞品视觉矩阵，记录主体占比、角度、轮廓、明暗和可识别属性。
3. 提出一个顾客可理解的差异变量，如合法角度、裁切或实物结构可见度。
4. 验证新图仍准确代表出售商品、类目可识别且不含禁用元素。
5. 在可用的一方实验工具中设置对照；否则采用谨慎的前后窗口并记录干扰。
6. 同时看 CTR、CVR、退货和抑制状态，点击上升但转化下降不视为成功。

## 判断规则

- 相似商品入口的存在不证明其排序因子或可被主图策略操纵。
- 不得为了“差异化”加入文字、徽章、道具、色块或未售配件。
- 主图变化与流量变化只能在隔离主要变量后建立有限因果结论。

## 必须交付的结果

- 类目视觉矩阵
- 单变量主图假设
- 合规与实验方案
- 结果判定和回退条件

结尾列出站点、数据窗口、口径、证据、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行表、指标和质量检查见 [references/playbook.md](references/playbook.md)。

