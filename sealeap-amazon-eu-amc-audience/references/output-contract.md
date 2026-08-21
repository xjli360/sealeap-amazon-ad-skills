# AMC 输出契约

## 1. 对象与权限

```yaml
advertiser_id: <verified-or-NEEDS_DATA>
amc_instance_id: <verified-or-NEEDS_DATA>
ads_profile_id: <verified-or-NEEDS_DATA>
marketplace: <UK|DE|FR|IT|ES|NL|SE|PL|BE|other>
timezone: <value>
currency: <value>
scope_verified: false
authorization: READ_ONLY|DRAFT_ONLY|APPROVED
```

## 2. 业务问题与模型

```text
decision_to_make:
business_question:
selected_model:
why_this_model:
counterfactual_or_comparison:
decision_deadline:
```

## 3. 数据与信源

| 来源 | query/template/report/page | 对象 | 窗口/获取时间 | 覆盖 | 限制 | 标签 |
|---|---|---|---|---|---|---|

使用 `ACCOUNT_FACT`、`CURRENT_POLICY`、`TRAINING_CASE`、`HYPOTHESIS`。

## 4. 查询计划

```yaml
tables_or_template: <current verified names>
campaign_groups: <definitions>
conversion_event: <definition>
lookback_and_attribution: <values>
filters: <marketplace, ASIN, campaign, dates>
dimensions: <minimum necessary>
metrics: <minimum necessary>
privacy_expectation: <threshold/suppression behavior>
result_status: NOT_RUN|RUNNING|READY|SUPPRESSED|FAILED
```

不得在输出中包含用户级标识或可重识别组合。

## 5. 受众定义卡

```yaml
audience_id_or_draft_name: <value>
type: RULE_BASED|LOOKALIKE
include: <events and scope>
exclude: <events and scope>
lookback: <data-derived value>
marketplace: <value>
estimated_size: <value-or-PENDING>
activation_target: SP|SB|SD|DSP|NONE
expiry: <date>
training_case_reference: <PDF page or null>
status: DRAFT|HOLD|READY_FOR_REVIEW|APPROVED
```

## 6. 单变量激活动作卡

```yaml
action_id: AMC-YYYYMMDD-001
scope: <advertiser/instance/profile/campaign>
single_change: <one audience, bid adjustment, exclusion, or status>
current_value: <value>
proposed_value: <value>
evidence: <account result>
baseline_window: <dates>
measurement_window: <dates plus lag>
primary_metric: <metric>
guardrails: <profit, frequency, spend, inventory, privacy>
stop_condition: <condition>
rollback_value: <recorded original>
approval_required: true
```

## 7. 结论

输出 `PROCEED_TO_ANALYSIS`、`PROCEED_TO_REVIEW`、`HOLD` 或 `NO-GO`。结尾明确：

- 哪些是账户事实；
- 哪些是培训案例；
- 哪些当前官方规则仍待核验；
- 是否只有相关性证据；
- 哪些动作等待逐项批准，以及如何回退。
