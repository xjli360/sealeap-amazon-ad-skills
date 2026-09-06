# AI 运营模型

## 权限矩阵

| 环节 | AI 默认 | 人工职责 | 禁止自动化 |
|---|---|---|---|
| 市场/竞品研究 | 读、整理、候选 | 选择来源与决策标准 | 伪造不可用数据 |
| 选品 | 粗筛、评分、风险提示 | 样品/DFM/BOM/供应商/合规 GO | 下采购 |
| Listing/本地化 | 事实约束草稿 | 商品事实、母语、政策审核 | 直接发布 |
| 广告 | 诊断、实验草案 | 预算、账户、审批 | 无批准改 bid/budget/state |
| 库存 | 情景与风险 | 现金、仓储和补货决定 | 发货/移除/销毁 |
| 客服/复购 | 聚合主题、草稿 | 个案与政策审核 | 操纵评论/未经批准联系 |
| 风险 | 规则检查、告警 | 法律/合规决策 | 绕过平台控制 |

## 推荐架构

```text
scoped sources
  -> deterministic recall/filter
  -> model selection and reasoning
  -> evidence + rejected-candidate log
  -> human review
  -> approval card
  -> one scoped write
  -> read-back verification + rollback
```

规则先粗选，模型只接收相关候选；被模型拒绝的候选仍留在审计日志。

## 指标

- 能力：cycle time、人工审校分钟、返工率、事实错误、合规阻断、工具失败；
- 决策：候选→审核→实验→采用的转化；
- 业务：贡献利润、库存周转、退货、TACOS/广告利润、上新成功率；
- 安全：越权写入 0、跨主体泄漏 0、不可回退操作 0。
