---
name: sealeap-amazon-product-targeting
description: Research, diagnose, and draft Amazon Ads ASIN and category product-targeting plans that complement keyword targeting, including audience expansion, competitor and category traffic, cross-sell, upsell, self-defense, negative targeting, placement analysis, and single-variable experiments. Use for 商品投放, ASIN 定向, 品类定向, Product Targeting, 关键词引流遇到瓶颈, 关联流量, 互补品/替代品, 竞品详情页抢流量, 自家 ASIN 防御, Best Sellers/New Releases 候选, 自动与手动广告联动, or the local file named 如何提升关键词引流效率. Default to research and draft; verify current marketplace capabilities and never mutate live campaigns without explicit human approval.
---

# Amazon Ads 商品投放 · ASIN/品类定向与关键词联动

## 目标

把商品投放从“找一批竞品 ASIN 去打”升级为一条可复核的流量设计链：先还原商品与消费者任务，再识别关键词覆盖不到的商品页、类目节点、互补/替代和自家详情页流量，形成候选池，最后用独立 Campaign/Ad Group 做单变量验证。

源文件名与实际内容不一致：文件名是《如何提升关键词引流效率？》，但 39 页课件实际标题和正文均为《商品投放实用案例分享》。本 Skill 以实际内容为准，并保留关键词与商品投放联动部分。先读 [references/source-and-guardrails.md](references/source-and-guardrails.md)。

## 不可妥协的边界

- 商品投放包括课程中的品类定向和 ASIN 定向；“扩展商品投放”、细化条件、否定能力、广告位和支持广告产品均以当前 marketplace 控制台/API 为准。
- 课件中标为“第三方卖家意见”的 3WCS、榜单分级、欧洲站贴标签、日本站反查词和阻力带案例只能作为 `SELLER_HYPOTHESIS`，不能写成 Amazon 官方机制。
- 不声称商品投放会让系统“收录关键词”、增加自然排名或给 ASIN 贴上确定标签。只观察可测的曝光、点击、订单、流量位置和利润变化。
- 不因为竞品是 FBM、自家是 FBA 就认定一定更有竞争力；必须比较当前价格、配送承诺、评分、评价量、变体、优惠和商品匹配。
- 不复制竞品文案、素材、商标表达或虚构比较优势；只使用公开商品事实与合法定向能力。
- `store_id`、profile、ASIN 或 marketplace 不等于授权。读取与写入都必须绑定当前验证的服务端账户范围。
- 不使用固定“点击 N 次无单”否定阈值。按利润、流量、归因窗口和统计证据定义停止规则。
- 默认只读和草案。任何 target、negative target、bid、budget、placement、status 或结构变更必须逐项人工确认。

## 先声明模式

1. `RESEARCH`：只读构建流量地图与候选池；默认；
2. `DIAGNOSE`：诊断现有商品投放；
3. `DRAFT`：生成分层结构与单变量实验；
4. `RELEASE_PREP`：生成审批卡、旧值/新值、护栏和回退；
5. `APPROVED_WRITE`：只执行用户本轮明确批准的一个动作，写后复读。

## 核心工作流

### 1. 锁定对象、目标和基线

记录：

- 已验证 seller、marketplace、广告 profile、广告产品、ASIN/SKU 与父子体；
- 目标只能选一个：`扩大覆盖 / 突破关键词瓶颈 / 类目节点 / 细分人群 / 交叉销售 / 升级销售 / 自家防御 / 竞品进攻`；
- 当前关键词、自动和商品投放结构及近 7/14/30 天表现；
- 贡献毛利、盈亏线、库存、Featured Offer、价格/优惠、评价与配送；
- 基线窗口、归因窗口、当前变更和季节事件。

缺少明确目标时先输出 `NEEDS_DATA`，不要把七种场景全部混在一个 Campaign。

### 2. 建立商品事实与 3WCS 假设表

用 [references/use-cases-and-selection.md](references/use-cases-and-selection.md) 建立：

```text
What: 商品身份、功能、特性、材质、颜色、尺寸、售卖方式
Who: 真实购买对象与购买任务
Where: 使用场景
Competitor: 同需求、同价格带、可替代的竞品
Substitute: 关联、互补或替代商品
```

3WCS 来自第三方卖家观点。每一项都要绑定商品事实、账户查询或市场观察证据；不能凭想象填人群与场景。

### 3. 还原当前流量结构

至少获取：

- Campaign / Ad Group / Targeting / Search Term / Placement 报告；
- advertised product 与 purchased product 维度；
- 当前自动投放、手动关键词、手动商品投放及 negative targeting；
- 搜索结果与详情页的当前可见广告/自然位置观察；
- Brand Analytics、Search Query Performance 或账户可用的一方查询证据；
- 当前 Best Sellers / New Releases、类目节点与候选 ASIN 前台事实。

按 `搜索流量 / 商品详情页 / 类目节点 / 互补 / 替代 / 自家 / 竞品` 聚合曝光、点击、花费、订单、销售和贡献利润。不要把单个低样本 ASIN 当成稳定规律。

### 4. 选择一个应用场景

课件给出七种商品投放场景：扩大覆盖、绕开关键词瓶颈、类目节点、细分人群、交叉/升级销售、自家防御、竞品进攻。具体选择器见 [references/use-cases-and-selection.md](references/use-cases-and-selection.md)。

一轮只选择一个主场景。若同时存在防御和进攻需求，拆成不同 Campaign、预算和实验卡。

### 5. 建立候选 ASIN/品类池

候选来源可以包括：

- 已有自动或商品投放中真实出单/高质量点击的 ASIN；
- purchased product 与 search term 关联出的商品；
- 当前类目、榜单和新品榜中的相关 ASIN；
- 自家变体、配件、升级款与互补商品；
- 高自然排名目标的公开观察；
- 关键词流量研究中的互补/替代主题。

每个候选记录：

```text
candidate / source / relationship / customer_task / relevance /
price_delivery_rating_gap / observed_traffic / account_performance /
profit_ceiling / risk / evidence_ids / freshness
```

候选分为：

- `TIER_1_TESTABLE`：相关、可竞争、有账户或市场证据；
- `TIER_2_EXPLORE`：相关但数据不足，只能小预算探索；
- `EXCLUDE`：不相关、明显不可竞争、无流量或合规风险。

### 6. 设计品类与 ASIN 定向

#### 品类定向

- 只使用当前控制台实际提供的品牌、价格、评分、配送或其它细化条件；
- 记录细化前后覆盖范围，避免“精准”到没有曝光；
- 类目节点必须与商品任务相关，不能只因流量大就投。

#### ASIN 定向

- 自家防御、竞品进攻、互补、替代与升级分别建组；
- 拆开强竞品、可竞争竞品与探索候选；
- “扩展商品投放”若当前可用，单独建组并标明系统可能扩展到替代/互补商品；
- 搜索结果页曝光位置是竞价与系统匹配结果，不作展示保证。

### 7. 与关键词和自动投放联动

读取 [references/keyword-product-linkage.md](references/keyword-product-linkage.md)，采用三轨结构：

```text
自动投放：发现查询与 ASIN，验证基础关联
手动关键词：精细控制搜索意图、排名与品牌防御
手动商品投放：覆盖详情页、类目、互补/替代、进攻与防御
```

迁移规则：

1. 从自动/历史报告发现候选；
2. 验证商品与消费者任务相关性；
3. 候选 ASIN 单独进入手动商品投放；
4. 对候选 ASIN 反查到的词仍需一方查询/账户数据验证后才进入手动关键词；
5. 不在原活动立即否定，除非存在明确重复竞价问题且有证据；
6. 保留源、目的、日期与去重策略。

### 8. 否定与清理

先按当前广告产品确认支持的否定类型。候选否定必须有：

- 不相关商品事实；或
- 可复核的长期低质量流量与足够样本；或
- 明显不可竞争且不符合实验目的；或
- 品牌/商品合规风险。

将“否定整个品牌”和“否定单个 ASIN”分开评估。若同品牌仍有相关、可竞争的商品，不做整品牌否定。

### 9. 生成单变量实验卡

一张卡只允许一个 `store + campaign + unique ad group + main variable`，并写：

- 主场景、候选与关系类型；
- 来源和证据 ID；
- 当前基线与唯一动作的新旧值；
- 预算上限、bid/placement 护栏；
- 冻结的关键词、Listing、价格、优惠和其它 target；
- 成功、停止、回退和归因等待；
- 人工确认状态。

可以运行：

```bash
python3 scripts/targeting_plan_check.py --input references/targeting-plan.example.json
```

脚本只做静态结构校验，不验证 ASIN 存在性、实时资格或经济性。

### 10. 审批与写后验证

进入 `RELEASE_PREP` 后展示 profile、campaign、ad group、target/negative target、旧值、新值、最大花费、证据和回退。只有用户本轮明确批准后执行。

写后复读目标状态与控制台结果；请求接受不等于已经开始稳定投放。

## 必须交付

按 [references/output-contract.md](references/output-contract.md) 输出：

- 授权、口径、商品事实和当前三轨流量地图；
- 单一应用场景和候选池证据；
- ASIN/品类/细化/否定草案；
- 自动、关键词与商品投放的迁移/去重关系；
- 单变量实验、花费护栏、回退和审批对象；
- `DRAFT`、`READY_FOR_REVIEW`、`APPROVED` 或 `HOLD`。
