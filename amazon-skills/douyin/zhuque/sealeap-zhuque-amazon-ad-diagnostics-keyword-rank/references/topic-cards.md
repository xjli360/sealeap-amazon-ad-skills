# Amazon 广告诊断与实验：关键词排名、利润模型、政策变化：专项证据卡

以下是分析台账字段，不是可直接传给某个 API 的参数；取数前需映射到实时 schema。只补齐当前判断必需的字段，未知项保留缺口。

本文件汇总该组内相近主题的 49 张证据卡。只加载当前问题直接相关的卡片，不要无差别执行全部内容。

## 账户验证

- 判断要求：核对主体、文件一致性、截止日期和官方入口，拒绝代过审承诺。
- 最小证据字段：`subject_ref`, `official_request_type`, `document_type`, `consistency_issue`, `due_date`, `submission_receipt`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 高客单价

- 判断要求：把决策周期、信任证据、获客成本、退货与现金流纳入验证。
- 最小证据字段：`order_value`, `pre_ad_order_contribution`, `purchase_cycle`, `expected_order_cvr`, `return_loss`, `service_cost`, `cash_limit`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## ROAS

- 判断要求：用统一归因窗和利润口径解释 ROAS，避免把销售回报直接等同净利润。
- 最小证据字段：`attributed_sales`, `ad_spend`, `attribution_window`, `currency`, `advertised_vs_purchased_asin`, `measurement_scope`。
- 口径检查：ROAS = 同口径归因销售额 / 广告花费；只有非零且口径相同的 ACoS 与 ROAS 才互为倒数，百分比需先转小数。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 供应链

- 判断要求：统一规格询价，核验产能、质量、交期、合规和备选方案。
- 最小证据字段：`specification_version`, `supplier_ref`, `quote_currency`, `unit_price`, `moq`, `lead_time`, `sample_result`, `quality_terms`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 现金流

- 判断要求：按回款、采购、在途和库存周期建立现金缺口预警。
- 最小证据字段：`cash_balance`, `collection_date`, `supplier_payment_date`, `inventory_commitment`, `fixed_outflow`, `forecast_period`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 关键词排名

- 判断要求：按固定站点、时间和查询记录排名，结合库存、价格、评价和广告干扰解释变化。
- 最小证据字段：`query`, `asin_or_variant`, `organic_or_paid`, `observed_position`, `postcode`, `device`, `login_state`, `observed_at`。
- 覆盖本簇语义单元：6 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 季节性

- 判断要求：将需求窗口、备货、排名和广告节奏对齐，并区分事件效应。
- 最小证据字段：`marketplace`, `keyword_or_sku`, `historical_periods`, `comparable_baseline`, `event_dates`, `trend_range`, `arrival_date`。
- 覆盖本簇语义单元：8 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 利润模型

- 判断要求：统一收入、平台费、广告、退货、物流、税费和资金成本口径。
- 最小证据字段：`net_revenue`, `variable_cost`, `pre_ad_order_contribution`, `ad_spend`, `fixed_cost_allocation`, `quantity_per_order`, `currency`。
- 覆盖本簇语义单元：11 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## AI 工作流

- 判断要求：把 AI 限定为有输入、证据、审核和回退的可复核流程。
- 最小证据字段：`task`, `input_contract`, `tool_version`, `permission_scope`, `baseline`, `error_rate`, `review_cost`, `stop_condition`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## AMC 分析

- 判断要求：只使用聚合且合规的数据，定义人群、路径、时间窗和可验证激活目标。
- 最小证据字段：`business_question`, `table_grain`, `join_keys`, `event_window`, `privacy_threshold`, `aggregation_grain`, `suppression_status`。
- 口径检查：被隐私阈值抑制的 NULL 不能当作 0；最终结果保持平台允许的聚合粒度，不反查个体。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## Featured Offer

- 判断要求：先核对资格、价格、库存、配送和账户健康，再解释流量或转化变化。
- 最小证据字段：`asin`, `seller_offer`, `featured_offer_status`, `price`, `shipping_promise`, `availability`, `checked_at`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 差异化

- 判断要求：从未满足问题、工程约束和可验证收益推导差异，不只改颜色或包装。
- 最小证据字段：`buyer_problem`, `existing_alternative`, `proposed_change`, `proof_method`, `incremental_cost`, `failure_condition`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 尺寸重量

- 判断要求：对照实物、包装和平台测量记录，重算档位并准备复测证据。
- 最小证据字段：`sku`, `product_or_package`, `length`, `width`, `height`, `weight`, `units`, `measurement_method`, `measured_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 账户健康

- 判断要求：从通知、指标、证据和根因建立最小纠正计划，不编造材料。
- 最小证据字段：`account_ref`, `notice_type`, `affected_asin`, `metric_definition`, `observed_value`, `due_date`, `corrective_evidence`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 评价与口碑

- 判断要求：只分析合规获取的 VOC；禁止操纵评价、诱导好评或联系受限买家。
- 最小证据字段：`asin_and_variant`, `review_date`, `rating`, `verified_status_if_visible`, `topic`, `sample_size`, `dedup_rule`, `sampling_limit`。
- 覆盖本簇语义单元：10 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 政策变化

- 判断要求：保存官方原文、适用站点、生效日期、受影响对象和待验证解释。
- 最小证据字段：`official_source`, `publication_date`, `effective_date`, `marketplace`, `affected_scope`, `explicit_rule`, `unresolved_interpretation`。
- 覆盖本簇语义单元：13 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 成本结构

- 判断要求：拆解可变、固定和一次性成本，给出单位、币种、时间和敏感性。
- 最小证据字段：`cost_item`, `variable_or_fixed`, `per_unit_or_order`, `amount`, `currency`, `tax_treatment`, `effective_period`, `evidence_ref`。
- 覆盖本簇语义单元：11 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## SD 广告

- 判断要求：区分上下文、受众和再营销目标，并设置频次与增量验证。
- 最小证据字段：`marketplace`, `ad_format`, `audience_or_context`, `optimization_goal`, `billing_model`, `budget_scope`, `attribution_definition`。
- 覆盖本簇语义单元：4 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 预算分配

- 判断要求：按活动角色、边际回报、库存和利润约束分配预算，并设置停止条件。
- 最小证据字段：`campaign`, `configured_daily_budget`, `budget_rule`, `spend`, `exhaustion_time`, `loss_limit`, `shared_budget_scope`。
- 口径检查：SP 日预算属于 campaign；同一活动下的 ad group 共享该预算。要独立预算时拆分 campaign，并复核实际预算规则。
- 覆盖本簇语义单元：16 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 用户画像

- 判断要求：用行为与场景证据描述人群，不以刻板标签替代真实需求。
- 最小证据字段：`buyer_role`, `user_role`, `task`, `trigger`, `observed_behavior`, `sample_source`, `sample_size`, `counterexample`。
- 覆盖本簇语义单元：5 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 新品启动

- 判断要求：先建立零数据基线，再用小预算、单变量和明确停止条件验证。
- 最小证据字段：`launch_stage`, `retail_readiness`, `first_inventory_eta`, `test_budget`, `loss_limit`, `evidence_goal`, `review_date`。
- 覆盖本簇语义单元：10 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 关键词体系

- 判断要求：按品类、属性、人群、场景和问题收益组织词库，并记录来源与相关性。
- 最小证据字段：`keyword`, `language`, `marketplace`, `purchase_intent`, `relevance_reason`, `source_type`, `observed_window`, `evidence_status`。
- 覆盖本簇语义单元：15 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 点击表现

- 判断要求：按搜索结果与广告位拆分点击数据，区分素材、价格、承诺和流量相关性问题。
- 最小证据字段：`impressions`, `clicks`, `ctr`, `campaign_or_target`, `placement`, `reporting_window`, `attribution_maturity`。
- 覆盖本簇语义单元：17 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 归因分析

- 判断要求：统一归因窗口并区分相关性与因果性，保留自然与付费流量的边界。
- 最小证据字段：`ad_product`, `click_or_view_basis`, `attribution_window`, `event_date_basis`, `purchased_asin_scope`, `dedup_rule`, `maturity`。
- 口径检查：同一订单可能涉及不同广告产品的归因口径；跨报告相加或相减前核对重叠与日期口径。
- 覆盖本簇语义单元：8 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 运营工具

- 判断要求：先核对工具的数据来源、权限、费用和导出字段，再决定是否接入。
- 最小证据字段：`provider`, `tool_name`, `live_schema_date`, `supported_marketplace`, `data_definition`, `permission_scope`, `quota_or_cost`。
- 覆盖本簇语义单元：8 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 转化率

- 判断要求：把转化问题拆成流量意图、详情页说服力、价格评价、库存配送和购买障碍。
- 最小证据字段：`attributed_orders`, `clicks`, `sessions_if_available`, `ordered_units`, `conversion_definition`, `attribution_window`, `sample_size`。
- 口径检查：用于获客成本的 CVR 按归因订单 / 点击计算；Units per Session 是另一口径，不能直接代入。
- 覆盖本簇语义单元：9 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## ACOS

- 判断要求：同时核对销售额口径、广告成本、贡献毛利和归因窗口，不单看一个百分比。
- 最小证据字段：`ad_spend`, `attributed_sales`, `attributed_orders`, `attribution_window`, `advertised_vs_purchased_asin`, `currency`。
- 口径检查：ACoS = 广告花费 / 同口径归因销售额；分母为 0 时标为未定义，并单列花费与订单。
- 覆盖本簇语义单元：5 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 匹配方式

- 判断要求：分别定义发现、验证和收割角色，避免不同匹配方式互相争抢。
- 最小证据字段：`campaign`, `ad_group`, `target_text`, `match_type`, `matched_query`, `relevance`, `performance_window`。
- 覆盖本簇语义单元：12 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## CPC

- 判断要求：按关键词、广告位和匹配方式拆解点击成本，并与可承受 CPC 做差额分析。
- 最小证据字段：`ad_spend`, `clicks`, `currency`, `target_or_placement`, `reporting_window`, `bidding_strategy`, `bid_adjustments`。
- 口径检查：CPC = 广告花费 / 点击数；点击数为 0 时不计算，不把出价当作实际 CPC。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## TACOS

- 判断要求：联合广告与自然销售评估总广告依赖，避免以压低投放换取表面改善。
- 最小证据字段：`ad_spend`, `total_sales`, `total_sales_scope`, `accounting_period`, `currency`, `cross_asin_or_channel_overlap`。
- 口径检查：TACoS = 广告花费 / 同范围总销售额；不能用跨归因窗口的总销售额减广告销售额，冒充实测自然销售额。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 库存管理

- 判断要求：以销量速度、在途、交期和安全库存建立补货与断货预案。
- 最小证据字段：`sku`, `daily_demand_range`, `usable_stock`, `inbound_eta`, `lead_time`, `safety_stock`, `reorder_point`, `cash_limit`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 图片与视频

- 判断要求：建立信息优先级、事实证据、可读性和单变量创意测试。
- 最小证据字段：`asset_version`, `placement`, `product_fact_ref`, `claim`, `dimensions`, `mobile_preview`, `rejection_reason`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 客服与工单

- 判断要求：建立问题、证据、请求动作、时限和升级路径，避免无差别重复开案。
- 最小证据字段：`case_ref`, `issue`, `timeline`, `evidence_ref`, `requested_action`, `due_date`, `response_status`, `escalation_reason`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 站外流量

- 判断要求：单独标记站外窗口和可归因链接，避免把相关性当成增量因果。
- 最小证据字段：`channel`, `campaign_tag`, `landing_asin`, `clicks`, `conversion_definition`, `attribution_method`, `spend`, `incrementality_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## SP 广告

- 判断要求：明确 SP 活动在发现、排名、转化或防守中的单一角色。
- 最小证据字段：`marketplace`, `campaign`, `ad_group`, `advertised_asin`, `target`, `placement`, `bid`, `campaign_budget`, `attribution_window`。
- 覆盖本簇语义单元：4 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 搜索词分析

- 判断要求：在 query 层聚合曝光、点击、订单和花费，再决定收词、否定或页面补强。
- 最小证据字段：`target`, `matched_search_term_or_asin`, `match_type`, `clicks`, `spend`, `attributed_orders`, `attribution_window`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 竞价策略

- 判断要求：记录基础竞价、动态竞价和广告位加价的叠加关系，只测试一个主变量。
- 最小证据字段：`target`, `current_bid`, `dynamic_strategy`, `placement_adjustment`, `order_cvr`, `pre_ad_order_contribution`, `risk_limit`。
- 覆盖本簇语义单元：8 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## SB 广告

- 判断要求：核对品牌资格、落地页、创意、关键词与新客指标。
- 最小证据字段：`marketplace`, `eligibility`, `ad_format`, `landing_page`, `target_or_audience`, `campaign_budget`, `attribution_definition`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 自动广告

- 判断要求：分拆自动投放子类型，提取有效搜索词并隔离浪费流量。
- 最小证据字段：`campaign`, `ad_group`, `automatic_target_group`, `bid`, `matched_query_or_asin`, `negative_target`, `performance_window`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## Listing 诊断

- 判断要求：从合规、可发现性、点击和转化四层审计当前详情页。
- 最小证据字段：`marketplace`, `asin`, `field_name`, `current_value`, `submitted_value`, `issue_code`, `captured_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 使用场景

- 判断要求：把时间、地点、任务、触发和限制写成可验证的需求链。
- 最小证据字段：`buyer_task`, `use_environment`, `trigger`, `frequency`, `constraint`, `observed_problem`, `supporting_evidence`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 变体关系

- 判断要求：核对允许的变体主题、子体事实、评论关系与合并拆分风险。
- 最小证据字段：`marketplace`, `product_type`, `parent_asin`, `child_asin`, `sku`, `current_theme`, `valid_theme`, `differentiating_attributes`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 市场机会

- 判断要求：先验证需求、直接竞争、价格带和进入门槛，再讨论开发。
- 最小证据字段：`buyer_task`, `direct_competitor_rule`, `demand_window`, `demand_estimate`, `price_band`, `entry_barrier`, `missing_evidence`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 广告曝光

- 判断要求：核对投放资格、相关性、竞价、预算、状态和流量入口，再定位曝光缺口。
- 最小证据字段：`campaign_or_target`, `placement`, `impressions`, `eligibility_status`, `budget_status`, `reporting_window`。
- 覆盖本簇语义单元：5 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 账号关联

- 判断要求：按主体、人员、设备、网络、支付和资料建立隔离台账，避免规避平台规则。
- 最小证据字段：`subject_ref`, `account_ref`, `authorized_operator_ref`, `access_environment_ref`, `sharing_reason`, `policy_ref`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 广告位

- 判断要求：按搜索顶部、其余搜索和商品页分层核对流量质量与转化。
- 最小证据字段：`campaign`, `placement`, `base_bid`, `placement_adjustment`, `bidding_strategy`, `impressions`, `clicks`, `spend`, `attributed_orders`。
- 口径检查：降低基础竞价并抬高某个位置倍率不能保证只获得该位置流量；用位置报告核验实际分布。
- 覆盖本簇语义单元：6 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 类目与节点

- 判断要求：核对 product type、browse node、属性和前台归类，避免把错类流量当广告问题。
- 最小证据字段：`marketplace`, `asin`, `product_type`, `browse_node`, `required_attributes`, `listing_issue`, `checked_at`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 品牌与备案

- 判断要求：核对权利主体、资格、品牌资产和站点范围，区分申请与实际生效。
- 最小证据字段：`brand_name`, `rights_owner_ref`, `marketplace`, `registry_status`, `rights_scope`, `evidence_date`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 竞品验证

- 判断要求：按相同购买对象、场景、功能和价格带定义直接竞品，并识别异常样本。
- 最小证据字段：`asin`, `parent_child_scope`, `buyer_task_fit`, `price`, `rating`, `review_count`, `fulfillment`, `observed_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。
