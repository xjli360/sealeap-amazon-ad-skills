---
name: sealeap-baize-amazon-stockout-recovery
description: "Plan a compliant Amazon post-stockout recovery by rebuilding precise traffic, reassessing lost organic and related-product exposure, and scaling only after conversion stabilizes. Use for 补货后转化变差、断货后自然流量掉了、广告重启、受众重新校准. Do not use for review or order manipulation."
---

# Amazon 断货后流量恢复

## 目标

Plan a compliant Amazon post-stockout recovery by rebuilding precise traffic, reassessing lost organic and related-product exposure, and scaling only after conversion stabilizes.

## 不可妥协的边界

- 当前 Amazon 官方政策、账户资格、站点字段和一方数据优先于本 Skill 的经验框架。
- 第三方数据一律标为估算或前台观测，不得写成 Amazon 一方事实。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 一次实验只改变一个主要变量，并记录基线、样本、成功、停止和回退条件。
- 不得复制来源材料或竞品表达；输出必须按当前任务重新组织并可由现有证据支撑。
- 不抓取客户邮箱、不购买评论、不刷单、不使用所谓测评订单恢复权重。
- 断货导致画像变化属于待验证解释，应以实际流量结构变化为证据。

## 先判断任务模式

1. **诊断**：读取现状、证据和缺口，不生成线上写入动作。
2. **方案草案**：输出可审核的结构、参数范围、实验和回退值。
3. **执行准备**：只生成待批准变更表或 API/控制台操作草案。
4. **已批准执行**：仅对用户在当前会话明确批准的对象和字段执行，并立即回读核验。

用户未指定时采用“诊断”。

## 开始前要拿到

- marketplace、ASIN/SKU、库存阶段、补货与到仓时间
- 断货或备货前后的销量、流量、广告、自然位置和转化基线
- COGS、头程、仓储、平台费、退货和清仓成本
- 可比产品的成熟度、销量区间和需求趋势

缺失项必须标为 `NEEDS_EVIDENCE`；不得猜数字、补属性或把不同站点、ASIN、变体、币种和时间窗混在一起。

## 工作流

先读取 [references/playbook.md](references/playbook.md)，确认该方法适用于当前对象。按以下顺序执行：

1. 保存断货前稳定期、断货期和补货后的同口径数据快照。
2. 区分自然曝光、关联商品页流量、关键词广告和受众流量的变化。
3. 先恢复历史上最精准的手动词，并以低风险流量验证页面承接。
4. 仅对功能、价格与评价基础接近的商品做隔离式 ASIN 测试。
5. 转化稳定后分阶段恢复探索流量、促销和预算，每次只改一个变量。

最后做数据充分性检查，并把结论分成 `FACT / ESTIMATE / HYPOTHESIS / UNKNOWN`。若关键证据不足，状态写 `HOLD`。

## 必须交付的结果

- 三阶段损失诊断
- 精准重启清单
- 恢复阶梯
- 合规禁区与回退线
- 数据范围、来源、采集时间、样本与限制。
- 关键假设、待补证据、风险和不可确定项。
- 若有动作：对象、旧值、新值、预期、停止条件、回退值与审批状态。

方案状态使用 `READY FOR REVIEW / DRAFT / HOLD / STOP`；如已执行，另行记录实际结果及回读证据。未得到明确批准时，不得声称已修改线上对象。
