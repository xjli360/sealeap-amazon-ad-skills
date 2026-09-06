---
name: sealeap-amazon-creative-ai
description: Turn verified Amazon product and audience evidence into reviewable AI-assisted advertising concepts, copy, image/video briefs, variants, and controlled creative tests. Use for 对话式AI广告素材, Creative Agent, Creative Studio, AI爆款素材, AI视频脚本, 商品广告创意, prompt共创, 素材A/B测试, POE/ABA insight-to-creative, or converting the authorized conversational-AI seller case into a repeatable workflow. Verify current tool availability and policy, keep human fact/brand/compliance review, and never publish generated assets or change live ads without explicit approval.
---

# Amazon 广告 AI 创意工作流

## 目标

把“让 AI 做一条爆款素材”改成可复核的创意实验：用真实商品、受众和目标约束模型，生成相互有意义差异的概念，逐条做事实/品牌/政策审查，再用预注册指标比较，而不是把一次好结果归因于 AI。

开始前读 [references/source-and-guardrails.md](references/source-and-guardrails.md)。生成概念和 prompt 读 [references/creative-workflow.md](references/creative-workflow.md)，审核与实验读 [references/review-and-testing.md](references/review-and-testing.md)。

## 工作流

### 1. 确认模式

- `IDEATE`：只生成方向；
- `BRIEF`：输出可交付给设计/视频团队的 brief；
- `GENERATE_PREP`：准备给当前可用 AI 工具的 prompt，不提交；
- `TEST_PREP`：做审核、版本管理和 A/B 草案；
- `APPROVED_PUBLISH`：仅在用户明确批准具体素材与投放对象后执行。

默认 `BRIEF`，不把工具入口存在等同于当前账户可用。

### 2. 建立事实包

至少需要 marketplace、ASIN、目标人群、使用场景、广告目标、允许的商品事实、禁用声明、品牌语气、格式/时长、PDP 证据和现有表现。可用 Product Opportunity Explorer、Brand Analytics、搜索词、评论主题和账户报告提供洞察，但必须保留来源、日期与作用域。

缺少商品事实时不让模型猜图中属性、材质、尺寸、兼容性或功效。

### 3. 写清创意命题

用一句话固定：`为[人群]在[场景]展示[经验证的单一价值]，目标是[行为]`。每个版本只改变一个创意假设，例如痛点、演示方式、开场钩子或叙事视角。

### 4. 人机共创

按 [references/creative-workflow.md](references/creative-workflow.md) 先发散 5–10 个概念，再按相关性、可证明性、差异化、无声/移动端可懂性和制作可行性筛到 2–4 个。将被拒概念与原因保留，避免下次重复。

### 5. 生成并版本化

每个产物记录 `asset_id / concept_id / prompt_version / model_or_tool / seed_if_available / source_assets / generated_at / editor / status`。AI 产物先标 `DRAFT_AI`；人工修订后标 `REVIEWED_DRAFT`，不能直接称“官方素材”或“已合规”。

### 6. 三层审核

1. `FACT`：所有文字与画面是否由商品档案支持；
2. `BRAND`：语气、视觉、Logo、目标人群和差异化是否一致；
3. `POLICY`：当前 Amazon 广告政策、类目限制、IP/肖像/商标、生成式内容要求和技术规格。

任一层 `HOLD` 就不进入测试。

### 7. 控制实验

固定人群、投放、预算、ASIN、PDP、时间逻辑和其它主要变量，只比较一个创意维度。预注册主指标、护栏、样本门槛、最大花费、停止线、归因成熟日和回退。

### 8. 复盘

分别报告素材生产效率与媒体效果。节省制作时间/成本不等于广告表现更好；CTR 上升不等于利润或增量销售上升。

## 必须交付

- 事实包、缺口与禁止猜测项；
- 创意命题、候选矩阵和筛选理由；
- 每个入选概念的 brief/prompt 与版本信息；
- FACT/BRAND/POLICY 审核表；
- 单变量测试卡和审批状态。
