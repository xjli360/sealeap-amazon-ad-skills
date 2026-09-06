# Amazon 品牌、内容与增长：图片与视频、运营工具、AI 工作流：专项证据卡

以下是分析台账字段，不是可直接传给某个 API 的参数；取数前需映射到实时 schema。只补齐当前判断必需的字段，未知项保留缺口。

本文件汇总该组内相近主题的 14 张证据卡。只加载当前问题直接相关的卡片，不要无差别执行全部内容。

## 图片与视频

- 判断要求：建立信息优先级、事实证据、可读性和单变量创意测试。
- 最小证据字段：`asset_version`, `placement`, `product_fact_ref`, `claim`, `dimensions`, `mobile_preview`, `rejection_reason`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 运营工具

- 判断要求：先核对工具的数据来源、权限、费用和导出字段，再决定是否接入。
- 最小证据字段：`provider`, `tool_name`, `live_schema_date`, `supported_marketplace`, `data_definition`, `permission_scope`, `quota_or_cost`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## AI 工作流

- 判断要求：把 AI 限定为有输入、证据、审核和回退的可复核流程。
- 最小证据字段：`task`, `input_contract`, `tool_version`, `permission_scope`, `baseline`, `error_rate`, `review_cost`, `stop_condition`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## Featured Offer

- 判断要求：先核对资格、价格、库存、配送和账户健康，再解释流量或转化变化。
- 最小证据字段：`asin`, `seller_offer`, `featured_offer_status`, `price`, `shipping_promise`, `availability`, `checked_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## Listing 诊断

- 判断要求：从合规、可发现性、点击和转化四层审计当前详情页。
- 最小证据字段：`marketplace`, `asin`, `field_name`, `current_value`, `submitted_value`, `issue_code`, `captured_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 五点描述

- 判断要求：按购买问题组织收益、事实和适用边界，避免重复或虚假承诺。
- 最小证据字段：`buyer_question`, `product_fact`, `benefit`, `evidence_ref`, `field_order`, `proposed_copy`, `applicable_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 使用场景

- 判断要求：把时间、地点、任务、触发和限制写成可验证的需求链。
- 最小证据字段：`buyer_task`, `use_environment`, `trigger`, `frequency`, `constraint`, `observed_problem`, `supporting_evidence`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 品牌与备案

- 判断要求：核对权利主体、资格、品牌资产和站点范围，区分申请与实际生效。
- 最小证据字段：`brand_name`, `rights_owner_ref`, `marketplace`, `registry_status`, `rights_scope`, `evidence_date`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 客服与工单

- 判断要求：建立问题、证据、请求动作、时限和升级路径，避免无差别重复开案。
- 最小证据字段：`case_ref`, `issue`, `timeline`, `evidence_ref`, `requested_action`, `due_date`, `response_status`, `escalation_reason`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 尺寸重量

- 判断要求：对照实物、包装和平台测量记录，重算档位并准备复测证据。
- 最小证据字段：`sku`, `product_or_package`, `length`, `width`, `height`, `weight`, `units`, `measurement_method`, `measured_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 知识产权

- 判断要求：做关键词、图像和权利状态初筛；法律结论必须由专业人士确认。
- 最小证据字段：`jurisdiction`, `right_type`, `application_or_registration_ref`, `owner_ref`, `legal_status`, `claim_scope`, `checked_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 站外流量

- 判断要求：单独标记站外窗口和可归因链接，避免把相关性当成增量因果。
- 最小证据字段：`channel`, `campaign_tag`, `landing_asin`, `clicks`, `conversion_definition`, `attribution_method`, `spend`, `incrementality_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 竞品验证

- 判断要求：按相同购买对象、场景、功能和价格带定义直接竞品，并识别异常样本。
- 最小证据字段：`asin`, `parent_child_scope`, `buyer_task_fit`, `price`, `rating`, `review_count`, `fulfillment`, `observed_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 账户健康

- 判断要求：从通知、指标、证据和根因建立最小纠正计划，不编造材料。
- 最小证据字段：`account_ref`, `notice_type`, `affected_asin`, `metric_definition`, `observed_value`, `due_date`, `corrective_evidence`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。
