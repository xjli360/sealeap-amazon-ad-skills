# Amazon 广告诊断与实验：账号关联、自动广告、类目与节点：专项证据卡

以下是分析台账字段，不是可直接传给某个 API 的参数；取数前需映射到实时 schema。只补齐当前判断必需的字段，未知项保留缺口。

本文件汇总该组内相近主题的 33 张证据卡。只加载当前问题直接相关的卡片，不要无差别执行全部内容。

## 账号关联

- 判断要求：按主体、人员、设备、网络、支付和资料建立隔离台账，避免规避平台规则。
- 最小证据字段：`subject_ref`, `account_ref`, `authorized_operator_ref`, `access_environment_ref`, `sharing_reason`, `policy_ref`。
- 覆盖本簇语义单元：5 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 否定投放

- 判断要求：以足够点击与明确不相关证据建立否定候选，保留审批和回退记录。
- 最小证据字段：`campaign_or_ad_group`, `matched_query_or_asin`, `negative_type`, `relevance_evidence`, `loss_evidence`, `recovery_condition`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 尺寸重量

- 判断要求：对照实物、包装和平台测量记录，重算档位并准备复测证据。
- 最小证据字段：`sku`, `product_or_package`, `length`, `width`, `height`, `weight`, `units`, `measurement_method`, `measured_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 标题

- 判断要求：依据实时类目规则和已证实产品事实设计可读标题，不堆词。
- 最小证据字段：`marketplace`, `product_type`, `current_title`, `product_facts`, `proposed_title`, `current_length_rule`, `claim_evidence`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 账户健康

- 判断要求：从通知、指标、证据和根因建立最小纠正计划，不编造材料。
- 最小证据字段：`account_ref`, `notice_type`, `affected_asin`, `metric_definition`, `observed_value`, `due_date`, `corrective_evidence`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 自动广告

- 判断要求：分拆自动投放子类型，提取有效搜索词并隔离浪费流量。
- 最小证据字段：`campaign`, `ad_group`, `automatic_target_group`, `bid`, `matched_query_or_asin`, `negative_target`, `performance_window`。
- 覆盖本簇语义单元：6 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 类目与节点

- 判断要求：核对 product type、browse node、属性和前台归类，避免把错类流量当广告问题。
- 最小证据字段：`marketplace`, `asin`, `product_type`, `browse_node`, `required_attributes`, `listing_issue`, `checked_at`。
- 覆盖本簇语义单元：8 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## Listing 诊断

- 判断要求：从合规、可发现性、点击和转化四层审计当前详情页。
- 最小证据字段：`marketplace`, `asin`, `field_name`, `current_value`, `submitted_value`, `issue_code`, `captured_at`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 使用场景

- 判断要求：把时间、地点、任务、触发和限制写成可验证的需求链。
- 最小证据字段：`buyer_task`, `use_environment`, `trigger`, `frequency`, `constraint`, `observed_problem`, `supporting_evidence`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 五点描述

- 判断要求：按购买问题组织收益、事实和适用边界，避免重复或虚假承诺。
- 最小证据字段：`buyer_question`, `product_fact`, `benefit`, `evidence_ref`, `field_order`, `proposed_copy`, `applicable_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

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

## 竞品验证

- 判断要求：按相同购买对象、场景、功能和价格带定义直接竞品，并识别异常样本。
- 最小证据字段：`asin`, `parent_child_scope`, `buyer_task_fit`, `price`, `rating`, `review_count`, `fulfillment`, `observed_at`。
- 覆盖本簇语义单元：6 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 商品投放

- 判断要求：按直接竞品、替代品、互补品和防守对象建立可复核 ASIN 池。
- 最小证据字段：`advertised_asin`, `target_asin_or_category`, `relationship`, `price_and_rating_gap`, `matched_asin`, `performance_window`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 新品启动

- 判断要求：先建立零数据基线，再用小预算、单变量和明确停止条件验证。
- 最小证据字段：`launch_stage`, `retail_readiness`, `first_inventory_eta`, `test_budget`, `loss_limit`, `evidence_goal`, `review_date`。
- 覆盖本簇语义单元：6 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 季节性

- 判断要求：将需求窗口、备货、排名和广告节奏对齐，并区分事件效应。
- 最小证据字段：`marketplace`, `keyword_or_sku`, `historical_periods`, `comparable_baseline`, `event_dates`, `trend_range`, `arrival_date`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 运营工具

- 判断要求：先核对工具的数据来源、权限、费用和导出字段，再决定是否接入。
- 最小证据字段：`provider`, `tool_name`, `live_schema_date`, `supported_marketplace`, `data_definition`, `permission_scope`, `quota_or_cost`。
- 覆盖本簇语义单元：5 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 关键词体系

- 判断要求：按品类、属性、人群、场景和问题收益组织词库，并记录来源与相关性。
- 最小证据字段：`keyword`, `language`, `marketplace`, `purchase_intent`, `relevance_reason`, `source_type`, `observed_window`, `evidence_status`。
- 覆盖本簇语义单元：8 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 手动广告

- 判断要求：明确关键词或商品投放对象、匹配方式、出价和否定关系。
- 最小证据字段：`campaign`, `ad_group`, `target_type`, `keyword_or_asin`, `match_type`, `bid`, `campaign_budget`, `performance_window`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 匹配方式

- 判断要求：分别定义发现、验证和收割角色，避免不同匹配方式互相争抢。
- 最小证据字段：`campaign`, `ad_group`, `target_text`, `match_type`, `matched_query`, `relevance`, `performance_window`。
- 覆盖本簇语义单元：7 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 用户画像

- 判断要求：用行为与场景证据描述人群，不以刻板标签替代真实需求。
- 最小证据字段：`buyer_role`, `user_role`, `task`, `trigger`, `observed_behavior`, `sample_source`, `sample_size`, `counterexample`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 评价与口碑

- 判断要求：只分析合规获取的 VOC；禁止操纵评价、诱导好评或联系受限买家。
- 最小证据字段：`asin_and_variant`, `review_date`, `rating`, `verified_status_if_visible`, `topic`, `sample_size`, `dedup_rule`, `sampling_limit`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 搜索词分析

- 判断要求：在 query 层聚合曝光、点击、订单和花费，再决定收词、否定或页面补强。
- 最小证据字段：`target`, `matched_search_term_or_asin`, `match_type`, `clicks`, `spend`, `attributed_orders`, `attribution_window`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 库存管理

- 判断要求：以销量速度、在途、交期和安全库存建立补货与断货预案。
- 最小证据字段：`sku`, `daily_demand_range`, `usable_stock`, `inbound_eta`, `lead_time`, `safety_stock`, `reorder_point`, `cash_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 关键词排名

- 判断要求：按固定站点、时间和查询记录排名，结合库存、价格、评价和广告干扰解释变化。
- 最小证据字段：`query`, `asin_or_variant`, `organic_or_paid`, `observed_position`, `postcode`, `device`, `login_state`, `observed_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 品牌与备案

- 判断要求：核对权利主体、资格、品牌资产和站点范围，区分申请与实际生效。
- 最小证据字段：`brand_name`, `rights_owner_ref`, `marketplace`, `registry_status`, `rights_scope`, `evidence_date`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 竞价策略

- 判断要求：记录基础竞价、动态竞价和广告位加价的叠加关系，只测试一个主变量。
- 最小证据字段：`target`, `current_bid`, `dynamic_strategy`, `placement_adjustment`, `order_cvr`, `pre_ad_order_contribution`, `risk_limit`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 政策变化

- 判断要求：保存官方原文、适用站点、生效日期、受影响对象和待验证解释。
- 最小证据字段：`official_source`, `publication_date`, `effective_date`, `marketplace`, `affected_scope`, `explicit_rule`, `unresolved_interpretation`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## SB 广告

- 判断要求：核对品牌资格、落地页、创意、关键词与新客指标。
- 最小证据字段：`marketplace`, `eligibility`, `ad_format`, `landing_page`, `target_or_audience`, `campaign_budget`, `attribution_definition`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 广告位

- 判断要求：按搜索顶部、其余搜索和商品页分层核对流量质量与转化。
- 最小证据字段：`campaign`, `placement`, `base_bid`, `placement_adjustment`, `bidding_strategy`, `impressions`, `clicks`, `spend`, `attributed_orders`。
- 口径检查：降低基础竞价并抬高某个位置倍率不能保证只获得该位置流量；用位置报告核验实际分布。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 点击表现

- 判断要求：按搜索结果与广告位拆分点击数据，区分素材、价格、承诺和流量相关性问题。
- 最小证据字段：`impressions`, `clicks`, `ctr`, `campaign_or_target`, `placement`, `reporting_window`, `attribution_maturity`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 预算分配

- 判断要求：按活动角色、边际回报、库存和利润约束分配预算，并设置停止条件。
- 最小证据字段：`campaign`, `configured_daily_budget`, `budget_rule`, `spend`, `exhaustion_time`, `loss_limit`, `shared_budget_scope`。
- 口径检查：SP 日预算属于 campaign；同一活动下的 ad group 共享该预算。要独立预算时拆分 campaign，并复核实际预算规则。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 转化率

- 判断要求：把转化问题拆成流量意图、详情页说服力、价格评价、库存配送和购买障碍。
- 最小证据字段：`attributed_orders`, `clicks`, `sessions_if_available`, `ordered_units`, `conversion_definition`, `attribution_window`, `sample_size`。
- 口径检查：用于获客成本的 CVR 按归因订单 / 点击计算；Units per Session 是另一口径，不能直接代入。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。
