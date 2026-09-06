---
name: sealeap-xuanwu-amazon-b2b-opportunity-gate
description: "Assess whether an Amazon catalog offer has genuine business-buyer demand and is operationally ready for B2B pricing, quantity discounts, documentation, and large-order fulfillment. Use when evaluating Amazon Business expansion or preparing a controlled B2B pilot."
---

# Amazon B2B 商采机会闸门

## 目标

把“平台规模增长”转化为单个 ASIN 可验证的企业采购机会，先验证商采任务、批量经济性和履约能力，再决定是否进入试点。

## 适用任务

- 做当前状态的只读诊断。
- 形成有证据、可审批、可回退的计划或单变量实验。
- 判断信息不足时应继续验证、暂停还是保持 `HOLD`。

## 开始前要拿到

- 站点、ASIN、product type、当前 B2C 销售与贡献毛利。
- 潜在企业买家角色、采购任务、复购周期、批量数量与必需单证。
- 企业价格、阶梯折扣、Deal/Coupon 叠加规则与 FBA/MFN 容量。

缺少字段时明确标为 `UNKNOWN` 或 `NEEDS_EVIDENCE`，不要补造数据。

## 不可妥协的边界

- Amazon 当前官方规则、账户实时状态和一方业务报告优先；公开内容与第三方数据只能作为待验证启发或代理证据。
- 数值、政策、因果与执行状态分别标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`。
- 不捏造销量、搜索量、成本、产品属性、合规状态、评论、广告结果或平台机制。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不保存或输出素材来源身份、账号、链接、文章编号、发布日期、阅读量、原始话术或其他可反查线索。
- 平台界面、功能、费率、资格和规则会变化；执行前必须在目标站点复核。

## 工作流

1. 定义企业买家的具体使用任务，排除只有“可批量购买”而没有组织采购理由的商品。
2. 用企业订单、询价、业务搜索词或客户访谈验证需求；公开市场规模只能作为背景。
3. 按数量档计算含折扣、广告、退货、包装、税费和履约异常的贡献毛利。
4. 核对企业资质、发票、合规文件、包装单位、交期和大单拆分能力。
5. 选择少量 ASIN 设置可回退的企业价格或数量折扣草案，并定义试点窗口。
6. 用 B2B 会话、订单、客单量、复购和净贡献复盘，未达到门槛则维持 HOLD。

## 判断规则

- 企业购可用不等于该 ASIN 存在企业需求；至少要有一条直接需求证据。
- 不得用平台总体 GMV 或个别大单案例外推自身销量。
- 折扣必须由数量带来的成本或复购价值支撑，不能穿透最低贡献毛利。

## 必须交付的结果

- B2B 需求证据卡
- 数量阶梯单位经济表
- 资质与履约差距清单
- 试点/暂缓结论及停止条件

结尾列出站点、数据窗口、口径、证据、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行表、指标和质量检查见 [references/playbook.md](references/playbook.md)。

