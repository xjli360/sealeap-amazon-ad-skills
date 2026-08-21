---
name: sealeap-amazon-jp-apparel-ads
description: "Diagnose and plan Amazon Japan apparel advertising with Japan-specific consumer behavior, seasonality, and ASIN lifecycle playbooks for long-lifecycle, short-lifecycle, and seasonal products. Use for 日本站服饰广告, JP apparel ads, 背包/内衣/泳装投放, ASIN 生命周期判断, 日本站新品冷启动, 品牌推广启动时机, Amazon Points, 日文功能词, 季节性备货与预热, 广告预算结构, ACOS/ROAS 诊断, 复购再营销, 或根据《亚马逊日本站服饰品类广告运营手册》输出可审批的投放方案. Default to analysis and draft; do not mutate live campaigns without explicit human approval."
---

# SeaLeap 亚马逊日本站服饰广告运营

把日本站服饰 ASIN 的产品类型、生命周期阶段、季节节点、消费者意图和账户真实数据合并成可审核的广告计划。先诊断，再选择日本站打法；不要把美国站或英国站的节奏直接套入日本站。

## 强制边界

- 只将本 Skill 用于 Amazon.co.jp 服饰及与服饰紧密相关的配件。跨站点需求必须重新验证关键词、季节和消费者意图。
- 把手册中的百分比、倍数、预算结构和竞价建议标记为 `MANUAL_BASELINE`，不当作当前账户的事实或必达 KPI。
- 优先使用当前账户一方数据：Campaign/Search Term/Targeting/Placement 报告、广告销售、总销售、利润、库存、退货和 Listing 证据。缺数据时输出 `DRAFT / HOLD`，不编数。
- 把 `store_id`、seller ID、profile ID 或 ASIN 当作业务对象，不当作授权。任何真实读写都要绑定服务端已验证的店铺与广告 profile scope。
- 默认只产出草案。调整预算、竞价、placement、target、否定词、状态或广告结构前，逐项展示旧值、新值、证据、影响范围和回退值，并等待人工确认。
- 每张实验卡只改一个主变量。不要同时改 Listing、价格、优惠、库存、竞价和定向后声称因果。

查看 [references/source-and-guardrails.md](references/source-and-guardrails.md) 获取原 PDF 页码映射、数据口径和不可直接执行的阈值说明。

## 工作流

### 1. 锁定投放对象

取得并固定：

- 广告 profile、seller、marketplace=`JP`、ASIN、SKU、父子体和产品类型；
- 上架日、当前销售曲线、历史峰值、季节节点、在途/可售库存和补货周期；
- 价格、优惠、Amazon Points 当前设置、星级、评论量、退货原因和单件贡献利润；
- 近30/14/7天广告数据，至少按 query/target、match type、placement、ASIN/SKU 拆分；
- 当前 Listing 的主图、标题、五点、尺码表、A+、日文本地化和功能性声明证据。

信息不完时明确列出 `NEEDS_DATA`，继续做有边界的诊断，不用想象补齐。

### 2. 判定生命周期类型与阶段

先根据真实销售曲线判定，再用手册案例类比：

| 类型 | 判断信号 | 日本站手册案例 | 主要任务 |
|---|---|---|---|
| 长生命周期 | 全年需求相对稳定，靠评论与品牌长期累积 | 背包 | 新品建信任，成长期放大规模，成熟期守阵地与再营销 |
| 短生命周期 | 快速起量后进入不可逆衰退，产品迭代快 | 内裤 | 新品用功能精准词起量，成长期建品牌，成熟期激活复购并让新款接力 |
| 季节性 | 需求集中在明确月份，错过窗口难以补救 | 泳装 | 旺季前抢排名和视觉信任，爬坡期放量，高峰期收割并累积品牌 |

阅读 [references/market-and-lifecycle.md](references/market-and-lifecycle.md) 判定日本站消费者特征、全年节奏和生命周期边界。不要仅按上架月数硬套阶段；销售趋势、需求节点和库存风险必须一起判断。

### 3. 做五层诊断

按“现状 → 证据 → 问题 → 动作 → 验证指标”输出：

1. **可售性**：库存、Buy Box、抑制、价格、配送、资格和季节备货是否支持放量。
2. **可发现性**：日文品类词、功能词、场景词和商品定向是否匹配真实产品。
3. **点击**：搜索结果中主图、标题前段、价格/积分、评分和视频首帧是否建立当地化信任。
4. **转化与退货**：尺码、材质、功能、做工、使用场景和限制是否在 Listing 中被如实说清。
5. **利润与增量**：把 CPC、CVR、ACOS、TACOS、广告/自然/总订单、退货后贡献利润和库存消耗合并判断，不以单一 ROAS 下结论。

### 4. 路由到站点专属打法

- 长生命周期或高信任门槛产品：阅读 [references/long-lifecycle.md](references/long-lifecycle.md)。
- 短生命周期、高频消耗或款式迭代产品：阅读 [references/short-lifecycle.md](references/short-lifecycle.md)。
- 需求高度集中在旺季的产品：阅读 [references/seasonal-lifecycle.md](references/seasonal-lifecycle.md)。

先借用最接近的案例生成“假设”，再用当前账户数据验证。不要因为产品也是服饰，就默认它与背包、内裤或泳装具有同一节奏。

### 5. 生成可审批的广告计划

为每个建议创建独立动作卡，包含：

- 目标 profile / marketplace / campaign / ad group / ASIN / SKU；
- 唯一主动作；
- 基线窗口、归因窗口、样本阈值和数据完整性；
- 旧值、新值和 `MANUAL_BASELINE` 仅作参考的说明；
- 主指标、护栏指标、成功/失败/停止/回退条件；
- 预期费用与退货后利润上限；
- 审批状态：`DRAFT`、`READY_FOR_REVIEW`、`APPROVED`或 `HOLD`。

使用 [references/output-contract.md](references/output-contract.md) 的结构交付。

### 6. 验证与回退

- 把当天的价格、优惠、积分、库存、评论变化、竞品事件和季节事件记为干扰项。
- 在达到预设样本或时间窗口后评估；不要用统一的7天或固定点击数替代品类和利润判断。
- 如果触发花费、利润、库存或转化护栏，按预先记录的回退值处理，并保留审计记录。

## 必须交付的结果

- 对象、数据时间、数据口径和完整性；
- 生命周期类型、阶段和判定证据；
- 日本站消费者意图与季节节点；
- 五层诊断与问题优先级；
- Campaign/Ad Group 结构、关键词/商品定向、placement、创意和再营销草案；
- 手册参考值与账户实际值的明确分离；
- 单变量实验卡、审批项、回退方案和未解决风险。

证据不足时明确输出 `HOLD`；不要把一份 2026 年培训手册写成已验证的当前账户结论。
