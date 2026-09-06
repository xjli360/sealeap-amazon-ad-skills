# Xiezhi Amazon Skills

本集合包含 35 个独立、可复用的 Amazon 工作流 Skill。每个 Skill 都有独立触发描述、证据要求、执行步骤、风险边界和输出契约；涉及第三方数据的 Skill 另带安全 MCP 客户端与凭证占位说明。

`xiezhi` 是匿名集合代号，不承载素材来源身份信息。仓库中不保存音视频、原始逐字稿、账号、链接、作品编号或互动数据。

## MCP 凭证

真实凭证只由用户在本地环境或密钥管理器中注入：

```bash
export SIF_MCP_SECRET_KEY='由用户本地填写'
export SELLERSPRITE_MCP_SECRET_KEY='由用户本地填写'
export APIFY_TOKEN='由用户本地填写'
```

不要提交真实值。所有可能消耗额度的调用都必须先 dry-run 并取得明确批准。

## Skill 索引

| Skill | 用途 | 目标 |
|---|---|---|
| `sealeap-xiezhi-amazon-three-factor-opportunity-screen` | Amazon 三因子机会粗筛 | 用销量、价格和评论三维启发式快速减少样本，再对陌生细分机会做严格二次验证。 |
| `sealeap-xiezhi-amazon-ad-efficiency-benchmark` | Amazon 广告效率竞品基准 | 用同口径竞品组比较广告覆盖与销量代理，识别低评论样本是否能靠少量精准流量正常出单，并把结论限定为代理指标。 |
| `sealeap-xiezhi-amazon-ad-relevance-weight-bootstrap` | Amazon 广告相关性启动 | 用精准购物意图、页面一致性和受控学习预算积累可解释的点击与转化信号，而不是依赖未经证实的权重公式。 |
| `sealeap-xiezhi-amazon-ai-product-research-governance` | Amazon AI 选品判断治理 | 让 AI 承担批量取数、整理和反证，而把竞品定义、需求真实性、差异化取舍与最终立项保留在人类决策门内。 |
| `sealeap-xiezhi-amazon-audience-first-product-discovery` | Amazon 人群优先选品 | 从身份明确且需求持续的人群出发，把其生活与活动场景转化为一条可验证的产品机会线。 |
| `sealeap-xiezhi-amazon-broad-plus-exact-launch-keywords` | Amazon 广泛加精准新品词路由 | 从直接竞品自然排名中提炼高相关词，用少量广泛词探索表达、精准词承接明确意图，并以搜索词证据持续迁移。 |
| `sealeap-xiezhi-amazon-commodity-bundle-repositioning` | Amazon 成熟产能组合重定位 | 利用成熟供应链的小批量与成本优势，通过真实场景、数量和组合设计提高价值，而不是简单加量卷规格。 |
| `sealeap-xiezhi-amazon-conversion-diagnostic-ladder` | Amazon 转化率分层诊断 | 先查商品与页面承接，再查广告流量，最后判断产品竞争力和可达市场份额，避免用调竞价掩盖根因。 |
| `sealeap-xiezhi-amazon-conversion-rate-prelaunch-estimation` | Amazon 上市前转化率估算 | 用头部链接和细分市场两种口径交叉估算转化率，再判断保本 CVR 是否现实。 |
| `sealeap-xiezhi-amazon-cpc-cvr-opportunity-gate` | Amazon CPC-CVR 机会快判 | 用精准流量成本和可达转化区间淘汰明显无法盈利的候选，把深研资源留给有证据的方向。 |
| `sealeap-xiezhi-amazon-cross-category-attribute-keyword-research` | Amazon 跨类目通用词选品 | 以消费者可搜索的通用属性为入口跨类目发现需求，再用盈利与竞争门槛收敛，而不是依赖一套固定参数。 |
| `sealeap-xiezhi-amazon-demand-driver-backtracking` | Amazon 热销需求驱动回溯 | 把销量当作结果而非答案，追溯真实购买动因，再横向扩场景、纵向扩人群和产品形态。 |
| `sealeap-xiezhi-amazon-evergreen-variation-roadmap` | Amazon 长期变体路线图 | 通过真实、合规且有独立需求的子体持续扩展产品线，同时把每个变体当作独立经济单元管理。 |
| `sealeap-xiezhi-amazon-factory-capability-market-matching` | Amazon 工厂能力与市场匹配 | 不把供应链优势误当市场优势，而将材料与工艺能力组合到具体人群、场景和任务中寻找可经营需求。 |
| `sealeap-xiezhi-amazon-first-product-low-risk-screen` | Amazon 首款产品低风险筛选 | 为首款产品建立需求、竞争、精准词、广告成本和供应链风险的最小可行闸门。 |
| `sealeap-xiezhi-amazon-high-ticket-unit-economics-gate` | Amazon 高客单单位经济闸门 | 不把高价当作机会本身，而用实际成本、CPC 与 CVR 验证更高售价是否带来足够的广告和清货容错。 |
| `sealeap-xiezhi-amazon-low-review-new-entrant-validation` | Amazon 低评论新品机会验证 | 不以首页老链接数量下结论，而通过近期低评论新品的正常增长和明确购买理由判断市场是否仍有入口。 |
| `sealeap-xiezhi-amazon-market-acos-feasibility` | Amazon 市场 ACoS 可承受性 | 把 ACoS 拆回 CPC、CVR、售价、贡献毛利和复购价值，先判断商业模型能否承受市场，再选择广告动作。 |
| `sealeap-xiezhi-amazon-niche-market-profitability-screen` | Amazon 冷门细分盈利筛选 | 把冷门定义为有精准需求、可解释的正常销量和较低直接竞争，并用单位经济与库存边界验证。 |
| `sealeap-xiezhi-amazon-product-knowledge-map-building` | Amazon 产品认知地图训练 | 先扩大对海外产品、人物和场景的认知，再把陌生商品转化为可继续研究的需求线索，而不是立即判断做或不做。 |
| `sealeap-xiezhi-amazon-product-selection-eight-gates` | Amazon 选品八道闸门 | 用八个相互独立的门槛把候选从有趣方向推进到可审计立项，任何关键证据缺失都保持 HOLD。 |
| `sealeap-xiezhi-amazon-product-test-decision-tree` | Amazon 产品测款决策树 | 只验证尚未被证据回答的最大不确定性，并用真实可履约库存、最小样本和明确止损控制测试成本。 |
| `sealeap-xiezhi-amazon-product-to-market-repositioning` | Amazon 产品到细分市场重定位 | 从产品资源出发寻找新的购买对象、场景和关键词，使竞争集合与价值主张真正改变。 |
| `sealeap-xiezhi-amazon-profit-bound-ad-operations` | Amazon 盈利边界广告运营 | 从选品阶段就限定精准流量和可承受点击，用小型广告结构寻找每个 SKU 的盈利流量区间，并及时降级失败品。 |
| `sealeap-xiezhi-amazon-red-ocean-micro-niche-discovery` | Amazon 红海微细分发现 | 从红海类目中定位近期正常做起的低评论差异样本，提取其精准属性，再发现未被充分覆盖的相邻微细分。 |
| `sealeap-xiezhi-amazon-scalable-portfolio-six-lanes` | Amazon 可复制组合六赛道 | 按团队能力把候选分入六种结构性机会赛道，每种赛道使用独立证据和风险门槛。 |
| `sealeap-xiezhi-amazon-scalable-product-portfolio-model` | Amazon 可复制产品组合模式 | 把单条链接的偶然成功转化为可复制的选品、供应链、推广、补货和淘汰系统，并控制单品依赖风险。 |
| `sealeap-xiezhi-amazon-scenario-keyword-product-discovery` | Amazon 场景词选品 | 先找到可搜索的具体场景，再为该场景中的消费者挑选产品，从而把大众商品迁移到更清晰的细分需求。 |
| `sealeap-xiezhi-amazon-scenario-led-differentiation` | Amazon 场景驱动差异化 | 在不盲目开模的前提下，用真实人群与使用任务重定义产品，使关键词、竞品、页面表达和购买理由同步改变。 |
| `sealeap-xiezhi-amazon-seasonal-blue-ocean-screening` | Amazon 季节性冷门机会筛选 | 从历史月份和未来进场窗口中找出有明确需求、直接竞品较少且能继续验证的候选细分市场。 |
| `sealeap-xiezhi-amazon-seasonal-keyword-growth-discovery` | Amazon 季节关键词增长选品 | 通过历史同比/环比和目标月份的搜索增长寻找事件型精准词，再从低价入口产品扩展更可盈利的同场景需求。 |
| `sealeap-xiezhi-amazon-seasonal-listing-lifecycle` | Amazon 季节 Listing 生命周期 | 把季节产品当作可复盘的年度循环，沉淀真实评价、素材、供应和广告经验，同时严格遵守变体与评价政策。 |
| `sealeap-xiezhi-amazon-seasonal-portfolio-calendar` | Amazon 季节活动产品组合日历 | 把每月不同的节日与社会活动需求编排成滚动产品组合，并以提前布局和保守库存控制季末风险。 |
| `sealeap-xiezhi-amazon-small-budget-fba-validation` | Amazon 小预算 FBA 验证 | 以资金上限和学习目标为约束，用少量真实产品完成注册、选品、采购、入仓、销售与回款闭环，并保留退出能力。 |
| `sealeap-xiezhi-amazon-store-order-capacity-scaling` | Amazon 店铺订单承载扩张 | 把货架宽度与店铺真实承载能力分开，按订单稳定性、利润、库存和团队容量分阶段扩充 SKU。 |
