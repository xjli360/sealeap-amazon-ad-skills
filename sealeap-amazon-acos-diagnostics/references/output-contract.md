# ACOS 诊断交付合同

## 1. 结论卡

```text
mode / status / primary_objective / marketplace / profile /
entity_level-id / date_range / attribution_window / currency /
data_maturity / break_even_status / top_driver / top_blocker
```

## 2. 数据质量与口径

列出原始字段、来源、更新时间、归因窗口、缺失值和一致性检查。任何无法回算的上报指标都标 `DATA_QUALITY_WARNING`。

## 3. 指标重算

| 指标 | 原始/上报 | 重算 | 口径 | Benchmark | 判断 |
|---|---:|---:|---|---:|---|
| Impressions | | | | | |
| Clicks / CTR | | | | | |
| Spend / CPC / CPM | | | | | |
| Orders / CVR / CPA | | | | | |
| Ad sales / AOV | | | | | |
| ACOS / ROAS | | | | | |
| Total sales / TACOS | | | | | |

## 4. 经济性

列贡献成本、break-even ACOS、广告归因贡献利润、总贡献利润、库存和现金护栏。缺数据时给公式和 `NEEDS_DATA`，不伪造结果。

## 5. 诊断链

| 观察 | 数学驱动 | 下钻维度 | 可能解释 | 排除证据 | 置信度 |
|---|---|---|---|---|---|

覆盖 CPC、CVR、AOV、placement、target/search term、advertised ASIN、Listing/价格/评价/配送和时间事件。

## 6. Benchmark

记录同业组、分位数、指标定义、日期、覆盖和当前资格。Benchmark 只支持方向判断。

## 7. 单变量实验卡

```text
experiment_id / strategic_objective / campaign / unique_ad_group /
one_variable / evidence / baseline / old_value / new_value /
frozen_variables / budget_cap / sample_requirement / attribution_wait /
success / guardrail / stop / rollback / approval_status
```

## 8. 审批与复读

只列本轮一个待确认动作。记录确认、请求/operation ID、复读时间、实际状态和回退。

## 9. 最终状态

- `DRAFT`：只读诊断或实验草案；
- `READY_FOR_REVIEW`：证据、范围、护栏、回退完整；
- `APPROVED`：用户本轮已批准当前动作；
- `HOLD`：授权、口径、经济性或数据质量不足。
