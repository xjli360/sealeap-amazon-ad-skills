---
name: sealeap-baize-amazon-ai-image-pipeline
description: "Create evidence-backed Amazon image and A+ briefs with AI while preserving the real product's shape, color, scale, included components, and policy compliance. Use for AI做亚马逊商品图、主图差异化、副图和A+规划、评论洞察转视觉、图片测款. Not for fabricating the product."
---

# Amazon AI 商品图工作流

## 目标

Create evidence-backed Amazon image and A+ briefs with AI while preserving the real product's shape, color, scale, included components, and policy compliance.

## 不可妥协的边界

- 当前 Amazon 官方政策、账户资格、站点字段和一方数据优先于本 Skill 的经验框架。
- 第三方数据一律标为估算或前台观测，不得写成 Amazon 一方事实。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 一次实验只改变一个主要变量，并记录基线、样本、成功、停止和回退条件。
- 不得复制来源材料或竞品表达；输出必须按当前任务重新组织并可由现有证据支撑。
- 不得改变商品尺寸、颜色、结构、数量、配件或效果来提高转化。
- 公开评论抓取需遵守条款、隐私与最小化原则；优先使用自有授权数据。

## 先判断任务模式

1. **诊断**：读取现状、证据和缺口，不生成线上写入动作。
2. **方案草案**：输出可审核的结构、参数范围、实验和回退值。
3. **执行准备**：只生成待批准变更表或 API/控制台操作草案。
4. **已批准执行**：仅对用户在当前会话明确批准的对象和字段执行，并立即回读核验。

用户未指定时采用“诊断”。

## 开始前要拿到

- 目标 marketplace、产品事实、品牌语气和当前政策约束
- 已授权的 Listing、关键词、评论/VOC、图片和竞品证据
- 每项数据的来源、时间、站点、样本和限制
- 人工审核人、发布边界和不可生成的声明或视觉特征

缺失项必须标为 `NEEDS_EVIDENCE`；不得猜数字、补属性或把不同站点、ASIN、变体、币种和时间窗混在一起。

## 工作流

先读取 [references/playbook.md](references/playbook.md)，确认该方法适用于当前对象。按以下顺序执行：

1. 收集产品事实、实拍素材、竞品页面和合规评论洞察。
2. 提炼购买动机、异议、使用场景和一个可视化差异点。
3. 先生成逐张副图和 A+ brief：目标、构图、文案、证据、素材和禁改项。
4. AI 仅产出构图与效果草案，产品主体用真实照片或核准 3D 素材替换。
5. 主图单独按当前站点规则审核白底、占比、文字、道具和准确性。
6. 把视觉概念用于未来改款时，与当前在售 Listing 严格区分。

最后做数据充分性检查，并把结论分成 `FACT / ESTIMATE / HYPOTHESIS / UNKNOWN`。若关键证据不足，状态写 `HOLD`。

## 第三方 MCP 数据

仅在自有数据不足且当前任务确实需要外部证据时，读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，再使用 `scripts/mcp_research.py`。本 Skill 的外部取数目的：获取公开竞品页面与评论的有限样本；不得绕过登录、验证码或访问控制。

- 先 `doctor`，再 `search-tools` 和 `describe`；工具名及参数以实时 `tools/list` 与 `inputSchema` 为准。
- Token 只从环境变量读取。不得写入命令参数、URL、Skill、报告、日志或 Git。
- `tools/call` 或 Actor 可能计费；先展示 Provider、工具、无密钥业务参数、预计成本与输出位置，核对已有授权覆盖后才加 `--allow-cost`；该标志不是费用上限。


## 必须交付的结果

- 视觉证据板
- 逐张图片 brief
- 主图合规清单
- 实物一致性审核
- 数据范围、来源、采集时间、样本与限制。
- 关键假设、待补证据、风险和不可确定项。
- 若有动作：对象、旧值、新值、预期、停止条件、回退值与审批状态。

方案状态使用 `READY FOR REVIEW / DRAFT / HOLD / STOP`；如已执行，另行记录实际结果及回读证据。未得到明确批准时，不得声称已修改线上对象。
