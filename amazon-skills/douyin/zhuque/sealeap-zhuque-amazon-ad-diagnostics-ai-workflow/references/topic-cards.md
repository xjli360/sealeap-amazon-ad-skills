# Amazon 广告诊断与实验：AI 工作流、图片与视频、站外流量：专项证据卡

以下是分析台账字段，不是可直接传给某个 API 的参数；取数前需映射到实时 schema。只补齐当前判断必需的字段，未知项保留缺口。

本文件汇总该组内相近主题的 11 张证据卡。只加载当前问题直接相关的卡片，不要无差别执行全部内容。

## AI 工作流

- 判断要求：把 AI 限定为有输入、证据、审核和回退的可复核流程。
- 最小证据字段：`task`, `input_contract`, `tool_version`, `permission_scope`, `baseline`, `error_rate`, `review_cost`, `stop_condition`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 图片与视频

- 判断要求：建立信息优先级、事实证据、可读性和单变量创意测试。
- 最小证据字段：`asset_version`, `placement`, `product_fact_ref`, `claim`, `dimensions`, `mobile_preview`, `rejection_reason`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 站外流量

- 判断要求：单独标记站外窗口和可归因链接，避免把相关性当成增量因果。
- 最小证据字段：`channel`, `campaign_tag`, `landing_asin`, `clicks`, `conversion_definition`, `attribution_method`, `spend`, `incrementality_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 使用场景

- 判断要求：把时间、地点、任务、触发和限制写成可验证的需求链。
- 最小证据字段：`buyer_task`, `use_environment`, `trigger`, `frequency`, `constraint`, `observed_problem`, `supporting_evidence`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 市场机会

- 判断要求：先验证需求、直接竞争、价格带和进入门槛，再讨论开发。
- 最小证据字段：`buyer_task`, `direct_competitor_rule`, `demand_window`, `demand_estimate`, `price_band`, `entry_barrier`, `missing_evidence`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 品牌与备案

- 判断要求：核对权利主体、资格、品牌资产和站点范围，区分申请与实际生效。
- 最小证据字段：`brand_name`, `rights_owner_ref`, `marketplace`, `registry_status`, `rights_scope`, `evidence_date`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 搜索词分析

- 判断要求：在 query 层聚合曝光、点击、订单和花费，再决定收词、否定或页面补强。
- 最小证据字段：`target`, `matched_search_term_or_asin`, `match_type`, `clicks`, `spend`, `attributed_orders`, `attribution_window`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## SB 广告

- 判断要求：核对品牌资格、落地页、创意、关键词与新客指标。
- 最小证据字段：`marketplace`, `eligibility`, `ad_format`, `landing_page`, `target_or_audience`, `campaign_budget`, `attribution_definition`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 评价与口碑

- 判断要求：只分析合规获取的 VOC；禁止操纵评价、诱导好评或联系受限买家。
- 最小证据字段：`asin_and_variant`, `review_date`, `rating`, `verified_status_if_visible`, `topic`, `sample_size`, `dedup_rule`, `sampling_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 类目与节点

- 判断要求：核对 product type、browse node、属性和前台归类，避免把错类流量当广告问题。
- 最小证据字段：`marketplace`, `asin`, `product_type`, `browse_node`, `required_attributes`, `listing_issue`, `checked_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 广告位

- 判断要求：按搜索顶部、其余搜索和商品页分层核对流量质量与转化。
- 最小证据字段：`campaign`, `placement`, `base_bid`, `placement_adjustment`, `bidding_strategy`, `impressions`, `clicks`, `spend`, `attributed_orders`。
- 口径检查：降低基础竞价并抬高某个位置倍率不能保证只获得该位置流量；用位置报告核验实际分布。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。
