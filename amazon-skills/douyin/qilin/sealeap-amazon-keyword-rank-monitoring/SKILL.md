---
name: sealeap-amazon-keyword-rank-monitoring
description: Create a disciplined Amazon keyword-position monitoring system that prioritizes revenue-contributing terms, separates organic and sponsored observations, controls measurement noise, and triggers evidence-based diagnostics. Use when the user asks which keyword ranks to track, how often to track them, or what to do when a core term drops. Do not automate bid changes from a single noisy snapshot.
---

# Amazon 关键词位置监控

## 目标

把关键词位置监控从盯排名变成面向订单贡献的预警系统，用连续证据触发诊断而非情绪化调价。

## 适用任务

- 决定哪些词需要日更、周更或仅观察。
- 核心出单词位置下降时判断原因和动作。
- 寻找某个 ASIN 在不同位置区间的稳定出单区。

## 开始前要拿到

- 查询级订单或品牌分析贡献、广告搜索词和业务报告。
- 自然与广告位置快照、采集时间、设备或区域条件。
- 价格、库存、促销、评分和竞争环境事件。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 位置采集受个性化、地域和时间影响，单点不是事实全貌。
- 不得因小时级波动立即自动加价；必须通过连续窗口和业务指标确认。
- 监控工具需遵守 Amazon 条款和数据访问权限。
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

### 1. 确定监控集合

按订单、收入、利润和战略价值给词分级；核心贡献词高频监控，探索词降低频率。

### 2. 标准化采集

固定站点、时间窗、设备口径和自然或广告标签，保存历史而非覆盖旧值。

### 3. 建立舒适区

把位置区间与会话、订单、CVR、CPA 对齐，识别稳定区间但不宣称固定因果。

### 4. 设置预警

只有连续越过位置、订单或利润护栏才触发；同时检查库存、Featured Offer、价格、评论和广告预算。

### 5. 生成干预草稿

根据根因建议恢复预算、修商品页、调整目标或观察；避免只靠提高竞价追位置。

### 6. 复盘干预

记录干预前后趋势和外部事件，判断是否真有改善。

## 判断标准

- 自然与广告位置分开。
- 核心词选择可追溯到订单或战略证据。
- 预警包含连续性、业务影响和根因检查。

## 必须交付的结果

- 关键词监控分级表。
- 标准采集字段和频率。
- 预警阈值与诊断树。
- 待批准干预建议。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
