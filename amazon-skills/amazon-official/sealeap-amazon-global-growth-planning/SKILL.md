---
name: sealeap-amazon-global-growth-planning
description: Build a human-governed global Amazon growth roadmap that connects AI-assisted insights, product/listing/localization/operations workflows, marketplace sequencing, and a verified opportunity calendar. Use for 亚马逊全球开店趋势, 跨境电商AI转型, AI智能体工作流, 全球站点布局, 节日商机日历, 复活节/樱花季/地球日/墨西哥儿童节, operator-to-decision-maker transition, or converting the authorized 2026 whitepaper and April poster into a measurable plan. Treat trend statistics, cases, dates, tools, and opportunity lists as snapshots; never automate protected business writes without explicit human approval.
---

# Amazon 全球增长与 AI 运营规划

## 目标

将“用 AI 做全球化”拆成有人负责、可验证、可暂停的运营链：AI 负责发现、整理和起草，人负责商品事实、经济性、合规、品牌和外部写入；站点与节日机会只有通过当前证据闸门才进入执行。

开始前读 [references/source-and-guardrails.md](references/source-and-guardrails.md)。建立 AI 工作流读 [references/ai-operating-model.md](references/ai-operating-model.md)，规划时机读 [references/opportunity-calendar.md](references/opportunity-calendar.md)。

## 工作流

### 1. 固定业务结果

选择一个 90–180 天结果：验证新站点、缩短 Listing 周期、提高补货准确性、降低广告浪费、建立新品管线或降低合规风险。不要以“部署 AI”作为结果。

### 2. 画当前流程

按洞察、选品、供应链、Listing/本地化、上架、广告、库存、客服/复购、风险分段，记录输入、系统、负责人、决策、外部写入和失败成本。

### 3. 给 AI 分配角色

- `ASSIST`：总结、翻译、格式化；
- `ANALYZE`：在有证据的数据上诊断；
- `DRAFT`：生成可审核方案；
- `RECOMMEND`：给出候选与证据/风险；
- `EXECUTE_AFTER_APPROVAL`：仅在逐对象批准后调用受保护操作。

高风险环节不得从 `DRAFT` 自动跳到 `EXECUTE`。

### 4. 选择站点/节日机会

白皮书与海报只生成候选。逐项验证当前日期、当地需求、竞争、product type、合规、库存/交期、本地化、贡献毛利和广告资格。用 [references/opportunity-calendar.md](references/opportunity-calendar.md) 输出 `GO / HOLD / REJECT`。

### 5. 构建证据链

每个决策保存来源、时间、站点、主体/账户、商品、原始指标、计算、假设和审批。外部工具不可用时把空缺写成 gap，不让模型补数字。

### 6. 设计最小工作流

先实现一个可逆闭环：读数据 → 粗筛 → 模型筛选 → 人工审核 → 草案 → 单对象批准 → 写后复读。保留被拒候选和原因，便于审计与迭代。

### 7. 衡量能力与业务

同时报告：处理时间、人工返工、事实/合规错误、建议采纳率，以及收入、贡献利润、库存、退货、广告效率等业务结果。生产效率不能替代业务效果。

## 必须交付

- 明确业务结果与当前流程；
- AI 角色/权限矩阵和人工闸门；
- 站点/节日候选及当前证据；
- 一个最小可逆工作流和失败处理；
- 能力指标与业务指标；
- `DRAFT / PILOT_READY / HOLD` 状态。
