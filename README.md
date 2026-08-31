<div align="center">
  <p>
    <a href="https://sealeap.cn" title="Visit SeaLeap"><img src="assets/sealeap-logo.png" width="116" align="middle" alt="SeaLeap logo" /></a>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <a href="https://advertising.amazon.com" title="Visit Amazon Ads"><img src="assets/amazon-ads-logo.png" width="336" align="middle" alt="Amazon Ads logo" /></a>
  </p>
  <h1>SeaLeap Amazon Ads Skills</h1>
  <p><strong>Give your AI agent an evidence-first Amazon Ads operating brain.</strong></p>
  <p>让 Agent 不只会“给建议”，而是会诊断、会算账、会留证据、会等待人工批准。</p>

  <p>
    <a href="https://sealeap.cn"><img src="https://img.shields.io/badge/Website-sealeap.cn-0ea5e9?style=for-the-badge&logo=safari&logoColor=white" alt="SeaLeap website" /></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge" alt="MIT License" /></a>
    <a href="https://github.com/xjli360/sealeap-amazon-ad-skills/stargazers"><img src="https://img.shields.io/github/stars/xjli360/sealeap-amazon-ad-skills?style=for-the-badge&logo=github&color=ff9900" alt="GitHub stars" /></a>
    <img src="https://img.shields.io/badge/Amazon_Ads-Official_Content_Authorized-ff9900?style=for-the-badge" alt="Amazon Ads official content authorized for use" />
    <img src="https://img.shields.io/badge/Agent_Skills-19-00a8e1?style=for-the-badge" alt="19 Agent Skills" />
    <a href="https://github.com/xjli360/sealeap-amazon-ad-skills/issues"><img src="https://img.shields.io/badge/Contributions-Welcome-8b5cf6?style=for-the-badge" alt="Contributions welcome" /></a>
  </p>

  <p>
    <a href="https://sealeap.cn">SeaLeap Website</a> ·
    <a href="#-skill-map">Explore the Skills</a> ·
    <a href="#-quick-start">Quick Start</a> ·
    <a href="#-license">License</a> ·
    <a href="#-star--contribute">Star & Contribute</a>
  </p>
</div>

---

> [!IMPORTANT]
> **Amazon Ads 官方内容授权**
>
> 本仓库所使用并提炼的 Amazon Ads 课程与官方材料，均为 **Amazon Ads 官方授权 SeaLeap 使用的内容**。SeaLeap 在授权范围内对这些材料进行结构化整理、方法提炼与 Agent Skill 化，并保留来源、快照时点和执行护栏。
>
> **Official content authorization:** The Amazon Ads courses and official materials distilled in this repository are content that Amazon Ads has officially authorized SeaLeap to use. SeaLeap independently converts the authorized source material into structured Agent Skills with source traceability and operating guardrails.

## Why this repository

Most AI advice for Amazon Ads sounds confident but cannot show its work. This collection is built for a different standard:

- **Operational, not generic** — each Skill has a concrete workflow, input expectations, output contract, and decision gates.
- **Evidence-aware** — account facts, current platform policy, training cases, and hypotheses stay explicitly separated.
- **Profit-aware** — ACOS is connected to CPC, CVR, contribution margin, inventory, returns, and lifecycle goals.
- **Agent-ready** — every directory under `skills/` is a self-contained Skill with a standard `SKILL.md` entrypoint.
- **Human-controlled** — diagnosis and drafts are the default; live changes require explicit, itemized approval.

> **One rule runs through every Skill:** never turn a course example, benchmark, or AI guess into a live campaign setting without current account evidence.

## 🧭 Skill map

| Skill | What it helps an agent do | Best for |
|---|---|---|
| [ACOS Diagnostics](skills/sealeap-amazon-acos-diagnostics/) | Reconcile ACOS, profit drivers, placement/search terms, and peer benchmarks | High ACOS, weak conversion, unclear break-even point |
| [Ad Architecture](skills/sealeap-amazon-ad-architecture/) | Work backward from sales and profit goals into campaign roles, keywords, budgets, and stages | Launch architecture, portfolio design, seasonal planning |
| [EU & Peak AMC Audiences](skills/sealeap-amazon-eu-amc-audience/) | Plan privacy-safe journey analysis, no-code/rule/lookalike audiences, activation, and evaluation | AMC, Europe, peak audiences, path/time-to-conversion, remarketing |
| [Full-Funnel Growth](skills/sealeap-amazon-full-funnel-growth/) | Map awareness-to-loyalty journeys, retail readiness, channel roles, and incrementality tests | Brand + performance, high-ticket journeys, cross-channel measurement |
| [SP Video Ads](skills/sealeap-amazon-sp-video-ads/) | Brief, review, bid, and test Sponsored Products video-format ads | SPV eligibility, silent product video, video CTR/CVR/ACOS |
| [Creative AI](skills/sealeap-amazon-creative-ai/) | Turn verified product and audience evidence into reviewable AI creative experiments | Creative Agent/Studio, AI video/copy/image briefs, A/B tests |
| [Localization Marketing](skills/sealeap-amazon-localization-marketing/) | Rebuild local search language, Listing copy, and creative for each marketplace | Translation, multilingual keywords, culture and policy review |
| [Prime Day Planning](skills/sealeap-amazon-prime-day-planning/) | Query 116 qualified insight records and create guarded preheat/event/tail plans | Prime Day, ROAS/DPV/Units/Sales slices, event planning |
| [EU Multi-Market Ads](skills/sealeap-amazon-eu-multimarket-ads/) | Stage localized expansion for standard, non-standard, high-ticket, and seasonal products | UK/DE expansion, emerging EU markets, back-to-school |
| [Global Growth Planning](skills/sealeap-amazon-global-growth-planning/) | Connect human-governed AI workflows, site sequencing, and verified opportunity calendars | AI operations, global expansion, April holiday opportunities |
| [Fashion Category Growth](skills/sealeap-amazon-fashion-category-growth/) | Validate US/EU/JP fashion trends through brand, promotion, inventory, and returns gates | Apparel/shoes/bags/jewelry selection and category operations |
| [Consumer Electronics Growth](skills/sealeap-amazon-consumer-electronics-category-growth/) | Validate CE demand, technical facts, compliance, logistics, and lifecycle ads | Wireless, electronics, PC, camera, office, musical instruments |
| [Home & Lifestyle Growth](skills/sealeap-amazon-home-lifestyle-category-growth/) | Validate nine OHL segments through safety, fitment, logistics, and ad gates | Home, kitchen, furniture, auto, garden, sports, toys, pets |
| [US Apparel Lifecycle Ads](skills/sealeap-amazon-apparel-lifecycle-ads/) | Diagnose long-, short-, and seasonal-lifecycle apparel products with US playbooks | Fashion, underwear, swimwear, suits, accessories |
| [Canada Apparel Ads](skills/sealeap-amazon-ca-apparel-ads/) | Combine lifecycle, bilingual discovery, margin, and inventory guardrails | Amazon.ca apparel, coats, undergarments |
| [Japan Apparel Ads](skills/sealeap-amazon-jp-apparel-ads/) | Apply Japan-specific language, seasonality, Points, and lifecycle evidence | Bags, underwear, swimwear, localized launches |
| [UK Apparel Ads](skills/sealeap-amazon-uk-apparel-ads/) | Combine UK lifecycle, sizing, returns, compliance, and advertising economics | Black Friday, Boxing Day, swimwear, outerwear |
| [Listing Optimizer](skills/sealeap-amazon-listing-optimizer/) | Audit and draft titles, bullets, attributes, search terms, images, A+, video, and tests | CTR/CVR gaps, indexing, return prevention |
| [Product Targeting](skills/sealeap-amazon-product-targeting/) | Build ASIN/category pools for competitor, substitute, complement, cross-sell, and defense | Product/category targeting, detail-page traffic, ASIN defense |

## ⚡ Quick start

Clone the collection:

```bash
git clone https://github.com/xjli360/sealeap-amazon-ad-skills.git
cd sealeap-amazon-ad-skills
```

Choose the Skill that matches the job, then point your agent to `skills/<skill-name>/SKILL.md` or copy that directory into the Skills directory supported by your agent runtime. See [SOURCE_COVERAGE.md](SOURCE_COVERAGE.md) for the complete 2026-08-31 source-to-Skill registry.

Example prompt:

```text
Use sealeap-amazon-acos-diagnostics in DIAGNOSE mode.

Marketplace: US
Date range: last 30 days
Goal: determine whether the ACOS problem is driven by CPC, CVR,
traffic mix, attribution, or unit economics.

Do not change campaigns. Show missing evidence and propose exactly
one single-variable experiment for human review.
```

Each Skill tells the agent which reference files to load, what data is still missing, which claims are safe to make, and where human approval is mandatory.

## 🛡️ Built-in operating guardrails

- Read-only diagnosis is the default mode.
- Marketplace, profile, seller, store, ASIN, SKU, currency, attribution window, and date range must stay explicit.
- Campaign writes require current scope verification and itemized human approval.
- Every change plan includes evidence, expected effect, stop condition, and rollback value.
- One experiment changes one primary variable so the result remains attributable.
- Listing claims must be backed by verified product facts; competitor copy and invented claims are out of bounds.
- AMC workflows stay aggregated and privacy-safe; no user-level export or re-identification.

## 📦 Repository structure

```text
sealeap-amazon-ad-skills/
├── assets/
├── skills/
│   ├── sealeap-amazon-acos-diagnostics/
│   ├── sealeap-amazon-eu-amc-audience/
│   ├── sealeap-amazon-sp-video-ads/
│   └── ... 16 more self-contained Skills
├── README.md
└── SOURCE_COVERAGE.md
```

A Skill may include:

```text
SKILL.md              # Agent entrypoint and operating workflow
agents/openai.yaml    # Optional agent-facing metadata
references/           # Evidence model, playbooks, examples, output contracts
scripts/              # Deterministic checks and analysis helpers
transcripts/          # Source-linked learning material where included
```

## 🌊 Built by SeaLeap

[SeaLeap](https://sealeap.cn) turns e-commerce operating knowledge into reusable, auditable Agent Skills. The goal is simple: help agents and operators move faster **without losing evidence, accountability, or control**.

🌐 Website: **[sealeap.cn](https://sealeap.cn)**

If you are building an Amazon Ads agent, an internal operating copilot, or a repeatable advertising workflow, use these Skills as composable building blocks—not as a substitute for current account data or professional judgment.

## ⭐ Star & contribute

If this repository saves one wasted budget cycle, one unsupported claim, or one irreversible campaign change, please **[give it a star](https://github.com/xjli360/sealeap-amazon-ad-skills/stargazers)**. It helps more operators and Agent builders discover the project.

Useful contributions include:

- marketplace-specific policy refreshes with authoritative citations;
- anonymized test cases and reproducible metric checks;
- safer output contracts, approval gates, and rollback patterns;
- new marketplace or category Skills that preserve the same evidence standard;
- fixes for broken links, ambiguous terms, or stale platform assumptions.

Open an issue before proposing any workflow that writes to a live advertising account.

## 📄 License

SeaLeap-authored code and documentation in this repository are available under the [MIT License](LICENSE).

Trademark rights, brand assets (including the Amazon Advertising and SeaLeap logos), and third-party source materials or transcripts are not granted under the MIT License. See [NOTICE](NOTICE) for details.

## Trademark, source, and affiliation notice

This is a SeaLeap-maintained repository for education, research, and agent workflow design. The Amazon Ads courses and official materials distilled here are **officially authorized by Amazon Ads for SeaLeap's use**. SeaLeap independently performs the structural conversion, workflow design, source mapping, and Skill maintenance.

The Amazon Advertising logo is **used with permission** and displayed in its approved, unmodified form. The authorization to use source content and approved brand assets does not by itself state that Amazon authored, reviewed, sponsored, jointly published, endorses, or maintains this repository. Amazon, Amazon Ads, Amazon Advertising, and related marks are trademarks of Amazon.com, Inc. or its affiliates; their use remains subject to the current [Amazon Advertising marketing guidelines](https://m.media-amazon.com/images/G/01/AmazonMarketingServices/Amazon_Advertising_Marketing_Guidelines.pdf).

References to Amazon products and services are descriptive. Platform capabilities, eligibility, attribution, interfaces, and policies can change; verify them against current official documentation before acting. Source transcripts and course-derived notes, where present, remain subject to the rights of their respective owners and are included for traceability rather than as a transfer of ownership.

---

<div align="center">
  <strong>Evidence before confidence. Approval before action.</strong><br />
  <sub>Made with 🌊 by SeaLeap</sub>
</div>
