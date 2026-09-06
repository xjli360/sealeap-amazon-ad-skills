# 商品投放交付合同

## 1. 结论卡

```text
mode / status / marketplace / profile / advertised_ASIN-SKU /
ad_product / primary_use_case / date_range / attribution_window /
evidence_grade / budget_cap / top_blocker
```

## 2. 商品事实与 3WCS

| 维度 | 结论 | 证据 ID | 限制 |
|---|---|---|---|
| What | | | |
| Who | | | |
| Where | | | |
| Competitor | | | |
| Substitute/Complement | | | |

## 3. 当前三轨流量地图

| 轨道 | Campaign/Ad Group | 流量类型 | Impressions | Clicks | Spend | Orders | Sales | Profit | 诊断 |
|---|---|---|---:|---:|---:|---:|---:|---:|---|

## 4. 候选池

| Candidate | ASIN/Category | Relationship | Source | Relevance | Competitiveness | Account signal | Economics | Tier | Risk |
|---|---|---|---|---|---|---|---|---|---|

## 5. 定向草案

分别列 ASIN、品类、细化、expanded 与 negative targeting。每行包含当前资格核验、目标、campaign/ad group、bid 原则、预算、证据和状态。

## 6. 联动与去重台账

列发现来源、关键词/ASIN、目的地、源活动动作、去重规则与日期。不经证据不自动否定源活动。

## 7. 单变量实验卡

```text
experiment_id / use_case / campaign / unique_ad_group /
one_variable / target / relationship / evidence_ids /
baseline / old_value / new_value / frozen_variables /
budget_cap / attribution_wait / success / guardrail / stop / rollback /
approval_status
```

## 8. 审批与复读

只列本轮一个待确认动作；记录确认人/时间、请求 ID、复读结果和回退状态。

## 9. 最终状态

- `DRAFT`：候选或实验草案；
- `READY_FOR_REVIEW`：证据、资格、经济性、护栏和回退齐全；
- `APPROVED`：用户本轮已批准当前动作；
- `HOLD`：授权、相关性、经济性、资格或样本不足。
