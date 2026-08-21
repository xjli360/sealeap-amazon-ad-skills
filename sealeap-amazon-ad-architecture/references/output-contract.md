# 广告架构输出契约

## 1. 对象与授权

```yaml
marketplace: <value>
ads_profile_id: <verified-or-NEEDS_DATA>
seller_id: <verified-or-NEEDS_DATA>
asin_sku_parent_child: <scope>
scope_verified: false
authorization: READ_ONLY|DRAFT_ONLY|APPROVED
```

## 2. 数据覆盖

| 来源 | 报告/页码 | 对象 | 时间/获取时间 | 覆盖 | 限制 | 标签 |
|---|---|---|---|---|---|---|

使用 `ACCOUNT_FACT`、`CURRENT_POLICY`、`TRAINING_CASE`、`HYPOTHESIS`。

## 3. 阶段经营模型

| 阶段 | 日期 | 销量目标 | 利润目标 | 库存/补货 | 最大广告花费 | 日预算上限 | 截止/停止条件 |
|---|---|---:|---:|---|---:|---:|---|

附上 realized revenue、非广告变动成本、退货后贡献利润、break-even CPA/ACOS 的公式和输入来源。

## 4. 关键词/商品优先级

| query/target | 意图/相关性证据 | 当前数据 | 阶段任务 | 可承受 CPC/CPA | 风险 | 状态 |
|---|---|---|---|---:|---|---|

状态使用 `DISCOVER`、`VALIDATE`、`SCALE`、`DEFEND`、`HARVEST`、`STOP`。

## 5. Campaign map

```text
campaign | ad group | ad type | unique role | ASIN/SKU | targeting/match | negative/isolation | budget | bid/placement | entry rule | exit rule
```

没有资格的广告类型写 `NOT_AVAILABLE`。不明确的材料缩写写 `UNRESOLVED`。

## 6. 单变量动作卡

```yaml
action_id: ARCH-YYYYMMDD-001
status: DRAFT
scope: <profile/campaign/ad-group/ASIN/SKU>
single_change: <one budget, bid, target, negative, placement, status, or creative>
current_value: <value>
proposed_value: <value>
account_evidence: <report fact>
training_case_reference: <slide or null>
baseline_window: <dates and samples>
measurement_window: <dates plus attribution lag>
primary_metric: <metric>
guardrails: <profit, spend, inventory, returns, season>
success_condition: <condition>
stop_condition: <condition>
rollback_value: <recorded original>
confounders: <price, coupon, listing, reviews, competitor, season>
approval_required: true
```

## 7. 周复盘

| 周期 | 广告/自然/总销售 | ACOS/TACOS | 退货后利润 | 库存 | query/位置 | 干扰项 | 决策 |
|---|---|---|---|---|---|---|---|

决策只用 `KEEP`、`ITERATE`、`ROLLBACK`、`STOP`。

## 8. 结论

输出 `PROCEED_TO_REVIEW`、`HOLD` 或 `NO-GO`，并明确：

- 哪些数字来自当前账户，哪些只是培训案例；
- 预算是否受利润、库存或季节限制；
- 是否存在自然排名因果不确定性；
- 哪些动作待逐项确认，以及如何回退。
