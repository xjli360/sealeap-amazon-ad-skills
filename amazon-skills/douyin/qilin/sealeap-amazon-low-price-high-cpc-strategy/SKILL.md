---
name: sealeap-amazon-low-price-high-cpc-strategy
description: Evaluate and improve low-price, high-CPC Amazon products using break-even economics, legitimate bundles or multipacks, long-tail traffic, low-bid discovery, creator channels, and original video ads. Use when a product has thin margin, expensive clicks, or cannot profitably scale Sponsored Products. Respect variation, IP, and creator-program rules and keep execution behind approval.
---

# Amazon 低客单高 CPC 破局

## 目标

先量化利润薄与点击贵的矛盾，再从真实客单提升和获客成本下降两侧设计可验证方案。

## 适用任务

- 低售价商品在核心词上无法承受 CPC。
- 评估组合装、多件装、达人或视频广告是否有经济性。
- 决定继续优化、改变商品形态还是退出。

## 开始前要拿到

- 单件与组合装的完整费用、售价、退货和贡献利润。
- 按词和广告类型的 CPC、CVR、CPA 与预算。
- 可用原创素材、品牌资产和官方创作者或联盟渠道资格。

缺失的数据要明确列为缺口，并把结论标成事实、估算或假设；不要补造数字。

## 不可妥协的边界

- 组合装或变体必须是真实可购买且符合类目规则的商品，不得只为展示低价或共享评价。
- 不得下载、剪辑或投放未经授权的竞品视频；只用自有、许可或正式委托素材。
- 达人合作必须遵守披露、佣金、评价和站外引流政策。
- 当前 Amazon 官方政策、帮助页、账户资格和后台实际字段优先于本 Skill 中的经验框架；规则可能变化时先核验。
- 默认提供诊断或草案。写入前展示对象、旧值、新值、影响、停止线与回退，核对用户已有授权是否覆盖对象、动作与预算；范围已明确授权时继续执行并回读核验，只有未覆盖或扩大的范围才请求批准。
- 不输出原素材的创作者身份、账号、链接、视频编号或可反查线索；当前业务证据的官方来源、采集时间和口径仍需保留。

## 第三方 MCP 数据

只有在本任务确实需要外部市场、竞品、关键词或公开网页证据时，才读取 [references/mcp-data-plan.md](references/mcp-data-plan.md)，并使用 scripts/mcp_research.py。

- 先动态执行 tools/list、search-tools 和 describe，依据实时 inputSchema 构造参数，不照搬历史工具名。
- 凭证只从环境变量读取，不放进命令参数、URL、Skill、结果文件或 Git。
- tools/call 可能计费。调用前展示 Provider、工具名、无密钥参数、预计成本与输出位置，核对已有授权覆盖后才加 --allow-cost；该标志不是费用上限。
- 第三方数据标为估算或代理证据，记录 Provider、工具、无密钥参数、查询时间和原始结果位置；失败一次后记录缺口，不反复消耗额度。
- 脱敏结果用 --output 写到 Skill 包之外的任务私有目录；不假设安装位置受仓库 .gitignore 保护，不把运行结果写入 Skill 包。

## 工作流

### 1. 建立经济底线

计算单件和各组合装的盈亏平衡 ACoS、CPA 与 CPC，包含配送费、佣金、优惠和退货。

### 2. 评估客单提升

测试真实多件装、配件组合或价值升级，检查价格弹性、库存复杂度和转化变化。

### 3. 重构搜索预算

从高竞争核心词抽出一部分预算，验证高意图长尾、低竞价探索和更适合的商品目标。

### 4. 比较替代渠道

核算官方创作者合作、品牌视频或其他合规广告的总获客成本，而不是只比较表面 CPC。

### 5. 测试原创素材

围绕前三秒、使用场景、证明点和 CTA 建立素材矩阵，每次控制一个变量并保留版权记录。

### 6. 做组合决策

按利润、规模、运营复杂度和风险给出保留、转型、缩量或退出建议。

## 判断标准

- 所有方案比较的是贡献利润而非只看 ACoS。
- 组合装与素材均有真实性和权利链证明。
- 低竞价流量没有挤占主力预算或制造无效点击。

## 必须交付的结果

- 单件与组合装单位经济表。
- 搜索、商品、视频和创作者渠道对比。
- 分阶段实验与止损规则。
- 保留、转型、缩量或退出结论。

结尾列出数据窗口、关键假设、证据缺口、风险和下一步；如包含待执行动作，单独放在“待批准变更”中。
