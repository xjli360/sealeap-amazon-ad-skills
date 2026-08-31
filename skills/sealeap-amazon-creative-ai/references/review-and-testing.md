# 审核与测试

## 审核卡

| 层 | 检查 | 状态 |
|---|---|---|
| FACT | 商品/场景/兼容性/性能均有证据 | PASS/FIX/HOLD |
| FACT | 画面没有增加不存在的部件或结果 | PASS/FIX/HOLD |
| BRAND | 语气、Logo、色彩、受众一致 | PASS/FIX/HOLD |
| BRAND | 与现有素材有清楚且有意义的差异 | PASS/FIX/HOLD |
| POLICY | 当前 marketplace 广告规则已核验 | PASS/FIX/HOLD |
| RIGHTS | 参考资产、人物、音乐、商标可用 | PASS/FIX/HOLD |
| TECH | 尺寸、时长、文件、文字安全区合格 | PASS/FIX/HOLD |

## A/B 测试卡

```text
Hypothesis:
Control asset/version:
Treatment asset/version:
Only changed dimension:
Frozen media settings:
Primary metric:
Guardrails:
Minimum evidence:
Max spend:
Success / stop / inconclusive rules:
Attribution-maturity date:
Approval:
```

若同一时间改变受众、bid、PDP、价格或促销，不把结果归因于素材。异常大额订单需同时报告“含异常值”和“排除敏感性分析”，但不可偷偷删除。

## 复盘格式

- 生产效率：工时、外包/工具成本、版本数、审核返工；
- 媒体表现：绝对量、比率、花费、销售/利润、样本量；
- 干扰项：价格、促销、库存、位置、受众和竞品；
- 结论：`WINNER / LOSER / INCONCLUSIVE / POLICY_HOLD`；
- 下一步：只推进一个新变量。
