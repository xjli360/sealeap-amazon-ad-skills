# 经济模型与阶段目标

## 先统一口径

明确价格是否含税、折扣/优惠、退款、平台佣金、FBA/配送、COGS、头程、仓储、退货处理、人工和其他变动成本。不要把“毛利率”和“贡献利润率”混用。

## 公式

```text
net_revenue = units × realized_unit_revenue
non_ad_variable_cost = COGS + referral/FBA + inbound + returns + storage + coupon + other variable cost
contribution_before_ads = net_revenue - non_ad_variable_cost
max_ad_spend = contribution_before_ads - target_profit
break_even_CPA = contribution_before_ads / units
break_even_ACOS = contribution_before_ads / attributed_revenue
daily_budget_cap = min(max_ad_spend / active_days, inventory_cap, cashflow_cap, seasonal_cap)
```

若自然单与广告单混合，广告 ACOS 只应用于广告归因收入；整体经营同时报告 TACOS 和总贡献利润。

## 三阶段规划

| 字段 | 阶段 1 | 阶段 2 | 阶段 3 |
|---|---|---|---|
| 日期/旺季剩余天数 |  |  |  |
| 目标销量 |  |  |  |
| 目标利润/最大亏损 |  |  |  |
| 可售库存/补货 |  |  |  |
| 主要任务 | 发现/验证 | 放量/扩展 | 盈利/收缩 |
| 最大广告花费 |  |  |  |
| 日预算上限 |  |  |  |
| 停止条件 |  |  |  |

阶段名称按实际生命周期调整，不强制三段。

## PPTX 花环案例（`TRAINING_CASE`）

| 阶段 | 日期 | 价格 | 目标销量 | 目标利润 | 广告占收入 | 材料日预算 |
|---|---|---:|---:|---:|---:|---:|
| 1 | 10/01-10/31 | $50 | 200 | 约 -5% | 25% | $83 |
| 2 | 11/01-11/30 | $50 | 400 | 约 10% | 10% | $67 |
| 3 | 12/01-12/20 | $50 | 400 | 约 15% | 5% | $33 |

材料另假设产品毛利 30%、退货 7%、仓储 3%。这些数值只能展示倒推方法；应用时全部替换为当前 ASIN 事实，并复核税费和退货口径。

## 库存和季节约束

- 将库存按核心变体/尺码拆分，不用总库存掩盖断货。
- 计算补货最晚下单/入仓日、广告学习期、归因成熟日和促销截止。
- `max_ad_spend > 0` 不等于应花满；取利润、现金流、库存和需求上限的最小值。
- 阶段间未达到样本门槛时，不自动滚入下一阶段预算。
