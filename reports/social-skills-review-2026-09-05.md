# Douyin / Weixin Amazon Skills 检查与优化

2026-09-05。已检查并优化 `amazon-skills/douyin` 的 211 个 Skill 和 `amazon-skills/weixin` 的 50 个 Skill，保留原有 12 个匿名集合及各 Skill 的独立安装结构。问题集中在运行指令、业务指标口径、执行手册入口和共用 MCP 脚本；原有 261 个入口本身均能通过基础 frontmatter 校验。

## 已修正的问题

| 问题 | 最终调整 |
|---|---|
| 109 个聚类入口仍描述素材整理任务，并把集合边界当作运行限制 | 描述改为实际业务任务与触发条件；允许用户要求的跨来源交叉验证，保留来源归属及去标识化要求。 |
| 证据卡大量使用主题标签充当字段 | 2,310 处字段定义改为可填写的业务证据项，并明确分析台账字段不能直接作为 API 参数。素材出现次数仅表示覆盖情况，不作为市场需求或成功概率。 |
| 部分手册缺入口或遗漏工作流步骤 | 为 35 个 Skill 补齐执行手册链接，补齐 35 处遗漏步骤，移除 109 处重复入口。编号工作流与对应表格统一。 |
| 界面描述不符合长度要求 | 修复 87 个 `short_description`，保留原有其他元数据；默认提示中的授权表述同步调整。 |
| 每件、每单、点击与访客、归因收入与净收入混用 | 修正 CPC、CPA、CVR、ACoS 计算条件，明确多件订单与零分母处理。全渠道销量除以搜索点击不再作为有效 CVR；建议竞价不再等同于实付 CPC。 |
| 广告判断过度机械化 | 单变量要求限于需要归因的常规实验；允许已授权的止损或合规处置记录协调变更。独立 Sponsored Products 预算落实到 Campaign；自然订单和增量不能简单由归因报表差值推断。 |
| 平台迁移及市场取样存在错误承诺 | 变体回退先核验当前仍有效的主题与映射；商品检索记录样本上限、分页和遗漏，取消未经证明的“全量市场”说法。 |
| 已有授权在多个模板中被忽略 | 核对对象、动作、预算与现有授权后继续执行；未覆盖或扩大的范围才另行请求批准。方案状态与实际执行、回读证据分开记录。 |

例如，[上市前 CVR 估算](../amazon-skills/douyin/xiezhi/sealeap-xiezhi-amazon-conversion-rate-prelaunch-estimation/SKILL.md) 现在要求订单与点击来自可比流量范围；[账户合规证据卡](../amazon-skills/douyin/pixiu/sealeap-pixiu-amazon-account-compliance/references/topic-cards.md) 现在能直接用于建立证据台账。

## MCP 调用改进

180 份独立安装用的 `mcp_research.py` 已同步为同一实现，配套 180 份数据计划也已更新。保留分发副本，并用统一校验检测后续漂移。

- 完整输入校验使用 JSON Schema，覆盖嵌套对象、类型、枚举、范围、分支及本地引用。支持从 `describe` 导出 schema 做离线预检；真实调用重新校验在线 schema。拒绝重复 JSON 键、非有限数值和远程 schema 引用自动取数。
- 可能计费的调用先检查输出位置与授权标志。Apify Actor 执行额外绑定确切 `owner/name`；不能把工具名称、注解或 `--allow-cost` 当作公开数据授权和费用上限。
- 真实调用必须指定任务私有结果路径，结果文件权限为 `0600`。默认不覆盖，明确指定 `--force` 时原子替换；调用出错或保存失败时保留旧文件，并尽量另存已收到的完整脱敏响应及 run/request ID。不会自动重发可能计费的请求。
- 拒绝携带凭证的重定向，校验错误避免打印业务参数值；输出按结构脱敏，避免破坏 JSON。SSE 收到对应请求的结果即可结束读取，增加响应大小和超时边界。
- `doctor` 与本地 `--dry-run` 不访问 MCP。无 schema 的 dry-run 明确只是预览。独立安装时，结果保存不再依赖原仓库的 `.gitignore`。

可从任一 Skill 的 [MCP 数据计划](../amazon-skills/douyin/pixiu/sealeap-pixiu-amazon-account-compliance/references/mcp-data-plan.md) 查看依赖、命令和失败恢复路径。完整参数校验新增运行依赖 `jsonschema>=4.18,<5`；离线 doctor 和无 schema 的参数预览仍使用标准库。

## 验证结果与复用

| 检查 | 结果 |
|---|---|
| skill-creator 基础校验 | 261 / 261 通过 |
| 界面元数据与本地资源引用 | 261 份元数据、1,082 处本地引用通过；参考文档均可从入口到达 |
| 编号工作流与手册表格 | 179 / 179 一致；其他手册采用非编号结构 |
| Python 编译、脚本一致性与离线 doctor | 180 / 180 通过，脚本 SHA256 全部相同 |
| 离线回归测试 | 26 / 26 通过，覆盖有效调用及参数、费用、输出冲突、脱敏、传输和失败恢复 |
| 独立行为复核 | 同一脚本版本完成 18 个模拟场景；包括线上 schema 变化、Actor 标识绑定和失败证据保留 |

机器可读结果见 [全目录校验](social-skills-validation-2026-09-05.json) 和 [独立行为复核摘要](social-skills-forward-evaluation-2026-09-05.json)。后者的第 18 个场景专门证明：Actor 标识相同不能阻止输入换成未获授权的 URL，因此仍须按数据计划审核实际输入与范围。

从仓库根目录复验：

```bash
uv run --no-project --with pyyaml --with 'jsonschema>=4.18,<5' \
  python -B scripts/validate_social_skills.py --doctor

uv run --no-project --with 'jsonschema>=4.18,<5' \
  python -B -m unittest discover -s tests -p test_social_skill_mcp.py
```

验证脚本见 [validate_social_skills.py](../scripts/validate_social_skills.py)，回归用例见 [test_social_skill_mcp.py](../tests/test_social_skill_mcp.py)。测试使用合成响应并阻止真实网络请求；没有使用真实业务凭据或执行付费 MCP 调用。供应商在线可用性、真实计费、Actor 实际行为及各账户当前政策资格仍需在实际任务中验证。

本次保留了进入任务时的 Git 暂存区，未执行 `git add`、`commit` 或 `push`。目录中的既有移动与未提交工作保持原状；以上修改及新增校验材料位于工作区。

## 技术与业务口径依据

- [MCP 工具规范](https://modelcontextprotocol.io/specification/2025-11-25/server/tools)：输入 JSON Schema、工具错误与结构化结果，以及工具注解的信任边界。
- [MCP Streamable HTTP](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)：JSON / SSE 响应处理、请求与会话语义。
- [Apify MCP 官方文档](https://docs.apify.com/integrations/mcp)：Actor 发现、执行与输出获取；具体参数和计费覆盖须再核对选定工具。
- [Amazon Sponsored Products 指南](https://advertising.amazon.com/en-us/library/guides/sponsored-products-best-practices/)：Campaign 预算与广告组组织口径。
- [SIF MCP 接入说明](https://blog.sif.com/article/mcp-install/Sif-MCP安装文档) 与 [SellerSprite MCP 接入说明](https://open.sellersprite.com/mcp/16)：服务入口及请求头认证方式；本工具仅从环境读取凭证，不采用 URL 携带密钥的路径。

这些链接用于复核当前执行规范；不包含原始素材身份或来源映射。
