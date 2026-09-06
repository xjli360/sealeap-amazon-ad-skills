---
name: sealeap-kunpeng-amazon-image-compliance-audit
description: "Audit Amazon product images against current marketplace and category requirements, submission status, mobile readability, and factual accuracy. Use when images are rejected, replaced, suppressed, or due for a pre-publication compliance review."
---

# Amazon 图片合规审计

## 目标

从当前官方规则、类目覆盖规则和后台错误证据出发定位图片问题，避免把未经证实的“新规”或流量传言当作根因。

## 适用任务

- 做当前状态的只读诊断。
- 形成有证据、可审批、可回退的计划或单变量实验。
- 判断信息不足时应继续验证、暂停还是保持 `HOLD`。

## 开始前要拿到

- 站点、ASIN、product type、品牌角色和全部图片原文件。
- 当前类目风格指南、图片要求、后台 Submission status 或拒绝信息。
- 商品实物、包装清单、权利证明和移动/桌面预览。

缺少字段时明确标为 `UNKNOWN` 或 `NEEDS_EVIDENCE`，不要补造数据。

## 不可妥协的边界

- Amazon 当前官方规则、账户实时状态和一方业务报告优先；公开内容与第三方数据只能作为待验证启发或代理证据。
- 数值、政策、因果与执行状态分别标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`。
- 不捏造销量、搜索量、成本、产品属性、合规状态、评论、广告结果或平台机制。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不保存或输出素材来源身份、账号、链接、文章编号、发布日期、阅读量、原始话术或其他可反查线索。
- 平台界面、功能、费率、资格和规则会变化；执行前必须在目标站点复核。

## 工作流

1. 保存当前前台、后台和原文件证据，区分未展示、被替换、被拒绝与搜索抑制。
2. 核对通用要求与类目专属要求；发生冲突时以当前类目要求为准。
3. 逐图检查尺寸、清晰度、背景、主体占比、文字、道具、徽章、权利和商品一致性。
4. 把主图硬性要求与附图转化建议分开，不把建议写成政策。
5. 在手机和桌面预览顺序、裁切与可读性，列出最小修复草案。
6. 获批后提交单一修复并跟踪 Submission status；不以排名变化证明图片规则。

## 判断规则

- 图片不合规可能被拒绝、移除、替换或引发抑制，但具体处置以账户证据为准。
- 固定比例、固定张数或固定提升率若无当前一方依据，只能标为 ASSUMPTION。
- 不得展示未售配件、虚假效果、侵权素材或平台徽章。

## 必须交付的结果

- 逐图合规矩阵
- 后台错误与规则映射
- 最小修复清单
- 提交、验证与回退记录

结尾列出站点、数据窗口、口径、证据、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行表、指标和质量检查见 [references/playbook.md](references/playbook.md)。

