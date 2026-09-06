---
name: sealeap-baize-amazon-conversion-first-scaling
description: "Scale Amazon ad traffic only after conversion quality, click velocity, budget continuity, inventory, and contribution economics show that broader reach can be absorbed. Use for 点击突然变多转化下降、要不要加预算、自然排名与广告扩量、维护新品转化."
---

# Amazon 转化优先扩量

## 目标

Scale Amazon ad traffic only after conversion quality, click velocity, budget continuity, inventory, and contribution economics show that broader reach can be absorbed.

## 不可妥协的边界

- 当前 Amazon 官方政策、账户资格、站点字段和一方数据优先于本 Skill 的经验框架。
- 第三方数据一律标为估算或前台观测，不得写成 Amazon 一方事实。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 一次实验只改变一个主要变量，并记录基线、样本、成功、停止和回退条件。
- 不得复制来源材料或竞品表达；输出必须按当前任务重新组织并可由现有证据支撑。
- 固定转化率门槛只算案例先验，必须按品类和利润校准。
- 广告不会立刻等比例增加订单，扩量效果需用增量实验验证。

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

1. 建立精准流量基线并监测点击速度，而非只看日预算是否花完。
2. 流量扩大但转化下滑时优先降竞价或隔离位置，防止低意向扩散。
3. 只有高质量时段因预算中断且利润为正时才测试加预算。
4. 将自然排名变化与总订单、广告订单和利润一起观察。
5. 扩量采用阶梯，每阶设库存和累计亏损止损。

最后做数据充分性检查，并把结论分成 `FACT / ESTIMATE / HYPOTHESIS / UNKNOWN`。若关键证据不足，状态写 `HOLD`。

## 必须交付的结果

- 扩量资格
- 点击速度诊断
- 预算实验
- 止损和恢复条件
- 数据范围、来源、采集时间、样本与限制。
- 关键假设、待补证据、风险和不可确定项。
- 若有动作：对象、旧值、新值、预期、停止条件、回退值与审批状态。

方案状态使用 `READY FOR REVIEW / DRAFT / HOLD / STOP`；如已执行，另行记录实际结果及回读证据。未得到明确批准时，不得声称已修改线上对象。
