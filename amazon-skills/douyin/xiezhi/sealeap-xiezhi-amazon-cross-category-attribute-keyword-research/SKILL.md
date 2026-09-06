---
name: sealeap-xiezhi-amazon-cross-category-attribute-keyword-research
description: "Use material, feature, audience, occasion, style, and scenario keywords to discover Amazon opportunities across categories. Use when category-first filters are too narrow or the team wants to reuse a supply capability across multiple demand contexts."
---

# Amazon 跨类目通用词选品

## 目标

以消费者可搜索的通用属性为入口跨类目发现需求，再用盈利与竞争门槛收敛，而不是依赖一套固定参数。

## 适用任务

- 用材质、工艺、元素或场景词跨类目找产品。
- 把一个供应链能力映射到多个细分需求。
- 从大结果集中筛出低评论可盈利方向。

## 开始前要拿到

- 一个经过本地化验证的通用词。
- 全站点包含该词的商品、类目、价格、评论和销量数据。
- 目标利润、广告成本和进场时间。
- 供应链可做材质、工艺、图案和数量范围。

缺少字段时列出证据缺口，并把相关结论标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`；不要补造数据。

## 不可妥协的边界

- 第三方数据均为估算或代理证据；Amazon 一方报告、后台实时字段和产品事实优先。
- 经验阈值只能作为可调起点，必须展示敏感性分析，不能写成 Amazon 官方规则。
- 不得捏造销量、搜索量、CPC、CVR、成本、认证、产品属性或消费者需求。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不输出或保存素材来源身份、账号、链接、作品编号、互动数据、原始话术或其他可反查来源的线索。
- 热点元素、角色、图案、文字和品牌词必须先做 IP 核查。
- 词出现在标题中不等于需求成立，仍要验证搜索意图。

## 工作流

### 1. 定义通用词

从材质、工艺、属性、主题、人群、场景、节日或活动中选择能跨产品复用的搜索表达。

### 2. 全站发现

不预设单一类目，检索包含该词的商品并按产品形态与需求场景聚类。

### 3. 应用经济筛选

再以评论、价格、历史月份、预计利润和旺季窗口缩小范围，保留不同阈值结果。

### 4. 验证精准性

逐簇检查词与商品是否高度相关、是否存在真实直接竞品及正常低评论样本。

### 5. 进入立项

对候选补齐 CPC/CVR、差异化、供应链、IP、合规和库存证据。

## 判断标准

- 固定参数会限制视野；先用通用词发现，再根据产品经济和风险收敛。
- 评论不超过约 50、售价不低于约 25 等只可作探索起点。
- 跨类目复用的是能力和需求语言，不是直接复制产品。

## 第三方 MCP 数据

需要外部关键词、竞品、评论或公开网页证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，并使用 `scripts/mcp_research.py`。

- 先动态执行 `tools/list`、`search-tools` 和 `describe`，依据实时 `inputSchema` 构造参数。
- 凭证只从环境变量读取，不进入参数、URL、Skill、终端输出或 Git。
- 可能计费的 `tools/call` 先展示 Provider、工具、无密钥参数、预计成本与输出位置，核对已有授权；仅在授权覆盖本次范围时使用 `--allow-cost`，该标志不是费用上限。
- 脱敏结果用 `--output` 写入 Skill 包之外的任务私有目录；不假设安装位置受仓库 `.gitignore` 保护。第三方数据标为估算或代理证据。
- 失败一次后记录缺口，不以重复付费重试掩盖不可用状态。

## 必须交付的结果

- 通用词定义卡
- 跨类目商品聚类
- 筛选敏感性表
- 精准需求验证
- 立项候选清单

结尾列出站点、数据窗口、证据来源、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行细节、证据字段和质量检查见 [references/playbook.md](references/playbook.md)。
