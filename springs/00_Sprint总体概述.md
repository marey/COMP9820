# COMP9820 Sprint 整体概述（Sprint 1 / 2 / 3）

> 课程：COMP9820 Software Project Management（UNSW 26T1，讲师 Dr. Yuchao Jiang）
> 来源：Week 1–9 讲义整理（`../lectures/`）。讲义字幕中的 "spring" 即 **sprint**。
> 本文件汇总所有与 Sprint 相关的**通用**内容；各 Sprint 的专属任务清单与评分表见 `01/02/03_SprintN_详细任务.md`。

---

## 目录

1. [课程考核结构：只有一个项目、三个 Sprint](#1-课程考核结构只有一个项目三个-sprint)
2. [项目题目：Task Tracker](#2-项目题目task-tracker)
3. [Sprint 是什么（课程定义）](#3-sprint-是什么课程定义)
4. [贯穿三个 Sprint 的固定实践（Sprint Rituals）](#4-贯穿三个-sprint-的固定实践sprint-rituals)
5. [提交、Demo 与出勤规则](#5-提交demo-与出勤规则)
6. [评分逻辑与讲师的评分哲学](#6-评分逻辑与讲师的评分哲学)
7. [AI 使用与学术诚信](#7-ai-使用与学术诚信)
8. [三个 Sprint 的演进关系](#8-三个-sprint-的演进关系)
9. [各 Sprint 交付物一览表](#9-各-sprint-交付物一览表)
10. [技术栈与仓库约定](#10-技术栈与仓库约定)
11. [讲师反复强调的通用建议](#11-讲师反复强调的通用建议)
12. [Sprint 相关时间线（26T1）](#12-sprint-相关时间线26t1)

---

## 1. 课程考核结构：只有一个项目、三个 Sprint

- **没有期末考试、没有 quiz、lab 不计分**；唯一考核是一个**小组软件项目**，分 3 个 Sprint 完成（Week 1–10）。
- 每个 Sprint 都有 **组分（Group）+ 个人分（Individual）**，因为每个人投入不同；每个 Sprint 末 tutor 都会给反馈，不会到最后才知道情况。
- 课程网站 **Assignments Overview** 原文：

> The assessments in this course are built around one group software project. Working in a team, you will apply and practice software project management concepts such as planning, collaboration, agile workflows, and reflective practice.

| Sprint & Weeks | 主题 | 权重 | 截止 | 交付物（Deliverables） |
|---|---|---|---|---|
| **Sprint 1**（Weeks 1–3） | Foundations & First Flight | Group **25%** / Individual **5%** | **Week 4 Monday 12:00** | Project demo · Agile software team practice · Sprint report |
| **Sprint 2**（Weeks 4–6） | Quality, CI & Deployment | Group **25%** / Individual **5%** | **Week 7 Monday 12:00** | Project demo · Agile software team practice · Sprint report |
| **Sprint 3**（Weeks 7–10） | Ownership, Risk & Portfolio | Group **30%** / Individual **10%** | **Week 10 Friday 17:00** | Project demo · Agile software team practice · Portfolio and final report |

- 合计 100%：组分 80 + 个人分 20。
- Special consideration 需在 UNSW 中央系统申请；Sprint 1 即使获批也**不延期**（会吃掉 Sprint 2 时间），但评分时会考虑。
- 讲师明确：**Sprint 1 分最好拿，Sprint 2 更难，Sprint 3 最难**——每个 Sprint 都在为下一个打基础（Sprint 2 用到 Sprint 1+2 学的东西，Sprint 3 同理）。Sprint 1 平均分高于 HD；Sprint 2/3 的 rubric 工作量更大、质量要求更高。

### 分组
- **每组 4–5 人，Week 1 lab 随机分组**（公平起见；原则之一：组里不会只有一个女生，除非本人愿意）。不能到场要邮件 tutor 保留位置。
- 把小组当作**创业公司**：有人擅长编码、有人擅长规划与冲突处理，尽力贡献即可；但**每个人都必须写代码**（不写代码无法学会管理代码、处理冲突）。
- 建议每个 Sprint **轮换角色/leader**。

---

## 2. 项目题目：Task Tracker

讲师编的小故事（课程网站 Project Overview）：

> "Procrastination Warriors" 们用便利贴、聊天记录、截图记任务，结果任务遗忘、deadline 错过；于是一群学生开发者（就是你们）创建了神奇的 **Task Tracker**：可添加、编辑、删除、分配任务，让每个人都清楚该做什么。

- **整个 10 周同一题目**，三个 Sprint 层层递进；Sprint 2/3 建立在 Sprint 1 之上。
- Sprint 1 所有组做同样的最小功能（add & delete task）；从 Sprint 2 起功能由**你们自己写的用户故事**决定，课程不规定具体功能（如登录/用户）。
- 讲师/tutor 扮演**客户**："我有问题和需求，你来解决。"
- Starter code：Flask 最小应用（`app.py` 后端 + `templates/index.html` 前端 + `requirements.txt` + README），每人 GitLab 已建好项目仓库和 `lab_git` 练习仓库。

---

## 3. Sprint 是什么（课程定义）

Week 2 课件原文：

> A sprint is a fixed amount of time (e.g. week, fortnight) where you set a number of tasks to be completed in the team. After that period is up, you review progress, and set tasks for the next sprint.
> - **Time is fixed, scope is flexible**
> - Plan only for the next sprint
> - Typically have a release at the end of each sprint

讲师补充：
- Sprint 对应敏捷的 **fast feedback + iterations**：不规划明年，只规划最近的一两周，因为未来会变。
- 每个 Sprint 末要**带来价值**；本课不做真实 release，而是 **demo 给 tutor**（tutor 扮演客户）："你带来了什么价值？"
- Sprint 末组内互相反馈/review：这周怎么样？工具合适吗？流程要不要改？——这就是 **Sprint Retrospective**。
- 敏捷是哲学不是流程："You cannot use Agile, you can only be Agile."——Sprint、Standup、Retro 等只是**起点**，各组要定制适合自己的方式。

---

## 4. 贯穿三个 Sprint 的固定实践（Sprint Rituals）

以下实践从 Week 2 一直用到 Week 10，每个 Sprint 都会被评分（"Sprint ritual 与 Sprint 1 相同"）。

### 4.1 Git 实践（Git Practice 页）
- **一切贡献都通过 Git 提交**："在业界我们不是上传文件到 Moodle 来交作业，而是用 Git。" **推到 `main` 即提交。**
- **main 永远只放能工作的代码**；从 Sprint 2 起还要求 **main 永远绿（CI 通过）**。
- 流程：`git pull` → `git checkout -b <branch>` → 开发 → `git add`/`git commit -m "有意义的信息"` → `git push --set-upstream origin <branch>` → GitLab 建 **Merge Request** → 组员 review/approve → **作者自己 merge**。
- **绝不直接在 main 上改、绝不合并坏代码。**
- **Commit message**：Descriptive yet Concise / Single-Purpose / Unique and Non-Repetitive。✅ "Fix login failure when password contains special characters"；❌ "Fix stuff" / "random" / "update"。
- **分支命名**：`<type>-<feature-name>-<short-description>`，如 `feature-add-task`、`bugfix-password-validation`、`docs-update-readme`（可加自己名字）。
- **MR 规范**：每个 MR 一个功能或一组相关改动；标题清楚（❌ "Fix"/"Update"，✅ "Add user authentication feature"）；描述写 add/delete/change 了什么；**必须由他人 review 并 approve，再由作者合并**。
- **Issue ↔ Commit ↔ MR 关联**：Issue 代表工作、Commit 代表实现、MR 代表审查与集成；在 commit/MR 描述里写 `Closes #N`（Sprint 1 建议、Sprint 2 起必做）。
- Sprint 1 要求**每人 ≥1 个合入 main 的 MR**（为了人人练到 Git）；Sprint 2 网页仍写 "at least one MR per person" 但讲师口头放宽；Sprint 3 个人分要求 "at least one substantial MR contribution"。

### 4.2 Standups（站会）
- 回答三问：What did I do since last standup? / What will I do before next standup? / What's blocking me?
- **形式**：异步在 **MS Teams 频道**发帖即可（不是视频会）；最多 15 分钟，通常 2–5 分钟足够。**强烈建议用 MS Teams**——tutor 能看到证据；用 WhatsApp/Discord 出冲突时课程无法查证。
- **频率**：Sprint 1 每周 ≥2 次（Weeks 2–3）；Sprint 2/3 每周 **3 次**（推荐 Mon/Wed/Fri）；每个 Sprint 都有 **1 次在 lab 上当着 tutor** 做（tutor 记录出席、可能追问细节、给技术/非技术指导）。
- **不是给 tutor 的状态汇报**，是团队自己对齐、**尽早暴露 blocker**；要有 **Action Items** 和一个发起人（Scrum Master 角色，适合想练 coaching/领导力的人）。
- 质量要求：具体（"写了 2 个用户故事"而非"做了些东西"）、简短、透明；没 blocker 写 None。
- **按个人计分**。Red flags：几周没发帖、只有一个人发、复制粘贴、没人帮解 blocker、缺三问格式。
- 证据在 Teams，**不用推到仓库**。

### 4.3 Weekly Meetings（周会）
- Sprint 1 不要求；**Sprint 2 起每周至少 1 次全员会议**（Weeks 4–6、7–9），可在 lab/live class 上开（人齐省时间），但**不是说不用课外开会**。
- 需要 **meeting minutes**：出席人、（可选）议程、讨论要点、**行动项（action items）/决策**；存放在仓库带时间戳的位置（`meetings/`、Wiki 或 `MEETING_MINUTES.md`）。可用 Teams 录制 + AI 纪要，但内容必须真实。
- 周会 = "更长的站会"：结对编码、讨论、规划、解决问题；站会异步、周会同步。

### 4.4 Issue Board（GitLab Plan → Issues）
- 跟踪任务的描述、状态（backlog/to-do/doing/done）、负责人；**拆成小 issue** 而非一个巨大 issue。
- Sprint 1：建 board、加任务、分配；**每个用户故事一个 issue** 并附验收标准（不是所有 issue 都是故事——契约、bug 也是 issue）。
- Sprint 2 进阶：**Labels**（bug/feature/testing/deployment/documentation）、**Milestones**（"Sprint 2"）可选；**MR 链接 issue（`Closes #X`）必做**；assignee、due date；保持 To Do / In Progress / Done 更新。
- Sprint 3：board 持续使用，issue/MR 可标注与风险的关系（"Mitigates R3"）；可建 "refactoring for complexity" issue 细分指派。

### 4.5 Teamwork Contract（团队契约）
- 写明成员期望与责任的**活文档**，存在仓库（建议 `teamwork.md`，Markdown 可追踪变更；PDF 不扣分），全员同意，随 Sprint 更新并**留下更新历史**（改了什么/为什么/日期）。
- 模板（课程网站，可选）：Purpose / Team Members & Skills（**技能而非角色**：Customer / Development / Coaching skills；Team Learning Goal）/ Communication Plan（平台 MS Teams、会议时间、standup 频率、响应时限、缺席怎么办）/ Work Distribution（分工、完不成怎么办、code review 规则）/ Team Ground Rules / Conflict Resolution（含上报路径）/ Quality Standards（Definition of Done，Sprint 2 正式定；讲师建议以后项目把 DoD 写进契约）/ Contract Updates。
- Sprint 1 的交付物之一；Sprint 3 要求"updated for Sprint 3 if needed（含 role rotation）"。
- 契约是**规划**（怎么协作），Retro 是**反思**——两者不同。

### 4.6 Sprint Retrospective（回顾）
- **每个 Sprint 末做一次**（heartbeat 型，60–90 分钟），全员参加、不请 tutor（保持安全），指定 facilitator（可轮换，中立、不参与、保密）。
- **五步法**（*The Art of Agile Development*）：① Prime Directive（全员朗读并口头同意）→ ② 静默头脑风暴（Enjoyable / Frustrating / Puzzling / Keep / More / Less）→ ③ Mute mapping 静默分组 + 点投票选一个主题 → ④ Generate insights（问"为什么"，不谈解法）→ ⑤ Retrospective objective（选一两个改进实验 + 志愿者跟进）；收尾：全员同意、加到 board、站会里跟踪。
- **心理安全**贯穿一切：出现指责/不尊重就停止 retro。
- **交付**：仓库里一个 markdown（如 `retro.md`），写过程（谁 facilitate、用时）、数据（what went well / challenges / more / less，可贴白板照片）、insights（模式、根因）、**改进目标 + 谁负责 + 如何跟踪**。Sprint 1 retro 例外允许迟交到 Week 4 class 前；Sprint 2/3 必须截止前交。

### 4.7 Teamwork Evaluation（组员互评）
- 每个 Sprint 截止后在 **Moodle** 开放约三天（Sprint 1：Week 4 周一中午–周三中午），链接由讲师发。
- 四个维度：**Participation · Dependability · Team Wellbeing · Work contribution**。
- **保密**：只有 tutor/讲师可见；**不直接计分**，只用于让教学团队了解小组状况（掉队、不公平、"超级英雄"）；但**必须提交**才能拿 "Sprint Retro & Teamwork Evaluation" 的分数；组员不交只影响自己。

### 4.8 Demo（每个 Sprint 末在 lab 上）
- Sprint 1/2：**非正式** demo，15–20 分钟 Q&A，不用准备演讲，展示给客户带来了什么价值、如何做到、为什么。tutor 可能要求现场改一行代码/加一个功能以确认是你自己的工作。
- Sprint 3：**正式 presentation**（带幻灯片，10–15 分钟 + ≤5 分钟 Q&A），两位 tutor 打分取平均，其他组旁听提问，每个成员都要讲。
- **全员必须到场，缺席该 Sprint 记 0 分**（除非批准的 special consideration）。

### 4.9 Testing / CI / Coverage / Maintainability（Sprint 2 起延续到 Sprint 3）
- TDD（Red → Green → Refactor），pytest + `tests/` + `conftest.py` fixture；**"测试先于实现"的证明是 git 历史**（先提交测试再提交实现），不用另写文档。
- `.gitlab-ci.yml` 在仓库根目录，每次 push / MR 自动跑 pytest；**没绿勾不合并**。
- `pytest-cov` 覆盖率报告；不追求 100%，但 Sprint 3 要求**后端覆盖率 > 70%**；覆盖边界/错误路径，不要用 AI 刷廉价测试。
- 7 个设计问题（DRY、KISS、over/under design、coupling、YAGNI、conventions）；**没有强测试套件不要重构**。

---

## 5. 提交、Demo 与出勤规则

| 规则 | 内容 |
|---|---|
| 提交方式 | **Push to `main` = 提交**。评分取截止前 `main` 上最新的 commit；之后的 commit 不算。Sprint 3 要求该 commit **CI 绿**且仓库完整。 |
| 例外 | Standup 在 Teams 频道（tutor 有权限），不用推仓库；Sprint 3 的 Portfolio 在 **Moodle** 单独提交。 |
| 迟交 | **不接受迟交**，除非 special consideration（Sprint 1 连 SC 也不延期）。唯一例外：Sprint 1 retro 可迟交到 Week 4 class 前。 |
| 不要最后一刻推 | 所有组共用同一个 CI runner；截止前集中 push 会排长队。 |
| Demo 出勤 | 每个 Sprint 的 lab demo **全员必须到场**，否则该 Sprint 0 分。 |
| 文档长度 | 所有报告只规定**上限**不设下限："we aim for short brief documentations as long as that's telling enough stories"；**质量 > 数量**，不要交 20–30 页。 |
| 提问渠道 | 有疑问**及早**发论坛/邮件；反馈表用于长期改进，不适合提问（Sprint 1 有人在反馈表里问功能要求，讲师截止后才看到）。 |

---

## 6. 评分逻辑与讲师的评分哲学

- **组分 + 个人分**；组分看团队交付与过程证据，个人分看 Git 贡献（分支/commit/MR）与 standup 参与。
- **不按功能数量给分**："groups will not be penalised having a very 'simple' or 'few' stories"——奖励有说服力的**用户价值故事**、展示流程能跑通、GitLab 上可验证的**过程证据**。讲师故意不设功能数量基线，不想让人为凑数牺牲质量与过程。
- **可追溯性（traceability）**是贯穿评分的核心：issue（含验收标准）↔ MR（`Closes #n`）↔ commit ↔ 测试/CI ↔ 报告（风险、复杂度）↔ README 链接——tutor 要能从仓库**验证**而不是推断。
- **过程证据要真实**：Sprint 1 有组 lab 上讨论质量很高，但会议记录/commit message 明显是 AI 生成、质量反而差，**因此得了更低的分**。
- 每个 rubric 都有 Strong / Developing / Limited / Not demonstrated（或 5 / 4–3 / 2–1 / 0）四档；"Use Strong as the target"。
- 验收标准未达成要能解释（时间不够 or 判断不重要而改）。
- 三个 Sprint 的重心转移：Sprint 1 敏捷实践占大头 → Sprint 2 质量/CI → Sprint 3 敏捷实践分值"大幅下降"，重心到 demo、风险、复杂度、README、portfolio。

---

## 7. AI 使用与学术诚信

- 讲师自己也用 AI、业界看重 AI 素养，**不禁止**，但：
  - 必须**正式声明**：用了什么工具、用在哪部分、为什么；
  - 必须**知道自己在做什么、能解释每一行代码**——demo 时 tutor 可能要求现场改某行/加功能；做不到 = 不了解自己的工作 = 抄袭，该 Sprint 记 0；
  - "Code generated by ChatGPT, GitHub Copilot, Gemini and similar AI/LLM tools will be treated as plagiarism unless proper acknowledgements."
- **不要合并任何自己没完全理解的 AI 生成代码**（Reddit 开发者最后悔的事）。
- 可用 GenAI 起草/组织报告文字（如让它总结 commit message 讲故事），但 AI 会自作假设——**必须审核、核对、编辑**，内容要与 commit/MR 一致并声明。
- 不要用 AI 批量生成廉价测试刷覆盖率数字。
- 常规学术诚信：程序必须完全是本组的工作；不向组外任何人展示/提供代码；不用公开仓库；抄袭检测软件会两两比对（含往期）。处罚可含负分、课程自动不及格等。

---

## 8. 三个 Sprint 的演进关系

| 维度 | Sprint 1 | Sprint 2 | Sprint 3 |
|---|---|---|---|
| 主题 | 打基础：敏捷团队实践 + 用户故事 + Git | 从"做出来"到"做得好"：测试、CI、质量、部署 | 端到端交付：持久化/复杂度、风险、README、Portfolio、正式 Demo |
| 功能 | 全组相同：显示 + add + delete（最小即可，无需 UI 美化/持久化） | 自己故事里的新功能（beyond add/delete），带测试与 CI | 继续/修改/新增故事；≥1 个 meaningful 改进；如需则持久化 |
| Standup | ≥2 次/周 | 3 次/周 | 3 次/周（同 Sprint 2） |
| 周会 | 不要求 | ≥1 次/周 + 纪要 | ≥1 次/周 + 纪要（Weeks 7–9） |
| Git/MR | 每人 ≥1 MR，peer review | 同上（口头放宽人均要求），MR 引用 pipeline、链接 issue | 同 Sprint 2；个人 ≥1 substantial MR |
| Issue board | 建立并使用；每故事一个 issue | 进阶：labels/milestones 可选，`Closes #X` 必做 | 持续使用；与风险/重构关联 |
| 测试/CI | 无要求 | TDD + pytest；CI pipeline **必做**；覆盖率 | 延续 Sprint 2 标准；CI 绿；后端覆盖率 > 70% |
| 部署 | 无 | Week 6 deployment lab（Vercel），指南标 pending | **不要求**（IP 考虑），localhost 即可；Week 9 后可选分享 |
| 文档 | `teamwork.md`、`stories.md`、`retro.md` | 会议纪要、retro、（更新的）契约、`.gitlab-ci.yml` | README（模板）、`RISK_REPORT.md`、`docs/REFACTORING_AND_COMPLEXITY.md`、会议纪要、retro、契约、个人 Portfolio |
| Demo | 非正式，Week 4 lab | 非正式，Week 7 lab（功能+测试、pipeline/coverage、文档位置） | 正式 presentation，Week 10 lab，两位 tutor |
| 分值 | 25 + 5 | 25 + 5 | 30 + 10（Demo 15 / 过程 15 / 个人 10） |
| 难度 | 最易（"easy marks"） | 更难 | 最难 |

---

## 9. 各 Sprint 交付物一览表

| 交付物 | S1 | S2 | S3 | 位置 |
|---|---|---|---|---|
| 可运行的 Task Tracker 代码（feature 分支 + MR 合入 main） | ✅ | ✅ | ✅ | GitLab `main` |
| Teamwork Contract（`teamwork.md`） | ✅ 新建 | 🔄 更新（DoD） | 🔄 更新（role rotation） | 仓库 |
| Issue Board（每故事一个 issue） | ✅ | ✅ 进阶 | ✅ | GitLab |
| 用户故事 + 需求工程过程 + UAC（`stories.md`） | ✅ | 🔄 继续 | 🔄 可修改/新增 | 仓库 |
| Standup 记录 | ✅ ≥2/周 | ✅ 3/周 | ✅ 3/周 | MS Teams |
| 周会纪要 | – | ✅ | ✅ | 仓库 `meetings/` 等 |
| Sprint Retro（`retro.md`） | ✅ | ✅ | ✅ | 仓库 |
| Teamwork Evaluation | ✅ | ✅ | ✅ | Moodle |
| `.gitlab-ci.yml` + tests/ + conftest.py | – | ✅ | ✅ | 仓库根目录 |
| 覆盖率报告（pytest-cov） | – | ✅ | ✅（>70%） | CI/本地 |
| 部署 | – | 🔶 lab/pending | 🔶 可选 | Vercel 等 |
| README（模板） | – | – | ✅ | 仓库根 |
| 风险报告 `RISK_REPORT.md` | – | – | ✅ | 仓库根，README 链接 |
| 重构与复杂度报告 | – | – | ✅ | `docs/REFACTORING_AND_COMPLEXITY.md` |
| 个人 Portfolio（≤1000 词，PDF 即可） | – | – | ✅ | Moodle |
| Demo | 非正式 | 非正式 | 正式 + 幻灯片 | lab |

---

## 10. 技术栈与仓库约定

- **必须 Python（Flask）+ HTML/CSS**：课程只支持这些，且保证组内每个人都能贡献（不是只有一两个会 JS 的人）。
- GitLab：`gitlab.cse.unsw.edu.au`；COMP9820 下的项目自带 CI runner（个人项目可能 "no runner available"）。
- 典型仓库结构（Sprint 3 完成态）：

```
tasktracker/
├── app.py                      # Flask 后端（路由；Sprint 3 可加 JSON 持久化）
├── templates/index.html        # 前端
├── requirements.txt            # Flask、pytest、pytest-cov …
├── tests/test_app.py           # pytest 测试
├── conftest.py                 # client fixture；每个测试前重置数据 / tmp_path
├── .gitlab-ci.yml              # CI：image python:3.11 → pip install -r requirements.txt → pytest
├── tasks.json                  # （可选）持久化数据文件
├── README.md                   # Sprint 3 用 README_template 重写，链接各报告
├── RISK_REPORT.md              # Sprint 3 风险报告（或 risk/RISK_REPORT.md）
├── docs/REFACTORING_AND_COMPLEXITY.md
├── teamwork.md                 # 团队契约（含更新历史）
├── stories.md                  # 需求工程过程 + 用户故事 + UAC
├── retro.md / retro_sprintN.md # 各 Sprint 回顾
└── meetings/                   # 周会纪要（Sprint 2 起）
```

- 用户故事格式：**As a (role) I want (something) so that (result)**；验收标准 rule-based 或 Given/When/Then 任选。
- Standup 模板：`📅 [Day], [Date] - Daily Standup / 1. What did you do since last standup? 2. What will you do before next standup? 3. Any blockers? @all Respond by end of day!`

---

## 11. 讲师反复强调的通用建议

1. **按周计划表走就不会掉队**；没有每周交付物，落后一点不慌，但不要等最后一刻。
2. **沟通能解决大多数冲突**：先直接、礼貌地和当事人沟通（Teams），解决不了再邮件 tutor；组员失联 48–72 小时先担心安全并报告 tutor，然后当其不会回来继续推进。
3. **心理安全**：敢于发言、频繁透明地沟通，卡住了立刻说；别等到 deadline 才说"我卡了两周"。
4. **Practice, practice, practice**：Git、测试、retro 都需要练习；Git 很多人要几周才真正掌握；第一周就统一虚拟环境、教会所有人处理 merge conflict、不要删别人的代码。
5. **一致的 review 流程**极有价值；MR 小而可审优于大爆炸式改动。
6. **每个 Sprint 都要给用户带来价值**，功能不必花哨，UI 不必漂亮；先 MVP 再迭代；需求永远不完美，及时停掉不再有效的故事。
7. **只规划下一个 Sprint**，不规划 Sprint 100。
8. **有疑问尽早问**（论坛、tutor、help session），别攒到 Sprint 2/3。
9. 保持回路短：**plan → build → test → deploy → reflect**——SPM 的心跳。
10. 三大贯穿主题：**Traceability · Automation · Psychological safety**。

---

## 12. Sprint 相关时间线（26T1）

| 周 | 日期 | 讲座主题 | Sprint 相关事件 |
|---|---|---|---|
| W1 | 2026-02-16 | Intro to SPM · Git Solo/Team | Week 1 lab 分组；lab_git；Sprint 1 指南发布 |
| W2 | 02-23 | Agile Software Team Practices | 开始 standup（≥2/周）、契约、issue board、add/delete 功能；Help sessions 开始 |
| W3 | 03-02 | Planning & Stories · Retrospective | 写用户故事（`stories.md`）、做 Sprint 1 retro |
| **W4 Mon 12:00** | 03-09 | Testing/TDD · CI | **Sprint 1 截止**；Week 4 lab demo；互评开放（Mon–Wed 中午）；Sprint 2 指南发布（细则次日定稿） |
| W5 | 03-16 | Coverage Reports · Maintainability | Sprint 1 成绩发布（Moodle Grades，平均 > HD） |
| W6 | 03-23 | Deployment / DevOps（无讲义文件夹） | Deployment lab（Vercel） |
| **W7 Mon 12:00** | 03-30 | Persistence · Software Complexity | **Sprint 2 截止**；Week 7 lab demo；Sprint 3 指南发布 |
| W8 | 04-06（Easter Monday，录播于 04-09） | Risk Management | 写风险报告 + README |
| W9 | 04-13 | Reflection, Synthesis & Next Steps（最后一讲） | 完成复杂度报告、demo 准备、Portfolio 草稿、Sprint 3 retro |
| **W10** | 04-20 周 | 无讲座 | Week 10 lab **Final Demo**（周二或周五，各组不同）；**周五 17:00 Sprint 3 截止**（GitLab + Moodle） |
