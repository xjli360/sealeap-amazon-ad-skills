---
name: sealeap-amazon-uk-apparel-ads
description: "Diagnose and plan Amazon UK apparel advertising with UK-specific consumer behavior, seasonality, compliance gates, and ASIN lifecycle playbooks for long-lifecycle, short-lifecycle, and seasonal products. Use for 英国站服饰广告, UK apparel ads, 睡衣/泳衣/外套投放, ASIN 生命周期判断, Black Friday/Boxing Day 节奏, UK/EU 尺码, 品牌推广与视频, 季节性预算日历, 退货率与广告利润, ACOS/ROAS 诊断, 复购再营销, 或根据《亚马逊英国站服饰品类广告运营手册》输出可审批的投放方案. Default to analysis and draft; do not mutate live campaigns without explicit human approval."
---

# SeaLeap 亚马逊英国站服饰广告运营

把英国站服饰 ASIN 的产品类型、生命周期阶段、本地节日、尺码/退货风险和账户真实数据合并成可审核的广告计划。先判断它是长生命周期、短生命周期还是季节性，再按英国站节奏与当前账户证据定义动作。

## 强制边界

- 只将本 Skill 用于 Amazon.co.uk 服饰及与服饰紧密相关的配件。不要把美国站或欧盟站点的尺码、节庆或竞价直接套入。
- 把手册中的市场规模、搜索量、头尾倍数、预算比例、竞价倍数和固定阈值标记为 `MANUAL_BASELINE`，不当作当前账户事实或必达 KPI。
- 将 VAT、UKCA、塑料包装税、促销文案、广告资格和品牌徽章视为时效性高的合规问题。执行前核对当前官方规则；本 Skill 不提供法律结论。
- 优先使用当前账户一方数据：Campaign/Search Term/Targeting/Placement 报告、广告/总销售、利润、库存、退货和 Listing 证据。数据不足时输出 `DRAFT / HOLD`，不编数。
- 把 `store_id`、seller ID、profile ID 和 ASIN 当作业务对象，不当作授权。任何读写都要绑定服务端已验证的店铺和 Ads profile scope。
- 默认只产出草案。调整预算、竞价、placement、target、否定词、状态或广告结构前，逐项展示旧值、新值、证据、影响范围和回退值，并等待人工确认。
- 每张实验卡只改一个主变量。不要同时改 Listing、价格、优惠、库存、竞价和定向后声称因果。

阅读 [references/source-and-guardrails.md](references/source-and-guardrails.md) 获取原 PDF 页码映射、数据口径和高风险阈值说明。

## 工作流

### 1. 锁定投放对象

取得并固定：

- 广告 profile、seller、marketplace=`UK`、ASIN、SKU、父子体和产品类型；
- 上架日、当前销售曲线、历史峰值、旺季节点、在途/可售库存、补货周期与英国天气风险；
- 价格、优惠、星级、评论量、退货原因、VAT/产品合规状态和单件贡献利润；
- 近30/14/7天广告数据，至少按 query/target、match type、placement、ASIN/SKU 拆分；
- 当前 Listing 的主图、标题、五点、UK/EU 尺码表、材质、长度/版型、A+、视频和英国英语本地化。

信息不完时明确列出 `NEEDS_DATA`，继续做有边界的诊断，不用想象补齐。

### 2. 判定生命周期类型与阶段

| 类型 | 判断信号 | 英国站手册案例 | 主要任务 |
|---|---|---|---|
| 长生命周期 | 全年需求稳定，评论和品牌可持续积累 | 女士睡衣 | 新品建面料/版型信任，成熟期扩大规模、防守品牌与激活复购 |
| 短生命周期 | 单峰快速上升后持续衰退，下一季不一定恢复 | 泳衣 | 低成本建关键词历史，旺季放量，高峰后按日历收缩并让新款接力 |
| 季节性 | 每年周期性回升，多年峰值可复利 | 外套 | 旺季前预热，黑五与 Boxing Day 连续放量，淡季防守并唤醒老客 |

阅读 [references/market-and-lifecycle.md](references/market-and-lifecycle.md) 判定英国站消费者特征、Q4 节奏和生命周期边界。不要仅按上架月数硬套阶段；销售趋势、库存、退货和旺季日历必须一起判断。

### 3. 做六层诊断

按“现状 → 证据 → 问题 → 动作 → 验证指标”输出：

1. **合规与可售性**：VAT/适用认证、库存、Buy Box、抑制、价格、促销、配送和资格是否支持放量。
2. **可发现性**：英国英语品类词、功能词、礼品/节日词和商品定向是否匹配真实产品。
3. **点击**：主图、标题前段、价格、评分、视频首帧和本地场景是否建立信任。
4. **转化与退货**：UK/EU 尺码、长度、胸围、版型、材质、透明度、保暖/防水声明和色差是否被如实说清。
5. **利润与增量**：合并 CPC、CVR、ACOS、TACOS、广告/自然/总订单、退货后利润和库存消耗，不以单一 ROAS 下结论。
6. **季节可执行性**：创意审核、入仓、优惠、Black Friday、Boxing Day、天气变化和预算降档是否有明确日历。

### 4. 路由到站点专属打法

- 长生命周期或睡衣/内衣类高信任门槛品：阅读 [references/long-lifecycle.md](references/long-lifecycle.md)。
- 短生命周期、泳衣或款式迭代快的季节品：阅读 [references/short-lifecycle.md](references/short-lifecycle.md)。
- 外套等每年可回升的季节性产品：阅读 [references/seasonal-lifecycle.md](references/seasonal-lifecycle.md)。

先借用最接近案例产生待验证假设，再用当前账户数据确认。不要因为产品也是服饰，就默认它与女士睡衣、泳衣或外套具有同一节奏。

### 5. 生成可审批的广告计划

为每个建议创建独立动作卡，包含：

- 目标 profile / marketplace / campaign / ad group / ASIN / SKU；
- 唯一主动作；
- 基线窗口、归因窗口、样本阈值和数据完整性；
- 旧值、新值和 `MANUAL_BASELINE` 仅作参考的说明；
- 主指标、护栏指标、成功/失败/停止/回退条件；
- 预期费用、退货后利润上限、库存和季节截止日；
- 审批状态：`DRAFT`、`READY_FOR_REVIEW`、`APPROVED`或 `HOLD`。

使用 [references/output-contract.md](references/output-contract.md) 的结构交付。

### 6. 验证与回退

- 把当天价格、优惠、库存、评论变化、天气、竞品事件和节日记为干扰项。
- 在达到预设样本或时间窗口后评估；不要用手册的 `CTR 0.5%`、`ACOS 60-100%`、固定7天或固定点击数替代当前品类和利润判断。
- 如果触发花费、利润、库存、退货或季节截止护栏，按预先记录的回退值处理，并保留审计记录。

## 必须交付的结果

- 对象、数据时间、数据口径、授权和完整性；
- 生命周期类型、阶段和判定证据；
- 英国站消费者意图、尺码/退货风险与季节日历；
- 六层诊断和问题优先级；
- Campaign/Ad Group 结构、关键词/商品定向、placement、创意、再营销与降档草案；
- 手册参考值与账户实际值的明确分离；
- 单变量实验卡、审批项、回退方案和未解决风险。

证据不足时明确输出 `HOLD`；不要把一份 2026 年培训手册写成已验证的当前账户结论。
