---
name: sealeap-amazon-fashion-category-growth
description: Research and plan Amazon fashion-category growth across the US, Europe, and Japan using trend validation, marketplace-specific selection, brand/store/content tools, promotion economics, inventory routing, and return-reduction gates. Use for 时尚品类选品, 美欧日服饰趋势, fashion opportunity scan, 女装男装童装鞋靴箱包珠宝, 品牌旗舰店与帖子, 促销组合, AWD/FBA库存, 尺码退货, or converting the authorized 2025 fashion guide into a current evidence plan. Route lifecycle campaign execution to the apparel-ads Skills; treat all 2025 trends, product lists, tools, and case figures as snapshots until currently verified.
---

# Amazon 时尚品类增长

## 目标

将时尚手册中的趋势与商品清单变成验证队列，而不是“热卖推荐”：先用当前站点需求和竞争证据筛选，再检查差异化、合规、利润、库存与退货，最后才进入 Listing、品牌、促销和广告实验。

先读 [references/source-and-guardrails.md](references/source-and-guardrails.md) 和 [references/source-map.md](references/source-map.md)。做机会筛选与品牌增长读 [references/opportunity-and-brand.md](references/opportunity-and-brand.md)；做库存与退货读 [references/inventory-and-returns.md](references/inventory-and-returns.md)。

## 与其它 Skill 的分工

- 本 Skill：类目趋势、选品验证、品牌/促销、库存和退货系统；
- `sealeap-amazon-apparel-lifecycle-ads`：美国服饰广告生命周期；
- `sealeap-amazon-jp-apparel-ads`、`...-uk-...`、`...-ca-...`：站点广告打法；
- `sealeap-amazon-localization-marketing`：具体字段与素材本地化。

## 工作流

### 1. 固定站点与细分类目

记录 marketplace、product type、性别/年龄、服装/鞋/箱包/珠宝、季节、目标价带和上新时间。不能把美国、欧洲和日本趋势混成一个全球需求。

### 2. 从源候选建立验证队列

手册的 2025 色彩、面料、廓形、场景和推荐品仅标 `SOURCE_CANDIDATE`。对每个候选补齐当前搜索需求、销量/点击代理、竞争、评价门槛、退货主题、季节窗口和来源日期。

### 3. 产品可行性闸门

检查事实/材质、尺码体系、版型一致性、色差、标签、目标站点法规、知识产权、供应商能力、MOQ、交期、变体复杂度、落地成本、贡献毛利、退货敏感性和库存风险。任一硬闸门失败即 `REJECT`。

### 4. 建立本地商品表达

用当前目标站点搜索词和评价重建标题、属性、尺码表、图片/视频和使用场景。模特信息、颜色/面料特写、包容性和穿搭灵感都必须与实物一致。

### 5. 规划品牌与内容

只有完成 Brand Registry/当前资格核验后，才考虑品牌店、帖子、品牌受众优惠或 AI 内容工具。选择一个目的：建立信任、帮助搭配、解释面料/版型、交叉销售或复购；不要为了使用工具而创建内容。

### 6. 计算促销

核验当前 Deal/Coupon 规则、参考价、费用、库存和毛利。爆品集中、折扣深度、本地活动和品类活动的课程结果是历史调查，不是促销配方。

### 7. 设计库存与退货方案

按旺季/常青、多变体、FBA/AWD/其它当前可用履约方式建情景；用退货原因反推尺码、颜色、材质、图片和质量改进。库存清理动作先算回收价值与品牌影响。

### 8. 输出一个验证实验

只验证一个核心假设，例如某本地趋势、尺码表达、面料特写、搭配图或促销结构。固定价格/流量等主要变量，设置成功/停止线和回退。

## 必须交付

- 站点/细分类目/季节作用域；
- `SOURCE_CANDIDATE → CURRENT_EVIDENCE → DECISION` 队列；
- 合规、利润、供应链、库存和退货闸门；
- 品牌/内容/促销草案；
- 一个实验和 `GO / HOLD / REJECT` 状态。
