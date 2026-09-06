# ACOS 诊断树

## 0. 策略闸门

```text
ACOS 变化
→ 是否影响本轮主目标？
  ├─ 否：记录并监控，不为优化而优化
  └─ 是：进入经济性与分解
```

测试、守位、品牌获客、推排名和成熟品利润需要不同成功指标。没有主目标时，任何“高/低”判断都不完整。

## 1. 经济性闸门

```text
ACOS vs break-even ACOS
TACOS 与总贡献利润
库存与现金约束
增量/自然替代风险
```

ACOS 低于盈亏线：广告归因口径可能盈利，但不证明增量盈利。

ACOS 高于盈亏线：成熟品利润目标通常需处理；新品验证、守位或品牌获客可能短期容忍，但必须有预算上限和后续价值证据。

## 2. 数学分解

```text
ACOS = CPC / (CVR × AOV)
```

比较两个时期时，建议分别报告 CPC、CVR 和 AOV 的变化，不用单一 ACOS 掩盖抵消关系。若要做贡献归因，可用对数变化或逐项替换，但必须说明顺序效应。

## 3. 曝光与流量资格

曝光低先检查：

- Campaign/Ad Group/Ad 状态与审核；
- 预算耗尽、bid 与竞价资格；
- 库存、Featured Offer、可售与配送；
- 定向范围和搜索需求；
- 日期、季节与报告延迟。

曝光正常不等于预算和竞价没有问题；只表示需要继续下钻。

## 4. CTR 断点

切分：placement、target/search term、match type、advertised ASIN、日期、创意版本。

可能解释：

- 查询或 ASIN 不相关；
- 主图/视频/标题前段不清楚；
- 价格、优惠、评分、配送或品牌弱；
- 广告位竞争环境不同；
- 商品卡与用户意图不匹配。

需要排除的证据：前台快照、竞品同口径、页面事件、placement 报告和查询分组。

## 5. CPC 断点

可能解释：bid、动态竞价、placement 加价、竞争期、热门目标、预算迁移或广告产品组合。

判断顺序：

1. 对比账户自身历史与当前 placement/target；
2. 再看当前可用 Benchmark；
3. 结合 CVR、AOV 和贡献利润计算点击价值；
4. 只对根因对应对象设计动作。

低于同业 CPC 不自动代表好；可能同时拿不到有效位置或流量。

## 6. CVR 断点

先排流量，再排页面：

```text
search term / target relevance
→ advertised ASIN 与变体
→ price / coupon / Featured Offer / delivery
→ rating / reviews / returns
→ main image / title / bullets / A+ / video
→ mobile and desktop rendering
```

用查询属性聚合，而不是根据 1–2 次点击的单词偶然值下结论。固定“点击 N 次无单就否定”不是通用规则。

## 7. AOV 与组合断点

检查折扣、低价子体、捆绑、跨 ASIN 归因、件单价与订单金额变化。提升 AOV 的动作可能降低 CVR 或增加退货，必须重新算贡献利润。

## 8. 从根因到实验

优先级：

1. 授权、可售、库存、数据质量；
2. 明显不相关流量；
3. Listing/价格/配送等 CVR 根因；
4. bid/placement/预算效率；
5. 扩量、品牌或组合优化。

一轮只改一个主变量，并冻结其它可能影响 CTR/CVR/CPC 的动作。
