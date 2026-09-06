---
name: sealeap-amazon-sp-video-ads
description: Plan, review, diagnose, and safely launch Amazon Sponsored Products video-format ads (SP video/SPV), including eligibility, video briefs, policy checks, ASIN and thumbnail mapping, bid adjustments, measurement, and controlled tests. Use for 商品推广视频, SPV, Sponsored Products video, 静音商品视频, 搜索结果视频素材, 视频竞价加成, 3–5条视频测试, video CTR/CVR/ACOS, or converting the authorized SPV intro, shooting, and syndication materials into an approval-ready plan. Treat all specs and availability as source snapshots until verified in the current marketplace and console; never upload or change live ads without explicit approval.
---

# Amazon 商品推广视频样式（SPV）

## 目标

将一个已验证的 ASIN 变成可审核、可测试、可回退的视频广告方案：先确认当前账户是否具备 SP 视频样式，再建立 3–5 个单一概念素材，逐条通过商品事实与政策审查，最后在独立的竞价实验中判断视频是否带来增量价值。

开始前读 [references/source-and-guardrails.md](references/source-and-guardrails.md)。制作素材读 [references/creative-brief-and-review.md](references/creative-brief-and-review.md)；设置与测量读 [references/activation-and-measurement.md](references/activation-and-measurement.md)。

## 不可跳过的边界

- SPV 的站点、账户、类目、展示位置、视频数量、字段限制、文件规格和竞价范围可能变化；必须在当前控制台或官方文档复核。
- 课程材料出现互相冲突的文案字符限制；遇到冲突一律以当前 UI 校验为准。
- 视频中的商品、功能、兼容性、性能、认证和场景必须由当前 PDP/产品档案支持。
- 默认只生成 brief、审核结果和草案。上传素材、调 bid/budget/placement 或启停广告均需用户明确批准。

## 工作流

### 1. 确认作用域与资格

记录 marketplace、profile、campaign、ad group、ASIN、类目、语言、日期与权限。进入当前广告控制台确认：SP 视频样式可见、该 ASIN 可选、素材规格/字段校验和报告字段存在。无法确认则输出 `ELIGIBILITY_NEEDS_VERIFICATION`，不声称可上线。

### 2. 验证商品与零售准备度

检查 Featured Offer、库存、配送、评分、价格/优惠、移动端详情页、变体和已有视频。若视频承诺与 PDP 不一致、库存不足或详情页不能承接，状态为 `HOLD_RETAIL_READINESS`。

### 3. 建立素材矩阵

先确定 3–5 个不同概念，每条视频只讲一个核心价值：痛点解决、核心功能、使用场景、上手方式、差异化或可信证明。不要把同一条片简单换封面当不同概念。

使用 [references/creative-brief-and-review.md](references/creative-brief-and-review.md) 逐条输出：目标人群、使用场景、首屏钩子、镜头表、唯一价值、商品占屏、封面/缩略图、PDP 证据、禁用元素和版本号。

### 4. 做政策与质量审查

逐项判定 `PASS / FIX / HOLD`：

- 商品是否清晰、持续可辨、与广告 ASIN 一致；
- 是否真实演示而非静态幻灯片或过度渲染；
- 是否存在未经证实的文字、字幕、旁白、Logo、emoji、对比或功效声明；
- 是否有黑边、失真、低清、危险使用、无关人物/商品；
- 产品名称、描述和缩略图是否符合当前字段限制。

### 5. 设计独立测试

优先比较一个变量：视频概念、视频与非视频、缩略图或视频加价。固定 ASIN、target、日期逻辑、预算和其它 placement 调整。已有叠加系数时先算实际最大出价，避免把视频加价、位置加价和动态竞价当成彼此独立。

### 6. 上线前审批

审批卡必须列出 profile、campaign、ad group、ASIN、视频文件/asset ID、缩略图、文案、target、基准 bid、每个调整系数、最大可能出价、预算、停止线和回退值。

### 7. 观察与复盘

等待当前归因窗口成熟。至少同时看曝光、点击、CTR、CPC、花费、订单、销售、CVR、ACOS/ROAS，以及当前报告支持的视频观看指标。比较绝对值、比例和样本量，不只报 uplift。

## 必须交付

- 当前资格与规格复核结果；
- 商品事实表和零售准备度；
- 3–5 条单概念 brief 与逐条审核；
- 实际竞价堆叠计算、预算上限和单变量实验；
- 审批对象、停止线、回退和最终状态。
