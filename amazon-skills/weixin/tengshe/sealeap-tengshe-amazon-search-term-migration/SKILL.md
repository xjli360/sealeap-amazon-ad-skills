---
name: sealeap-tengshe-amazon-search-term-migration
description: "Migrate proven Amazon customer search terms from broad, phrase, or automatic discovery into controlled exact targeting while checking overlap, economics, negatives, and sample quality. Use when harvesting high-performing queries."
---

# Amazon 搜索词精准迁移

## 目标

区分后台关键词与买家实际搜索词，只把有重复相关和经济证据的查询迁入精准结构，并在否定原来源前检查增量与重叠。

## 何时使用

- 广泛/词组/自动活动出现出单搜索词
- 不知道迁移 target 还是 customer search term
- 考虑精准化、加否定或独立预算

## 开始前要拿到

- 同一窗口的 targeting 与 search term 报告
- target、matched query、匹配类型、点击、订单、CVR、CPC 和销售
- 贡献毛利、目标 ACOS/ROAS、预算和库存
- 现有精准词、重复活动、否定项、位置与页面变更

缺失项必须标为 `UNKNOWN` 或 `NEEDS_EVIDENCE`；不得猜数字、补属性，或混用不同站点、ASIN、币种和时间窗。

## 不可妥协的边界

- 当前 Amazon 官方规则、目标账户实时状态和一方业务报告优先；公开内容与第三方数据只能作为待验证启发或代理证据。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 数值、政策、因果和执行状态分别标为 `FACT`、`ESTIMATE`、`ASSUMPTION` 或 `UNKNOWN`。
- 不保存或输出素材来源身份、账号、链接、文章编号、发布日期、阅读量、原始话术或其他可反查线索。
- 个案、论坛回答和示例 SQL 只能形成候选方法，不能证明普遍因果。
- 后台投放关键词与实际搜索词不可混淆；迁移对象通常应是可验证的客户查询。
- 一次偶然订单不足以证明稳定性；按点击、订单重复性、相关性和利润设门槛。
- 迁移后不自动否定原来源，先评估发现价值、流量重叠和总业务影响。

## 工作流

1. 对齐 targeting 和 search term 报告的站点、窗口、归因和对象。
2. 把 target 与实际查询分栏，清理拼写、变体、品牌和不相关意图。
3. 按相关性、重复订单、CVR、CPC、利润和样本质量筛选迁移候选。
4. 为候选建立精准广告单元，按经济性定价；SP 需要独立预算时拆分 campaign，先保留原发现来源用于比较。
5. 检查现有精准覆盖与内部竞争；仅在有证据时对原来源加否定。
6. 观察总查询表现、发现量和净贡献，决定保留、调价、回退或继续发现。

## 判断状态

- `READY`：当前规则、输入、基线和动作边界均已核实。
- `HOLD`：方向可能成立，但关键数据、样本、资格或审批仍缺失。
- `STOP`：存在违规、隐私越界、经济性不可承受、数据不可解释或无法回退。

## 必须交付的结果

- target—查询映射表
- 候选证据与拒绝原因
- 精准迁移/否定草案
- 迁移前后总业务复盘
- 数据范围、采集时间、定义、证据状态、限制和待批准动作

详细台账与质量门见 [references/playbook.md](references/playbook.md)。

