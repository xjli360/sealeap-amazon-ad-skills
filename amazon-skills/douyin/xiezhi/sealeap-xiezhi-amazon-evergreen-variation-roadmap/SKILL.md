---
name: sealeap-xiezhi-amazon-evergreen-variation-roadmap
description: "Plan a compliant long-lived Amazon variation roadmap for products that can legitimately expand by color, size, pattern, or other allowed themes. Use when a team wants recurring niche launches under one valid parent without abusing review sharing."
---

# Amazon 长期变体路线图

## 目标

通过真实、合规且有独立需求的子体持续扩展产品线，同时把每个变体当作独立经济单元管理。

## 适用任务

- 判断产品是否适合长期加变体。
- 规划主题/图案/颜色的年度扩展。
- 为每个子体设计独立关键词、库存与广告。

## 开始前要拿到

- 当前 product type 与实时允许的 variation theme。
- 每个候选子体的真实属性、图片、SKU、库存和 GTIN 状态。
- 主题/元素的需求、关键词、IP 与季节证据。
- 父体及子体的销量、评论、退货和广告表现。

缺少字段时列出证据缺口，并把相关结论标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`；不要补造数据。

## 不可妥协的边界

- 第三方数据均为估算或代理证据；Amazon 一方报告、后台实时字段和产品事实优先。
- 经验阈值只能作为可调起点，必须展示敏感性分析，不能写成 Amazon 官方规则。
- 不得捏造销量、搜索量、CPC、CVR、成本、认证、产品属性或消费者需求。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不输出或保存素材来源身份、账号、链接、作品编号、互动数据、原始话术或其他可反查来源的线索。
- 禁止虚假、占位、重复或不相关子体。
- 禁止通过拆分、合并或移除子体规避差评、共享不相关评论或操纵排名。

## 工作流

### 1. 验证结构资格

确认产品本质相同且差异完全符合当前类目允许主题；不符合则使用独立 Listing。

### 2. 建立元素雷达

从季节、活动、风格、图案、颜色和人群需求形成候选，但先做文化与 IP 筛查。

### 3. 逐子体验证

为每个子体单独核验精准词、竞品、价格、成本、需求和可达销量。

### 4. 制定发布节奏

按供应链小批能力和需求窗口排序，一次发布有限数量并设置停止条件。

### 5. 独立经营

每个子体维护准确图片、属性、库存和适用广告；按真实表现补货或停产。

### 6. 父体健康审计

监控共享体验、评分、退货和选择复杂度；不通过拆并子体操纵评论或排名。

## 判断标准

- 一个父体真正贡献流量的子体可能有限，不能因共享关系无限扩张。
- 可小批定制和低换款成本是适用条件，但仍需验证每个子体需求。
- 历史评论共享只在合法真实变体关系下发生，不能作为设计变体的目的。

## 第三方 MCP 数据

需要外部关键词、竞品、评论或公开网页证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，并使用 `scripts/mcp_research.py`。

- 先动态执行 `tools/list`、`search-tools` 和 `describe`，依据实时 `inputSchema` 构造参数。
- 凭证只从环境变量读取，不进入参数、URL、Skill、终端输出或 Git。
- 可能计费的 `tools/call` 先展示 Provider、工具、无密钥参数、预计成本与输出位置，核对已有授权；仅在授权覆盖本次范围时使用 `--allow-cost`，该标志不是费用上限。
- 脱敏结果用 `--output` 写入 Skill 包之外的任务私有目录；不假设安装位置受仓库 `.gitignore` 保护。第三方数据标为估算或代理证据。
- 失败一次后记录缺口，不以重复付费重试掩盖不可用状态。

## 必须交付的结果

- 变体资格矩阵
- 元素/主题雷达
- 子体商业卡
- 发布与淘汰路线图
- 父体健康监控

结尾列出站点、数据窗口、证据来源、关键假设、缺口、风险、下一步和所有待批准动作。证据不足时写 `HOLD`，不得包装成可直接执行。

执行细节、证据字段和质量检查见 [references/playbook.md](references/playbook.md)。
