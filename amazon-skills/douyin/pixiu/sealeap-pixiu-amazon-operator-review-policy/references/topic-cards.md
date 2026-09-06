# Amazon 跨境经营复盘：政策变化、客服与工单、手动广告：专项证据卡

以下是分析台账字段，不是可直接传给某个 API 的参数；取数前需映射到实时 schema。只补齐当前判断必需的字段，未知项保留缺口。

本文件汇总该组内相近主题的 21 张证据卡。只加载当前问题直接相关的卡片，不要无差别执行全部内容。

## 客服与工单

- 判断要求：建立问题、证据、请求动作、时限和升级路径，避免无差别重复开案。
- 最小证据字段：`case_ref`, `issue`, `timeline`, `evidence_ref`, `requested_action`, `due_date`, `response_status`, `escalation_reason`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 手动广告

- 判断要求：明确关键词或商品投放对象、匹配方式、出价和否定关系。
- 最小证据字段：`campaign`, `ad_group`, `target_type`, `keyword_or_asin`, `match_type`, `bid`, `campaign_budget`, `performance_window`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 标题

- 判断要求：依据实时类目规则和已证实产品事实设计可读标题，不堆词。
- 最小证据字段：`marketplace`, `product_type`, `current_title`, `product_facts`, `proposed_title`, `current_length_rule`, `claim_evidence`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 政策变化

- 判断要求：保存官方原文、适用站点、生效日期、受影响对象和待验证解释。
- 最小证据字段：`official_source`, `publication_date`, `effective_date`, `marketplace`, `affected_scope`, `explicit_rule`, `unresolved_interpretation`。
- 覆盖本簇语义单元：25 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 账户健康

- 判断要求：从通知、指标、证据和根因建立最小纠正计划，不编造材料。
- 最小证据字段：`account_ref`, `notice_type`, `affected_asin`, `metric_definition`, `observed_value`, `due_date`, `corrective_evidence`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 账号关联

- 判断要求：按主体、人员、设备、网络、支付和资料建立隔离台账，避免规避平台规则。
- 最小证据字段：`subject_ref`, `account_ref`, `authorized_operator_ref`, `access_environment_ref`, `sharing_reason`, `policy_ref`。
- 覆盖本簇语义单元：4 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 知识产权

- 判断要求：做关键词、图像和权利状态初筛；法律结论必须由专业人士确认。
- 最小证据字段：`jurisdiction`, `right_type`, `application_or_registration_ref`, `owner_ref`, `legal_status`, `claim_scope`, `checked_at`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 品牌与备案

- 判断要求：核对权利主体、资格、品牌资产和站点范围，区分申请与实际生效。
- 最小证据字段：`brand_name`, `rights_owner_ref`, `marketplace`, `registry_status`, `rights_scope`, `evidence_date`。
- 覆盖本簇语义单元：5 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 转化率

- 判断要求：把转化问题拆成流量意图、详情页说服力、价格评价、库存配送和购买障碍。
- 最小证据字段：`attributed_orders`, `clicks`, `sessions_if_available`, `ordered_units`, `conversion_definition`, `attribution_window`, `sample_size`。
- 口径检查：用于获客成本的 CVR 按归因订单 / 点击计算；Units per Session 是另一口径，不能直接代入。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## CPC

- 判断要求：按关键词、广告位和匹配方式拆解点击成本，并与可承受 CPC 做差额分析。
- 最小证据字段：`ad_spend`, `clicks`, `currency`, `target_or_placement`, `reporting_window`, `bidding_strategy`, `bid_adjustments`。
- 口径检查：CPC = 广告花费 / 点击数；点击数为 0 时不计算，不把出价当作实际 CPC。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 账户验证

- 判断要求：核对主体、文件一致性、截止日期和官方入口，拒绝代过审承诺。
- 最小证据字段：`subject_ref`, `official_request_type`, `document_type`, `consistency_issue`, `due_date`, `submission_receipt`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 运营工具

- 判断要求：先核对工具的数据来源、权限、费用和导出字段，再决定是否接入。
- 最小证据字段：`provider`, `tool_name`, `live_schema_date`, `supported_marketplace`, `data_definition`, `permission_scope`, `quota_or_cost`。
- 覆盖本簇语义单元：5 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## Listing 诊断

- 判断要求：从合规、可发现性、点击和转化四层审计当前详情页。
- 最小证据字段：`marketplace`, `asin`, `field_name`, `current_value`, `submitted_value`, `issue_code`, `captured_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 评价与口碑

- 判断要求：只分析合规获取的 VOC；禁止操纵评价、诱导好评或联系受限买家。
- 最小证据字段：`asin_and_variant`, `review_date`, `rating`, `verified_status_if_visible`, `topic`, `sample_size`, `dedup_rule`, `sampling_limit`。
- 覆盖本簇语义单元：5 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 税务与出口

- 判断要求：核对主体、交易链、单证和适用规则，并交由合格税务人员复核。
- 最小证据字段：`subject_ref`, `jurisdiction`, `reporting_period`, `income_definition`, `refund_amount`, `fee_amount`, `fx_basis`, `evidence_ref`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 高客单价

- 判断要求：把决策周期、信任证据、获客成本、退货与现金流纳入验证。
- 最小证据字段：`order_value`, `pre_ad_order_contribution`, `purchase_cycle`, `expected_order_cvr`, `return_loss`, `service_cost`, `cash_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 类目与节点

- 判断要求：核对 product type、browse node、属性和前台归类，避免把错类流量当广告问题。
- 最小证据字段：`marketplace`, `asin`, `product_type`, `browse_node`, `required_attributes`, `listing_issue`, `checked_at`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 关键词体系

- 判断要求：按品类、属性、人群、场景和问题收益组织词库，并记录来源与相关性。
- 最小证据字段：`keyword`, `language`, `marketplace`, `purchase_intent`, `relevance_reason`, `source_type`, `observed_window`, `evidence_status`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 成本结构

- 判断要求：拆解可变、固定和一次性成本，给出单位、币种、时间和敏感性。
- 最小证据字段：`cost_item`, `variable_or_fixed`, `per_unit_or_order`, `amount`, `currency`, `tax_treatment`, `effective_period`, `evidence_ref`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 新品启动

- 判断要求：先建立零数据基线，再用小预算、单变量和明确停止条件验证。
- 最小证据字段：`launch_stage`, `retail_readiness`, `first_inventory_eta`, `test_budget`, `loss_limit`, `evidence_goal`, `review_date`。
- 覆盖本簇语义单元：3 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 竞品验证

- 判断要求：按相同购买对象、场景、功能和价格带定义直接竞品，并识别异常样本。
- 最小证据字段：`asin`, `parent_child_scope`, `buyer_task_fit`, `price`, `rating`, `review_count`, `fulfillment`, `observed_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。
