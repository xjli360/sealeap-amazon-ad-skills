---
name: sealeap-amazon-variation-ad-structure
description: Design Amazon Ads for legitimate parent-child variations by selecting a hero child, allocating queries by variant attributes, isolating budgets, and monitoring halo effects and inventory. Use when the user asks how to advertise many variants, prevent child ASINs from competing, choose a hero variation, or split keywords by color, size, pack count, or style. Never create invalid variations or execute without approval.
---

# Amazon 多变体广告架构

## 目标

在合法变体关系内，让每个子体承担与自身属性匹配的流量，并用主推子体集中验证通用需求。

## 适用任务

- 颜色、尺寸、数量或风格变体过多导致预算分散。
- 需要确定主推子体和非主推子体的投放强度。
- 不同变体在同一关键词下互相抢量。

## 开始前要拿到

- 父子关系、变体主题、各子 ASIN 属性、价格、库存和利润。
- 子体级广告表现、业务报告和搜索词。
- 关键词词根分类及与各变体的事实匹配。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 仅使用 Amazon 当前允许且商品真实共享的变体主题；不得为共享评论或排名强行合并。
- 主推款不能只按一次广告结果决定，要同时看库存、利润、评分和长期需求。
- 预算集中不是固定比例，必须按数据和缺货风险动态计算。
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

### 1. 验证变体合法性

确认每个子体仅在允许属性上变化，标题、图片和属性与实物一致。

### 2. 选择主推候选

综合历史转化、需求、利润、库存和评价，先列一个或多个候选，再用隔离实验确定主推。

### 3. 按属性分词

把颜色、尺寸、数量、场景等专属查询分配给对应子体；通用词和核心卖点词由主推候选承担。

### 4. 隔离广告职责

主推子体负责通用发现和核心词，其他子体以属性相关广告为主；不同职责分开预算和命名。

### 5. 迁移与去重

稳定查询迁移到对应子体的精准层，并检查父体展示导致的交叉点击和重复投放。

### 6. 监控组合结果

同时看子体利润、父体总销量、变体切换、库存与自然溢出；主推缺货前提前降载或切换。

## 判断标准

- 每个关键词能解释为何属于该子体。
- 子体级数据与父体总盘不混淆。
- 主推策略包含缺货和利润恶化的替代方案。

## 必须交付的结果

- 主推候选评分表。
- 变体到关键词的分配矩阵。
- 子体广告架构与预算职责。
- 去重、迁移和库存切换规则。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
