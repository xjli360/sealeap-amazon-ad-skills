# 英国站服饰广告输出契约

所有输出都使用当前账户证据，并把手册参考值标成 `MANUAL_BASELINE`。未取得生产写入授权时，只能输出草案。

## 目录

1. 对象与授权
2. 数据与信源
3. 生命周期判定
4. 六层诊断
5. 广告结构草案
6. 单变量动作卡
7. 季节执行日历
8. 结论格式

## 1. 对象与授权

```yaml
marketplace: UK
seller_id: <known-or-NEEDS_DATA>
ads_profile_id: <verified-or-NEEDS_DATA>
store_scope_verified: false
asin: <ASIN>
sku: <SKU-or-NEEDS_DATA>
parent_child_scope: <scope>
authorization: DRAFT_ONLY
```

## 2. 数据与信源

| 信源 | 报告/页码 | 对象 | 时间窗口/获取时间 | 覆盖度 | 限制 |
|---|---|---|---|---|---|
| Amazon Ads | Search Term | query/ASIN | YYYY-MM-DD..YYYY-MM-DD | x% | attribution lag |
| Seller Central | orders/returns | SKU | 同期 | x% | return lag |
| 手册 | PDF p.xx | case | 2026 manual | descriptive | not current account fact |

列出缺失的库存、利润、退货、自然单、Listing 或合规证据，并标记 `NEEDS_DATA`。

## 3. 生命周期判定

```text
type: LONG | SHORT | SEASONAL | UNCERTAIN
stage: NEW | GROWTH | MATURE | EXIT | UNCERTAIN
evidence: sales slope + annual pattern + listing age + inventory + returns + weather/calendar
counter_evidence: ...
confidence: LOW | MEDIUM | HIGH
```

## 4. 六层诊断

按优先级逐项写：

| 层级 | 现状证据 | 问题 | 单一建议 | 验证指标 | 状态 |
|---|---|---|---|---|---|
| 合规与可售性 |  |  |  |  | HOLD/DRAFT |
| 可发现性 |  |  |  |  |  |
| 点击 |  |  |  |  |  |
| 转化与退货 |  |  |  |  |  |
| 利润与增量 |  |  |  |  |  |
| 季节可执行性 |  |  |  |  |  |

必须说明 UK/EU 尺码、材质/功效证据、退货原因、天气、促销与旺季截止日。KOC/站外营销单列，不与 PPC 归因混合。

## 5. 广告结构草案

```text
campaign/ad group | ad type | intent | match/target | ASIN/SKU | current value | proposed value | evidence | exclusions
```

分别列品牌词、非品牌核心词、功能/版型长尾、商品定向、placement、创意、再营销和季节降档。没有 SB/SBV/SD 资格时标记 `NOT_AVAILABLE`。

## 6. 单变量动作卡

```yaml
action_id: UK-YYYYMMDD-001
status: DRAFT
scope:
  profile_id: <verified-id>
  marketplace: UK
  campaign_id: <id>
  ad_group_id: <id-or-null>
  asin_sku: <value>
single_change: <only one primary variable>
baseline:
  window: <dates>
  samples: <clicks/orders/spend>
  current_value: <value>
proposal:
  new_value: <value>
  manual_baseline: <reference-or-null>
reason: <account evidence>
primary_metric: <metric>
guardrails:
  break_even_acos_or_cpa: <value-or-NEEDS_DATA>
  return_adjusted_profit: <rule>
  inventory: <rule>
  spend: <rule>
  seasonal_deadline: <date-or-NEEDS_DATA>
decision:
  success: <condition>
  stop: <condition>
  rollback_value: <recorded original>
confounders: [price, coupon, reviews, weather, competitor, delivery]
approval_required: true
```

不要用手册阈值自动填充 `success` 或 `stop`。若利润、授权、库存、合规或数据样本不足，将状态设为 `HOLD`。

## 7. 季节执行日历

| 截止日 | 依赖 | 动作草案 | 审批人 | 停止条件 | 回退 |
|---|---|---|---|---|---|

将素材审核、入仓、尺码齐全、促销资格、Black Friday、Boxing Day、天气复核和旺季降档分开列出。

## 8. 结论格式

先给出 `PROCEED_TO_REVIEW`、`HOLD` 或 `NO-GO`，再列最多三个高优先级动作。结尾必须包含：

- 哪些是当前账户事实；
- 哪些只是 `MANUAL_BASELINE`；
- 哪些仍需当前官方规则核验；
- 哪些动作等待人工逐项确认；
- 如何回退和何时复盘。
