# Sprint 3 — Ownership, Risk & Portfolio（详细任务）

> 周期：Weeks 7–10 · 截止：**Week 10 Friday 17:00**（Final Demo 在 Week 10 lab，各组周二或周五） · 权重：Group **30%** + Individual **10%**（指南内部按 40 分计：Demo 15 + 过程证据 15 + 个人 10）
> 来源：Week 7 Sprint 3 Guideline 走读（§1–§7 全文 + 评分表）与 Persistence / Software Complexity 讲座；Week 8 Risk Management 录播（§4.2 风险报告要求与模板）；Week 9 Reflection 讲座（§4.5 Portfolio、GitLab Analytics、Done Done）。
> 指南由 6–7 位学生志愿者审阅后发布；所有报告只规定**上限**不设下限。

---

## 目录

1. [概览与目标](#1-概览与目标)
2. [建议周计划（Suggested Weekly Planner）](#2-建议周计划suggested-weekly-planner)
3. [实践与期望（§4）](#3-实践与期望4)
   - 4.1 Agile Practices + README
   - 4.2 Risk report（风险报告）
   - 4.3 Demo（正式演示）
   - 4.4 Complexity, persistence, and technical debt（重构与复杂度报告）
   - 4.5 Portfolio（个人作品集）
4. [任务清单（按交付物）](#4-任务清单按交付物)
5. [评分标准（§5，共 40 分）](#5-评分标准5共-40-分)
6. [提交与 Final Demo（§6）+ 学术诚信（§7）](#6-提交与-final-demo6--学术诚信7)
7. [技术要点速查：持久化 / 复杂度 / 风险管理](#7-技术要点速查持久化--复杂度--风险管理)
8. [课堂 Q&A 要点汇总](#8-课堂-qa-要点汇总)
9. [Sprint 3 任务总结](#9-sprint-3-任务总结)

---

## 1. 概览与目标

**指南原文（1. Overview）**

> Sprint 3 is the final stage of the COMP9820 project. Your team already has a working Task Tracker, CI, and quality practices from Sprint 1–2. The focus now is end-to-end software project work: you practice the full cycle together—delivery, risk and process, individual reflection, and a polished package you can present (code, evidence, and narrative) as one coherent product.

**2. Sprint 3 Goals（原文）**
- Complete the project with a coherent set of rich user stories that together show a full, convincing product (work from Sprints 1–3). Continue implementing and refining stories; teams may modify Sprint 1/2 stories (if understanding has changed) and/or add new stories where they create clear user value. Finishing all stories from Sprint 1 is not the goal but creating clear value for the users is more important. **At least one meaningful product improvement in Sprint 3** (e.g., UI/UX or a different feature apart from user stories to add an innovation factor).
- Keep the project sustainable as complexity grows following strategies from lecture 7.2; implement persistence if it is part of your project. Submit a brief group report on refactoring and complexity.
- While applying concepts learned in Weeks 7–9, continue the same core practices from earlier sprints (e.g., TDD/testing, CI pipeline, code maintainability, Agile practices and Git).
- Manage uncertainty through a practical Risk report that identifies key risks, how you mitigated or accepted them, and how that connects to real project decisions.
- Package learning and contribution in an Individual portfolio (what you learned, contributed, and how you grew across the course).
- Ship and present a client-ready project with a README file and a presentation in the Week 10 lab demo: final product plus a clear story of your product and your process.

**讲师定位**
- Sprint 3 的目标是"**交付**"——把产品打包好交给 stakeholder/client。两条线：① Week 10 lab **正式 Final Demo**（讲故事：用户是谁、带来什么价值，展示 Sprint 1–3 全部 story）；② Week 10 周五提交代码库 + 报告等"过程证据"。
- 敏捷实践与 Sprint 2 **完全相同**；新增的是 README、风险报告、重构与复杂度报告、个人 Portfolio、正式 demo。
- "meaningful improvement" 是否算数不确定 → 问 tutor/同学/论坛。
- **最难的 Sprint**；工作量看目标——冲高分工作量大，pass 不难。

---

## 2. 建议周计划（Suggested Weekly Planner）

| Week | Focus | Tasks（原文） |
|---|---|---|
| 7 | Complexity & persistence | Weekly meeting; rotate roles (optional) and update team contract; plan Sprint 3; identify technical debt; begin persistence work if needed; for complexity, tie work to lecture 7.2; start notes or a draft for the refactoring & complexity report (§4.4); keep issue board current; standups; continue story/polish work. |
| 8 | Risk management in practice | Weekly meeting; risk report; add a project README.md using the README template; continue story/polish work; standups. |
| 9 | Portfolio packaging & polish | Weekly meeting; continue story/polish work; ensure tests/CI pass; finalise the refactoring & complexity report (§4.4) and link it from the README; improve documentation and demo script; individuals draft portfolio; sprint retro; standups. |
| 10 | Final demo | Final demo during Week 10 lab; finalise risk report and sprint artifacts; submit by the Sprint 3 deadline. |

Relevant lectures: Week 7 (Complexity, Persistence), Week 8 (Risk), Week 9 (Portfolio).

💬 **Demo 日期各组不同**：周二 demo 的组要在周二前把代码准备好，周三–五写报告/portfolio；周五 demo 的组所有东西都得在周五前就绪。提前规划时间。

---

## 3. 实践与期望（§4）

> This section is practical guidance for how to work in Sprint 3 (practices, artifacts). Section 5 describes success criteria (what strong performance looks like). You do not need two separate checklists—use Section 4 to organise your sprint, and Section 5 to see how that work is assessed.

### 4.1 Agile Practices
> - Git usage, standups, issue board, group retro, weekly meetings, and team contract — same guidelines as Sprint 2
> - Testing, CI, coverage, and maintainability: continue the Sprint 2 bar; §4.4 explains how to sustain this as complexity grows; §5.1.B states how it is assessed in the repo.
> - **README**: Copy README_template.md into your repo root as README.md and fill it in (product, how to run locally, how to run checks, links to the risk report, the refactoring & complexity report, and other artifacts). Make evidence easy to find (consistent filenames/paths; link key artifacts from the README or issue board).

💬 目前你们的 README 大概还是 starter code 那份很长的使用说明，要替换成自己项目的：项目是什么、如何运行、环境/数据库设置、如何跑检查、各报告链接。用模板，不需要太长。

### 4.2 Risk report（Week 8 讲座后发布）
> Submit a group risk report: a practical register you can trace to real work. More details and examples can be found in Lecture 8.1 (Risk management). You can download this template for your risk report: **RISK_REPORT_TEMPLATE.md**
>
> - **Fields (one block per risk)**
>   - **Risk statement** — Prefer the form: *If [cause happens], then [bad outcome] because [reason].*
>   - **Likelihood (L) and Impact (I)** — enough to justify prioritisation (e.g. a simple scale or labels).
>   - **Owner** — who monitors or drives mitigation for that risk.
>   - **Mitigation or contingency** — what you do to reduce probability or impact before failure (mitigation), and/or what you do if it happens anyway (contingency). You may relate choices to **Avoid / Reduce / Transfer / Retain**.
>   - **Evidence link** — path, test, issue, MR, or commit that shows the mitigation in the repo (so tutors can verify).
>   - **Status** — e.g. open / mitigated / accepted / resolved.
>   - **Last reviewed** — date; optional short monitoring notes if useful.
> - **Make it actionable**：Map risk → concrete decisions or work (issues/MRs/meeting notes)；Map mitigation → how you will know it worked (tests, CI, a lightweight indicator).
> - **Tips**：Keep a short **list of 3 meaningful project risks**, not a long generic catalogue；Tie each risk to repo evidence (issue / MR / commit / test).
> - **Where to put it**：`RISK_REPORT.md` at the repo root (或 `risk/RISK_REPORT.md`)，linked from the README。模板起点 `Student_Guide/RISK_REPORT_TEMPLATE.md`（可选，可用自己结构）。

**一个风险块的模板（讲座练习）**
```markdown
### R1 — short title

Risk statement: If … then … because …
L / I: … / …
Owner: …
Mitigation or contingency: …
Evidence: … (path, test name, MR, or issue)
Status: …
Last reviewed: … (date or e.g. weekly)
```

**完整示例（持久化失败）**
- Risk statement：If `tasks.json` is missing, invalid JSON, or the app lacks file permission, then tasks are not saved or startup/load fails because persistence assumes a readable file.
- L / I：moderate / high —— **都要给理由**（可能性：首次部署时文件未创建、路径错、只读卷、写入中断截断；影响：核心功能崩、每次加载报错、demo/评分失败）。
- Owner：负责持久化的组员。
- Mitigation：在 `json.load()` 周围校验/捕获错误；返回空列表或清晰错误页；保存时先写临时文件再替换；文档记录权限与 `DATA_FILE`。Contingency：记录好的重置路径（删除坏文件恢复）、热修复。
- Evidence：`app.py`（`DATA_FILE`、`json.load`、`save()`、`/add`、`/delete/<index>`）、`tests/test_app.py`、`conftest.py`（fixture 把 `DATA_FILE` 指向 `tmp_path`）。
- 监控指标（每风险 1–2 个）：JSON 解析错误数、"重启后任务仍在"测试通过率、删除相关测试失败数、空/无效提交被正确拒绝次数、main CI 绿、计划外回滚次数。
- issue/MR 可标注 "Mitigates R3" 建立风险→工作的可追溯性。

### 4.3 Demo
> A live demo will be at your Week 10 lab with your tutors and class. This is a **formal presentation with slides** which is different from Sprint 1 and 2 informal demo. The whole team is present. You run your Task Tracker, give your product and process story. This shows your team can explain and justify decisions.
>
> The goal is to demonstrate the final product end-to-end and demonstrate professional communication about both what you built and how and why you built it. **The demo is assessed on depth and richness of user, problem, value, and decisions.**
>
> **Notes:**
> - Teams are **not required to deploy** your project (e.g. a hosted URL) due to UNSW IP considerations. You can run your Task Tracker locally during the demo.
> - Optional deployment and peer viewing (after Week 9): if your team is comfortable with a public URL, you may deploy after Week 9 and share a link so other teams can try your app… We will make a channel for this purpose on Discourse Forum after Week 9.
> - Scope of final demo: In Week 10, teams demo the **whole project** (not only Sprint 3 changes), including the implemented story set across Sprints 1–3.
>
> **Minimum expectations:**
> - Rehearse a clear flow: for example, user/problem → value and implemented stories → live system run → reflections.
> - Ensure the product runs reliably in a clean environment and key flows are stable.
> - Share speaking roles so all team members can explain decisions and answer questions.
> - Do at least one timed run-through before demo and adjust based on what felt unclear.
>
> Each group's demo involves a presentation for **10–15 mins with up to 5 mins Q&A**. During the Q&A: team answers questions from tutors and other groups, and can quickly open relevant issues/MRs/tests/risk notes.

💬 讲师补充：**两位 tutor 打分取平均**；其他组旁听、任何人可提问；**每个成员都要讲**自己负责的部分并能答问；不逐文件讲代码，讲产品故事（用户是谁、为何重要、如何满足需求、价值）；"Running the product"时 tutor 可能说"点一下那个按钮给我看"。不部署的组可在论坛频道贴 5 分钟产品介绍视频互相反馈。

### 4.4 Complexity, persistence, and technical debt
> This subsection is how to manage engineering work as the codebase grows—not a second list of quality expectations. More details in Lecture 7.2.
> - **What "addressing complexity" means here**: Instead of shrinking the feature set or pretending the problem is simple, you are expected to show that you can **name** and **act on** structural issues: what complexity is **essential** to your users' needs versus **accidental** (e.g. duplicated logic, unclear boundaries).
> - **Design levers**
>   - **Coupling / cohesion**: Prefer looser coupling between components and higher cohesion within a module. Refactors that clarify boundaries (e.g. routes vs services vs persistence) are exactly the kind of work this sprint is asking for.
>   - **Cyclomatic complexity**: Use branching complexity in functions as one *measurable* input to refactoring—identify a function with many if/else/while paths, refactor to simplify or split, and optionally note a before/after. Common per-function ceilings (around 8–10) are *guidance*, not a hard rule.
> - **Process**：Treat complexity as a project management problem as well as a technical one: keep responsibilities clear and refactoring intentional (issues/MRs say *why*). Prefer **small, reviewable MRs** over big-bang changes.
> - **If your project requires persistence**, focus on: Correctness and reliability (data isn't lost, behaviour is consistent); Clear instructions to run locally (including any DB or env setup).
>
> **Submit a brief report as a group (rough guide: 1–2 pages or the equivalent in Markdown)** that explains how your team managed complexity and refactoring across the Sprints. At minimum:
> 1. **Essential vs accidental**: Name at least one area where complexity is inherent to the product (essential) and at least one where you reduced or contained accidental complexity (or explain why you accepted it).
> 2. **Structure**: Describe how coupling/cohesion improved—or what boundary you clarified (e.g. separating UI from business logic, or persistence from routes)—with links to MRs/issues.
> 3. **Measurement**: Discuss cyclomatic complexity for one concrete refactor with links to MRs/issues.
>
> Throughout: what you changed, why it mattered, and evidence—link to merge requests, issues, and/or commits (you may use generative AI to help draft or organise the text—review for accuracy, ensure it reflects your work, follow UNSW policy on AI use and acknowledgement). Link the report from your README.
> Suggested location: `docs/REFACTORING_AND_COMPLEXITY.md` (keep the name stable once linked).

💬 讲师补充：不需要对项目每一行做全面重构，"just do some practice using your project will be enough"；圈复杂度只需选**一个最复杂的函数**计算并尝试降低（天生复杂无法降低的可以保留并写明 "complicated by nature"）；可建 "refactoring for complexity" issue 细分 cohesion / coupling / cyclomatic 任务并指派；报告可**多次 commit**；技巧——**互相重构对方的代码**更容易发现问题。

### 4.5 Portfolio (Individual)
> Your portfolio is your personal evidence pack. Expectations for the portfolio itself are in §5.2.
> Typical contents:
> - What you worked on across Sprints (stories, quality, PM artifacts)
> - Evidence (links to MRs/issues/commits, screenshots, short write-ups)
> - Reflection: what improved, what you would do differently, and what you learned about software project management and process
>
> Maximum words (recommended): **1000** (excluding links and screenshots)
> Portfolio submission: submit on **Moodle**.

💬 Week 9 讲师补充：
- 不需要做网站，**交 PDF 即可**；网上的作品集（emmabostian/developer-portfolios 等）细节少，**本课要求更详细**，将来可压缩成正式作品集；先为这一个项目写，将来再合并。
- 证据可以是：测试示例、文档、对风险的贡献、GitLab **Analyze → Repository / Contributor analytics**（"我把大部分提交贡献给了文档/测试/功能代码"——只是一个信号，要配 README 质量与可演示成果）。
- **反思很重要**：雇主知道这是短期学生项目，但要能说下次会怎么不同、对 SPM 与过程学到了什么；展示成长与权衡，不只是时间线。
- 面试结构练习："我们的 Task Tracker 项目表明我能帮助 SPM，因为——证据（MR、测试、CI、部署、风险文档、README）+ 具体例子。"

---

## 4. 任务清单（按交付物）

### ☑ A. 产品与故事
- [ ] 规划 Sprint 3：继续/完善故事，可修改 Sprint 1/2 故事或新增有明确价值的故事；**不必做完 Sprint 1 的所有故事**。
- [ ] **≥1 个 meaningful product improvement**（UI/UX 或新功能/创新点）。
- [ ] 如项目需要：实现**持久化**（JSON 文件：`json` + `pathlib`，启动时 `json.load`，每次变更后 `save()`；测试用 `tmp_path`；README 写明数据文件位置与环境）。
- [ ] 延续 TDD / 测试 / CI / 覆盖率（**后端 > 70%**）/ 可维护性；main 上被评分的 commit **CI 绿**。
- [ ] issue 含验收标准；MR `Closes #n`、小而可审；AC 未达成要能解释。

### ☑ B. README（Week 8）
- [ ] 复制 `README_template.md` 为根目录 `README.md`：产品目的、本地运行（Python 版本、`pip install -r requirements.txt`、数据文件/环境变量）、如何跑测试/检查、链接风险报告、重构与复杂度报告、会议纪要、retro、契约等；步骤可用、内容与仓库一致；路径/文件名稳定。

### ☑ C. 风险报告 `RISK_REPORT.md`（Week 8）
- [ ] 约 **3 个**对本项目真正重要的风险（候选：并发写入 `tasks.json`、`tasks.json` 缺失/损坏/无权限、删除索引语义、输入校验、安全/隐私（密钥、日志）、进度/CI）。
- [ ] 每个风险 7 个字段：Statement（If…then…because…）/ L & I（附理由）/ Owner / Mitigation or contingency（标 Avoid/Reduce/Transfer/Retain）/ Evidence link / Status / Last reviewed。
- [ ] 每风险 1–2 个监控指标；每周（或改动持久化/部署后）重访更新；issue/MR 标注 "Mitigates Rn"。
- [ ] 从 README 链接。

### ☑ D. 重构与复杂度报告 `docs/REFACTORING_AND_COMPLEXITY.md`（Week 7 起草、Week 9 完成）
- [ ] essential vs accidental 各至少一例（说明理由）。
- [ ] coupling/cohesion 改善或澄清的边界（routes / services / persistence；UI vs 业务逻辑），链接 MR/issue。
- [ ] 一次具体重构的圈复杂度讨论（画控制流图，V(G) = e − n + 2，前后对比），链接 MR/issue。
- [ ] 1–2 页；可用 GenAI 辅助但审核并声明；从 README 链接。

### ☑ E. 敏捷过程文档（同 Sprint 2）
- [ ] Issue board 持续使用（issue 移动、assignee、MR 关闭 issue）。
- [ ] **Weeks 7–9 每周 ≥1 次全员会议**，纪要含议程、决策、行动项。
- [ ] Standup 每周 3 次（Teams 证据；含 lab 上 1 次）。
- [ ] **Sprint 3 retro**（有意义的反思与改进行动项）。
- [ ] 契约按需更新（Sprint 3、role rotation、ways of working）。

### ☑ F. 个人 Portfolio（Moodle，Week 9 草稿，Week 10 周五前提交）
- [ ] ≤1000 词（不含链接/截图），PDF 即可：跨 Sprint 做了什么 + 证据链接/截图 + 反思（改进、会怎样不同、学到什么）。

### ☑ G. Final Demo（Week 10 lab）
- [ ] 幻灯片 + 脚本：用户/问题 → 价值与已实现故事（Sprint 1–3）→ 现场运行 → 反思/决策；10–15 分钟 + ≤5 分钟 Q&A。
- [ ] 干净环境稳定运行；至少一次**计时彩排**；全员分工发言；Q&A 时能快速打开 issue/MR/测试/CI/风险记录。
- [ ] （可选）Week 9 后部署并在论坛频道分享链接，或录 5 分钟介绍视频。

### ☑ H. 提交（Week 10 周五 17:00）
- [ ] GitLab `main`：README（链接可用）、风险报告、复杂度报告、代码（含 meaningful 改进、issue/MR 可追溯、CI 绿、测试）、board、Weeks 7–9 会议纪要、Sprint 3 retro、契约。
- [ ] Moodle：个人 Portfolio。
- [ ] Teams：standup 证据。
- [ ] 所有 GenAI 辅助内容已审核、符合事实并正确声明。

---

## 5. 评分标准（§5，共 40 分）

> §5.1 covers the group (live demo + repo evidence); §5.2 covers the individual (portfolio and participation). Use **Strong** as the target for each row; Developing = present but with gaps.
>
> **Interpreting "enough" product**: Marks are not awarded for maximising the number of features. They reward a convincing stakeholder value story, working software for the flows you showcase, sound process evidence on GitLab, and the criteria in the tables below. Groups will not be penalised having a very "simple" or "few" stories, however, having too few/simple stories may mean limited value.

### 5.1.A Week 10 final demo — 15 Marks（两位 tutor 打分取平均）

| What the demo looks for | Marks | Strong | Developing | Limited | Not demonstrated |
|---|---|---|---|---|---|
| **User, problem, value & decisions** | 8 | Deliver a convincing stakeholder value story with strong stories and show the usefulness of the product. At least one **meaningful** product improvement in Sprint 3; Team explains who the user is, what problem you focused on, what value means for your product, and what key decisions shaped the final project—going beyond a feature-by-feature walkthrough. | Several of user / problem / value / decisions appear, but depth is uneven, or wording is generic, or the team keeps slipping into feature lists without tying them back to user, problem, and value. | At most one of user, problem, value, or decisions is explained with any substance; or two or more only named (buzzwords) with no real explanation; or the narrative is almost entirely "here's what we built". | No coherent product story. |
| **Running the product** | 5 | For the flows you choose to showcase, the app behaves as intended; steps and screen changes are easy to follow; if something goes wrong, the team recovers quickly and explains limits or environment in concrete terms. | Those flows basically work, but there is noticeable friction here and there (clumsy setup, one or two glitches, short pause to refresh/retry). | Several breakdowns or long stalls; repeated confusion; audience loses the thread; or the team drops or skips large parts of what they planned to show. | The product does not run for a meaningful demo. |
| **Q&A** | 2 | Answers are specific and consistent across team members; can open issues/MRs/tests/CI when asked to justify a claim. | Reasonable answers but vague or slow to locate detail. | N/A | Cannot engage with questions. |

### 5.1.B Repo and process evidence (practice made visible) — 15 Marks

> Evidence that your team ran the process and left a verifiable trail in GitLab: main issues, MRs, CI, README.md, reports, meeting notes, contract, retro, and an issue board you actually use. Standups may be evidenced in Teams.
>
> **Quick checklist — On main before the deadline**: root README.md with working links; risk + refactoring & complexity reports; meeting notes for Weeks 7–9; Sprint 3 retro; team contract (Sprint 3 + role rotation); issues/MRs tied to delivery; CI green on main; board in use; link risks to work where relevant.

| Component | Marks | Strong | Developing | Limited | Not demonstrated |
|---|---|---|---|---|---|
| **Shipped work & traceability** | 2 | Delivered work on main has issues with acceptance criteria; MRs reference issues (e.g. Closes #n). It is clear what shipped from issues/MRs and verify it (run app, follow AC, or tests)—not infer only from code. MRs are reviewable (not one opaque mega-merge). | Linkage patchy: weak AC, some MRs without issue refs, uneven story → code mapping. | N/A | Cannot tell what shipped or it is not on main. |
| **Engineering quality (tests, CI, design)** | 2 | CI green on the pipeline for the marked main commit. Tests cover important behaviour. **Backend code coverage above 70%.** | Flaky CI, thin tests, weak coverage habit, or messy MRs—but core practices visible. | N/A | No meaningful tests/CI or cannot assess from the repo. |
| **Risk report and risk–work traceability** | 4 | Report: per risk, likelihood, impact, owner, mitigation/contingency, status (and last reviewed if useful). Where relevant, issues/MRs state how work relates to risks (e.g. "Mitigates R3"); risk → work traceable. | Report missing fields or mostly generic; and/or occasional/inconsistent risk–work links. | Very thin or unclear report; and/or almost no risk–work links. | Missing or unusable report; or no traceability. |
| **Refactoring & complexity report** | 3 | Concrete examples tied to essential vs accidental, coupling/cohesion, and a cyclomatic-complexity discussion for one concrete refactor; MR/issue/commit links work and match the text. | Few links or vague tie to repo; or lecture concepts named but not applied to *this* project. | Mostly placeholder / boilerplate. | Missing or unusable. |
| **Agile process and team documentation (board, meetings, retro, contract)** | 2 | Issue board in use: issues move, assignees, MRs close issues with links. Meetings: at least one full-team meeting per week in Weeks 7–9; notes include agenda, decisions, action items. Sprint 3 group retro: meaningful reflection and action items. Contract: updated for Sprint 3 if needed (role rotation, ways of working). | Board thin or uneven; sparse or irregular meeting notes; retro shallow/checkbox-level; contract updated but unclear. | N/A | No usable board/process evidence; or no meeting documentation; or no retro; or no contract evidence. |
| **README and repository findability** | 2 | Root README.md from README_template: product purpose, run locally, tests/checks, links to reports and key artifacts; steps work; content matches repo. Stable paths/names; core artifacts locatable from README. | README missing a section or stale; and/or artifacts only findable with extra effort. | N/A | No usable README or cannot find core artifacts. |

💬 讲师：敏捷实践这一项分值从之前**大幅下降**，因为 Sprint 3 重心转移到 demo、风险、复杂度等。

### 5.2 Individual Success Criteria — 10 Marks

| Component | Marks | Strong | Developing | Limited | Not demonstrated |
|---|---|---|---|---|---|
| **Portfolio – value + evidence** | 6 | Portfolio is well-structured and specific: shows what you did, what value it created, what you learned, and includes strong evidence links (issues/MRs/commits/screenshots). Reflection shows growth and trade-offs, not just a timeline. | Portfolio exists but is somewhat generic; value/evidence links incomplete; reflection shallow. | Portfolio is very brief, mostly claims with little evidence or value framing. | No portfolio. |
| **Git practice** | 2 | You have meaningful commits and at least one substantial MR contribution during Sprint 3. Work is clearly attributable and aligned with team goals (issues/risk mitigations/stories). | Some commits/MR activity, but impact unclear or poorly linked to issues. | N/A | No meaningful git contribution. |
| **Standups + participation** | 2 | Regular standup participation across Sprint 3 (evidence in Teams), you communicate blockers, and you contribute to team coordination and delivery. | Some standup participation, but inconsistent. | N/A | No standup participation evidence. |

**分值结构**：Demo 15（8 + 5 + 2）+ 过程证据 15（2 + 2 + 4 + 3 + 2 + 2）+ 个人 10（6 + 2 + 2）= 40。

---

## 6. 提交与 Final Demo（§6）+ 学术诚信（§7）

> **Sprint 3 deadline: Week 10 Friday 5pm.**
>
> **What to submit:**
> **1. GitLab — group repo (`main`)** — Push your final state to `main` before the deadline. The commit on main at the deadline is what is marked (ensure CI is green and the repo is complete for that commit). Your group submission is the whole project picture on GitLab, not only code. `main` should include at least:
> - Root *README.md*, with working links to the risk report and the refactoring & complexity report, plus how to run the app and checks locally.
> - Risk report (group), in-repo and clearly linked from the README (§4.2).
> - Refactoring & complexity report (group), in-repo and linked from the README (§4.4).
> - Shipped Task Tracker code on *main*, at least one meaningful product improvement in Sprint 3; with issues and merge requests that show traceability (stories, AC, `Closes #n`), CI passing, tests.
> - Agile artifacts: issue board in use, meeting notes for Weeks 7–9, Sprint 3 group retro, team contract (Sprint 3, including role rotation where applicable).
>
> **2. Moodle — individual** — Submit your individual portfolio on Moodle by the same Sprint 3 deadline. Tutors mark the portfolio from Moodle.
> **3. Standups are evidenced in Teams** (not uploaded as a single "file"); participation is assessed as in §5.2.
> **4. Final demo and attendance** — In the Week 10 lab, your team gives the formal demo (product + process story, Q&A). **All team members must attend the Week 10 demo otherwise 0 marks for Sprint 3** unless special consideration applies.
>
> **7. Plagiarism & academic integrity** — The same rules as Sprint 1–2 apply: your work must be your group's own. Do not share code with other groups, do not use public repos, and follow the course policy on AI tools and acknowledgements (including if you use generative AI to help write the refactoring & complexity report—it must remain accurate, tied to your commits/MRs, and properly acknowledged).

💬 讲师关于 GenAI：可让 GenAI 总结 commit message 讲故事，但它会自作假设，**务必审核、核对、编辑**；Sprint 1 有组的会议记录/commit 明显是 AI 生成且质量差 → 得分更低。

---

## 7. 技术要点速查：持久化 / 复杂度 / 风险管理

### 持久化（Lecture 7.1）
- **Persistence** = 程序状态比创建它的进程活得久（重启后数据还在）；本课定义为存到磁盘。三种存储：内存（不持久）→ 文件 → 数据库（SQL/NoSQL，门槛与性能更高；学 SQL 修 COMP3311）。**本项目文件系统足够。**
- JSON 文件方案（约 5–6 行改动）：
  ```python
  import json
  from pathlib import Path
  DATA_FILE = Path(__file__).resolve().parent / 'tasks.json'
  if DATA_FILE.exists():
      with open(DATA_FILE, encoding='utf-8') as f:
          tasks = json.load(f)
  def save():
      with open(DATA_FILE, 'w', encoding='utf-8') as f:
          json.dump(tasks, f, indent=2)
  # add_task / delete_task 修改 tasks 后调用 save()
  ```
- Sprint 期望：**正确性与可靠性**（数据不意外丢失；add/delete/restart 后行为与文档一致）；**清晰的本地设置**（README：Python 版本、依赖、数据文件位置、环境变量）；加载/保存纪律（启动加载一次、每次变更保存，策略一致）；**测试用临时文件**（pytest `tmp_path`）不覆盖真实 `tasks.json`；用 MR/issue 证明修复了竞态、编码错误、坏路径。图片可存文件路径/外部 URL，注意大小。Persistence 非必须，取决于故事。

### 软件复杂度（Lecture 7.2）
- Brooks《No Silver Bullet》：**本质复杂度**（问题固有，如客户要的 30 个功能；不可去除，用好设计管理）vs **偶然复杂度**（非固有，如特定格式解析、工具/配置过载、流程与文档过载；可缓解难根除，占现代软件 50–70%+）。区分靠人的判断，边界随技术移动（C 手动管内存曾是本质，Python 里再手动就是偶然）。
- 度量：**Coupling**（组件间依赖；松好）、**Cohesion**（模块内元素归属；高好）、**Cyclomatic Complexity**（分支复杂度：画控制流图，**V(G) = e − n + 2**；if/else = 2；常见上限 8–10，仅指导）。
- 圈复杂度例：`day_to_year` 原版 8 − 6 + 2 = 4，重构后 7 − 6 + 2 = 3。
- 缺点：忽略非分支语句的复杂度；诱导无意义拆函数。为何度量：改善可维护性、估算工作量/成本、评估质量、指导重构。

### 风险管理（Lecture 8.1）
- 风险 = 尚未发生但可能造成损失的问题；= 负面事件概率 + 影响描述；源于不确定性（信息缺失）；反面是机会。项目失败多为管理原因（沟通、估算、计划跟踪、风险管理弱）。
- 来源：外部压力（干系人拉扯、政治）、人/协作（沟通缺口、对"done/correct"认知缺口、角色不清、反馈慢）、安全/伦理（输入处理、密钥泄露、隐私同意、公平、透明/合规）。Task Tracker 例：删除语义不清、持久化时机假设不一致、测试缺口发现太晚、归属不清、并发写入 `tasks.json`。
- 四步法：识别 → 分析概率 + 影响（给理由）→ 排优先级 → 缓解（降概率/减影响）；定期重访；关注安全质量风险。四种应对：Avoid / Reduce / Transfer / Retain。
- **风险退役**：实施缓解 + 证据（测试/监控/评审）表明风险行为不再发生 → 标 mitigated/resolved。
- 证据（de Bakker et al. 2009）：风险管理只在改变干系人意识与行为、真正被关注时才有效——是文化不是文书。

---

## 8. 课堂 Q&A 要点汇总

| 问题 | 答案 |
|---|---|
| 必须部署（Vercel）吗？ | Sprint 3 不要求（IP 考虑），localhost 即可；全组同意可公开部署；Week 9 后论坛频道可分享链接或 5 分钟视频。 |
| Demo 要逐文件讲代码吗？ | 不要；讲产品故事（用户、问题、价值、决策），按推荐流程可调整。 |
| Demo 谁打分？ | 本组 tutor + 另一位 tutor 取平均；其他组旁听提问；每个成员都要讲。 |
| "meaningful improvement" 算不算？ | 不确定就问 tutor/同学/论坛。 |
| 报告要多长？ | 只有上限（复杂度报告 1–2 页；portfolio ≤1000 词），短而有信息量即可。 |
| 复杂度报告要重构全部代码吗？ | 不用，做一些练习即可；圈复杂度只选一个最复杂的函数。 |
| 天生复杂的函数降不下来？ | 保留并写明 "complicated by nature"，不拆也可以。 |
| 想保存图片怎么办？ | 存文件路径或外部 URL 等，选最适合的，注意大小。 |
| 用 SQL 太复杂？ | 用 JSON 文件持久化，简单快速；persistence 非必须。 |
| 风险要写多少个？ | 约 3 个真正重要的，不要通用长清单；每个绑定仓库证据。 |
| 模板必须用吗？ | 可选（RISK_REPORT_TEMPLATE.md / README_template.md），可用自己结构。 |
| Portfolio 要做网站吗？ | 不用，PDF 即可；比网上作品集更详细；反思很重要。 |
| 工作量如何？ | 看目标：冲高分工作量大，pass 不难。 |
| Done 的定义各组不同？ | 是；将来把 Definition of Done 写进小组契约（Lecture 9.2 Done Done 未讲）。 |

---

## 9. Sprint 3 任务总结

**一句话**：把 Sprint 1–2 的产品与实践打包成一个"可交付给客户"的整体——继续以用户价值为核心完善故事并至少做一个有意义的改进（如需则加持久化），在复杂度增长下用耦合/内聚/圈复杂度有意识地重构并写 1–2 页报告，用可追溯的风险登记表管理不确定性，用模板重写 README 让所有证据可查，个人写 ≤1000 词的证据 + 反思 Portfolio，最后在 Week 10 lab 做一场正式的 10–15 分钟演示。

**核心要求速记**
- 截止 **W10 Fri 17:00**：GitLab `main`（README、`RISK_REPORT.md`、`docs/REFACTORING_AND_COMPLEXITY.md`、代码、board、W7–9 纪要、retro、契约）+ Moodle Portfolio + Teams standup。
- **W10 lab Final Demo 全员必到，否则 Sprint 3 记 0 分**；10–15 min + ≤5 min Q&A；两位 tutor 平均；带幻灯片；全员发言；至少一次计时彩排。
- 评分 40：Demo 15（用户/问题/价值/决策 8、产品运行 5、Q&A 2）+ 过程证据 15（追溯 2、工程质量 2 [CI 绿、覆盖率 >70%]、风险报告 4、复杂度报告 3、敏捷文档 2、README 2）+ 个人 10（Portfolio 6、Git 2、Standup 2）。
- 不按功能数量给分；不要求部署；报告只有上限。
- 风险报告：~3 个风险 × 7 字段，If…then…because…，L/I 给理由，Avoid/Reduce/Transfer/Retain，证据链接，Status + Last reviewed。
- 复杂度报告：essential vs accidental、coupling/cohesion 边界、一个函数的圈复杂度前后对比，全部链接 MR/issue。
- GenAI 可辅助写报告但必须审核并声明；AI 生成的失实记录会扣分。

**讲师给的 Sprint 3 "拿分策略"**
1. 按周计划：W7 复杂度/持久化 + 规划 + 报告草稿；W8 风险报告 + README；W9 报告收尾 + demo 脚本 + portfolio 草稿 + retro；W10 demo + 提交。
2. Demo 讲故事不讲代码：user/problem → value & stories → live run → reflections；准备好随时打开 issue/MR/测试/CI/风险记录回答 Q&A。
3. 可追溯性贯穿一切：issue（AC）↔ MR（`Closes #n` / `Mitigates Rn`）↔ 测试/CI ↔ 报告 ↔ README 链接。
4. 把复杂度当项目管理问题：建 issue 细分指派、小 MR、说明 why；互相重构对方代码。
5. 提前按 demo 日期（周二/周五）倒排时间；不要最后一刻推 main（CI runner 排队）。
