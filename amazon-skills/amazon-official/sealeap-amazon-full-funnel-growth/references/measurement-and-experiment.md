# 衡量与实验

## 指标字典

- `reach`：去重触达；必须说明可去重范围。
- `frequency`：曝光/去重触达；高频不是自动浪费，要结合后续行为。
- `NTB`：品牌新客；使用当前平台定义与回看窗口。
- `incremental sales/orders`：相对可信对照的新增，而非归因报表总量。
- `contribution profit`：收入扣除商品、平台、履约、折扣、退货及广告等可变成本。
- `brand search lift`：品牌搜索变化；需控制季节、促销、价格和其它媒体。
- `path overlap`：多触点组合的关联；除非实验支持，不写因果。

## 单变量实验卡

```text
Decision:
Scope: marketplace / profile / audience / ASIN / dates
Evidence:
Hypothesis:
Primary variable:
Control/frozen variables:
Primary metric:
Guardrails:
Minimum evidence:
Max spend:
Success line:
Stop line:
Attribution-maturity date:
Rollback:
Approval status:
```

## 合格实验顺序

1. 确认库存、价格、配送与页面稳定；
2. 选择一个最大漏损和一个可变因素；
3. 优先使用平台实验、地理/人群对照或时间交错；
4. 预先登记主指标、护栏和停止线；
5. 等待归因成熟，并同时报告绝对值、比例和样本量；
6. 若有促销、库存或竞品冲击，降级为 `INCONCLUSIVE`。

最后点击、归因路径和前后对比都可用于发现问题，但都不能单独证明增量。
