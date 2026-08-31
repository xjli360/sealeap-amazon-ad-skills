# 来源与护栏

## 授权源与规范化数据

- 原文件：`亚马逊会员日 - 数据洞察.xlsx`；1 个工作表，116 条记录；SHA-256 见根目录 `SOURCE_COVERAGE.md`。
- 规范化副本：`references/prime-day-insights-2025.csv`；列为 `Family Brief, Content, Metrics, Ad Products, Marketplaces`；逐行保留原英文洞察与限定条件。
- 规范化只改变容器格式，不翻译或拆除 `Content` 内 qualifier。

## 数据快照

- 数据均为 Consumables 或其细分切片，不应外推到所有类目；
- 指标分布：ROAS 41 条、DPV 38 条、Units 26 条、Sales 11 条；
- 广告产品组合并不均衡，包含 Sponsored Ads 总称、SP、SB、Display 及组合；
- uplift 行的基准期为 2025-06-29 至 2025-07-05，事件期为 2025-07-06 至 2025-07-12；
- ROAS 行按 2025-07-06 至 2025-07-12 衡量；
- 各行常带最低花费、Seller/GGS、brand owner、domestic、High GMS 等限制。

## 禁止操作

- 不把所有行平均成“Prime Day 行业基准”；
- 不比较不同行的 ROAS 与 uplift 当成同一指标；
- 不忽略 `Content` 中的资格条件；
- 不把区域行覆盖到未列出的 marketplace；
- 不把 2025 结果预测为当前活动表现；
- 不因数据来自 Amazon 内部就省略当前账户、库存和利润核验。

## 引用格式

引用某条记录时同时给出：`row number + marketplace + metric + ad product + value + dates + full qualifier summary`。CSV 首行为表头，数据行从 2 开始。
