---
name: sealeap-amazon-eu-amc-audience
description: "Diagnose and plan Amazon Marketing Cloud (AMC) analytics and audience activation for European Amazon Ads accounts, including journey/path analysis, time to conversion, reach and frequency, ad-type overlap, new-to-brand, rule-based and lookalike audiences, seasonal off-peak audiences, and SP/SB/SD/DSP activation. Use for 欧洲站 AMC, 亚马逊营销云, AMC 人群包, 潮汐人群, 转化路径, 广告叠加, DSP+AMC, 购买转化周期, 新客分析, 受众竞价加成, AMC query/use case selection, 或把《欧洲转化破局》材料转为可审批的数据与投放方案. Default to read-only analysis and draft actions; never expose user-level data or mutate campaigns/audiences without verified scope and explicit human approval."
---

# SeaLeap 欧洲站 AMC 受众与衡量

把欧洲站的增长问题转换为可审计的 AMC 分析、受众定义、激活草案和衡量方案。先确定业务问题和数据资格，再选择模型；不要先创建人群包，再寻找解释。

## 强制边界

- 把 AMC 定义为隐私安全的数据净室/分析与受众层，不把它说成普通广告报表、用户级 CDP 或直接投放系统。
- 只使用聚合、匿名化或假名化信号。不得尝试导出、重识别、拼接或推断个人身份；不得规避最小受众量、隐私阈值或查询抑制。
- 把源材料中的模型数量、受众窗口、触达频次、运行时长、案例成果和账户截图标为 `TRAINING_CASE`，不当作当前账户事实或官方通用门槛。
- 在使用前核对当前 AMC 实例、marketplace、广告主、可用表、lookback、受众资格、激活渠道、延迟和官方政策。欧洲各站不要无依据合并。
- 将 advertiser/profile/store/AMC instance ID 视为业务对象，不视为授权。只在服务端已验证的主体和站点范围内读取或写入。
- 默认只输出分析与草案。创建查询、保存受众、调整 audience bid、预算、竞价或状态前，逐项等待人工确认。
- 一张实验卡只改变一个主变量。路径、重叠和相关性不能单独证明增量或因果。

阅读 [references/source-and-guardrails.md](references/source-and-guardrails.md) 获取 PDF 页码映射、证据等级和内容限制。

## 工作流

### 1. 锁定问题、主体与站点

记录业务目标、国家站点、广告主、AMC instance、Ads profile、品牌/ASIN、广告类型、时间窗和负责人。把问题写成可回答句，例如：

- 哪些广告组合触达后更可能产生新客，而不是“哪个广告最好”；
- 旺季曝光未购买人群是否值得淡季再营销；
- 高客单产品从首次触达到购买需要多久、多少次触达；
- SP/SB/SD/DSP 的路径和重叠是否支持预算或频次假设。

### 2. 通过就绪门

检查实例与权限、站点和时区、数据覆盖、广告活动映射、转化定义、归因/回看窗口、隐私阈值、受众可激活性、库存和退货后利润。使用 [references/readiness-and-europe.md](references/readiness-and-europe.md)。

缺少关键条件时输出 `HOLD / NEEDS_DATA`；不要把 `No results returned` 自动解释为零，也不要默认数据在其他页面必然存在。

### 3. 选择最小分析模型

按问题只选必要模型：

| 业务问题 | 首选分析 | 主要输出 |
|---|---|---|
| 决策周期 | Time to Conversion | 转化耗时分布与对比 |
| 渠道先后关系 | Path to Conversion by Campaign Groups | 路径、触点顺序、辅助触达 |
| 重复覆盖 | Ad-type overlap / reach-frequency | 独占、重叠、频次与浪费假设 |
| 拉新 | New-to-brand | 新客购买/销售占比与路径 |
| 旺季长尾 | Seasonal off-peak exposure | 旺季曝光未转化候选受众 |
| 人群扩展 | Rule-based / lookalike | 精准规则或相似拓展草案 |

阅读 [references/analysis-models.md](references/analysis-models.md) 获取指标定义、对比原则和误读防护。

### 4. 定义受众而非复制案例

用“纳入条件 + 排除条件 + 时间窗 + marketplace + 预估规模 + 用途 + 到期日”定义受众。根据问题选择规则型或相似型；不要把拼图桌案例中的 30/60/90 天窗口套给所有产品。

阅读 [references/audience-playbooks.md](references/audience-playbooks.md) 获取潮汐人群、探索者、痛点/场景、竞品关注者和全漏斗分层方法。

### 5. 生成激活草案

明确激活位置是 SP、SB、SD 还是 DSP，以及 `include`、`exclude`、竞价加成、再营销或相似拓展中的哪一个。先确认当前控制台支持该受众与操作，再创建单变量动作卡。

使用 [references/activation-and-measurement.md](references/activation-and-measurement.md) 设计基线、对照、冷却期、延迟、主指标和停止条件。

### 6. 审批、执行与复盘

- 在动作卡中展示原值、新值、估算成本、利润/频次/库存护栏、受众定义和回退值。
- 只有 `APPROVED` 且 scope 已验证时才能写入；审批一个受众不等于批准修改所有关联 campaign。
- 保存查询版本、参数、运行时间、数据覆盖、受众状态、激活时间和干扰项。
- 到期后关闭或复核受众，避免历史窗口永久运行。

使用 [references/output-contract.md](references/output-contract.md) 交付。

## 必须交付

- 对象、站点、授权、时间/时区、数据覆盖和限制；
- 业务问题与为何选择该 AMC 模型；
- 查询/模板参数、指标字典和结果解释；
- 受众纳入/排除、窗口、规模状态和隐私门槛；
- 激活渠道、单变量动作卡、审批与回退；
- 对照/增量设计、归因延迟、利润和库存护栏；
- `ACCOUNT_FACT`、`CURRENT_POLICY`、`TRAINING_CASE` 与 `HYPOTHESIS` 的明确分离。

证据不足时给出下一步取数清单，不编造 audience size、ROAS、频次或增量结论。
