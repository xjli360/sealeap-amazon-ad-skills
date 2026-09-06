# Amazon 跨境经营复盘：AI 工作流、用户画像、运营工具：专项证据卡

以下是分析台账字段，不是可直接传给某个 API 的参数；取数前需映射到实时 schema。只补齐当前判断必需的字段，未知项保留缺口。

本文件汇总该组内相近主题的 27 张证据卡。只加载当前问题直接相关的卡片，不要无差别执行全部内容。

## 自动广告

- 判断要求：分拆自动投放子类型，提取有效搜索词并隔离浪费流量。
- 最小证据字段：`campaign`, `ad_group`, `automatic_target_group`, `bid`, `matched_query_or_asin`, `negative_target`, `performance_window`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## AI 工作流

- 判断要求：把 AI 限定为有输入、证据、审核和回退的可复核流程。
- 最小证据字段：`task`, `input_contract`, `tool_version`, `permission_scope`, `baseline`, `error_rate`, `review_cost`, `stop_condition`。
- 覆盖本簇语义单元：12 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 用户画像

- 判断要求：用行为与场景证据描述人群，不以刻板标签替代真实需求。
- 最小证据字段：`buyer_role`, `user_role`, `task`, `trigger`, `observed_behavior`, `sample_source`, `sample_size`, `counterexample`。
- 覆盖本簇语义单元：9 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 使用场景

- 判断要求：把时间、地点、任务、触发和限制写成可验证的需求链。
- 最小证据字段：`buyer_task`, `use_environment`, `trigger`, `frequency`, `constraint`, `observed_problem`, `supporting_evidence`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 转化率

- 判断要求：把转化问题拆成流量意图、详情页说服力、价格评价、库存配送和购买障碍。
- 最小证据字段：`attributed_orders`, `clicks`, `sessions_if_available`, `ordered_units`, `conversion_definition`, `attribution_window`, `sample_size`。
- 口径检查：用于获客成本的 CVR 按归因订单 / 点击计算；Units per Session 是另一口径，不能直接代入。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 卖家精灵

- 判断要求：先发现实时 MCP schema，再以第三方估算口径获取关键词、竞品或评论证据。
- 最小证据字段：`tool_name`, `input_schema_date`, `marketplace`, `nonsecret_arguments`, `metric_definition`, `observation_window`, `result_path`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 归因分析

- 判断要求：统一归因窗口并区分相关性与因果性，保留自然与付费流量的边界。
- 最小证据字段：`ad_product`, `click_or_view_basis`, `attribution_window`, `event_date_basis`, `purchased_asin_scope`, `dedup_rule`, `maturity`。
- 口径检查：同一订单可能涉及不同广告产品的归因口径；跨报告相加或相减前核对重叠与日期口径。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 竞价策略

- 判断要求：记录基础竞价、动态竞价和广告位加价的叠加关系，只测试一个主变量。
- 最小证据字段：`target`, `current_bid`, `dynamic_strategy`, `placement_adjustment`, `order_cvr`, `pre_ad_order_contribution`, `risk_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 关键词体系

- 判断要求：按品类、属性、人群、场景和问题收益组织词库，并记录来源与相关性。
- 最小证据字段：`keyword`, `language`, `marketplace`, `purchase_intent`, `relevance_reason`, `source_type`, `observed_window`, `evidence_status`。
- 覆盖本簇语义单元：4 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## Featured Offer

- 判断要求：先核对资格、价格、库存、配送和账户健康，再解释流量或转化变化。
- 最小证据字段：`asin`, `seller_offer`, `featured_offer_status`, `price`, `shipping_promise`, `availability`, `checked_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 图片与视频

- 判断要求：建立信息优先级、事实证据、可读性和单变量创意测试。
- 最小证据字段：`asset_version`, `placement`, `product_fact_ref`, `claim`, `dimensions`, `mobile_preview`, `rejection_reason`。
- 覆盖本簇语义单元：4 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 运营工具

- 判断要求：先核对工具的数据来源、权限、费用和导出字段，再决定是否接入。
- 最小证据字段：`provider`, `tool_name`, `live_schema_date`, `supported_marketplace`, `data_definition`, `permission_scope`, `quota_or_cost`。
- 覆盖本簇语义单元：12 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## Listing 诊断

- 判断要求：从合规、可发现性、点击和转化四层审计当前详情页。
- 最小证据字段：`marketplace`, `asin`, `field_name`, `current_value`, `submitted_value`, `issue_code`, `captured_at`。
- 覆盖本簇语义单元：5 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 点击表现

- 判断要求：按搜索结果与广告位拆分点击数据，区分素材、价格、承诺和流量相关性问题。
- 最小证据字段：`impressions`, `clicks`, `ctr`, `campaign_or_target`, `placement`, `reporting_window`, `attribution_maturity`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 知识产权

- 判断要求：做关键词、图像和权利状态初筛；法律结论必须由专业人士确认。
- 最小证据字段：`jurisdiction`, `right_type`, `application_or_registration_ref`, `owner_ref`, `legal_status`, `claim_scope`, `checked_at`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 尺寸重量

- 判断要求：对照实物、包装和平台测量记录，重算档位并准备复测证据。
- 最小证据字段：`sku`, `product_or_package`, `length`, `width`, `height`, `weight`, `units`, `measurement_method`, `measured_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 新品启动

- 判断要求：先建立零数据基线，再用小预算、单变量和明确停止条件验证。
- 最小证据字段：`launch_stage`, `retail_readiness`, `first_inventory_eta`, `test_budget`, `loss_limit`, `evidence_goal`, `review_date`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 市场机会

- 判断要求：先验证需求、直接竞争、价格带和进入门槛，再讨论开发。
- 最小证据字段：`buyer_task`, `direct_competitor_rule`, `demand_window`, `demand_estimate`, `price_band`, `entry_barrier`, `missing_evidence`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 类目与节点

- 判断要求：核对 product type、browse node、属性和前台归类，避免把错类流量当广告问题。
- 最小证据字段：`marketplace`, `asin`, `product_type`, `browse_node`, `required_attributes`, `listing_issue`, `checked_at`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 竞品验证

- 判断要求：按相同购买对象、场景、功能和价格带定义直接竞品，并识别异常样本。
- 最小证据字段：`asin`, `parent_child_scope`, `buyer_task_fit`, `price`, `rating`, `review_count`, `fulfillment`, `observed_at`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 评价与口碑

- 判断要求：只分析合规获取的 VOC；禁止操纵评价、诱导好评或联系受限买家。
- 最小证据字段：`asin_and_variant`, `review_date`, `rating`, `verified_status_if_visible`, `topic`, `sample_size`, `dedup_rule`, `sampling_limit`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 库存管理

- 判断要求：以销量速度、在途、交期和安全库存建立补货与断货预案。
- 最小证据字段：`sku`, `daily_demand_range`, `usable_stock`, `inbound_eta`, `lead_time`, `safety_stock`, `reorder_point`, `cash_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 发货与入库

- 判断要求：逐节点记录创建、承运、签收、接收和可售状态，异常按证据升级。
- 最小证据字段：`shipment_ref`, `sku`, `expected_units`, `shipped_units`, `delivered_units`, `received_units`, `available_units`, `event_time`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 税务与出口

- 判断要求：核对主体、交易链、单证和适用规则，并交由合格税务人员复核。
- 最小证据字段：`subject_ref`, `jurisdiction`, `reporting_period`, `income_definition`, `refund_amount`, `fee_amount`, `fx_basis`, `evidence_ref`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 站外流量

- 判断要求：单独标记站外窗口和可归因链接，避免把相关性当成增量因果。
- 最小证据字段：`channel`, `campaign_tag`, `landing_asin`, `clicks`, `conversion_definition`, `attribution_method`, `spend`, `incrementality_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 关键词排名

- 判断要求：按固定站点、时间和查询记录排名，结合库存、价格、评价和广告干扰解释变化。
- 最小证据字段：`query`, `asin_or_variant`, `organic_or_paid`, `observed_position`, `postcode`, `device`, `login_state`, `observed_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 政策变化

- 判断要求：保存官方原文、适用站点、生效日期、受影响对象和待验证解释。
- 最小证据字段：`official_source`, `publication_date`, `effective_date`, `marketplace`, `affected_scope`, `explicit_rule`, `unresolved_interpretation`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。
