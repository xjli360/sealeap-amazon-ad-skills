# 证据、漏斗诊断与实验

## 目录

- [证据等级](#证据等级)
- [最小数据包](#最小数据包)
- [查询级诊断](#查询级诊断)
- [广告数据边界](#广告数据边界)
- [竞品与 VOC](#竞品与-voc)
- [Sorftime 安全取数](#sorftime-安全取数)
- [实验设计](#实验设计)

## 证据等级

用以下标签区分事实与推断：

| 等级 | 类型 | 可支持的结论 |
|---|---|---|
| `A` | 实物、包装、说明书、检测/认证、品牌确认 | 商品事实与声明 |
| `B` | Amazon 一方 Listing、PTD、issues、SQP、业务/广告报告、退货 | 店铺或 ASIN 的实际表现 |
| `C` | 目标站点前台、搜索结果和竞品页面快照 | 当时的页面与市场观察 |
| `D` | Sorftime 等第三方估算、抽样评论、模型推断 | 候选方向，不是 Amazon 实际数据 |

每条证据必须记录：

```text
evidence_id / grade / source / report-or-endpoint / marketplace /
ASIN-SKU-query / fetched_at / date_coverage / sample / limitations
```

不得用低等级证据覆盖高等级事实。多个来源口径不一致时并列展示，不擅自平均。

## 最小数据包

### 合规与可售

- 当前 Product Type Definition 与 checksum；
- `getListingsItem` 的属性、issues、关系、offer 和库存状态；
- 前台桌面/移动快照；
- 账户政策或抑制通知。

### 搜索与转化

- Search Query Performance：ASIN/品牌在 query 级的展示、点击、加购和购买漏斗；
- Search Catalog Performance：商品维度的搜索参与；
- Sales and Traffic：page views/sessions、Unit Session Percentage、Featured Offer 等；
- Ads Search Term/Targeting：impressions、clicks、cost、orders、sales、match type、placement；
- 退货原因、原始评论与 Q&A；
- 同期价格、优惠、库存、评分和广告变更。

Brand Analytics 报告的可用性取决于 Brand Registry 与相应 SP-API role。无法取得时写明缺口，不用第三方数据伪装成一方数据。

官方报告入口：

- https://developer-docs.amazon.com/sp-api/docs/report-type-values
- https://developer-docs.amazon.com/sp-api/lang-zh_CN/docs/report-type-values-analytics

## 查询级诊断

不要只看 campaign 平均值。按 `query + ASIN/SKU + match type + placement + time window` 聚合，并保留分子/分母：

| 现象 | 可能解释 | 先排除 | Listing 候选动作 |
|---|---|---|---|
| query 无展示/份额低 | 相关性、索引或属性不足 | 需求、竞价、预算、资格 | 检查类目/属性、title/bullets/backend 覆盖 |
| 有展示、CTR 低 | 搜索结果承诺弱或不匹配 | placement、价格、评分、配送 | 单测主图或标题前段 |
| 有点击、CVR 低 | 页面未回答问题或流量错配 | 价格、评论、配送、库存 | 辅图、五点、规格、适配、A+、限制 |
| 有成交但 Listing 未覆盖 | 查询可能代表真实需求 | 样本、事实匹配、自然语序 | 进入字段候选，不自动发布 |
| 高花费无成交 | 相关性差或页面/offer 弱 | 归因窗口、最大可承受 CPA | 不相关词做否定候选；相关词再诊断页面 |
| 退货/差评主题集中 | 预期差或商品问题 | 质量、履约、批次 | 明示尺寸、适配、用法、限制或停止宣传 |

“系统推荐了某关键词/品类”只说明模型当前相关性判断，不等于 Listing 质量分，也不能单独证明应加入该词。

## 广告数据边界

Amazon Ads Search Term report：

- 展示买家使用的搜索词，也可能包含非搜索场景推断的最佳匹配；
- 只包含至少获得 1 次广告点击的 search term，因此 impressions 不一定与 Campaign Manager 一致；
- Sponsored Products 的当前公开帮助页说明可用回溯窗口为 65 天；
- ASIN 形式的 customer search term 可来自自动投放或商品属性投放。

来源：https://advertising.amazon.com/help/G3HEFZYWZF84NPS9

把广告词分为：

- `LISTING-CANDIDATE`：高相关、有事实、代表购买意图；
- `AD-ONLY`：适合定向但不适合自然文案；
- `NEGATIVE-CANDIDATE`：不相关或经济性不成立，仍需审批；
- `INSUFFICIENT-SAMPLE`：样本不足；
- `CONFLICTED`：流量、转化、利润或退货信号冲突。

Listing 草稿与广告 bid/placement/negative 变更必须分开审批和实验。

## 竞品与 VOC

### 竞品

观察：

- 商品形态、价格带、变体结构和购买问题；
- 信息层级、规格呈现、图片任务和 A+ 模块；
- 竞品评论中反复出现的期望差与未满足需求。

不要复制文案、图像、商标、专利性结构或独特视觉。竞品销量、关键词和排名若来自第三方，标为估算/观测。

### VOC

分别保留正面、负面和中性主题以及样本数。把评论主题与退货原因、Q&A、客服问题互证。评论中的个体观点不能直接变成产品事实或功效声明。

输出：

```text
theme / sentiment / sample / verbatim-reference / fact-check /
purchase-question / proposed-field / confidence
```

## Sorftime 安全取数

Sorftime 是可选的第四级证据。优先用 Amazon 一方数据；只有内部数据不足或需要站外补充时才调用。

凭证由现有 ecomi 从 `~/.ecomi/sorftime.json` 读取。文件权限保持 `600`；不得把密钥写入 Skill、报告、命令、日志或 Git。

先只查看工具能力：

```bash
ecomi sorftime --list
ecomi sorftime --describe product_traffic_terms
```

默认只生成计划，不联网：

```bash
python3 scripts/sorftime_plan.py \
  --asin B0XXXXXXXX \
  --site US \
  --keyword "core query"
```

确认调用数与范围后，才显式执行：

```bash
python3 scripts/sorftime_plan.py \
  --asin B0XXXXXXXX \
  --site US \
  --keyword "core query" \
  --execute \
  --output-dir evidence/sorftime
```

最小包：`product_detail`、`product_traffic_terms`、`product_reviews`，以及每个核心 query 的 `keyword_detail`。只有信息增益明确时才启用 `--deep`；默认总调用上限 8。`UK` 规范化为 `GB`。

## 实验设计

### 先写实验卡

```text
hypothesis / target-ASIN-SKU-marketplace / primary-variable /
version-A / version-B / baseline-window / attribution-window /
minimum-information / primary-metric / guardrails /
success-rule / stop-rule / rollback-rule / confounders
```

### 样本与经济性

- 保留 impressions、clicks、orders、visitors 等原始计数，不只报比率。
- 用商品单件广告前贡献利润计算最大可承受 CPA；用广告前贡献率作为 break-even ACOS 的业务基准。
- 样本要求应由基线率、期望最小提升、流量与风险决定。没有统计方法时写 `DIRECTIONAL`，不要用固定点击次数假装显著。
- 处理转化归因延迟和退货滞后；窗口未结束时不宣布结果。

### 选择实验类型

- `MYE-SINGLE`：解释标题、图片、要点、描述或 A+ 的单一影响；
- `MYE-MULTI`：寻找整体最佳组合；只归因到组合；
- `SEQUENTIAL`：无 MYE 资格时使用，降低因果置信度；
- `HOLDOUT/OTHER`：有成熟分析能力时使用并记录分流规则。

Amazon 当前 MYE 说明：https://sell.amazon.com/tools/manage-your-experiments
