---
name: sealeap-xuanwu-amazon-price-history-governance
description: "Govern Amazon price changes and promotions with an auditable price timeline, reference-price eligibility, margin floors, and customer-visible history. Use when frequent repricing, deal planning, or price-history features may affect trust and promotion quality."
---

# Amazon 价格历史治理

## 目标

用真实价格时间线和单位经济管理日常价与促销价，避免频繁摆动、虚假参考价或只为制造折扣而改价。

## 何时使用

- 买家端出现价格历史或目标价提醒
- 促销资格、参考价或划线价经常失效
- 需要建立稳定价格走廊和活动日历

## 开始前要拿到

- ASIN、站点、过去至少一个完整商业周期的成交价和标价时间线
- 优惠券、Deal、会员折扣、叠加规则与参考价状态
- COGS、平台费、广告、退货、税费和最低贡献毛利
- 竞品价格只作同口径前台观察，并记录采集时间

缺失项必须标为 `UNKNOWN` 或 `NEEDS_EVIDENCE`；不得猜数字、补属性，或混用不同站点、ASIN、币种和时间窗。

## 不可妥协的边界

- 当前 Amazon 官方规则、目标账户实时状态和一方业务报告优先；公开内容与第三方数据只能作为待验证启发或代理证据。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 数值、政策、因果和执行状态分别标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`。
- 不保存或输出素材来源身份、账号、链接、文章编号、发布日期、阅读量、原始话术或其他可反查线索。
- 不得先抬价再降价、虚构 MSRP/List Price 或操纵历史价格来制造优惠。
- 买家端价格历史的覆盖市场、窗口和展示方式会变化，执行前实测。
- 参考价资格与最低价规则以当前站点为准；第三方价格追踪只作代理。

## 工作流

1. 合并标价、实际成交价、促销、优惠券和异常价格，形成可审计时间线。
2. 标出频繁摆动、短时抬价、叠加折扣和低于毛利底线的区间。
3. 核对当前参考价、Deal 与促销资格规则，区分可用、不可用和未知。
4. 按日常价、计划促销价、最低安全价定义价格走廊与审批权限。
5. 把活动日历与库存、广告、补货和价格历史可见性联动。
6. 每次调价后复核前台展示、实际成交、净贡献和资格，异常时回退。

## 判断状态

- `READY`：关键输入、资格与当前规则已核实，方案有成功、停止和回退条件。
- `HOLD`：方向可能成立，但关键证据或审批仍缺失。
- `STOP`：存在硬性违规、不可承受的经济性、虚假信息或无法回退的风险。

## 必须交付的结果

- 价格与促销时间线
- 参考价/资格检查表
- 价格走廊、活动日历和审批矩阵
- 异常检测与回退记录
- 数据范围、采集时间、定义、证据状态、限制和待批准动作

详细台账与质量门见 [references/playbook.md](references/playbook.md)。

