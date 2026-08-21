# AMC 就绪门与欧洲站范围

## 1. 资格与权限

确认：

- advertiser、Ads profile 与 AMC instance 的绑定关系；
- 当前用户/服务账号具有查询、受众或激活所需的最小权限；
- 目标广告类型与 marketplace 的数据已进入实例；
- 受众可否激活到目标 SP/SB/SD/DSP，以及生效延迟；
- 接受协议、实例可见和 campaign 管理授权是不同状态。

任何一项未知都标记 `NEEDS_DATA`。不要因为能看 Ads 报表就推断拥有 AMC 或 audience 权限。

## 2. 数据覆盖

至少记录：

- 数据起止日、查询执行时间、时区、币种和 marketplace；
- 纳入的 campaign/ad product、ASIN、品牌、转化事件与订单范围；
- attribution/lookback、conversion lag、退货延迟和数据抑制；
- campaign 重命名、重建、停投、促销和缺货等断点；
- audience size 状态与是否达到当前隐私/激活门槛。

`No results returned` 可能来自筛选、字段、表、窗口、权限、延迟或隐私阈值；先排查口径，再判断业务结果。

## 3. 欧洲站分层

- 按 UK、DE、FR、IT、ES、NL、SE、PL、BE 等实际账户分别确认，不预设可跨站共享。
- 保留当地语言、货币、VAT/价格、配送、退货、节日和促销差异。
- 统一分析前先定义汇率日、税前/税后收入和同一转化口径；否则只做站点内比较。
- 高客单价或长决策周期是假设入口，不是自动增加再营销频次的理由。

## 4. 业务可执行性

在生成受众前检查：

- Listing、Buy Box、库存和配送是否支持流量；
- 退货后贡献利润和盈亏平衡 CPA/ROAS；
- 创意、落地页与当地语言是否匹配受众意图；
- 旺季结束日、补货周期和受众/归因延迟；
- 是否有可比较的基线、对照或分阶段设计。

若不可执行，保留分析价值但将激活状态设为 `HOLD`。

## 5. 就绪结论

输出以下之一：

- `READY_FOR_ANALYSIS`：可运行只读分析；
- `READY_FOR_AUDIENCE_DRAFT`：可定义人群但未批准创建；
- `READY_FOR_APPROVAL`：参数、风险和回退齐全；
- `HOLD`：列出明确缺口和解除条件。
