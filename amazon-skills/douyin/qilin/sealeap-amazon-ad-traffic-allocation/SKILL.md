---
name: sealeap-amazon-ad-traffic-allocation
description: Apply a simple Amazon Ads allocation model that separates discovery from exploitation, tests keyword and placement effects, and reallocates budget toward evidence-backed conversion pockets. Use when the user asks for a clear mental model for Amazon ads, how to find good traffic, how to compare placements, or how to reduce poor traffic. Draft only unless live changes are explicitly approved.
---

# Amazon 广告流量分配

## 目标

用“发现高转化组合”和“重分配预算”两个循环管理广告，避免同时改变关键词、位置和预算导致无法归因。

## 适用任务

- 解释广告结构中探索活动与主力活动的职责。
- 诊断同一关键词在不同广告位表现差异。
- 在预算固定时放大赢家、减少输家。

## 开始前要拿到

- 查询、目标、广告活动和广告位级表现。
- 商品价格、利润、阶段目标和库存状态。
- 已知的关键词相关性与商品投放相似度。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 广告位报告不等于可精确控制的自然页码或固定展示位置。
- 不可在样本不足时把预算从一个随机赢家全部迁走。
- 广告优化不能绕过商品页承接力、价格和库存问题。
- 当前 Amazon 官方政策、帮助页、账户资格和后台实际字段优先于本 Skill 中的经验框架；规则可能变化时先核验。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不输出原素材的创作者身份、账号、链接、视频编号或可反查线索；当前业务证据的官方来源、采集时间和口径仍需保留。

## 工作流

### 1. 拆分两个循环

探索循环负责找词、商品目标和广告位；利用循环负责给已验证组合稳定预算。

### 2. 隔离变量

先固定目标测试广告位，或固定广告位策略测试目标，避免多变量一起变化。

### 3. 定义赢家

以相关性、CVR、CPA、贡献利润和样本强度联合判定，而不是只看订单或 ACoS。

### 4. 迁移预算

小步增加赢家预算或竞价，减少低相关和持续亏损流量；每次保留前后对照。

### 5. 持续再探索

保留受控探索预算，防止主力词老化或流量结构变化后失去新机会。

### 6. 监控总盘

观察 TACoS、总贡献利润、自然订单、库存和广告间蚕食。

## 判断标准

- 每个建议指出它属于探索还是利用。
- 预算迁移有最小样本和最大调整幅度。
- 报告同时呈现局部广告指标和总业务结果。

## 必须交付的结果

- 探索与利用广告地图。
- 关键词加广告位组合的绩效表。
- 预算增加、减少和继续观察清单。
- 下一轮单变量实验。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
