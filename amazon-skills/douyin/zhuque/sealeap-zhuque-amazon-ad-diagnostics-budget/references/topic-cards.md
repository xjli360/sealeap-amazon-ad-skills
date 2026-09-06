# Amazon 广告诊断与实验：预算分配、竞价策略、匹配方式：专项证据卡

以下是分析台账字段，不是可直接传给某个 API 的参数；取数前需映射到实时 schema。只补齐当前判断必需的字段，未知项保留缺口。

本文件汇总该组内相近主题的 5 张证据卡。只加载当前问题直接相关的卡片，不要无差别执行全部内容。

## 站外流量

- 判断要求：单独标记站外窗口和可归因链接，避免把相关性当成增量因果。
- 最小证据字段：`channel`, `campaign_tag`, `landing_asin`, `clicks`, `conversion_definition`, `attribution_method`, `spend`, `incrementality_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 预算分配

- 判断要求：按活动角色、边际回报、库存和利润约束分配预算，并设置停止条件。
- 最小证据字段：`campaign`, `configured_daily_budget`, `budget_rule`, `spend`, `exhaustion_time`, `loss_limit`, `shared_budget_scope`。
- 口径检查：SP 日预算属于 campaign；同一活动下的 ad group 共享该预算。要独立预算时拆分 campaign，并复核实际预算规则。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 竞价策略

- 判断要求：记录基础竞价、动态竞价和广告位加价的叠加关系，只测试一个主变量。
- 最小证据字段：`target`, `current_bid`, `dynamic_strategy`, `placement_adjustment`, `order_cvr`, `pre_ad_order_contribution`, `risk_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 匹配方式

- 判断要求：分别定义发现、验证和收割角色，避免不同匹配方式互相争抢。
- 最小证据字段：`campaign`, `ad_group`, `target_text`, `match_type`, `matched_query`, `relevance`, `performance_window`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 广告位

- 判断要求：按搜索顶部、其余搜索和商品页分层核对流量质量与转化。
- 最小证据字段：`campaign`, `placement`, `base_bid`, `placement_adjustment`, `bidding_strategy`, `impressions`, `clicks`, `spend`, `attributed_orders`。
- 口径检查：降低基础竞价并抬高某个位置倍率不能保证只获得该位置流量；用位置报告核验实际分布。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。
