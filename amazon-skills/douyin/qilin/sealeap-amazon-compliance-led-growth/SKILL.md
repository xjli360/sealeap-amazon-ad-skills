---
name: sealeap-amazon-compliance-led-growth
description: Build an Amazon growth strategy that treats tax, product safety, account, IP, and logistics compliance as non-negotiable constraints, then compares niches, price bands, operating models, and marketplaces using weighted economics. Use when the user asks how to find opportunities as compliance costs rise or whether to shift product, model, or marketplace. Reject evasion and infringement strategies.
---

# Amazon 合规驱动增长

## 目标

先把合规成本纳入单位经济，再从细分产品、真实门槛、经营模式和站点匹配中寻找可持续机会。

## 适用任务

- 税务或产品合规成本上升后重新评估业务。
- 比较红海细分、高客单、物流或资质门槛产品。
- 选择精品、组合管理、季节性或不同站点。

## 开始前要拿到

- 主体、站点、税务、海关、产品安全、环保、IP 和账号要求。
- 细分市场需求、价格、退货、竞争、物流和贡献利润。
- 团队供应链、认证、语言、本地化和资本优势。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 不得把侵权擦边、赶在权利人行动前退出、黑帽或多账号隔离风险当作竞争优势。
- 税务与合规判断必须由当前官方规则和合格专业人士确认。
- 受限品或高门槛产品只有在真实具备资质与持续维护能力时才能进入。
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

### 1. 建立合规底盘

按主体与站点列出税务、报关、产品、环境、IP、标签和账户义务，计算一次性与持续成本。

### 2. 寻找细分机会

在大类中按人群、风格、任务或痛点切分，验证需求、粘性和差异化，而非仅凭主观蓝海判断。

### 3. 评估真实门槛

比较高客单、物流、认证、技术、售后和品牌门槛，确认团队能合法持续地交付。

### 4. 比较经营模式

用产品生命周期、SKU 数、团队能力、库存和学习速度比较精品、组合、季节性等模式。

### 5. 比较站点

统一口径评估需求、竞争、税费、合规、本地化和现金周期，避免只看订单体量。

### 6. 加权决策

输出市场乘以模式乘以商品的候选组合，按利润、现金、能力和合规评分，并设计小规模验证。

## 判断标准

- 税费和合规成本已进入利润模型。
- 所谓门槛是可合法构建的能力。
- 站点比较使用统一货币和数据窗口。

## 必须交付的结果

- 合规义务与成本清单。
- 商品、模式、站点机会矩阵。
- 加权评分与风险红旗。
- 候选组合的验证计划。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
