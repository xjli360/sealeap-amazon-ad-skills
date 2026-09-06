---
name: sealeap-baize-amazon-budget-placement-control
description: "Control Amazon ad budget and placement as separate levers, diagnosing when click acceleration dilutes conversion and when additional budget can extend profitable traffic. Use for 加预算后转化下降、点击太快、怎么调顶部和商品页、预算不足还是竞价过高."
---

# Amazon 预算与广告位控制

## 目标

Control Amazon ad budget and placement as separate levers, diagnosing when click acceleration dilutes conversion and when additional budget can extend profitable traffic.

## 不可妥协的边界

- 当前 Amazon 官方政策、账户资格、站点字段和一方数据优先于本 Skill 的经验框架。
- 第三方数据一律标为估算或前台观测，不得写成 Amazon 一方事实。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 一次实验只改变一个主要变量，并记录基线、样本、成功、停止和回退条件。
- 不得复制来源材料或竞品表达；输出必须按当前任务重新组织并可由现有证据支撑。
- 加预算不保证订单同比增加，可能扩大到更弱流量。
- 所谓系统偏好或店铺历史分配只能写为假设，不作为确定机制。

## 先判断任务模式

1. **诊断**：读取现状、证据和缺口，不生成线上写入动作。
2. **方案草案**：输出可审核的结构、参数范围、实验和回退值。
3. **执行准备**：只生成待批准变更表或 API/控制台操作草案。
4. **已批准执行**：仅对用户在当前会话明确批准的对象和字段执行，并立即回读核验。

用户未指定时采用“诊断”。

## 开始前要拿到

- marketplace、店铺、ASIN/SKU、广告类型和目标
- 同口径的 Campaign、Targeting、Search Term、Placement 与 Advertised Product 报告
- 售价、优惠、COGS、Amazon 费用、退款与目标贡献利润
- 库存、Buy Box、Listing、评论和同期市场事件

缺失项必须标为 `NEEDS_EVIDENCE`；不得猜数字、补属性或把不同站点、ASIN、变体、币种和时间窗混在一起。

## 工作流

先读取 [references/playbook.md](references/playbook.md)，确认该方法适用于当前对象。按以下顺序执行：

1. 建立预算中断时段、点击速度和各位置效率的基线。
2. 判断预算是否真的截断高质量流量，还是竞价过高导致过快消耗。
3. 先用小幅竞价调整控制流量速度，再决定是否增加预算。
4. 差位置用较低基础价控制，好位置用单独倍率测试。
5. 每轮只改变预算、基础价或一个位置倍率中的一项。

最后做数据充分性检查，并把结论分成 `FACT / ESTIMATE / HYPOTHESIS / UNKNOWN`。若关键证据不足，状态写 `HOLD`。

## 必须交付的结果

- 预算瓶颈诊断
- 位置效率表
- 单变量调整
- 扩量回退线
- 数据范围、来源、采集时间、样本与限制。
- 关键假设、待补证据、风险和不可确定项。
- 若有动作：对象、旧值、新值、预期、停止条件、回退值与审批状态。

方案状态使用 `READY FOR REVIEW / DRAFT / HOLD / STOP`；如已执行，另行记录实际结果及回读证据。未得到明确批准时，不得声称已修改线上对象。
