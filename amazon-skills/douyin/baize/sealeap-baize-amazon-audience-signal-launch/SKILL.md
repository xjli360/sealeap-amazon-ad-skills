---
name: sealeap-baize-amazon-audience-signal-launch
description: "Plan an Amazon new-product traffic mix that limits early audience noise across manual keywords, product targeting, display audiences, and video while testing whether weak conversion is traffic- or product-led. Use for 新品人群标签、用户画像、相同关键词转化不同、展示或视频广告受众、前期控流量."
---

# Amazon 新品受众信号控制

## 目标

Plan an Amazon new-product traffic mix that limits early audience noise across manual keywords, product targeting, display audiences, and video while testing whether weak conversion is traffic- or product-led.

## 不可妥协的边界

- 当前 Amazon 官方政策、账户资格、站点字段和一方数据优先于本 Skill 的经验框架。
- 第三方数据一律标为估算或前台观测，不得写成 Amazon 一方事实。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 一次实验只改变一个主要变量，并记录基线、样本、成功、停止和回退条件。
- 不得复制来源材料或竞品表达；输出必须按当前任务重新组织并可由现有证据支撑。
- 不得声称能看见个体画像或平台内部标签。
- 受众推断必须保持聚合、隐私安全并接受产品根因的可能性。

## 先判断任务模式

1. **诊断**：读取现状、证据和缺口，不生成线上写入动作。
2. **方案草案**：输出可审核的结构、参数范围、实验和回退值。
3. **执行准备**：只生成待批准变更表或 API/控制台操作草案。
4. **已批准执行**：仅对用户在当前会话明确批准的对象和字段执行，并立即回读核验。

用户未指定时采用“诊断”。

## 开始前要拿到

- marketplace、ASIN/SKU、产品事实与目标购买任务
- 关键词、商品投放、展示和视频的聚合表现
- 受众包定义、资格、站点限制和隐私边界
- 价格、评论、页面、库存与转化基线

缺失项必须标为 `NEEDS_EVIDENCE`；不得猜数字、补属性或把不同站点、ASIN、变体、币种和时间窗混在一起。

## 工作流

先读取 [references/playbook.md](references/playbook.md)，确认该方法适用于当前对象。按以下顺序执行：

1. 把所谓人群标签改写为可观测的查询、商品页、受众包和转化行为。
2. 启动期优先高意图属性词，控制宽泛流量占比。
3. 商品投放只选替代性和价格评价基础接近的对象。
4. 展示与视频受众使用独立预算，并记录受众资格与站点限制。
5. 若精准流量长期仍差，回到价格、评论、图片与产品竞争力。

最后做数据充分性检查，并把结论分成 `FACT / ESTIMATE / HYPOTHESIS / UNKNOWN`。若关键证据不足，状态写 `HOLD`。

## 必须交付的结果

- 流量来源图
- 受众相关性假设
- 启动配比
- 产品侧回查条件
- 数据范围、来源、采集时间、样本与限制。
- 关键假设、待补证据、风险和不可确定项。
- 若有动作：对象、旧值、新值、预期、停止条件、回退值与审批状态。

方案状态使用 `READY FOR REVIEW / DRAFT / HOLD / STOP`；如已执行，另行记录实际结果及回读证据。未得到明确批准时，不得声称已修改线上对象。
