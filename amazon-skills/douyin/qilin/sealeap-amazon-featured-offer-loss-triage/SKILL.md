---
name: sealeap-amazon-featured-offer-loss-triage
description: Triage loss of the Amazon Featured Offer by checking account health, order defect signals, price competitiveness, offer and fulfillment state, listing classification, unauthorized sellers, and external price evidence before escalating. Use when the Buy Box or purchase button disappears or repeatedly returns. Do not assume sabotage, manipulate feedback, or edit other sellers' data.
---

# Amazon Featured Offer 丢失排查

## 目标

用证据区分账户绩效、价格、Offer、商品信息、库存配送和第三方问题，选择可持续恢复路径。

## 适用任务

- 链接突然失去 Featured Offer。
- 降价后仍未恢复。
- 怀疑外部低价、跟卖或商品信息异常。

## 开始前要拿到

- 站点、ASIN、SKU、Offer 状态、价格、库存、配送与首次丢失时间。
- 账户健康、ODR、取消率、迟发率和政策通知。
- 价格健康、商品信息变更、类目、跟卖与外部页面证据。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 购物车丢失不能默认是恶搞；先排除自身账户、价格和库存原因。
- 不得购买虚假 feedback、越权修改其他站点商品信息或提交虚假品牌投诉。
- 外部页面投诉只在确有品牌、版权或商标权利且证据充分时进行。
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

### 1. 确认事件范围

判断是单 Offer、单 ASIN、全店或特定时间段，并保存前后价格与状态证据。

### 2. 检查账户与履约

核对 ODR、取消、迟发、有效追踪、库存、配送速度和卖家绩效通知。

### 3. 检查价格

查看价格健康、自动定价、历史价格和可见外部报价，区分真实渠道冲突与疑似冒用。

### 4. 检查商品信息

核对类目、敏感属性、品牌、标题和近期贡献者变更，使用官方证据恢复正确事实。

### 5. 检查第三方 Offer

识别授权与未授权卖家；对假货或侵权按 Brand Registry 或官方路径举证，不把正常跟卖等同侵权。

### 6. 提交与监控

用单一事实包开 case，记录恢复时间和复发条件；若反复发生，建立价格与商品信息监控。

## 判断标准

- 根因结论有后台或公开证据。
- 恢复动作不会制造亏损、虚假反馈或新的政策风险。
- 对外投诉基于实际权利。

## 必须交付的结果

- Featured Offer 事件时间线。
- 账户、价格、Offer、内容和第三方排查表。
- 支持或权利报告草稿。
- 复发监控与利润护栏。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
