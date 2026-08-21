# 加拿大站服饰广告交付合同

## 1. 结论卡

```text
mode / status / marketplace / profile / ASIN-SKU / parent-child /
ASIN_LIFECYCLE / SEASON_WINDOW / primary_objective /
data_window / attribution_window / evidence_grade / top_blocker
```

## 2. 证据范围

列出账户、商品、课程与假设证据，分别写 `source / scope / fetched_at / coverage / limitations`。课程数字必须标 `COURSE_BASELINE`。

## 3. 双时间轴与适配判断

说明生命周期阶段、季节窗口、判定证据、备选解释，以及是否适配 Coat 或 Underpants 完整打法。

## 4. 五层诊断

| 层级 | 观察 | 证据 | 排除项 | 结论 | 优先动作 |
|---|---|---|---|---|---|
| 可售/库存 | | | | | |
| 流量与语言 | | | | | |
| 点击 | | | | | |
| 转化/退货 | | | | | |
| 利润/增量 | | | | | |

## 5. 课程基线与账户草案

并排给出：

| 广告类型 | COURSE_BASELINE | ACCOUNT_ACTUAL | DRAFT | 差异原因 |
|---|---:|---:|---:|---|

所有预算列必须合计 100%，并单列总预算、币种和最大日花费。

## 6. 流量结构

分别列英文/法语、品牌/类目/属性/场景/竞品、自家防御、自动探索、浏览再营销和历史购买复购。每项包含目标、证据、匹配/定向、排除项、预算、bid/placement 原则和状态。

## 7. 页面与创意承接

| 购买问题 | 商品事实 | 页面证据 | 创意任务 | 合规风险 | 状态 |
|---|---|---|---|---|---|

## 8. 单变量实验卡

```text
experiment_id / campaign / unique_ad_group / one_variable /
baseline / action_old_new / frozen_variables / budget_cap /
observation_requirement / attribution_wait / success / stop / rollback /
owner / approval_status
```

## 9. 审批与执行记录

只列本轮可批准的单一动作。记录确认人、确认时间、请求 ID、复读结果和回退状态。

## 10. 最终状态

- `DRAFT`：有方向但不可执行；
- `READY_FOR_REVIEW`：证据、范围、护栏与回退齐全，等待确认；
- `APPROVED`：用户已明确批准当前对象与动作；
- `HOLD`：授权、数据、商品事实、利润或库存不满足。
