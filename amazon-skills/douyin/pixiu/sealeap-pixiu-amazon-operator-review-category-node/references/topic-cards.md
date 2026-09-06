# Amazon 跨境经营复盘：类目与节点、五点描述、变体关系：专项证据卡

以下是分析台账字段，不是可直接传给某个 API 的参数；取数前需映射到实时 schema。只补齐当前判断必需的字段，未知项保留缺口。

本文件汇总该组内相近主题的 9 张证据卡。只加载当前问题直接相关的卡片，不要无差别执行全部内容。

## 五点描述

- 判断要求：按购买问题组织收益、事实和适用边界，避免重复或虚假承诺。
- 最小证据字段：`buyer_question`, `product_fact`, `benefit`, `evidence_ref`, `field_order`, `proposed_copy`, `applicable_limit`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 变体关系

- 判断要求：核对允许的变体主题、子体事实、评论关系与合并拆分风险。
- 最小证据字段：`marketplace`, `product_type`, `parent_asin`, `child_asin`, `sku`, `current_theme`, `valid_theme`, `differentiating_attributes`。
- 覆盖本簇语义单元：2 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 类目与节点

- 判断要求：核对 product type、browse node、属性和前台归类，避免把错类流量当广告问题。
- 最小证据字段：`marketplace`, `asin`, `product_type`, `browse_node`, `required_attributes`, `listing_issue`, `checked_at`。
- 覆盖本簇语义单元：4 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## Listing 诊断

- 判断要求：从合规、可发现性、点击和转化四层审计当前详情页。
- 最小证据字段：`marketplace`, `asin`, `field_name`, `current_value`, `submitted_value`, `issue_code`, `captured_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 点击表现

- 判断要求：按搜索结果与广告位拆分点击数据，区分素材、价格、承诺和流量相关性问题。
- 最小证据字段：`impressions`, `clicks`, `ctr`, `campaign_or_target`, `placement`, `reporting_window`, `attribution_maturity`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 知识产权

- 判断要求：做关键词、图像和权利状态初筛；法律结论必须由专业人士确认。
- 最小证据字段：`jurisdiction`, `right_type`, `application_or_registration_ref`, `owner_ref`, `legal_status`, `claim_scope`, `checked_at`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 品牌与备案

- 判断要求：核对权利主体、资格、品牌资产和站点范围，区分申请与实际生效。
- 最小证据字段：`brand_name`, `rights_owner_ref`, `marketplace`, `registry_status`, `rights_scope`, `evidence_date`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 运营工具

- 判断要求：先核对工具的数据来源、权限、费用和导出字段，再决定是否接入。
- 最小证据字段：`provider`, `tool_name`, `live_schema_date`, `supported_marketplace`, `data_definition`, `permission_scope`, `quota_or_cost`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。

## 成本结构

- 判断要求：拆解可变、固定和一次性成本，给出单位、币种、时间和敏感性。
- 最小证据字段：`cost_item`, `variable_or_fixed`, `per_unit_or_order`, `amount`, `currency`, `tax_treatment`, `effective_period`, `evidence_ref`。
- 覆盖本簇语义单元：1 个
- 输出要求：记录事实、证据来源、站点、时间窗、假设、缺口、风险、停止条件和下一步。
