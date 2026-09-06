---
name: sealeap-amazon-return-rate-reduction
description: Reduce avoidable Amazon returns through root-cause analysis, accurate listing content, packaging and quality fixes, official Product Support features, manuals, support videos, spare-parts workflows, and privacy-safe service operations. Use when customers return products due to setup, usage, missing parts, or delayed support. Never request reviews during support or build an unauthorized customer list.
---

# Amazon 退货率降低

## 目标

把可避免退货按根因分流，在 Amazon 允许的支持入口中更快解决安装、使用和零配件问题。

## 适用任务

- 安装或使用困难导致退货。
- 大件商品因小配件损坏整单退回。
- 评估电话、视频、说明书或 AI 客服。

## 开始前要拿到

- 退货原因、退款、客户联系主题、差评主题和批次质量数据。
- 当前站点 Product Support、说明书、视频、电话或零配件功能资格。
- 客服语言、时区、隐私、录音、升级和人工接管要求。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 联系方式只放在 Amazon 明确允许的字段和场景，不绕过平台消息规则。
- 售后过程中不得索要好评、引导改评、评价门控或把客户沉淀成未授权私域名单。
- AI 客服必须遵守隐私、披露、录音和消费者保护要求，并保留人工升级。
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

### 1. 量化退货根因

按 ASIN、变体、批次、原因、时间和成本建立 Pareto，先处理高频且可避免问题。

### 2. 修正商品承诺

让图片、尺寸、兼容性、安装难度和限制与实物一致，减少购买前误解。

### 3. 补足自助支持

在当前官方允许的位置提供清晰说明书、故障排查、安装或使用视频，并验证移动端可读性。

### 4. 设计零配件闭环

为适合商品建立配件库存、资格、验证、防欺诈和物流 SLA，比较补件与整单退货成本。

### 5. 配置客服

使用合规号码或平台入口，建立语言覆盖、响应时限、AI 到人工升级和敏感问题处理。

### 6. 验证成效

比较实施前后退货率、原因分布、解决率、响应时长、成本和客户满意度。

## 判断标准

- 功能资格和联系方式规则已核对当前官方文档。
- 支持不与评价请求或营销再触达绑定。
- 退货下降没有以拒绝合法退款为代价。

## 必须交付的结果

- 退货根因 Pareto。
- 内容、说明、视频和配件修复清单。
- 客服与 AI 升级 SOP。
- 实施前后评估方案。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
