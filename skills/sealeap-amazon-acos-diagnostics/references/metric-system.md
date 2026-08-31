# ACOS 指标系统与口径

## 基础公式

同一分析作用域内：

```text
CTR = clicks / impressions
CPC = spend / clicks
CPM = spend / impressions × 1000
CVR = attributed_orders / clicks
AOV = attributed_sales / attributed_orders
CPA = spend / attributed_orders
ACOS = spend / attributed_sales
ROAS = attributed_sales / spend = 1 / ACOS_decimal
TACOS = spend / total_sales
ACOS = CPC / (CVR_decimal × AOV)
```

百分比展示时乘以 100。分母为 0 时返回 `N/A`，不要返回 0。

## 盈亏线

课程用“除广告外毛利率”解释盈亏 ACOS。真实经营中应明确使用广告前贡献毛利率：

```text
revenue
- discount borne by seller
- COGS
- Amazon referral/FBA/fulfillment fees
- variable shipping/handling
- expected returns/refunds and other variable costs
= contribution margin before ads
```

```text
break_even_acos = contribution_margin_before_ads / revenue
ad_contribution_profit = attributed_sales × contribution_margin_rate - spend
```

税费、退款、优惠和品牌归因是否计入，按企业财务口径单列。缺任何关键成本时标 `PROVISIONAL`，不要写“确定盈利”。

## 作用域一致性

每个指标必须绑定：

```text
seller / marketplace / profile / currency / timezone /
ad_product / entity_level / entity_id / date_range /
attribution_window / fetched_at / report_or_endpoint
```

禁止：

- 用 7 天订单配 14 天花费；
- 把广告销售额当作总销售额；
- 把不同广告产品的 attribution window 混在一个 CVR；
- 把 campaign CPC 与单个 search term CVR 拼成分解公式；
- 在汇率未统一时相加多个 marketplace。

## 品牌新客与视频指标

课程列出：

- 品牌新客购买占比；
- 品牌新客购买率；
- 品牌新客单次购买成本；
- 视频完播率；
- 单次完整观看成本。

课程将“品牌新客”描述为过去 12 个月未购买该品牌商品的顾客。执行时以当前报告字段定义、广告产品、归因窗口和资格为准。

## 数据质量检查

- `clicks ≤ impressions`；
- `orders ≤ clicks` 通常成立，但某些订单/购买口径可能一单多件，先确认字段；
- `spend ≈ CPC × clicks`；
- `sales ≈ AOV × orders`；
- `ACOS_decimal × ROAS ≈ 1`；
- placement 或 target 分项之和应与上层总计在报告口径允许误差内一致；
- 归因窗口未成熟时不比较最近日期与完整历史窗口。

任何检查失败都先标 `DATA_QUALITY_WARNING`，再解释原因。
