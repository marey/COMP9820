# Sprint 1 — Foundations & First Flight（详细任务）

> 周期：Weeks 1–3 · 截止：**Week 4 Monday 12:00（2026-03-09）** · 权重：Group **25%** + Individual **5%**
> 来源：Week 1 Assignments Overview / Sprint 1 Guidelines；Week 2 Sprint 1 指南与评分表走读、Git Practice 页、Starter Code；Week 3 指南更新（2.2 Planning & stories、2.3 Sprint retrospective、评分表细化）；Week 4 开场 Sprint 1 Q&A；Week 5 成绩反馈。

---

## 目录

1. [概览与目标](#1-概览与目标)
2. [建议周计划（Suggested Weekly Planner）](#2-建议周计划suggested-weekly-planner)
3. [任务清单（按交付物）](#3-任务清单按交付物)
4. [实践与期望（指南 §2 原文 + 讲师解释）](#4-实践与期望指南-2-原文--讲师解释)
5. [评分标准（Marking Rubric）](#5-评分标准marking-rubric)
6. [提交与 Demo（§3.3）](#6-提交与-demo33)
7. [学术诚信（§4）](#7-学术诚信4)
8. [课堂 Q&A 要点汇总](#8-课堂-qa-要点汇总)
9. [Sprint 1 任务总结](#9-sprint-1-任务总结)

---

## 1. 概览与目标

**课程网站原文（2. Sprint 1: Foundations & First Flight）**

> Sprint 1 的重点是为团队与产品打基础，把神奇想法变成真实的、协作构建的系统。
>
> **Goals for Sprint 1**
> - You will begin by practicing Agile software team principles, including collaboration, communication, and shared responsibility.
> - The team will translate their ideas into clear user stories, establish good Git habits through branching, committing, and peer-reviewed merges, and deliver an initial set of new features.
> - By the end of this sprint, the group should have a functioning project structure, a shared understanding of their product, and evidence of collaborative development and management practices.

**讲师定位**
- Sprint 1 = 打基础 / 第一次起飞：练敏捷团队实践、协作、用户故事、良好 Git 习惯；最终有可运行的项目结构。
- **最容易拿分的 Sprint（"easy marks"）**：契约、issue board、站会"照做就得分"；难的只有给 starter code 加功能，但 Features Demo 只占 30 分中的 5 分，无前后端经验也能拿高分。
- 让有 CS 背景和没背景的人都跟上；建议有经验的同学帮新手，让所有人整个学期都能贡献。
- 交付物尽量少文档；**没有每周交付物**，不检查"Week 2 做完了吗"。

---

## 2. 建议周计划（Suggested Weekly Planner）

| Week | Tasks（原文） | 中文 |
|---|---|---|
| 1 | join a group, master Git, understand starter code | 加入小组（Week 1 lab 随机分组）；完成 lab_git（SSH key、clone、add/commit/push、pull、冲突、分支）；理解 Flask starter code |
| 2 | write group contract, add tasks on issue board, add new features to starter code (add & delete tasks) following git practices, ≥2 standups | 写团队契约；issue board 加任务；按 Git 规范给 starter code 加 add & delete 功能；≥2 次站会 |
| 3 | plan features to have and write user stories, manage issue board, sprint retro including teamwork evaluation, ≥2 standups | 规划功能并写用户故事；管理 issue board；Sprint retro（含互评）；≥2 次站会 |

相关讲座：Week 1（Git）、Week 2（Agile team practices、starter code）、Week 3（Planning & stories、Retro）。

---

## 3. 任务清单（按交付物）

### ☑ A. Git 与代码（Features）
- [ ] 每人完成 `lab_git`（不计分但"超级超级重要"）；Windows 用户按 *Installing Git for Windows Systems*（WSL）配置。
- [ ] 理解 starter code：`app.py`（后端，路由 = 请求→响应）、`templates/index.html`（前端）、`requirements.txt`、README（How to Run / Making Your First Changes / Common Questions）。
- [ ] 在 **feature 分支**上实现 **add task** 与 **delete task**（分开做，是两件事）；能显示任务列表 + 能添加 + 能删除即可。
  - **不需要**：漂亮 UI、邮件确认、数据库/持久化（刷新后数据还在）、空输入校验。
  - 讲师最小示例：`My Tasks` + 输入框 + `Add Task` 按钮 + 每条任务带 `Delete`——"这已经绰绰有余"。
- [ ] 每人 **≥1 个分支、≥2 个 commit**，遵守分支命名与 commit message 规范。
- [ ] 每人 **≥1 个合入 `main` 的 Merge Request**：标题/描述清楚、指定组员 reviewer、被 approve 后由作者合并。
  - 事情太少怎么办：两人一组做 add、两人一组做 delete；其余人可用团队契约、用户故事、retro 文档各开分支做 MR（"现实中没人这样做，设计成这样是为了人人练到 Git"）。几人可共用一个分支，但每人都要有一次合入 main 的经历。
- [ ] commit / MR 里用 `Closes #N` 关联 issue（Sprint 1 建议）。
- [ ] **绝不直接在 main 上改、绝不合并坏代码。**

### ☑ B. Teamwork Contract（`teamwork.md`）
- [ ] 用课程模板（可选）写契约并推到 main：成员技能（Customer / Development / Coaching，主要 + 附加 + 想学的技能）、沟通计划（**MS Teams**、会议时间、standup 天数、响应时限、缺席处理）、分工与 code review 规则、ground rules、冲突解决与上报路径、质量标准（DoD 先写自认为合适的，Sprint 2 正式定）、更新历史。
- [ ] 全员同意；Sprint 内可改但要记录改了什么/为什么。

### ☑ C. Issue Board
- [ ] GitLab Plan → Issues 建 board；把工作拆成**小 issue**（如 research Flask / backend add / frontend add …），分配负责人、指定 reviewer；拖动 Open/Closed。
- [ ] Week 3 起：**每个用户故事一个 issue**，issue 里附验收标准；链接到 board。

### ☑ D. Standups（Weeks 2–3，每周 ≥2 次）
- [ ] 指定发起人，在 Teams 频道发模板，每人回答三问 + Action Items。
- [ ] 每周一次在 **lab 上当着 tutor** 做（tutor 记录出席、可能追问）；另一次组内自行做并记录。
- [ ] 遵守 Standup Guide（具体、简短、透明；不复制粘贴）。

### ☑ E. Planning & Stories（`stories.md`，Week 3 新增 §2.2）
- [ ] **(1) Discovery Process（需求工程四步）**并记录：
  - **Elicitation**：访谈同学/朋友（潜在用户）、观察、组内头脑风暴、调研 Trello/Asana/Jira/GitLab board 等——写下访谈了谁、问了什么、出现了哪些主题；
  - **Analysis**：分组主题、识别依赖（先创建才能编辑）、冲突、**只为下一个 Sprint** 排优先级；
  - **Specification**：写成故事 + 验收标准，拆分大故事；
  - **Validation**：回访受访者/组员确认"这是你要的吗？UAC 漏了什么？优先级对吗？"
- [ ] **(2) 写用户故事**："As a … I want … so that …"；客户中心、非技术语言、描述问题不描述解法；先聚焦 1–2 类用户；拆分（按优先级 / 数据边界 / 操作）；每个故事附**具体、可测试的 UAC**（rule-based 要点式 或 Given/When/Then 任选，可各练一种）。故事数量要**多于** add/delete 两个（为整个学期规划）。
- [ ] **(3) 连接 GitLab**：每个故事一个 issue，放上 board。
- [ ] 在**新分支**（如 `stories`）上建 `stories.md` → commit → push → MR → review → 合并；线下卡片可拍照贴进 md。**质量 > 数量**，展示思考过程，不要 20–30 页。

### ☑ F. Sprint Retrospective（`retro.md`，Week 3 新增 §2.3）
- [ ] Sprint 末开 60–90 分钟 retro（全员、无 tutor、指定 facilitator、五步法）。
- [ ] markdown 记录：过程（谁 facilitate、用时）、数据（what went well / challenges / more / less，可贴白板照片）、insights（模式、根因）、**Retrospective Objective**（承诺的改进目标、谁志愿跟进、如何跟踪）。
- [ ] 同样走新分支 + MR。

### ☑ G. Teamwork Evaluation（Moodle，Week 4 周一中午–周三中午）
- [ ] 每人填写对组员的评价（Participation / Dependability / Team Wellbeing / Work contribution）。保密、不计分，但**必交**才能拿 Retro & Evaluation 的 5 分。

### ☑ H. 提交与 Demo
- [ ] Week 4 周一 12:00 前把所有内容推到 `main`（不要最后一刻）。
- [ ] Week 4 lab **全员到场** demo（15–20 分钟 Q&A）。

---

## 4. 实践与期望（指南 §2 原文 + 讲师解释）

### 2.1 Agile software team practice

**2.1.1 Git practice** — Follow Git Practice and from the Week 1 lecture.
- 一切推送到 GitLab 的内容都必须遵守（MR、commit message、分支命名）。Git Practice 页要点：
  - Why it matters：清晰的 commit 帮助 reviewer 快速理解、未来开发者（含你自己）调试扩展、保持项目历史干净。
  - Merge requests：每个 MR 一个功能或一组相关改动；**Sprint 1 每人至少一个 MR**；所有 MR 必须由组内他人 approve（peer review），再由作者合并。
  - 分支命名 `<type>-<feature-name>-<short-description>`；MR 标题简洁明确。

**2.1.2 Participation and standups** — 原文：

> Two standups per week during Weeks 2–3 is required. During your lab class in Weeks 2–3, you and your team will conduct one short standup in the presence of your tutor. Each member of the team will briefly state what they have done in the past week, what they intend to do over the next week, and what issues they have faced or are currently facing. This is so your tutor, who is acting as a representative of the client, is kept informed of your progress. They will make note of your presence and may ask you to elaborate on the work you've done. Project check-ins are also excellent opportunities for your tutor to provide you with both technical and non-technical guidance. Other than the standup during your lab session, you should do at least another standup with your group and document the standup. Please also follow the Standup Guide.

**2.1.3 Teamwork Contract and Evaluation** — 找模板写契约并加入仓库；Sprint 末由组员互评四个维度：
- **Participation**：参与度、出席、提建议、承担任务、保持沟通；
- **Dependability**：按时、按质完成分配任务；
- **Team Wellbeing**：沟通、协调会议、倾听、促进讨论、提建议；
- **Work contribution**：对项目开发的贡献。

**2.2 Planning – user stories**（Week 3 发布，见 §3.E）
**2.3 Sprint retrospective**（Week 3 发布，见 §3.F）

---

## 5. 评分标准（Marking Rubric）

### 3.1 Group Marking（25 Marks）

| Component | Marks | 5 | 4–3 | 2–1 | 0 |
|---|---|---|---|---|---|
| **Git Merge Requests** | 5 | A minimum of 1 merge request (MR) per person in your group into the `main` branch. Merge requests are properly created, clearly described, peer-reviewed, and approved. | Minor issues in descriptions or review quality. | Merge requests exist but lack clarity or proper review. | No proper merge request workflow. |
| **User Stories**（Week 3 细化版） | 5 | Clear "As a…, I want…, so that…" format · Specific, testable acceptance criteria · Stories show thoughtful planning with discovery process documented (Elicitation → Analysis → Specification → Validation) | Mostly clear stories with minor vagueness · Basic or partially unclear acceptance criteria · Little evidence of planning process · Some acceptance criteria missing or vague | Basic or partially unclear stories · Little evidence of planning process · Missing acceptance criteria | Missing or incorrect format · No evidence of Requirements Engineering process |
| **Features Demo** | 5 | Add & delete task features fully functional, clearly demonstrated. | Core functionality works with minor issues. | Partially implemented or unstable features. | Not demonstrated or non-functional. |
| **Issue Board & Team Contract** | 5 | Issue board actively managed with meaningful task tracking. Team contract is specific and practical. | Evidence of use but limited depth. | Minimal engagement or superficial documentation. | Missing key components. |
| **Sprint Retro & Teamwork Evaluation**（Week 3 细化版） | 5 | Retro demonstrates genuine reflection · Identifies both strengths & improvement areas · Includes thoughtful teamwork evaluation · Shows evidence of following the retrospective process · Clear retrospective objective with follow-through plan | Some reflection but limited depth · Missing some key components · Teamwork evaluation present but superficial | Superficial or generic reflection · Lacks meaningful analysis · Teamwork evaluation missing or inadequate | Missing retrospective document · No meaningful evaluation or reflection |

### 3.2 Individual Marking（5 Marks）

| Component | Marks | Full Marks | Partial | Minimal | 0 |
|---|---|---|---|---|---|
| **Git Commit & Branching** | 3 | Creates ≥1 branches, makes ≥2 commits, and follows naming & workflow conventions correctly. | Minor inconsistencies in commits or branch usage. | Minimal or low-quality commits. | No meaningful contribution. |
| **Participation & Standups** | 2 | 2 standups per week in weeks 2–3 & Engagement in lab classes (2 marks) | Participates but inconsistently (1 mark) | N/A | No meaningful participation |

**评分说明**
- 总分 30：组分 25（5 项各 5）+ 个人分 5（3 + 2）。
- Teamwork Evaluation 本身不计分，但**不提交拿不到 Retro & Evaluation 的 5 分**。
- Standup 按个人计分：tutor 看 Teams 频道——次数、每个人都参与、更新质量、action items 是否被跟踪。
- 结果：Sprint 1 平均分高于 HD；成绩在 Moodle → Grades，Week 5 class 上 tutor 解释反馈。

---

## 6. 提交与 Demo（§3.3）

> **Sprint 1 deadline: Week 4 Monday 12pm.**
> - To submit your work, simply have your main branch on the gitlab website contain your groups most recent copy of your project. I.E. "Pushing to main" is equivalent to submitting. When marking, we take the most recent submission on your main branch that is prior to the deadline.
> - We will not mark commits pushed to main after the submission time. We do not accept late submissions for Sprint 1, because the extension will eat into your time for Sprint 1 [网页原文如此，意指 Sprint 2]. Please see Special Considerations page on course website on how we accommodate approved special considerations for Sprint 1.
> - **Demonstrations**: You will demonstrate your Sprint 1 project during your Week 4 lab sessions. All team members **must** attend these lab sessions. Team members who do not attend a demonstration may receive a mark of 0 for that sprint. If you are unable to attend a demonstration due to circumstances beyond your control, you must apply for special consideration. Demonstrations consist of a 15–20 minute Q&A in front of your tutor and potentially some other students in your class.

讲师强调：
- 站会在 Teams 里不用推仓库；契约、故事、retro 等都推到 main（建议 Markdown）。
- **无迟交、无延期**（即使有 special consideration；获批者评分时考虑）。例外：**Sprint 1 的 retro 允许迟交到 Week 4 你的 class 之前**（仅此一次，因大家对提交时间有混淆）。
- Demo 非正式，不用准备演讲：展示给客户带来什么价值、如何做到、为什么；目的之一是确认工作是你自己的（可能让你现场改代码），也是 tutor 反馈、帮助规划下一 Sprint 的机会。

---

## 7. 学术诚信（§4）

- 程序必须完全是本组的工作；不向组外任何人展示/提供；不用公开仓库；不抄他人想法或代码。
- **AI 生成代码未正确声明 = 抄袭**；即使声明了也必须能解释代码。
- 处罚：负分、自动不及格等。

---

## 8. 课堂 Q&A 要点汇总

| 问题 | 答案 |
|---|---|
| Sprint 1 功能到底要多少？ | 显示 + add + delete，最小即可；无需 UI 美化、邮件确认、持久化。 |
| add 和 delete 要分开吗？ | 分开（不同的事），且用户故事要多于这两个。 |
| 每人都要 MR 但事情太少？ | 分工：两人 add、两人 delete，其余人合并契约/故事/retro 文档；可共用分支但每人都要合一次 main。 |
| 一个分支够整个项目吗？ | 每人都要有自己的分支，否则怎么合并到 main；分工可随时改。 |
| 用户类型怎么定？ | 各组自定（学生、mentor、product owner、admin…），先聚焦 1–2 类。 |
| Sprint 2/3 在 Sprint 1 基础上继续？ | 是，同一项目做 10 周；本周写故事就是在为整个学期规划。 |
| 契约还能改？ | 随时可改，活文档，留更新历史。 |
| 语言？ | 后端 Python（Flask），前端 HTML/CSS，不允许其他语言。 |
| Sprint 2 指南何时发？ | Week 4，逐周发布以免信息过载。 |
| 故事文档要多长？ | 质量 > 数量，可贴卡片照片，"不要 20–30 页"。 |
| 要测试代码吗？ | Sprint 1 尚未讲测试，展示价值的方式就是向 tutor 演示功能。 |
| 组员不交东西/失联？ | 先 Teams 联系；24–72 小时无回应先担心安全并报告 tutor；然后跳过其工作继续，计分问题找 tutor。 |
| 契约要在截止前交吗？（Week 4） | 契约是规划文档（Sprint 1 交付物）；你问的其实是 retro——Sprint 1 retro 可迟交到本周 class 前。 |
| retro 要多长？ | 不必长：证明开了会、走了流程、学到了什么、下个 Sprint 改什么。 |
| Sprint 1 "东西太多"？ | 初衷是文档越少越好；讲师会看提交情况调整 Sprint 2/3。 |

---

## 9. Sprint 1 任务总结

**一句话**：用最小的功能（显示/add/delete）作载体，把敏捷团队的"基本功"全部练一遍——Git 分支 + peer-reviewed MR、团队契约、Issue Board、异步站会、需求工程 → 用户故事 + UAC、五步 Retro + 互评——并在 Week 4 lab 上向"客户"demo 价值。

**核心要求速记**
- 截止 **W4 Mon 12:00**，推 main 即提交，无迟交；W4 lab 全员 demo。
- 组分 25：MR 5 / 用户故事 5 / 功能 demo 5 / board+契约 5 / retro+互评 5；个人 5：commit&branch 3 / standup 2。
- 每人：≥1 分支、≥2 commit、≥1 个合入 main 的 MR；每周 ≥2 次 standup（1 次在 lab）。
- 三个 markdown：`teamwork.md`、`stories.md`（含 Elicitation→Analysis→Specification→Validation + 故事 + UAC + issue 链接）、`retro.md`（过程/数据/insights/目标+负责人）。
- 互评 Moodle 必交（W4 Mon–Wed 中午）。
- AI 须声明且能解释代码；main 永远只放能工作的代码。

**讲师给的 Sprint 1 "拿分策略"**
1. 易分先拿：契约、board、standup 照做就得分。
2. 功能只占 5 分，做最小版本；把时间投在理解 starter code、练 Git、协作、反思、规划上。
3. 有经验者帮新手，保证每人都有 MR；Sprint 1 打好基础，后面越来越难。
4. 有疑问及早问论坛/tutor，别在反馈表里提问。
