# 创意工作流与 prompt 结构

## 输入事实包

```yaml
marketplace:
asin:
product_type:
verified_features: []
prohibited_or_unverified_claims: []
audience:
occasion:
problem:
single_value:
proof_on_pdp:
brand_voice:
visual_system:
ad_objective:
format:
duration_or_dimensions:
must_include: []
must_avoid: []
```

## 发散矩阵

至少跨两个维度发散，而不是只换形容词：

| 维度 | 方向 |
|---|---|
| 人群时刻 | 首次使用、通勤、家庭、礼赠、专业任务 |
| 价值表达 | 痛点解决、现场演示、结果证据、对比选择标准 |
| 开场 | 商品动作、问题瞬间、前后状态、反常识问题 |
| 叙事 | 第一人称、步骤、场景切片、产品特写 |
| 信任 | 材料/结构、可验证规格、真实操作、售后事实 |

## 可执行 prompt

```text
Role: advertising concept collaborator
Task: create [N] concepts for [format]
Audience and moment: [...]
One verified value: [...]
Allowed facts only: [...]
PDP evidence: [...]
Brand voice and visual rules: [...]
Technical constraints: [...]
Must avoid: [...]
For each concept output: concept name, hook, scene sequence,
copy, product visibility, evidence locator, risks, and one testable hypothesis.
Do not invent missing product facts. Mark uncertainty as NEEDS_DATA.
```

## 筛选评分

每项 0–2 分：受众相关性、事实可证、单一信息、品牌差异、格式适配、移动端/无声可懂、制作可行、政策风险。任一事实或政策项为 0 时直接淘汰，不用总分抵消。
