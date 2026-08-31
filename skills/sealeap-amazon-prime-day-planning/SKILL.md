---
name: sealeap-amazon-prime-day-planning
description: Filter, interpret, and turn the authorized 2025 Amazon Prime Day advertising insight records into a qualified event plan without averaging incompatible slices or treating historical benchmarks as forecasts. Use for Prime Day/会员日广告规划, 旺季预算, ROAS/DPV/Units/Sales benchmark, marketplace insight lookup, Sponsored Ads/SP/SB/Display mix, event baseline comparison, preheat/peak/tail plan, or querying the included 116-row insight dataset. Default to analysis and draft; verify the current event dates, eligibility, policies, inventory, economics, and account data before any live change.
---

# Amazon Prime Day 广告规划

## 目标

从 116 条带限定条件的历史洞察中找到“真正适用于当前问题的行”，保留 marketplace、广告产品、指标、广告主资格、品类、花费门槛和时间窗口，再将其降级为规划先验，用当前账户数据决定活动节奏与实验。

先读 [references/source-and-guardrails.md](references/source-and-guardrails.md)。查询数据使用 `scripts/filter_insights.py`；输出计划参考 [references/planning-workflow.md](references/planning-workflow.md)。

## 查询数据

查看摘要：

```bash
python3 scripts/filter_insights.py --summary
```

按站点、指标和广告产品筛选：

```bash
python3 scripts/filter_insights.py --marketplace DE --metric ROAS --ad-product "Sponsored Brands"
```

搜索限定条件：

```bash
python3 scripts/filter_insights.py --marketplace US --contains "brand owner" --format json
```

`marketplace` 会匹配行中列出的单站点/区域；`All` 不是任意行通配符，而是源数据明确标记的全球切片。

## 工作流

### 1. 锁定当前事件

确认年份、marketplace、官方 event dates、广告 profile、时区、币种、ASIN/品类、Deal/优惠资格、库存到仓时间和活动目标。不得沿用 2025 时间窗口作为当前日历。

### 2. 锁定经济性与库存

计算贡献毛利、盈亏平衡 ACOS、促销成本、库存覆盖天数、补货截止和断货风险。销量目标超出库存或现金流承受时先 `HOLD_SCALE`。

### 3. 筛选可比洞察

从最严格条件开始：单站点 > 区域 > `All`；同指标、同广告产品、相近广告主资格/品类/花费门槛。每个候选行完整保留 `Content` 中的限定说明。

如果没有足够可比行，输出 `NO_COMPARABLE_SOURCE_SLICE`，不要拿全球/其它品类数字填空。

### 4. 解释而非平均

- DPV、Units、Sales 的 uplift 是事件期对材料所列基准期的比较；
- ROAS 是材料所列事件期内的比率；
- 各行可能来自不同 marketplace、资格和广告产品，不得求简单平均或排名；
- 历史洞察只帮助设定问题和护栏，不直接设置预算或目标。

### 5. 形成三阶段计划

- `PREHEAT`：验证零售准备、扩充合格搜索词/人群、建立基线；
- `EVENT`：把预算优先给当前账户已证明的高贡献对象，设置实时停止线；
- `TAIL`：收紧低效流量、继续合规再营销、等待归因成熟并复盘。

每阶段只给活动角色、证据和上下限；不照抄资料预算比例。

### 6. 设计一个实验

只改变一个变量，例如预算释放节奏、广告产品组合、关键词层或创意。固定其它主要条件，记录最大花费、库存护栏、成功/停止线和回退。

### 7. 审批与复读

所有 bid、budget、campaign 状态、target、Deal 或优惠变更必须列出逐对象旧值/新值并等待批准。写后复读当前值；请求成功不等于事件表现已改善。

## 必须交付

- 当前事件、账户、经济性和库存作用域；
- 选中的源行及全部 qualifier；
- 为什么可比、为什么其它行被拒绝；
- PREHEAT / EVENT / TAIL 草案；
- 一个单变量实验、审批和回退；
- `DRAFT / READY_FOR_REVIEW / HOLD` 状态。
