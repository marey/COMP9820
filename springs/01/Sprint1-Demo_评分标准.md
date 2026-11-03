# Sprint 1 Demo Grading Criteria　Sprint 1 演示评分标准与解读（满分 10 分）

> **来源**：本目录 `Sprint1-Demo.pdf`（Moodle「Assessments Hub → Sprint 1 - Demo」提交页的 Submission status + Feedback + Grade breakdown，导出于 2026-10-31）
>
> **开放 / 截止**：Opened: Wednesday, 14 October 2026, 12:00 AM　｜　Due: Sunday, 18 October 2026, 9:00 PM（Week 5 周日 21:00，提交的是 lab 现场演示的**录像**）
>
> **提交物**：一组一份，`.mov` 录像（示例文件名 `COMP9820 Sprint 1 Demo Recording–<组名>-26T3.mov`）；Moodle 显示 Grading status: Released，Graded on: Thursday, 29 October 2026
>
> **配套**：Sprint 2 的演示要求与评分项见 [Sprint2_Guidelines.md](../02/Sprint2_Guidelines.md) §3.1；项目背景（Shared Expense Splitter、GitLab 流程）见 [Sprint2_Guidelines_1.md](../02/Sprint2_Guidelines_1.md)
>
> 💡 **关于案例**：第 5 节的真实反馈来自 26T3 一个小组的评分页，组名已隐去。它拿了 3.5 / 10，丢分的方式非常典型，值得每个组在 Sprint 2 demo 前读一遍。

---

## 一页总结

**考什么**：10 分，只有 **3 个评分项**，每项 6 档（None / Very poor / Poor / Good / Very good / Excellent）。**Sprint Process Evidence 一项就占 4 分**，比"功能能不能跑"还重：这门课考的是过程，不是产品。

| # | 评分项 | 满分 | 档位分值 | 拿满分的关键词 | 最容易丢分的地方 |
|---|---|---|---|---|---|
| 1 | Sprint Process Evidence（Sprint 过程证据） | 4 | 0 / 0.5 / 1 / 2 / 3 / 4 | 被问到任何功能都能从 **story → issue → branch → MR（他人评审、有评论、评论导致了修改）→ main** 追溯；board 上 issue 在 sprint 内**持续移动**；**每个人都写过也评审过 MR** | **压根没展示 GitLab**（直接 0 分）；issue 在 deadline 前一次性批量建/关；MR 自己批准、没评论、不挂 issue |
| 2 | Working Features（可运行的功能） | 3 | 0 / 0.5 / 1 / 2 / 2.5 / 3 | Sprint 1 功能**通过 UI、从 main 运行**、结果正确、对得上验收标准；无报错、加载快；**像用户一样操作**；边界问题（只有部分成员分摊的费用）**用产品行为回答** | 从 feature 分支跑（最高 2）；只展示后端输出或代码；分摊金额加起来不等于总额；只展示模板自带的 Notes 示例（0 分） |
| 3 | Presentation, Teamwork and Q&A（展示、团队协作与问答） | 3 | 0 / 0.5 / 1 / 2 / 2.5 / 3 | **10–12 分钟内**；结构清楚、成员间交接顺畅；**每个人讲实质性的一部分**；任何人被问到**别人做的部分**也能答；能解释 Sprint 1 的决策理由 | 超时 / 远不足 10 分钟（最高 0.5）；一个人讲完；只会讲自己那块；幻灯片和 demo 来回切换 |

**三条分水岭**：

1. **Process 2 → 3 → 4**：2 分是"大部分工作走了 issue / branch / MR，但评审很薄"；3 分要求**能现场追溯一条被演示的功能**，且贡献分散；4 分要求**任意一条都能追溯**、评审有**导致修改的评论**、**每个成员都写过且评审过 MR**。评审质量和参与度是最后一分的分界。
2. **Features 2 → 2.5 → 3**：2 分的典型扣分是"**从 branch 而不是 main 运行**"或有小错误；2.5 要求 main + 正确 + 对验收标准；3 分要求**零错误**、按用户的方式操作、用产品**现场回答边界问题**。
3. **Presentation 2 → 2.5 → 3**：2 分是"接近 10–12 分钟，人人都讲但不均"；2.5 要求**在时限内**、人人都讲**实质内容**、问谁都答得准；3 分加上交接顺畅、**能答别人做的部分**、能讲**为什么这样决定**。

**rubric 里的硬门槛**（碰到就被锁在低档）：

| 门槛 | 锁在哪一档 |
|---|---|
| 没展示 GitLab（board / MR / 文档） | Process = None（0） |
| 只展示模板自带的 Notes 示例、或只放幻灯片 / 代码 | Features = None（0） |
| 功能从未合并的分支运行 | Features ≤ 2 |
| 远少于 10 分钟或超过 12 分钟 | Presentation ≤ 0.5（真实案例中超时 2 分钟以上被判为 Poor = 1） |
| 一个人讲完全场 | Presentation ≤ 0.5 |

> 🎯 **一句话总结**：Sprint 1 Demo 拿高分 = **先开 GitLab board 讲过程（4 分在这里）+ 从 main 跑的 UI 演示并对照验收标准（3 分）+ 10–12 分钟内人人讲一段、问谁都能答（3 分）**。顺序建议：board → 一条 story 的追溯 → 功能演示 → 回顾与下一步 → Q&A。

---

## 0. Submission Status　提交信息（Moodle 页面）

| 字段 | 原文 | 中文 |
|---|---|---|
| Opened | Wednesday, 14 October 2026, 12:00 AM | 2026 年 10 月 14 日（周三）0:00 开放 |
| Due | Sunday, 18 October 2026, 9:00 PM | 2026 年 10 月 18 日（周日）21:00 截止 |
| Group | *(组名)* | 以组为单位提交 |
| Submission status | Submitted for grading | 已提交待评分 |
| Grading status | Released | 成绩已发布 |
| Time remaining | Assignment was submitted 1 day 20 hours early | 提前 1 天 20 小时提交 |
| File submissions | `COMP9820 Sprint 1 Demo Recording–<组名>-26T3.mov` | 提交物是 lab 现场演示的录像 |
| Grade | 3.50 / 10.00 | 案例组得分 |
| Graded on | Thursday, 29 October 2026, 10:53 AM | 评分日期 |

> ⚠️ **录像是用来交叉评分和处理 Special Consideration 的**，分数来自 lab 现场的演示（Sprint 2 指南原话：*We require a recording of your live lab demo for cross-marking and special consideration purposes*）。所以录像要完整录下**音频 + 幻灯片 / 浏览器画面**，超过 Moodle 上传限制就传 UNSW OneDrive 并提交含链接的文本文件，链接设为 UNSW 内任何人可看。

---

## 1. Sprint Process Evidence　Sprint 过程证据（0–4 分）

| 分数 | 档位 | 原文描述 | 中文 |
|---|---|---|---|
| 0 | None | there's no backlog, issue board, branches or merge requests, or the team presents the application only. | 没有 backlog、issue board、分支或 merge request，**或者团队只展示了应用本身** |
| 0.5 | Very poor | there's a backlog or board, but the issues were created or closed in a batch near the deadline. Most work was merged into main with no evidence of review, or merge requests aren't linked to issues. | 有 backlog 或 board，但 issue 是在 deadline 前**一次性批量创建或关闭**的；大部分工作合进 main 时没有评审证据，或 MR 没有关联 issue |
| 1 | Poor | issues, branches and merge requests exist, but few link to each other, and some stories have no acceptance criteria or story points. Reviews are rare, self-approved or have few comments, and few merge requests links to issues. | issue、分支、MR 都有，但很少互相关联；部分 story 没有验收标准或 story points；评审很少、**自己批准自己**或几乎没评论；很少 MR 关联到 issue（原文 "merge requests links" 主谓不一致，原文如此） |
| 2 | Good | most stories have acceptance criteria and story points. Most work goes through an issue, a branch and a merge request. Reviews are thin, such as approvals with no comments, or 1 or 2 members account for most of the activity. | 大部分 story 有验收标准和 story points；大部分工作经过 issue → 分支 → MR；但**评审很薄**（例如只批准不评论），或者 **1–2 个人贡献了大部分活动** |
| 3 | Very good | the team can trace a demonstrated feature from its story, through an issue, a branch and a merge request reviewed by another member, to main. Contributions are spread across members. | 团队能把**一条演示过的功能**从 story 追溯到 issue、分支、**由另一名成员评审的 MR**，直到 main；贡献分散在各成员之间 |
| 4 | Excellent | the team traces any feature it demonstrated, when asked, from a testable, estimated story to main. The board shows issues moving through the sprint. Reviews are substantive, with comments that led to changes. Every member authored and reviewed merge requests. | 被问到**任意一条**演示过的功能，团队都能从一条**可测试、已估算**的 story 追溯到 main；board 显示 issue **在整个 sprint 中持续流动**；评审有实质内容，**评论导致了代码修改**；**每个成员都写过 MR、也评审过 MR** |

### 怎么拿分

这一项是 Demo 的重心，却最容易被当成"附带的"。真实案例里这一项拿 0 分，原因只有一句：**全程没展示 GitLab**。功能做得再好，没展示过程就是 None。

rubric 从 0 到 4 其实在检查同一条链的五个环节：

| 环节 | 0.5 / 1 分的样子 | 2 分 | 3 分 | 4 分 |
|---|---|---|---|---|
| Story / issue | 批量建、批量关；没验收标准、没 points | 大部分有验收标准和 points | 演示的那条能追溯 | **任意一条**都能追溯，story 可测试、已估算 |
| Branch | 直接在 main 上改 | 大部分走分支 | 演示的功能走了分支 | 同左 |
| MR + 评审 | 自己批准自己、没评论 | 只批准没评论 | **另一名成员**评审 | 评论**导致了修改** |
| 关联 | MR 不挂 issue | 大部分挂了 | 演示的那条挂了 | 全挂 |
| 参与度 | 1–2 人干完 | 1–2 人占大头 | 贡献分散 | **每个人都写过也评审过 MR** |

演示时建议按下面的顺序把这条链**现场点开**，每一步都在屏幕上停 10 秒：

1. **Issue board**：打开 board，让 tutor 看到 Open / Doing / Review / Done 列里 issue 的分布，而不是 Done 一列堆满。
2. **一条 story**：点进一个 issue，读出 user story 格式、验收标准、story points、milestone。
3. **分支与 MR**：从 issue 的 "related merge requests" 点进 MR，展示 reviewer 不是作者本人、评论区有讨论、"Changes" 里能看到评论后又推的 commit。
4. **合并到 main**：MR 状态 Merged，main 的 commit 历史里能看到这个 merge commit。
5. **贡献分布**：GitLab 的 Contributors 图或 MR 列表按 author / reviewer 过滤，证明人人都写过也评过。

> ⚠️ **"评论导致了修改"是 3 分和 4 分的分界**。只在 MR 里写 "LGTM" 不算实质评审。提前挑 1–2 个评审里真的改过东西的 MR 当例子，比如 reviewer 指出分摊金额四舍五入后加起来不等于总额，作者补了一个 commit 修复。
>
> ⚠️ **"when asked" 意味着 tutor 会随机点功能**。不要只准备一条链，确保**每个演示过的功能**都能在 10 秒内从 issue 点到 MR。

### 自查

- [ ] Board 上 issue 的创建和关闭时间分散在整个 sprint，不是最后一天
- [ ] 每条 story 有 user story 格式、验收标准、story points
- [ ] 每个 MR 挂了 issue，reviewer ≠ author，至少有一条实质评论
- [ ] 至少 1–2 个 MR 能展示"评论 → 修改 → 再推"的过程
- [ ] 每个成员的名字同时出现在 MR 的 author 列和 reviewer 列
- [ ] 演示脚本里有**明确的一段**用来展示 GitLab，而且排在功能演示之前

---

## 2. Working Features　可运行的功能（0–3 分）

| 分数 | 档位 | 原文描述 | 中文 |
|---|---|---|---|
| 0 | None | the team doesn't demonstrate a working feature. It shows nothing, only the starter template (including the Notes example), or slides and code instead of a live product. | 没有演示可运行的功能：什么都没展示，或只展示了**起始模板（包括 Notes 示例）**，或用幻灯片和代码代替了运行中的产品 |
| 0.5 | Very poor | the team attempts a Shared Expense Splitter feature, but it fails during the demo or works only partially. It may run from an unmerged branch or be shown only in code. | 尝试演示 Shared Expense Splitter 的功能，但演示中失败或只能部分工作；可能从未合并的分支运行，或只在代码里展示 |
| 1 | Poor | one core feature works, such as creating a group or adding an expense. Others are incomplete, shown only through backend output, or produce errors or wrong results, such as shares that don't add up to the expense total. | 只有一个核心功能能用（如创建群组或添加费用）；其他功能不完整、只通过后端输出展示，或产生错误 / 错误结果（如**各人分摊加起来不等于费用总额**） |
| 2 | Good | several core features work through the UI and give correct results for the cases shown. Minor errors, slow responses, or a feature running from a branch instead of main hold the demo back. | 多个核心功能通过 UI 可用，演示的用例结果正确；但有小错误、响应慢，或**某个功能从分支而不是 main 运行**，拖累了演示 |
| 2.5 | Very good | the team's Sprint 1 features work end to end through the UI, run from main, give correct results, and match their acceptance criteria. Any problems are cosmetic. | Sprint 1 的功能通过 UI 端到端可用、**从 main 运行**、结果正确、**与验收标准一致**；仅有外观上的小问题 |
| 3 | Excellent | everything at Very good, with no errors and reasonable load times. The team shows each feature as a user would use it, ties it to its acceptance criteria, and handles questions about edge cases, such as an expense shared by only part of the group, by showing the product's behaviour. | 在 Very good 的基础上**没有任何错误**、加载时间合理；团队**像用户一样**演示每个功能，把它和验收标准对应起来，并**通过展示产品行为**来回答边界问题（如一笔费用只由群组里的部分成员分摊） |

### 怎么拿分

Sprint 1 要演示的是通用版 Shared Expense Splitter 的核心功能（见 Sprint 2 指南对 Sprint 1 的概括：groups、expenses、splits、net balances、edit and delete、history）。rubric 里直接点名的用例就是演示脚本：

| rubric 里的用例 | 演示时怎么做 | 对应档位 |
|---|---|---|
| creating a group / adding an expense | 在 UI 里新建一个群组、加一笔费用 | 1 分的"一个核心功能" |
| shares add up to the expense total | 加一笔 100 元三人均分，当场指出 33.33 + 33.33 + 33.34 = 100 | 不做对就停在 1 分 |
| run from main | 演示前在终端 `git branch` 或 `git log --oneline -1` 让 tutor 看到当前在 main，再启动服务 | 不在 main 最高 2 分 |
| match their acceptance criteria | 演示每个功能前读一遍它的验收标准，演示后说"这条满足了" | 2.5 分的要求 |
| an expense shared by only part of the group | 准备好一笔只有 2 个人分摊的费用，被问到时**现场操作**而不是口头解释 | 3 分的要求 |

> ⚠️ **"Notes example" 不得分**。模板自带的示例功能不算 Sprint 1 功能，演示时直接跳过，不要花时间介绍。Sprint 2 的规则更严：Sprint 1 功能也不再得分，除非为变体演进过。
>
> ⚠️ **"slides and code instead of a live product" = 0 分**。幻灯片只用来放大纲和验收标准，功能一律在浏览器里操作。

真实案例里这一项拿了 2.5（Very good），tutor 的评语是 "Pleasing interface, but some workflows could be streamlined and being able to (optionally) name an expense would be helpful"：界面好看，但有些操作流程可以更顺，费用应当能（可选地）起名。这就是 2.5 和 3 的差距：**功能对了，但没有"像用户一样"去想**。给费用起名、少点一次按钮，这类改进在 Sprint 2 做变体时顺手就能带上。

### 自查

- [ ] 演示机上 `git status` 干净、当前分支是 main，且 main 包含所有要演示的 MR
- [ ] 演示前一天在**干净环境**（新 clone + 新 venv）跑一遍 README 的启动步骤
- [ ] 每个功能有一条验收标准可以读出来，演示用例覆盖验收标准里的数字
- [ ] 分摊金额的求和、净余额的正负都当场核对过
- [ ] 准备好 1–2 个边界用例（部分成员分摊、删除后余额变化）能现场操作
- [ ] 没有演示模板自带的 Notes 示例

---

## 3. Presentation, Teamwork and Q&A　展示、团队协作与问答（0–3 分）

| 分数 | 档位 | 原文描述 | 中文 |
|---|---|---|---|
| 0 | None | the team doesn't present or delivers no structured presentation and can't answer questions about its work. | 没有展示，或展示毫无结构，且无法回答关于自己工作的问题 |
| 0.5 | Very poor | the presentation is disorganised and hard to follow, or it runs far under 10 minutes or beyond 12 minutes. One member presents almost everything, and the team can't answer basic questions about its product or process. | 展示混乱、难以跟上，或**远少于 10 分钟 / 超过 12 分钟**；几乎由一个人讲完；团队答不出关于产品或过程的基本问题 |
| 1 | Poor | the structure is weak and needs frequent clarification. Speaking time is very uneven, with some members saying little or nothing. Answers are vague, and members can discuss only their own work, if that. | 结构弱、经常需要澄清；发言时间很不均，有成员几乎不说话；回答含糊，成员最多只能讲自己做的部分 |
| 2 | Good | the presentation is mostly clear and close to the 10–12 minutes. Every member speaks, though not equally. Most questions get accurate answers, but some members struggle with parts they didn't build. | 展示基本清楚、**接近** 10–12 分钟；每个人都发言但不均等；大部分问题回答准确，但有成员答不上自己没做的部分 |
| 2.5 | Very good | the presentation is well organised, easy to follow and within 10–12 minutes. Every member presents a substantive part. Questions to any member get clear, accurate answers about the product and the team's process. | 展示组织良好、易于跟上、**在 10–12 分钟内**；每个成员都讲了**实质性的一部分**；问任何成员都能得到关于产品和过程的清楚准确的回答 |
| 3 | Excellent | everything at Very good, with smooth handovers between members. Each member answers confidently about any part of the team's work, including parts they didn't build, and the team explains the reasons behind its Sprint 1 decisions and what it did. | 在 Very good 的基础上成员间**交接顺畅**；每个成员都能自信地回答团队工作的**任何部分（包括自己没做的）**；团队能解释 Sprint 1 各项决策**背后的原因**和做了什么 |

### 怎么拿分

三个硬指标：**时间（10–12 分钟）、人人讲实质内容、问谁都能答**。真实案例这一项只拿 1 分（Poor），tutor 写了三句话，每句都对应一个档位描述：

| tutor 评语 | 对应 rubric | 修法 |
|---|---|---|
| No need to introduce all team members at the start.（不需要在开头逐个介绍成员） | 时间浪费在没分的内容上 | 开场一句话："我们是 X 组，今天演示 Shared Expense Splitter 的 Sprint 1，顺序是 board → 功能 → 回顾"。名字在每人开讲时自己报一下就够 |
| The constant back and forth between slides and demo cost time and created confusion.（幻灯片和 demo 来回切换费时且混乱） | "structure is weak and needs frequent clarification" | 把幻灯片压缩到开头和结尾，中间一整段都留在浏览器 + GitLab；验收标准写在幻灯片上的话就打印出来或开第二个窗口并排放 |
| Went >2 min overtime.（超时 2 分钟以上） | "beyond 12 minutes" 是 Very poor 的描述 | 计时排练至少两遍，目标 11 分钟；指定一个人看表，到 10 分钟时无论讲到哪都切到收尾 |

> ⚠️ **"parts they didn't build" 是 2 分和 3 分的分界**。排练时互相提问对方负责的功能：它的 issue 号是多少、验收标准是什么、MR 里评审提了什么。每人至少能讲清**全部功能的用户流程**和**团队的 Git 流程**。
>
> ⚠️ **"reasons behind its Sprint 1 decisions"**：准备 2–3 条决策和理由，例如"为什么用 FastAPI 而不是 Flask""为什么分摊金额用整数分而不是浮点数""为什么 MR 要求至少一人批准"。这些在 Q&A 里被问到就是送分题。

### 自查

- [ ] 排练过两遍以上，计时在 10–12 分钟内，有人负责看表
- [ ] 每个成员有一段 1.5–2 分钟的实质内容（不是只读标题）
- [ ] 成员之间的交接有固定的一句话（"接下来由 B 演示添加费用"）
- [ ] 幻灯片 ≤ 5 页，中间不切回幻灯片
- [ ] 互相提问过对方的功能、issue、MR
- [ ] 准备了 2–3 条"为什么这样做"的决策理由
- [ ] 演示前 10 分钟到场调试投影 / 共享屏幕 / 录屏（[Sprint1_Demo注意事项.md](../../lectures/Sprint1_Demo注意事项.md) 的三条：不能超时、不需要自我介绍、提前调试设备）

---

## 4. 推荐 Demo 脚本（11 分钟）

按分值分配时间：过程 4 分、功能 3 分、展示 3 分，所以**过程证据的时间不能少于功能演示**。

| 时间 | 内容 | 画面 | 负责人 | 对应评分项 |
|---|---|---|---|---|
| 0:00–0:30 | 一句话开场：组名、产品、今天的顺序 | 幻灯片 1 | A | 3 |
| 0:30–3:30 | GitLab board；点进 1 条 story 读验收标准和 points；点进它的 MR 展示 reviewer、评论、评论后的 commit、Merged；Contributors 图 | GitLab | B | 1 |
| 3:30–4:00 | 终端：`git branch` 确认 main，启动服务 | 终端 → 浏览器 | C | 2 |
| 4:00–8:30 | 功能演示：建群组 → 加费用（均分，核对总额）→ 部分成员分摊 → 查看净余额 → 编辑 / 删除 → 历史。每个功能前读一句验收标准 | 浏览器（第二窗口放验收标准） | C、D、E 轮流 | 2、3 |
| 8:30–9:30 | 回看 board：演示过的功能各对应哪个 issue；Sprint 1 的 2–3 条决策与理由 | GitLab + 幻灯片 2 | F | 1、3 |
| 9:30–10:00 | 下一步（Sprint 2 变体、CI）一句话收尾 | 幻灯片 3 | A | 3 |
| 10:00– | Q&A：任何人被问到任何功能都能点开 issue → MR | GitLab / 浏览器 | 全员 | 1、2、3 |

> 💡 **浏览器预先开好四个标签页**：board、要追溯的 issue、它的 MR、运行中的应用。切换标签比切换窗口快，也不会出现"幻灯片和 demo 来回切"的问题。

---

## 5. 真实反馈案例　3.5 / 10

| 评分项 | 得分 | 档位 | tutor 评语 | 中文 | 教训 |
|---|---|---|---|---|---|
| Sprint Process Evidence | 0 / 4 | None | At no point did the team show the GitLab issue board, documentation or merge requests. | 全程没有展示 GitLab 的 issue board、文档或 merge request。 | **4 分一次性归零**。不是过程做得不好，是没给 tutor 看。GitLab 必须进演示脚本 |
| Working Features | 2.5 / 3 | Very good | Pleasing interface, but some workflows could be streamlined and being able to (optionally) name an expense would be helpful. | 界面令人愉悦，但一些工作流可以更精简，费用能（可选地）命名会更好。 | 功能本身达标。差的 0.5 是"像用户一样想"：少几次点击、给费用加个名字 |
| Presentation, Teamwork and Q&A | 1 / 3 | Poor | No need to introduce all team members at the start. The constant back and forth between slides and demo cost time and created confusion. Went >2 min overtime. | 开头不需要逐个介绍成员。幻灯片和演示之间不断来回切换浪费了时间并造成混乱。超时 2 分钟以上。 | 三件事都和**时间管理**有关：砍掉没分的内容、不来回切换、排练计时 |

这组功能做得不错（2.5 / 3），但总分只有 3.5，**丢掉的 6.5 分里 6 分来自"没展示过程"和"时间失控"**，都和代码质量无关。换句话说，同样的产品，只要加 3 分钟 GitLab 展示并把时长压到 12 分钟内，就能到 7 分以上。

---

## 6. Sprint 1 → Sprint 2 Demo　下一步看什么

Sprint 2 的 demo 在 Week 8 lab 现场进行，录像 2026-11-07（周六）21:00 前提交，评分项从 3 个变成 4 个（见 [Sprint2_Guidelines.md](../02/Sprint2_Guidelines.md) §3.1）：

| Sprint 1 评分项 | Sprint 2 评分项 | 变化 |
|---|---|---|
| Sprint Process Evidence（4） | 拆进 **CI pipeline strategy（2）** 和 Presentation（3） | 过程证据的重点从"issue → MR 追溯"扩展到"**在 MR 上运行的流水线**"：要解释 stage 设计、什么时候跑、为什么这样设计，并展示最近一次 MR 上的运行 |
| Working Features（3） | **Working features（3）** | 规则不变：UI、从 main 运行。新增：**Sprint 1 功能和模板功能不再得分**，除非为变体演进过 |
| Presentation, Teamwork and Q&A（3） | **Presentation, teamwork and Q&A（3）** | 不变：10–12 分钟、全员出席并发言（无 Special Consideration 缺席者该项 0 分）、问谁都能答 |
| — | **Variation and target users（2）** | 新增：解释变体、目标用户、成功标准 |

本文第 1–3 节的自查清单在 Sprint 2 照用，再加两条：**流水线的某次失败记录**（Sprint 2 报告也要这条证据）和**变体的目标用户一句话**。真实案例的三条教训（展示 GitLab、不来回切换、计时）在 Sprint 2 的 rubric 里一样有效。
