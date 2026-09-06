---
name: sealeap-amazon-ca-apparel-ads
description: Diagnose and draft Amazon Canada apparel advertising plans with lifecycle and seasonal timing, English/French search coverage, account evidence, profitability guardrails, and approval-ready experiments. Use for 加拿大站服饰广告, Amazon.ca Coat 外套夹克, Underpants 内衣文胸, 季节性长生命周期, 长生命周期, 新品期成长期成熟期, 广告预算配比, SP/SB/SBV/SD/商品投放, 法语关键词, 旺季预热, 复购再营销, CPC/ROAS/ACOS 异常, or when converting the authorized course material into an account-specific plan. Default to diagnosis and draft; never write live advertising changes without explicit human approval.
---

# 亚马逊加拿大站服饰广告 · 生命周期与季节节奏

## 目标

把加拿大站服饰广告从“照搬美国站”改成一条可复核的决策链：先同时判断 ASIN 生命周期与当年季节窗口，再核对消费者顾虑、英法语流量、利润和库存，最后生成分阶段广告结构与单变量实验草案。

本 Skill 的课程证据只详细覆盖两类产品：

- `Coat`：季节性长生命周期，课程核心是提前布局、旺季加码、旺季后释放积累；
- `Underpants`：长生命周期，课程核心是先建立合身/舒适/材质信任，再用品牌与再营销形成规模复利。

先读 [references/source-and-guardrails.md](references/source-and-guardrails.md)。需要预算表和课程对比数据时读 [references/lifecycle-playbooks.md](references/lifecycle-playbooks.md)；需要消费者与英法语流量背景时读 [references/canada-market-and-consumer.md](references/canada-market-and-consumer.md)。

## 不可妥协的边界

- 把课程比例、头尾 ASIN 倍数和消费者研究标为 `COURSE_BASELINE`；把当前 Campaign、Search Term、Placement、销量、利润、库存、评价与 Listing 数据标为 `ACCOUNT_ACTUAL`。
- 课程中的倍数是加拿大站服饰类目头部 25% ASIN 相对尾部 25% ASIN 的描述性对比，不是目标值、因果证明或执行阈值。
- 不把“更早投入”自动等同于“必然获得排名、复购或更高 ROAS”。先验证产品、可售性、相关性、转化和利润是否支撑。
- 不把法语查询示例直接扩写或翻译后投放。先验证当前 Amazon.ca 搜索相关性、商品事实、页面语言和账户数据。
- 不用无证据的“抑菌、保暖温度、透气提升、舒适度提升”等声明制作广告或 Listing。
- `store_id`、profile ID、ASIN 或 marketplace 只是业务标识，不是授权。所有读取和写入都必须绑定当前验证过的服务端账户范围。
- 默认只生成草案。预算、竞价、placement、target、否定词、状态和广告结构均属于外部写操作，必须逐项人工确认。
- 每轮实验只改变一个可归因主变量；不要同时改 Listing、价格、优惠、竞价、预算和定向后声称因果。

## 先声明模式

在结果顶部选择一种模式：

1. `DIAGNOSE`：只读诊断，不生成可执行变更；
2. `DRAFT`：生成结构、预算重心和实验草案；默认；
3. `RELEASE_PREP`：生成逐对象新旧值、护栏、回退和审批卡；
4. `APPROVED_WRITE`：仅执行用户本轮明确批准的对象和单一动作，写后复读。

## 核心工作流

### 1. 锁定对象、目标和双时间轴

记录：

- 已验证的 Amazon.ca 广告 profile、seller、ASIN/SKU、父子体、品类和品牌资格；
- 上架日、首次销售日、历史销售峰值、近 36 个月销售曲线和当前生命周期阶段；
- 当前月份、目标旺季起止、距第一波需求的周数、补货周期和库存覆盖；
- 主目标只能选一个：`验证相关性 / 抢旺季流量 / 建立品牌认知 / 守位 / 利润 / 复购`；
- 贡献毛利率、盈亏平衡 ACOS、目标 TACOS、预算上限和停止条件。

必须分别输出：

```text
ASIN_LIFECYCLE = NEW | GROWTH | MATURE | DECLINE | NEEDS_DATA
SEASON_WINDOW = OFF_SEASON | PREHEAT | PEAK | POST_PEAK | NON_SEASONAL | NEEDS_DATA
```

Coat 老品每年仍会重新进入 `PREHEAT → PEAK → POST_PEAK`。生命周期成熟不等于全年只降价；两轴冲突时，以当前需求、库存、利润和账户数据决定动作。

### 2. 判断课程适配范围

用真实销售曲线判断：

| 轨迹 | 课程代表 | 本 Skill 的处理 |
|---|---|---|
| 季节性长生命周期 | Coat | 使用完整分阶段打法 |
| 长生命周期 | Underpants | 使用完整分阶段打法 |
| 季节性短生命周期 | Shirt | 仅可识别，不得套用 Coat 预算 |
| 短生命周期 | Backpack / Swimwear | 仅可识别，不得套用 Underpants 预算 |

若商品不落在前两类，输出 `NEEDS_DATA` 并说明最接近的类比及差异；不要伪造课程未给出的阶段比例。

### 3. 建立消费者顾虑与页面就绪度

Coat 至少核对：保暖相关商品事实、材质/填充、适用温度证据、尺码、使用场景、配送承诺、品牌可信度、英文与法语页面信息。

Underpants 至少核对：尺码实测、版型差异、材质参数、弹性、缩水、刺激/舒适反馈、肩带或做工问题、退货原因和复购窗口。

输出“购买问题 → 账户/商品证据 → 页面是否已回答 → 广告能否承接”。页面和商品事实不足时，广告放量只能是 `HOLD` 或小规模验证。

### 4. 获取同口径账户证据

至少收集：

- Campaign / Ad Group / Targeting / Search Term / Placement 报告；
- advertised product 与 purchased product 维度；
- 近 7/14/30 天及去年同期的曝光、点击、花费、订单、广告销售额；
- 自然与广告总销售、库存、价格/优惠、Featured Offer、评分/评论和退货；
- 英文、法语、品牌、类目、属性、场景、竞品和不相关查询的分组表现；
- 变更日志、归因窗口、币种、时区和数据更新时间。

不要跨归因窗口、广告类型、币种或父子 ASIN 直接相加。样本不足时输出区间和缺口，不用固定点击数下结论。

### 5. 选择课程基线并重算账户预算

打开 [references/lifecycle-playbooks.md](references/lifecycle-playbooks.md)，只把对应类型与阶段的比例作为起点。可运行：

```bash
python3 scripts/budget_mix_check.py --product coat --stage growth
python3 scripts/budget_mix_check.py --product underpants --stage mature --allocation plan.json
```

重算时依次应用：

1. 删除账户当前不可用或无资格的广告产品；
2. 按目标、贡献毛利和库存限制总预算；
3. 按已验证查询、ASIN 和 placement 表现分配；
4. 保留探索预算但设单独活动与停止条件；
5. 明确课程基线与账户草案的差异及原因。

课程比例相加为 100% 也不代表账户计划合理。

### 6. 设计分层结构

将不同意图和证据强度拆开：

- 英文与法语查询分开观察；品牌、类目、属性/场景和竞品词分开；
- 探索与收割分开；自动、关键词、商品定向分开；
- 进攻竞品与防御自家 ASIN 分开；
- Coat 的预热、旺季与旺季后活动保留独立预算和日期护栏；
- Underpants 的首次获客与历史购买/浏览再营销分开衡量。

不要让多个目的共享同一预算后再推断哪个动作有效。

### 7. 形成诊断与动作梯度

按顺序判断：

```text
可售/库存/Featured Offer
→ 流量相关性与语言
→ CTR 与创意/价格/位置
→ CVR 与页面/评价/配送/查询
→ CPC 与竞价/竞争/placement
→ ACOS、TACOS、增量和贡献利润
```

先解决上游断点，再考虑加预算。Coat 旺季前的加码必须有库存、相关性和页面承接；Underpants 的品牌与再营销扩张必须有可信商品事实、评价基础和可定义的受众窗口。

### 8. 生成单变量实验卡

每张卡只包含一个 `store + campaign + unique ad group + main variable`，并写明：

- 当前观察、证据 ID、基线窗口和课程假设；
- 唯一动作及对象、新旧值、预算上限；
- 冻结变量；
- 最小观察要求、归因等待、成功/停止/回退条件；
- 库存、利润、花费、品牌和合规护栏；
- 负责人和人工确认状态。

### 9. 审批与写后验证

进入 `RELEASE_PREP` 时展示 profile、campaign、ad group、target/placement、旧值、新值、最大影响、回退值和证据。仅在用户本轮明确批准后执行。

写后复读实际状态并保存 request/operation ID 与时间。仅看到请求成功时写“已提交”；只有复读确认才写“已生效”。

## 必须交付

按 [references/output-contract.md](references/output-contract.md) 输出，至少包含：

- 授权范围、数据窗口、双时间轴和证据等级；
- 课程适配类型、消费者顾虑与页面就绪度；
- `COURSE_BASELINE` 与 `ACCOUNT_ACTUAL` 分开的阶段预算表；
- 英法语查询、关键词、商品定向、品牌与展示型推广结构；
- 利润/库存护栏和单变量实验卡；
- `DRAFT`、`READY_FOR_REVIEW`、`APPROVED` 或 `HOLD`。

`READY_FOR_REVIEW` 不等于已批准执行；没有当前账户数据时最终状态只能是 `DRAFT` 或 `HOLD`。
