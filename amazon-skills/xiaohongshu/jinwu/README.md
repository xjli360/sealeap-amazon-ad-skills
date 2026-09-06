# 金乌：筛选型经营、转化诊断与广告判断

本集合包含 9 个中等粒度匿名 Amazon Skill，覆盖 68 个短视频语义单元。`jinwu` 是匿名神兽代号，不承载素材来源身份。所有聚类只发生在 `jinwu` 内部，且保持同一业务域；不会与其他创作者集合交叉。

本集合源自一位以筛选型（精铺）经营为主线的亚马逊卖家的短视频问答，内容偏向‘先判断再动手’：先分清产品力与广告问题，再决定预算、竞价、关键词与备货；所有经验阈值均已降级为待验证假设。

| 业务域 | Skill | 专项焦点 | 语义单元 |
|---|---|---|---:|
| 跨境经营模式 | [sealeap-jinwu-amazon-lean-catalog-operating-model](sealeap-jinwu-amazon-lean-catalog-operating-model/) | 精铺与精品的模式选择、FBA 与自发货起步、只筛选不培养 | 10 |
| 平台、政策与多渠道 | [sealeap-jinwu-amazon-platform-policy-scenarios](sealeap-jinwu-amazon-platform-policy-scenarios/) | 第二平台评估、关税与免税政策情景推演、新兴站点与企业购、内容平台与站外流量 | 8 |
| 选品与产品开发 | [sealeap-jinwu-amazon-product-selection-scorecard](sealeap-jinwu-amazon-product-selection-scorecard/) | 四项核心选品指标、大卖看不上的细分切入、标品与非标品的结构差异、工厂首批小单框架 | 7 |
| 转化诊断 | [sealeap-jinwu-amazon-conversion-root-cause](sealeap-jinwu-amazon-conversion-root-cause/) | 三步排查顺序、流量准确性 vs 产品力、细分市场转化基准、补货决策的数据陷阱 | 10 |
| 广告预算、竞价与调整节奏 | [sealeap-jinwu-amazon-ad-budget-bid-cadence](sealeap-jinwu-amazon-ad-budget-bid-cadence/) | 加预算还是加竞价、调整频率的数据判据、分时与广告位倍率、自动广告竞价分档 | 8 |
| 关键词结构与否定 | [sealeap-jinwu-amazon-keyword-structure-negatives](sealeap-jinwu-amazon-keyword-structure-negatives/) | 标品与非标品的关键词广度、词库四维分类、按词级投产模型选词、否定的‘不准确 ≠ 不相关’ | 7 |
| 新品期与自然流量 | [sealeap-jinwu-amazon-new-product-organic-traffic](sealeap-jinwu-amazon-new-product-organic-traffic/) | 新品期起算点、自然单与广告单的比例诊断、关键词排名的三个驱动量、促销与价格带 | 8 |
| 目录与库存运维 | [sealeap-jinwu-amazon-catalog-inventory-operations](sealeap-jinwu-amazon-catalog-inventory-operations/) | 批量表格作为恢复能力、后台 AI 助手拆合变体、临近断货的广告处理、站外低价导致的购物车丢失 | 4 |
| 合规、评论与知识产权 | [sealeap-jinwu-amazon-compliance-reviews-ip](sealeap-jinwu-amazon-compliance-reviews-ip/) | 知识产权三类初筛、请求评论与差评沟通的边界、早期评论计划的解读、竞品异常起量的证据链 | 6 |

每个 Skill 的执行细节见其 `references/playbook.md`，逐卡方法见 `references/topic-cards.md`，调用入口见 `agents/openai.yaml`。

原始去标识化语义稿逐条保存在 Git 忽略目录。公开文件不保存来源账号、链接、笔记编号、发布日期、互动量或原始话术；所有 Skill 默认只读，任何采购、发布、广告、库存、价格、账户、评价或外部系统写操作必须先展示影响并取得明确批准。
