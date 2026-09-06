# Amazon 费用、利润与现金流：税务与出口、平台费用、季节性：专项证据卡

以下是分析台账字段，不是可直接传给某个 API 的参数；取数前需映射到实时 schema。只补齐当前判断必需的字段，未知项保留缺口。

本文件汇总该组内相近主题的 9 张证据卡。只加载当前问题直接相关的卡片，不要无差别执行全部内容。

## 季节性

- 判断要求：将需求窗口、备货、排名和广告节奏对齐，并区分事件效应。
- 最小证据字段：`marketplace`, `keyword_or_sku`, `historical_periods`, `comparable_baseline`, `event_dates`, `trend_range`, `arrival_date`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 政策变化

- 判断要求：保存官方原文、适用站点、生效日期、受影响对象和待验证解释。
- 最小证据字段：`official_source`, `publication_date`, `effective_date`, `marketplace`, `affected_scope`, `explicit_rule`, `unresolved_interpretation`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 新品启动

- 判断要求：先建立零数据基线，再用小预算、单变量和明确停止条件验证。
- 最小证据字段：`launch_stage`, `retail_readiness`, `first_inventory_eta`, `test_budget`, `loss_limit`, `evidence_goal`, `review_date`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 汇率风险

- 判断要求：用情景区间评估汇率对收入、成本和利润的影响，不预测单一路径。
- 最小证据字段：`base_currency`, `quote_currency`, `fx_rate`, `rate_source`, `effective_date`, `exposed_amount`, `scenario_range`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 税务与出口

- 判断要求：核对主体、交易链、单证和适用规则，并交由合格税务人员复核。
- 最小证据字段：`subject_ref`, `jurisdiction`, `reporting_period`, `income_definition`, `refund_amount`, `fee_amount`, `fx_basis`, `evidence_ref`。
- 覆盖本簇语义单元：6 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 平台费用

- 判断要求：以站点、日期、尺寸档和官方费率重算费用，保留账单证据。
- 最小证据字段：`marketplace`, `fee_type`, `effective_date`, `size_tier`, `unit_or_order_basis`, `billed_amount`, `official_rate_ref`。
- 覆盖本簇语义单元：5 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 利润模型

- 判断要求：统一收入、平台费、广告、退货、物流、税费和资金成本口径。
- 最小证据字段：`net_revenue`, `variable_cost`, `pre_ad_order_contribution`, `ad_spend`, `fixed_cost_allocation`, `quantity_per_order`, `currency`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 成本结构

- 判断要求：拆解可变、固定和一次性成本，给出单位、币种、时间和敏感性。
- 最小证据字段：`cost_item`, `variable_or_fixed`, `per_unit_or_order`, `amount`, `currency`, `tax_treatment`, `effective_period`, `evidence_ref`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 现金流

- 判断要求：按回款、采购、在途和库存周期建立现金缺口预警。
- 最小证据字段：`cash_balance`, `collection_date`, `supplier_payment_date`, `inventory_commitment`, `fixed_outflow`, `forecast_period`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。
