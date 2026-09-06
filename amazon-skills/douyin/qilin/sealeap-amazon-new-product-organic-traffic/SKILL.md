---
name: sealeap-amazon-new-product-organic-traffic
description: Build an evidence-based Amazon new-product traffic plan that moves from controlled discovery to stable converting terms and measures organic-rank and organic-order changes without claiming causality. Use when the user asks how a new ASIN can gain organic traffic, how to sequence auto, product targeting, broad, and exact campaigns, or when to taper launch ads. Default to read-only planning and require approval for live changes.
---

# Amazon 新品自然流量培育

## 目标

先用可控广告找出稳定转化词，再逐步集中预算并观察自然曝光与订单的变化，形成可持续而非靠单次冲量的新品基本盘。

## 适用任务

- 新品从零开始设计探索、收割和放量阶段。
- 判断某个词是否值得从自动或广泛迁移到精准。
- 制定广告减量而不破坏销量基本盘的毕业条件。

## 开始前要拿到

- ASIN 上线时间、库存覆盖、价格、优惠、内容完整度和合规评论状态。
- 搜索词、投放、广告位、业务报告及可获得的自然排名快照。
- 每单贡献毛利、目标订单、可承受测试预算和补货周期。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 自然排名受多因素影响；只能报告相关变化，不能承诺广告必然推升排名。
- 不得使用虚假订单、返现、搜索后购买、评论操纵或不合规变体来制造信号。
- 新品转化基础不合格或库存不足时，不用加预算掩盖商品问题。
- 当前 Amazon 官方政策、帮助页、账户资格和后台实际字段优先于本 Skill 中的经验框架；规则可能变化时先核验。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不输出原素材的创作者身份、账号、链接、视频编号或可反查线索；当前业务证据的官方来源、采集时间和口径仍需保留。

## 第三方 MCP 数据

只有在本任务确实需要外部市场、竞品、关键词或公开网页证据时，才读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，并使用 scripts/mcp_research.py。

- 先动态执行 tools/list、search-tools 和 describe，依据实时 inputSchema 构造参数，不照搬历史工具名。
- 凭证只从环境变量读取，不放进命令参数、URL、Skill、结果文件或 Git。
- tools/call 可能计费。调用前展示 Provider、工具名、无密钥参数、预计成本与输出位置，核对已有授权覆盖后才加 --allow-cost；该标志不是费用上限。
- 第三方数据标为估算或代理证据，记录 Provider、工具、无密钥参数、查询时间和原始结果位置；失败一次后记录缺口，不反复消耗额度。
- 脱敏结果用 --output 写到 Skill 包之外的任务私有目录；不假设安装位置受仓库 .gitignore 保护，不把运行结果写入 Skill 包。

## 工作流

### 1. 做上线门槛检查

确认商品可售、库存、价格、主图与详情、属性、合规资质和售后准备；先修复会直接压低转化的缺口。

### 2. 建立探索层

用紧密相关的自动流量和少量高相似商品目标探索搜索词与商品页面机会，限制预算并排除明确不相关流量。

### 3. 建立词根层

把已验证的搜索词按意图或属性词根归组，以较宽匹配继续发现同类长尾词，同时维护前置否定词。

### 4. 迁移稳定词

达到样本和利润门槛的词转入精准广告，单独管理预算与竞价；迁移前后记录重叠流量，避免内部抢量。

### 5. 跟踪自然侧

固定时间采集自然位置、自然会话和自然订单占比，与广告订单、价格和促销一起观察，避免单因果解释。

### 6. 设定毕业条件

当核心词转化稳定、自然侧连续多个周期不恶化且总利润成立时，小步降低探索预算；一旦销量或位置越过护栏则停止缩量并复盘。

## 判断标准

- 用查询级转化率、CPA、自然订单占比和库存风险联合判断，不只看 ACoS。
- 迁移词必须说明来源报告、样本量、相关性和预算需求。
- 每个阶段都有进入条件、退出条件和止损条件。

## 必须交付的结果

- 新品流量阶段图。
- 探索词、迁移词和否定词清单。
- 自然侧观测表与因果限制说明。
- 广告减量或继续投入的建议及待批准动作。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
