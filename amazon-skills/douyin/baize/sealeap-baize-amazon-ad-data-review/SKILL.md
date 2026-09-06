---
name: sealeap-baize-amazon-ad-data-review
description: "Review Amazon ad performance as a time sequence and explain how bid, placement, click velocity, conversion, and contribution profit changed after each intervention. Use for 广告日报复盘、调价后为什么变好或变差、点击速度分析、ACOS变化归因. Do not use for isolated one-day judgments."
---

# Amazon 广告逐日数据复盘

## 目标

Review Amazon ad performance as a time sequence and explain how bid, placement, click velocity, conversion, and contribution profit changed after each intervention.

## 不可妥协的边界

- 当前 Amazon 官方政策、账户资格、站点字段和一方数据优先于本 Skill 的经验框架。
- 第三方数据一律标为估算或前台观测，不得写成 Amazon 一方事实。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 一次实验只改变一个主要变量，并记录基线、样本、成功、停止和回退条件。
- 不得复制来源材料或竞品表达；输出必须按当前任务重新组织并可由现有证据支撑。
- 案例数值只说明复盘方法，不作为其他账户的阈值。
- 广告是否值得继续要看总利润与增量，不只看 ACOS。

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

1. 按日重建广告时间线，记录每次出价、预算、策略和位置倍率的生效时点。
2. 同时比较点击速度、CPC、CVR、订单、ACOS、总订单与贡献利润。
3. 把改变前的稳定窗口作为基线，避免把自然波动归因给某次操作。
4. 识别高价词吞量、位置前移导致意图变泛、预算中断等结构问题。
5. 根据证据选择保持、降价、重配位置或停止测试，并保留回退值。

最后做数据充分性检查，并把结论分成 `FACT / ESTIMATE / HYPOTHESIS / UNKNOWN`。若关键证据不足，状态写 `HOLD`。

## 必须交付的结果

- 逐日事件表
- 指标变化解释
- 可证与不可证结论
- 下一轮复测计划
- 数据范围、来源、采集时间、样本与限制。
- 关键假设、待补证据、风险和不可确定项。
- 若有动作：对象、旧值、新值、预期、停止条件、回退值与审批状态。

方案状态使用 `READY FOR REVIEW / DRAFT / HOLD / STOP`；如已执行，另行记录实际结果及回读证据。未得到明确批准时，不得声称已修改线上对象。
