# Amazon 跨境经营复盘：季节性、库存管理、发货与入库：专项证据卡

以下是分析台账字段，不是可直接传给某个 API 的参数；取数前需映射到实时 schema。只补齐当前判断必需的字段，未知项保留缺口。

本文件汇总该组内相近主题的 32 张证据卡。只加载当前问题直接相关的卡片，不要无差别执行全部内容。

## 季节性

- 判断要求：将需求窗口、备货、排名和广告节奏对齐，并区分事件效应。
- 最小证据字段：`marketplace`, `keyword_or_sku`, `historical_periods`, `comparable_baseline`, `event_dates`, `trend_range`, `arrival_date`。
- 覆盖本簇语义单元：42 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 预算分配

- 判断要求：按活动角色、边际回报、库存和利润约束分配预算，并设置停止条件。
- 最小证据字段：`campaign`, `configured_daily_budget`, `budget_rule`, `spend`, `exhaustion_time`, `loss_limit`, `shared_budget_scope`。
- 口径检查：SP 日预算属于 campaign；同一活动下的 ad group 共享该预算。要独立预算时拆分 campaign，并复核实际预算规则。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 库存管理

- 判断要求：以销量速度、在途、交期和安全库存建立补货与断货预案。
- 最小证据字段：`sku`, `daily_demand_range`, `usable_stock`, `inbound_eta`, `lead_time`, `safety_stock`, `reorder_point`, `cash_limit`。
- 覆盖本簇语义单元：35 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 关键词排名

- 判断要求：按固定站点、时间和查询记录排名，结合库存、价格、评价和广告干扰解释变化。
- 最小证据字段：`query`, `asin_or_variant`, `organic_or_paid`, `observed_position`, `postcode`, `device`, `login_state`, `observed_at`。
- 覆盖本簇语义单元：7 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 发货与入库

- 判断要求：逐节点记录创建、承运、签收、接收和可售状态，异常按证据升级。
- 最小证据字段：`shipment_ref`, `sku`, `expected_units`, `shipped_units`, `delivered_units`, `received_units`, `available_units`, `event_time`。
- 覆盖本簇语义单元：32 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## FBM

- 判断要求：核对承诺时效、库存同步、退货地址、承运与绩效风险。
- 最小证据字段：`sku`, `handling_time`, `carrier_service`, `delivery_promise`, `shipment_tracking`, `late_or_cancelled_orders`, `fulfillment_cost`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 用户画像

- 判断要求：用行为与场景证据描述人群，不以刻板标签替代真实需求。
- 最小证据字段：`buyer_role`, `user_role`, `task`, `trigger`, `observed_behavior`, `sample_source`, `sample_size`, `counterexample`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 归因分析

- 判断要求：统一归因窗口并区分相关性与因果性，保留自然与付费流量的边界。
- 最小证据字段：`ad_product`, `click_or_view_basis`, `attribution_window`, `event_date_basis`, `purchased_asin_scope`, `dedup_rule`, `maturity`。
- 口径检查：同一订单可能涉及不同广告产品的归因口径；跨报告相加或相减前核对重叠与日期口径。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 汇率风险

- 判断要求：用情景区间评估汇率对收入、成本和利润的影响，不预测单一路径。
- 最小证据字段：`base_currency`, `quote_currency`, `fx_rate`, `rate_source`, `effective_date`, `exposed_amount`, `scenario_range`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 退货与退款

- 判断要求：按原因、变体、时间和批次拆解，优先修正预期、质量和适配问题。
- 最小证据字段：`sku`, `orders_or_units`, `returned_orders_or_units`, `reason_code`, `refund_amount`, `recovery_value`, `reporting_window`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## Listing 诊断

- 判断要求：从合规、可发现性、点击和转化四层审计当前详情页。
- 最小证据字段：`marketplace`, `asin`, `field_name`, `current_value`, `submitted_value`, `issue_code`, `captured_at`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 平台费用

- 判断要求：以站点、日期、尺寸档和官方费率重算费用，保留账单证据。
- 最小证据字段：`marketplace`, `fee_type`, `effective_date`, `size_tier`, `unit_or_order_basis`, `billed_amount`, `official_rate_ref`。
- 覆盖本簇语义单元：5 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 转化率

- 判断要求：把转化问题拆成流量意图、详情页说服力、价格评价、库存配送和购买障碍。
- 最小证据字段：`attributed_orders`, `clicks`, `sessions_if_available`, `ordered_units`, `conversion_definition`, `attribution_window`, `sample_size`。
- 口径检查：用于获客成本的 CVR 按归因订单 / 点击计算；Units per Session 是另一口径，不能直接代入。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 类目与节点

- 判断要求：核对 product type、browse node、属性和前台归类，避免把错类流量当广告问题。
- 最小证据字段：`marketplace`, `asin`, `product_type`, `browse_node`, `required_attributes`, `listing_issue`, `checked_at`。
- 覆盖本簇语义单元：4 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## FBA

- 判断要求：核对配送模式、尺寸重量、费率、入仓要求和可追踪状态。
- 最小证据字段：`marketplace`, `sku`, `fulfillable_units`, `reserved_units`, `inbound_units`, `unfulfillable_units`, `inventory_age`, `snapshot_at`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 尺寸重量

- 判断要求：对照实物、包装和平台测量记录，重算档位并准备复测证据。
- 最小证据字段：`sku`, `product_or_package`, `length`, `width`, `height`, `weight`, `units`, `measurement_method`, `measured_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 匹配方式

- 判断要求：分别定义发现、验证和收割角色，避免不同匹配方式互相争抢。
- 最小证据字段：`campaign`, `ad_group`, `target_text`, `match_type`, `matched_query`, `relevance`, `performance_window`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 政策变化

- 判断要求：保存官方原文、适用站点、生效日期、受影响对象和待验证解释。
- 最小证据字段：`official_source`, `publication_date`, `effective_date`, `marketplace`, `affected_scope`, `explicit_rule`, `unresolved_interpretation`。
- 覆盖本簇语义单元：7 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 图片与视频

- 判断要求：建立信息优先级、事实证据、可读性和单变量创意测试。
- 最小证据字段：`asset_version`, `placement`, `product_fact_ref`, `claim`, `dimensions`, `mobile_preview`, `rejection_reason`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 竞品验证

- 判断要求：按相同购买对象、场景、功能和价格带定义直接竞品，并识别异常样本。
- 最小证据字段：`asin`, `parent_child_scope`, `buyer_task_fit`, `price`, `rating`, `review_count`, `fulfillment`, `observed_at`。
- 覆盖本簇语义单元：5 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 点击表现

- 判断要求：按搜索结果与广告位拆分点击数据，区分素材、价格、承诺和流量相关性问题。
- 最小证据字段：`impressions`, `clicks`, `ctr`, `campaign_or_target`, `placement`, `reporting_window`, `attribution_maturity`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 新品启动

- 判断要求：先建立零数据基线，再用小预算、单变量和明确停止条件验证。
- 最小证据字段：`launch_stage`, `retail_readiness`, `first_inventory_eta`, `test_budget`, `loss_limit`, `evidence_goal`, `review_date`。
- 覆盖本簇语义单元：6 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 账号关联

- 判断要求：按主体、人员、设备、网络、支付和资料建立隔离台账，避免规避平台规则。
- 最小证据字段：`subject_ref`, `account_ref`, `authorized_operator_ref`, `access_environment_ref`, `sharing_reason`, `policy_ref`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 运营工具

- 判断要求：先核对工具的数据来源、权限、费用和导出字段，再决定是否接入。
- 最小证据字段：`provider`, `tool_name`, `live_schema_date`, `supported_marketplace`, `data_definition`, `permission_scope`, `quota_or_cost`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 市场机会

- 判断要求：先验证需求、直接竞争、价格带和进入门槛，再讨论开发。
- 最小证据字段：`buyer_task`, `direct_competitor_rule`, `demand_window`, `demand_estimate`, `price_band`, `entry_barrier`, `missing_evidence`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 评价与口碑

- 判断要求：只分析合规获取的 VOC；禁止操纵评价、诱导好评或联系受限买家。
- 最小证据字段：`asin_and_variant`, `review_date`, `rating`, `verified_status_if_visible`, `topic`, `sample_size`, `dedup_rule`, `sampling_limit`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 关键词体系

- 判断要求：按品类、属性、人群、场景和问题收益组织词库，并记录来源与相关性。
- 最小证据字段：`keyword`, `language`, `marketplace`, `purchase_intent`, `relevance_reason`, `source_type`, `observed_window`, `evidence_status`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 利润模型

- 判断要求：统一收入、平台费、广告、退货、物流、税费和资金成本口径。
- 最小证据字段：`net_revenue`, `variable_cost`, `pre_ad_order_contribution`, `ad_spend`, `fixed_cost_allocation`, `quantity_per_order`, `currency`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 品牌与备案

- 判断要求：核对权利主体、资格、品牌资产和站点范围，区分申请与实际生效。
- 最小证据字段：`brand_name`, `rights_owner_ref`, `marketplace`, `registry_status`, `rights_scope`, `evidence_date`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 供应链

- 判断要求：统一规格询价，核验产能、质量、交期、合规和备选方案。
- 最小证据字段：`specification_version`, `supplier_ref`, `quote_currency`, `unit_price`, `moq`, `lead_time`, `sample_result`, `quality_terms`。
- 覆盖本簇语义单元：4 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 成本结构

- 判断要求：拆解可变、固定和一次性成本，给出单位、币种、时间和敏感性。
- 最小证据字段：`cost_item`, `variable_or_fixed`, `per_unit_or_order`, `amount`, `currency`, `tax_treatment`, `effective_period`, `evidence_ref`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 税务与出口

- 判断要求：核对主体、交易链、单证和适用规则，并交由合格税务人员复核。
- 最小证据字段：`subject_ref`, `jurisdiction`, `reporting_period`, `income_definition`, `refund_amount`, `fee_amount`, `fx_basis`, `evidence_ref`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。
