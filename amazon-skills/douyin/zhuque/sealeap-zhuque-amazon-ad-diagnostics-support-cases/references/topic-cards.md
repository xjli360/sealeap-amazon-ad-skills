# Amazon 广告诊断与实验：客服与工单、变体关系、评价与口碑：专项证据卡

以下是分析台账字段，不是可直接传给某个 API 的参数；取数前需映射到实时 schema。只补齐当前判断必需的字段，未知项保留缺口。

本文件汇总该组内相近主题的 6 张证据卡。只加载当前问题直接相关的卡片，不要无差别执行全部内容。

## 客服与工单

- 判断要求：建立问题、证据、请求动作、时限和升级路径，避免无差别重复开案。
- 最小证据字段：`case_ref`, `issue`, `timeline`, `evidence_ref`, `requested_action`, `due_date`, `response_status`, `escalation_reason`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 变体关系

- 判断要求：核对允许的变体主题、子体事实、评论关系与合并拆分风险。
- 最小证据字段：`marketplace`, `product_type`, `parent_asin`, `child_asin`, `sku`, `current_theme`, `valid_theme`, `differentiating_attributes`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 评价与口碑

- 判断要求：只分析合规获取的 VOC；禁止操纵评价、诱导好评或联系受限买家。
- 最小证据字段：`asin_and_variant`, `review_date`, `rating`, `verified_status_if_visible`, `topic`, `sample_size`, `dedup_rule`, `sampling_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 归因分析

- 判断要求：统一归因窗口并区分相关性与因果性，保留自然与付费流量的边界。
- 最小证据字段：`ad_product`, `click_or_view_basis`, `attribution_window`, `event_date_basis`, `purchased_asin_scope`, `dedup_rule`, `maturity`。
- 口径检查：同一订单可能涉及不同广告产品的归因口径；跨报告相加或相减前核对重叠与日期口径。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 成本结构

- 判断要求：拆解可变、固定和一次性成本，给出单位、币种、时间和敏感性。
- 最小证据字段：`cost_item`, `variable_or_fixed`, `per_unit_or_order`, `amount`, `currency`, `tax_treatment`, `effective_period`, `evidence_ref`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 运营工具

- 判断要求：先核对工具的数据来源、权限、费用和导出字段，再决定是否接入。
- 最小证据字段：`provider`, `tool_name`, `live_schema_date`, `supported_marketplace`, `data_definition`, `permission_scope`, `quota_or_cost`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。
