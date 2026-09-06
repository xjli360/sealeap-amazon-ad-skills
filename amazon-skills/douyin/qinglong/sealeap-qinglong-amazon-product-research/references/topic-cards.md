# Amazon 选品与产品开发：市场机会、运营工具、关键词体系：专项证据卡

以下是分析台账字段，不是可直接传给某个 API 的参数；取数前需映射到实时 schema。只补齐当前判断必需的字段，未知项保留缺口。

本文件汇总该组内相近主题的 26 张证据卡。只加载当前问题直接相关的卡片，不要无差别执行全部内容。

## 市场机会

- 判断要求：先验证需求、直接竞争、价格带和进入门槛，再讨论开发。
- 最小证据字段：`buyer_task`, `direct_competitor_rule`, `demand_window`, `demand_estimate`, `price_band`, `entry_barrier`, `missing_evidence`。
- 覆盖本簇语义单元：4 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 运营工具

- 判断要求：先核对工具的数据来源、权限、费用和导出字段，再决定是否接入。
- 最小证据字段：`provider`, `tool_name`, `live_schema_date`, `supported_marketplace`, `data_definition`, `permission_scope`, `quota_or_cost`。
- 覆盖本簇语义单元：4 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 关键词体系

- 判断要求：按品类、属性、人群、场景和问题收益组织词库，并记录来源与相关性。
- 最小证据字段：`keyword`, `language`, `marketplace`, `purchase_intent`, `relevance_reason`, `source_type`, `observed_window`, `evidence_status`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 卖家精灵

- 判断要求：先发现实时 MCP schema，再以第三方估算口径获取关键词、竞品或评论证据。
- 最小证据字段：`tool_name`, `input_schema_date`, `marketplace`, `nonsecret_arguments`, `metric_definition`, `observation_window`, `result_path`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 点击表现

- 判断要求：按搜索结果与广告位拆分点击数据，区分素材、价格、承诺和流量相关性问题。
- 最小证据字段：`impressions`, `clicks`, `ctr`, `campaign_or_target`, `placement`, `reporting_window`, `attribution_maturity`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 竞品验证

- 判断要求：按相同购买对象、场景、功能和价格带定义直接竞品，并识别异常样本。
- 最小证据字段：`asin`, `parent_child_scope`, `buyer_task_fit`, `price`, `rating`, `review_count`, `fulfillment`, `observed_at`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## FBA

- 判断要求：核对配送模式、尺寸重量、费率、入仓要求和可追踪状态。
- 最小证据字段：`marketplace`, `sku`, `fulfillable_units`, `reserved_units`, `inbound_units`, `unfulfillable_units`, `inventory_age`, `snapshot_at`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## Listing 诊断

- 判断要求：从合规、可发现性、点击和转化四层审计当前详情页。
- 最小证据字段：`marketplace`, `asin`, `field_name`, `current_value`, `submitted_value`, `issue_code`, `captured_at`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 发货与入库

- 判断要求：逐节点记录创建、承运、签收、接收和可售状态，异常按证据升级。
- 最小证据字段：`shipment_ref`, `sku`, `expected_units`, `shipped_units`, `delivered_units`, `received_units`, `available_units`, `event_time`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 现金流

- 判断要求：按回款、采购、在途和库存周期建立现金缺口预警。
- 最小证据字段：`cash_balance`, `collection_date`, `supplier_payment_date`, `inventory_commitment`, `fixed_outflow`, `forecast_period`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 知识产权

- 判断要求：做关键词、图像和权利状态初筛；法律结论必须由专业人士确认。
- 最小证据字段：`jurisdiction`, `right_type`, `application_or_registration_ref`, `owner_ref`, `legal_status`, `claim_scope`, `checked_at`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 类目与节点

- 判断要求：核对 product type、browse node、属性和前台归类，避免把错类流量当广告问题。
- 最小证据字段：`marketplace`, `asin`, `product_type`, `browse_node`, `required_attributes`, `listing_issue`, `checked_at`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## FBM

- 判断要求：核对承诺时效、库存同步、退货地址、承运与绩效风险。
- 最小证据字段：`sku`, `handling_time`, `carrier_service`, `delivery_promise`, `shipment_tracking`, `late_or_cancelled_orders`, `fulfillment_cost`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 供应链

- 判断要求：统一规格询价，核验产能、质量、交期、合规和备选方案。
- 最小证据字段：`specification_version`, `supplier_ref`, `quote_currency`, `unit_price`, `moq`, `lead_time`, `sample_result`, `quality_terms`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 关键词排名

- 判断要求：按固定站点、时间和查询记录排名，结合库存、价格、评价和广告干扰解释变化。
- 最小证据字段：`query`, `asin_or_variant`, `organic_or_paid`, `observed_position`, `postcode`, `device`, `login_state`, `observed_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 利润模型

- 判断要求：统一收入、平台费、广告、退货、物流、税费和资金成本口径。
- 最小证据字段：`net_revenue`, `variable_cost`, `pre_ad_order_contribution`, `ad_spend`, `fixed_cost_allocation`, `quantity_per_order`, `currency`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 品牌与备案

- 判断要求：核对权利主体、资格、品牌资产和站点范围，区分申请与实际生效。
- 最小证据字段：`brand_name`, `rights_owner_ref`, `marketplace`, `registry_status`, `rights_scope`, `evidence_date`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 图片与视频

- 判断要求：建立信息优先级、事实证据、可读性和单变量创意测试。
- 最小证据字段：`asset_version`, `placement`, `product_fact_ref`, `claim`, `dimensions`, `mobile_preview`, `rejection_reason`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 季节性

- 判断要求：将需求窗口、备货、排名和广告节奏对齐，并区分事件效应。
- 最小证据字段：`marketplace`, `keyword_or_sku`, `historical_periods`, `comparable_baseline`, `event_dates`, `trend_range`, `arrival_date`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 差异化

- 判断要求：从未满足问题、工程约束和可验证收益推导差异，不只改颜色或包装。
- 最小证据字段：`buyer_problem`, `existing_alternative`, `proposed_change`, `proof_method`, `incremental_cost`, `failure_condition`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 成本结构

- 判断要求：拆解可变、固定和一次性成本，给出单位、币种、时间和敏感性。
- 最小证据字段：`cost_item`, `variable_or_fixed`, `per_unit_or_order`, `amount`, `currency`, `tax_treatment`, `effective_period`, `evidence_ref`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 搜索词分析

- 判断要求：在 query 层聚合曝光、点击、订单和花费，再决定收词、否定或页面补强。
- 最小证据字段：`target`, `matched_search_term_or_asin`, `match_type`, `clicks`, `spend`, `attributed_orders`, `attribution_window`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 汇率风险

- 判断要求：用情景区间评估汇率对收入、成本和利润的影响，不预测单一路径。
- 最小证据字段：`base_currency`, `quote_currency`, `fx_rate`, `rate_source`, `effective_date`, `exposed_amount`, `scenario_range`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 用户画像

- 判断要求：用行为与场景证据描述人群，不以刻板标签替代真实需求。
- 最小证据字段：`buyer_role`, `user_role`, `task`, `trigger`, `observed_behavior`, `sample_source`, `sample_size`, `counterexample`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 站外流量

- 判断要求：单独标记站外窗口和可归因链接，避免把相关性当成增量因果。
- 最小证据字段：`channel`, `campaign_tag`, `landing_asin`, `clicks`, `conversion_definition`, `attribution_method`, `spend`, `incrementality_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 退货与退款

- 判断要求：按原因、变体、时间和批次拆解，优先修正预期、质量和适配问题。
- 最小证据字段：`sku`, `orders_or_units`, `returned_orders_or_units`, `reason_code`, `refund_amount`, `recovery_value`, `reporting_window`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。
