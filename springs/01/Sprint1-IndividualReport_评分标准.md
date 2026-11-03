# Sprint 1 Individual Report Grading Criteria　Sprint 1 个人报告评分标准与解读（满分 4 分）

> **来源**：本目录 `Sprint1-IndividualReport.pdf`（Moodle「Assessments Hub → Sprint 1 - Individual Report」提交页的 Submission status + Feedback + Grade breakdown，导出于 2026-10-31）
>
> **截止**：Due: Sunday, 18 October 2026, 9:00 PM（Week 5 周日 21:00，与 Sprint 1 Demo 录像同一天）
>
> **提交物**：每人一份 PDF，文件名格式 `z<学号>_<姓名>_COMP9820_Sprint1_IndividualReport.pdf`；Moodle 显示 Grading status: Released，Graded on: Thursday, 29 October 2026
>
> **配套**：Sprint 2 个人报告的要求见 [Sprint2_Guidelines.md](../02/Sprint2_Guidelines.md) §3.4（八个必答点、2 页上限）；Demo 评分标准见 [Sprint1-Demo_评分标准.md](Sprint1-Demo_评分标准.md)；项目背景（Shared Expense Splitter、GitLab 流程）见 [Sprint2_Guidelines_1.md](../02/Sprint2_Guidelines_1.md)
>
> 💡 **关于案例**：第 5 节的真实反馈来自 26T3 一位 Product Owner 的评分页，学号姓名已隐去。三项全部落在 **Good** 档，拿了 2.4 / 4。tutor 的评语写得很具体，每一句都对应 rubric 里 Good → Very good 的那条分界线，是写 Sprint 2 个人报告前最值得读的材料。

---

## 一页总结

**考什么**：4 分，**3 个评分项**，每项 6 档（None / Very poor / Poor / Good / Very good / Excellent）。**Contribution & Evidence 一项占 2 分**，另外两项各 1 分。三项有一个共同的评分逻辑：**说了什么不算，能证明的才算**。贡献要有 GitLab 链接，角色要有会议记录截图，反思要有 Sprint 1 的具体事件。

| # | 评分项 | 满分 | 档位分值 | 拿满分的关键词 | 最容易丢分的地方 |
|---|---|---|---|---|---|
| 1 | Contribution & Evidence（贡献与证据） | 2 | 0 / 0.4 / 0.8 / 1.2 / 1.6 / 2 | **每一条**贡献都挂 issue / MR / commit 链接且在 GitLab 能查到；**代码 + 非代码**（评审、看板、会议纪要）都算；说明自己的工作**如何嵌入团队的 Sprint 1**；说清自己的工作**对团队的影响**（解锁了谁、评审抓到了什么 bug） | 用 "we" 写团队的事（0 分）；"helped with the backend" 这类没链接的描述；只写"我评审了别人的 MR"却不说发现了什么、影响多大 |
| 2 | Scrum Role and Participation（Scrum 角色与参与） | 1 | 0 / 0.2 / 0.4 / 0.6 / 0.8 / 1 | 用 Sprint 1 的**具体例子**说明怎么履行角色；每次会议上自己**汇报了什么进度、提了什么阻碍、安排了什么**；Week 2–3 lab check-in 自己做了什么；**诚实反思**哪项职责做好了、哪项疏忽了；自己的参与**如何影响了团队决策** | 抄教科书定义（0.2）；"I attended most meetings"（0.4）；只写两次会议、没有会议纪要截图；说用了 issue board 却没有证据 |
| 3 | Reflection（反思） | 1 | 0 / 0.2 / 0.4 / 0.6 / 0.8 / 1 | 评价**自己的做法**而不是团队；什么有效、什么无效都有**原因**；Sprint 2 的一个改变**直接来自** Sprint 1 的一个问题；每个点背后有一个 Sprint 1 的真实事件；写明**怎么判断这个改变成功了** | 写成团队回顾（"the team …"）；"everything went well" 没原因；改变是"I will communicate better" 这类空话或一串愿望清单 |

**三条分水岭**：

1. **Contribution 1.2 → 1.6 → 2**：1.2 是"主要贡献有链接，但有的没证据、与团队 sprint 的关系只写了一句"；1.6 要求**每一条**都有证据、**代码和非代码都覆盖**、并解释自己的工作如何嵌入团队开发；2 分再加上**承担的职责**（不只是完成的任务）和**对团队的影响**。真实案例卡在 1.2 的原因是：MR 评审这件事放错了小节，而且没写评审的影响。
2. **Scrum Role 0.6 → 0.8 → 1**：0.6 是"有一两个具体例子，会议和 lab check-in 都提了但有一个很薄"；0.8 要求写出**每次会议上**自己沟通了进度、阻碍、下一步，以及 **Week 2–3 lab check-in** 的具体贡献；1 分再加上**诚实的自我评价**（做好的一项 + 疏忽的一项）和对团队决策的影响。
3. **Reflection 0.6 → 0.8 → 1**：0.6 是"三个问题都答了，但原因薄、改变和 Sprint 1 关系松"；0.8 要求**具体、诚实、针对自己**，原因清楚，改变直接来自一个 Sprint 1 的问题；1 分要求**每个点都有一个 Sprint 1 的例子**，并写明**用什么判断改变是否奏效**。

**rubric 里的硬门槛**（碰到就被锁在低档）：

| 门槛 | 锁在哪一档 |
|---|---|
| 贡献写的是团队的工作（"we"），或 GitLab 记录和你的说法矛盾 | Contribution = None（0） |
| 没有任何 issue / MR / commit 链接，GitLab 里查不到对应活动 | Contribution ≤ 0.4 |
| 没写 Scrum 角色名、没写参与 | Scrum Role = None（0） |
| 只有角色的教科书定义，没有自己做了什么 | Scrum Role ≤ 0.2 |
| 反思只是把完成的任务再列一遍 | Reflection = None（0） |
| 没有 Sprint 2 的改变，或只有"我会沟通得更好"这种意向 | Reflection ≤ 0.2 |

> 🎯 **一句话总结**：个人报告拿高分 = **每条贡献一个 GitLab 链接 + 每次会议一条"我说了什么" + 每个反思点一个 Sprint 1 的事件**。三项都在问同一个问题："你个人做了什么，证据在哪，它对团队有什么影响"。

---

## 0. Submission Status　提交信息（Moodle 页面）

| 字段 | 原文 | 中文 |
|---|---|---|
| Due | Sunday, 18 October 2026, 9:00 PM | 2026 年 10 月 18 日（周日）21:00 截止 |
| Submission status | Submitted for grading | 已提交待评分 |
| Grading status | Released | 成绩已发布 |
| Time remaining | Assignment was submitted 2 hours 1 min early | 提前 2 小时 1 分钟提交 |
| Last modified | Sunday, 18 October 2026, 6:58 PM | 最后修改时间 |
| File submissions | `z<学号>_<姓名>_COMP9820_Sprint1_IndividualReport.pdf` | 个人提交一份 PDF |
| Submission comments | Comments (0) | 无提交备注 |
| Grade | 2.40 / 4.00 | 案例得分 |
| Graded on | Thursday, 29 October 2026, 2:22 PM | 评分日期 |

> ⚠️ **个人报告和 Demo 录像同一天截止**（10 月 18 日周日 21:00）。Sprint 2 的个人报告截止是 11 月 7 日（周六）21:00，与团队报告、同伴互评同一天，迟交每天扣 5%、最多五天（见 Sprint 2 指南 §3.4）。

---

## 1. Contribution & Evidence　贡献与证据（0–2 分）

| 分数 | 档位 | 原文描述 | 中文 |
|---|---|---|---|
| 0 | None | the section is missing, it describes only the team's work ("we"), or GitLab contradicts the student's claims. | 该节缺失；或只描述了**团队**的工作（通篇 "we"）；或 **GitLab 记录与学生的说法矛盾** |
| 0.4 | Very poor | contributions are vague, such as "helped with the backend", with no references to issues, merge requests or commits. GitLab shows little or no matching activity. | 贡献描述含糊（如 "helped with the backend"），**没有引用任何 issue、MR 或 commit**；GitLab 里几乎查不到对应活动 |
| 0.8 | Poor | some specific contributions, but evidence is thin: one or two references that don't cover most claims, or evidence that only partly matches the repository. Little on how the work fitted into the team's sprint. | 有一些具体贡献，但证据薄：只有一两个引用、覆盖不了大部分说法，或证据与仓库只是部分吻合；几乎没写自己的工作如何嵌入团队的 sprint |
| 1.2 | Good | the main contributions are specific and mostly supported by issue, merge request or commit references that check out in GitLab. Some claims lack evidence, or the link to the team's sprint work is brief. | 主要贡献具体，**大部分**有 issue / MR / commit 引用且在 GitLab 能查到；但**有的说法没证据**，或与团队 sprint 工作的联系**只写了一句** |
| 1.6 | Very good | each contribution is specific and backed by evidence that checks out in GitLab, covering code and non-code work such as reviews, board management or minutes. The section explains how the student's work fitted into the team's Sprint 1 development. | **每一条**贡献都具体、都有 GitLab 可查的证据；覆盖**代码和非代码**工作（评审、看板管理、会议纪要）；说明了自己的工作如何嵌入团队的 Sprint 1 开发 |
| 2 | Excellent | everything at Very good, with responsibilities taken on, as well as tasks completed. The student shows how their work affected the team, for example a merge request that unblocked a teammate or a review that caught a defect, and all the evidence matches the repository. | 在 Very good 的基础上，既写**承担的职责**也写完成的任务；展示自己的工作**如何影响了团队**（例如一个 MR 解锁了队友、一次评审抓到了缺陷）；**全部**证据与仓库吻合 |

### 怎么拿分

这一项占一半分数，rubric 从 0 到 2 其实在查四件事：

| 维度 | 0.4 / 0.8 分的样子 | 1.2 分 | 1.6 分 | 2 分 |
|---|---|---|---|---|
| 具体程度 | "helped with the backend" | 主要贡献具体 | 每一条都具体 | 同左 + 承担的职责 |
| 证据 | 没链接 / 一两个链接 | 大部分有链接、能查到 | **每一条**都有链接 | **全部**与仓库吻合 |
| 覆盖面 | 只有代码 | 主要是代码 | **代码 + 非代码**（评审、看板、纪要） | 同左 |
| 与团队的关系 | 没写 | 一句话 | 解释如何嵌入团队的 Sprint 1 | **对团队的影响**：解锁了谁、抓到了什么 bug |

推荐的写法是**一条贡献一行表格**，tutor 一眼能对上 GitLab：

| 贡献 | 类型 | 证据 | 嵌入团队工作 | 影响 |
|---|---|---|---|---|
| 实现 `POST /groups/{id}/expenses` 的分摊计算 | 代码 | Issue #12、MR !8、commit `a1b2c3d` | 对应 story "As a member I can add an expense"，是 Sprint 1 的核心功能 | 合并后 B 的净余额功能才能开始 |
| 评审 C 的 MR !11（净余额） | 非代码 | MR !11 的评论 + 之后的 commit `e4f5g6h` | 评审是组内 MR 流程的要求 | 发现四舍五入后分摊总额与费用不等，C 补了一个 commit 修复 |
| 维护 issue board，每周把 Review 列的卡片清空 | 非代码 | Board 截图（附录 A）、issue 的 activity 记录 | PO 职责 | Week 3 时 Doing 列不再堆积 |

真实案例卡在 1.2，tutor 的两句评语正好对应 1.2 → 1.6 → 2 的两道坎：

| tutor 评语 | 对应 rubric | 修法 |
|---|---|---|
| i do understand that you included your reviews in the scrum role/participation section but try to include that in your contribution instead（你把 MR 评审写在了 Scrum 角色那节，应该放到贡献这节） | 1.6 要求 "covering code and non-code work such as reviews" | **评审是贡献，不是角色**。把评审过的每个 MR 列进贡献表，角色那节只留会议和 lab check-in |
| you mentioned that you reviewed other MRs but you should be specific as to what impact you had? what bug did you find? how important was it? how did you & the developer communicate this?（你说评审了别人的 MR，但要具体：有什么影响？发现了什么 bug？多重要？你和开发者怎么沟通的？） | 2 分要求 "a review that caught a defect"、"how their work affected the team" | 每条评审写四件事：**发现了什么、多严重、怎么沟通的（MR 评论链接）、作者改了什么（后续 commit）** |

> ⚠️ **"GitLab contradicts the student's claims" 直接 0 分**。tutor 会点开你给的链接。MR 的作者不是你、commit 不在你名下、issue 不是你关的，都算矛盾。只写自己真做过的，而且链接指向自己的活动。
>
> ⚠️ **非代码工作要主动写**。评审、会议纪要、看板整理、写验收标准都算贡献，但都要有证据：评审 = MR 评论链接；纪要 = 文档链接或截图；看板 = issue 的 activity 记录或截图。

### 自查

- [ ] 整节没有一句以 "we" 开头的贡献描述
- [ ] 每条贡献至少挂一个 issue / MR / commit 链接，且点开后作者是自己
- [ ] 贡献表里同时有代码行和非代码行（评审、看板、纪要至少一种）
- [ ] 每条评审写了：发现什么、多严重、评论链接、作者之后的修改
- [ ] 每条贡献有一句"它对应团队的哪条 story / 哪个功能"
- [ ] 至少一条贡献写了对团队的影响（解锁了谁、避免了什么 bug）

---

## 2. Scrum Role and Participation　Scrum 角色与参与（0–1 分）

| 分数 | 档位 | 原文描述 | 中文 |
|---|---|---|---|
| 0 | None | the section is missing. It doesn't name the student's Scrum role or describe their participation. | 该节缺失；没有写明学生的 Scrum 角色，也没描述参与情况 |
| 0.2 | Very poor | a textbook definition of the role, such as "the Scrum Master removes impediments", with nothing on what the student did. Meetings and lab checkpoints are missing or mentioned in a phrase. | 只有角色的**教科书定义**（如 "the Scrum Master removes impediments"），没写学生自己做了什么；会议和 lab checkpoint 缺失或只提了一句 |
| 0.4 | Poor | the role is named, with one general example. Meeting participation is described generally, such as "I attended most meetings", and lab checkpoints are missing or only mentioned. | 写了角色名，有一个泛泛的例子；会议参与写得笼统（如 "I attended most meetings"）；lab checkpoint 缺失或只提了一下 |
| 0.6 | Good | the student describes how they carried out the role, with one or two concrete examples. Meetings and lab checkpoints are both covered, but one is thin, such as attendance noted without what the student contributed. | 描述了自己如何履行角色，有**一两个具体例子**；会议和 lab checkpoint 都写了，但**有一个很薄**（如只记了出席、没写自己贡献了什么） |
| 0.8 | Very good | concrete examples of performing the role in Sprint 1. The section describes how the student communicated progress, blockers and upcoming work at team meetings, and what they contributed at the Weeks 2–3 lab check-ins. | 有 Sprint 1 中履行角色的具体例子；写明自己在团队会议上如何**汇报进度、提出阻碍、安排接下来的工作**，以及在 **Week 2–3 lab check-in** 上贡献了什么 |
| 1 | Excellent | everything at Very good, with honest reflection on how well the student performed the role, such as a responsibility they handled well and one they neglected. It also explains how their participation affected the team's decisions or progress. | 在 Very good 的基础上**诚实反思**自己把角色做得怎么样（例如一项做好的职责 + 一项疏忽的职责）；并说明自己的参与**如何影响了团队的决策或进度**（原文 "1 points" 为 Moodle 自动生成，原文如此） |

### 怎么拿分

这一项分三块：**角色、会议、lab check-in**。rubric 对会议的要求非常具体：每次会议都要写**自己说了什么**（进度、阻碍、下一步），不是"我参加了"。真实案例拿 0.6，tutor 列了四条改进，每条对应一个档位描述：

| tutor 评语 | 对应 rubric | 修法 |
|---|---|---|
| please include evidence of this, e.g screenshots of meeting minutes（请附证据，例如会议纪要截图） | "concrete examples"；没证据的例子算 thin | 附录放会议纪要截图，正文引用 "见附录 B，10 月 7 日会议" |
| you only describe 2 meetings in your report, but we would like to know what you did specifically, in every single meeting（只写了两次会议，我们想知道你在**每一次**会议上具体做了什么） | 0.8 要求 "how the student communicated progress, blockers and upcoming work at team meetings" | 一张会议表：日期 / 我汇报的进度 / 我提出的阻碍 / 我安排的下一步 / 纪要链接，**Sprint 1 的每次会议一行** |
| what impact did your actions have on the team? as the product owner, it is your responsibility to make sure that people are not blocked, what actions did you take in order to make sure everyone's productive?（你的行动对团队有什么影响？作为 PO，确保没人被阻塞是你的职责，你做了什么？） | 1 分要求 "how their participation affected the team's decisions or progress" | 按角色职责逐条写"职责 → 我做的事 → 结果"。PO 的职责：维护 backlog 优先级、写验收标准、解答需求问题、保证没人等需求。每条配一个 Sprint 1 的事件 |
| you also mention the use of the issue board, please include evidence of that as well in the appendix（你提到用了 issue board，也请在附录放证据） | 同第一条，"claims lack evidence" | 附录放 board 截图（带日期），或 issue activity 里"moved to Doing by <你>"的记录 |

> ⚠️ **lab check-in 是单独的一块**。Sprint 1 的 check-in 在 Week 2–3 的 lab，要写你在 check-in 上向 tutor 展示了什么、tutor 提了什么、你之后改了什么。只写"参加了 lab"算 thin，这项就停在 0.6。
>
> ⚠️ **"one they neglected" 是 0.8 和 1 的分界**。诚实写一项没做好的职责反而加分，例如 "作为 PO 我在 Week 2 没及时给 story 补验收标准，导致 B 的 MR 在评审时才发现理解有偏差"。

三种角色各自要证明的事：

| 角色 | 要写的职责 | 证据 |
|---|---|---|
| Product Owner | backlog 优先级、验收标准、回答需求问题、确保没人被阻塞 | issue 里的验收标准编辑记录、board 截图、会议纪要里"PO 决定……" |
| Scrum Master | 主持会议、记录阻碍、推动解决、维护流程（MR 评审规则） | 会议纪要、阻碍列表、MR 评审规则的文档 |
| Developer | 领取 story、汇报进度、评审他人 MR | MR 列表、每日 / 每周进度更新的纪要 |

### 自查

- [ ] 第一句写明角色名，第二句开始就是自己做的事，没有教科书定义
- [ ] Sprint 1 每次会议一行：日期、我汇报的进度、我提的阻碍、我安排的下一步、纪要链接
- [ ] Week 2–3 lab check-in 单独一段：展示了什么、tutor 反馈、之后改了什么
- [ ] 按角色职责逐条写"职责 → 做的事 → 对团队的结果"
- [ ] 有一项"做好了"和一项"疏忽了"的诚实评价
- [ ] 附录有会议纪要截图、board 截图，正文有引用

---

## 3. Reflection　反思（0–1 分）

| 分数 | 档位 | 原文描述 | 中文 |
|---|---|---|---|
| 0 | None | the section is missing, or it repeats the list of completed tasks with no evaluation. | 该节缺失，或只是**把完成的任务再列一遍**，没有评价 |
| 0.2 | Very poor | reflection is limited to statements such as "everything went well" or "communication could be better", with no causes. There's no change for Sprint 2, or only a general intention such as "I will communicate better". | 反思停留在 "everything went well" 或 "communication could be better" 这类陈述，**没有原因**；没有 Sprint 2 的改变，或只有 "I will communicate better" 这种笼统意向 |
| 0.4 | Poor | some reflection, but it's mainly about the team, not the student, or about what was delivered, not how the student worked. Causes are generic, and the Sprint 2 change is vague or one of a list of intentions. | 有一些反思，但**主要在说团队而不是自己**，或在说交付了什么而不是自己怎么工作的；原因泛泛；Sprint 2 的改变含糊，或只是一串意向中的一条 |
| 0.6 | Good | covers what worked, what didn't work and one change for Sprint 2. Some points are specific to the student's own approach, but the causes are thin, or the change is only loosely tied to the Sprint 1 experience. | 覆盖了什么有效、什么无效、Sprint 2 的一个改变；有些点针对自己的做法，但**原因薄**，或改变与 Sprint 1 的经历**联系松散** |
| 0.8 | Very good | specific, honest evaluation of the student's own approach, with clear causes for what worked and what didn't. One concrete, actionable change for Sprint 2 follows directly from a Sprint 1 problem. | 对**自己的做法**做了具体、诚实的评价，有效和无效都有清楚的原因；Sprint 2 的一个**具体、可执行**的改变**直接来自** Sprint 1 的一个问题 |
| 1 | Excellent | everything at Very good, with a Sprint 1 example behind each point, such as a blocker raised late that held up teammates. The change for Sprint 2 says how the student will tell whether it worked. | 在 Very good 的基础上**每个点背后都有一个 Sprint 1 的例子**（如某个阻碍提晚了、拖住了队友）；Sprint 2 的改变写明**学生将如何判断它是否奏效**（原文 "1 points" 为 Moodle 自动生成，原文如此） |

### 怎么拿分

反思三个问题：**什么有效、什么无效、Sprint 2 改一件事**。rubric 反复强调两个词：**"the student's own approach"**（写自己不写团队）和 **"causes"**（写原因不写现象）。真实案例拿 0.6，tutor 的评语直指"写成了团队回顾"：

| tutor 评语 | 对应 rubric | 修法 |
|---|---|---|
| we want you to focus on what went well for you, what didn't work for you, as opposed to the entire team（我们要的是对**你自己**有效 / 无效的，不是整个团队的） | 0.4 的描述 "mainly about the team, not the student" | 每句主语改成 "I"：不是 "the team's communication was slow"，而是 "I posted my blocker on Thursday but the stand-up was Monday, so B waited three days" |
| as the product owner, you can definitely talk about the impact that reviewing MRs had, do you think that it helped your team?（作为 PO，你完全可以谈评审 MR 的影响，你觉得它帮到团队了吗？） | 1 分要求 "a Sprint 1 example behind each point" | 把贡献那节的具体事件拿过来评价：评审 MR !11 发现了分摊总额不等，这说明我在验收标准里应当写明四舍五入规则 |
| is there anything you think you could've done better, in order to make sure that the team moved smoother?（有没有什么你可以做得更好、让团队更顺畅的？） | 0.8 要求 "change … follows directly from a Sprint 1 problem" | 改变 = Sprint 1 的一个问题的直接解法，不是新年愿望 |

拿 1 分的反思，每个点都是一个**事件 → 原因 → 改变 → 验证方式**的四段式：

| 项 | 0.2 的写法 | 1 分的写法 |
|---|---|---|
| 什么有效 | Everything went well. | 我在 Week 2 给每条 story 写了验收标准（Issue #3–#9），结果 Week 3 的三个 MR 评审都没有因为需求理解分歧返工。原因：开发前就把"分摊必须加起来等于总额"写死在验收标准里 |
| 什么无效 | Communication could be better. | 我在 10 月 9 日才把"部分成员分摊"的需求变更告诉 C，而 C 的 MR !11 已经按均分写完了，返工一天。原因：我在周中看到需求问题只记在自己的笔记里，没立刻开 issue |
| Sprint 2 改一件事 | I will communicate better. | 需求变更当天开 issue 并 @ 相关开发者，不等周一会议。**验证**：Sprint 2 结束时查所有需求变更 issue 的创建时间和对应 MR 的创建时间，变更应全部早于 MR 开始 |

> ⚠️ **"says how the student will tell whether it worked" 是 0.8 和 1 的分界**。改变后面加一句"Sprint 2 末我用什么数据判断"：MR 返工次数、阻碍从提出到解决的天数、会议纪要里 action item 的完成率，任选一个。
>
> ⚠️ **反思不是贡献的复述**。"I implemented X, Y, Z" 放在第 1 节；第 3 节只写"我做 X 的方式哪里好、哪里不好、为什么"。

### 自查

- [ ] 每句的主语是 "I"，没有一句在评价团队整体
- [ ] "有效"和"无效"各至少一个点，每个点有一个 Sprint 1 的具体事件（日期、issue / MR 号）
- [ ] 每个点写了原因，不只是现象
- [ ] Sprint 2 的改变只有一个，且是某个 Sprint 1 问题的直接解法
- [ ] 改变后面写了"用什么判断它是否奏效"
- [ ] 没有重复第 1 节的任务清单

---

## 4. 推荐报告结构（2 页 + 附录）

Sprint 2 指南对个人报告的篇幅要求是**建议不超过 2 页（不含截图）**。按分值分配篇幅：贡献 2 分占一页，角色和反思各半页，证据全部放附录。

| 节 | 篇幅 | 内容 | 形式 | 对应评分项 |
|---|---|---|---|---|
| 1. Contribution & Evidence | 1 页 | 贡献表：贡献 / 类型（代码 / 评审 / 看板 / 纪要）/ 证据链接 / 对应 story / 对团队的影响 | 表格，每行一条贡献 | 1 |
| 2. Scrum Role & Participation | 半页 | 角色一句话；职责 → 做的事 → 结果（3 条）；会议表（每次一行：日期 / 汇报 / 阻碍 / 下一步 / 纪要链接）；lab check-in 一段；做好的一项 + 疏忽的一项 | 短段落 + 表格 | 2 |
| 3. Reflection | 半页 | 有效（1–2 点）、无效（1–2 点）、Sprint 2 改一件事 + 验证方式；每点带事件和原因 | 段落 | 3 |
| Appendix | 不限 | A：GitLab 截图（MR 列表按作者过滤、评审评论、board）；B：会议纪要截图；C：lab check-in 记录 | 截图 + 标题 | 1、2 |

> 💡 **先写附录再写正文**。把 Sprint 1 所有自己的 MR、评审评论、会议纪要先截图编号，正文每一句话都引用一个编号。这样自然做到"每条说法有证据"，也不会出现 GitLab 和说法矛盾的情况。

---

## 5. 真实反馈案例　2.4 / 4

| 评分项 | 得分 | 档位 | tutor 评语 | 中文 | 教训 |
|---|---|---|---|---|---|
| Contribution & Evidence | 1.2 / 2 | Good | very good, i do understand that you included your reviews in the scrum role/participation section but try to include that in your contribution instead - the scrum role can focus more specifically on what you talked about/did during your meetings and lab checkpoints - that being said, you mentioned that you reviewed other MRs but you should be specific as to what impact you had? what bug did you find? how important was it? how did you & the developer communicate this? | 很好。我理解你把 MR 评审写在了 Scrum 角色 / 参与那一节，但应该放进贡献这节；角色那节可以更专注于你在会议和 lab checkpoint 上说了什么、做了什么。另外，你说评审了别人的 MR，但要具体：你有什么影响？发现了什么 bug？多重要？你和开发者是怎么沟通的？ | **评审是贡献**，要放对位置；评审要写到"发现什么 bug、多严重、怎么沟通、作者改了什么"，否则只算 "claims lack evidence" |
| Scrum Role and Participation | 0.6 / 1 | Good | you've successfully. stated your role and what you did but a couple of improvements; - please include evidence of this, e.g screenshots of meeting minutes - you only describe 2 meetings in your report, but we would like to know what you did specifically, in every single meeting. - what impact did your actions have on the team? as the product owner, it is your responsibility to make sure that people are not blocked, what actions did you take in order to make sure everyone's productive? - you also mention the use of the issue board, please include evidence of that as well in the appendix | 你成功写明了角色和做的事，但有几点改进：请附证据，例如会议纪要截图；你只写了两次会议，我们想知道你在每一次会议上具体做了什么；你的行动对团队有什么影响？作为 PO，确保没人被阻塞是你的职责，你做了什么让大家都能干活？你还提到用了 issue board，也请在附录放证据（原文 "successfully. stated" 标点原文如此） | 会议要**每次一行**；角色要按**职责 → 行动 → 影响**写；提到的每个工具（board）都要有截图 |
| Reflection | 0.6 / 1 | Good | with the reflection, we want you to focus on what went well for you, what didn't work for you, as opposed to the entire team. - for example, as the product owner, you can definitely talk about the impact that reviewing MRs had, do you think that it helped your team? is there anything you think you could've done better, in order to make sure that the team moved smoother? | 反思部分，我们要的是对**你**有效 / 无效的，而不是整个团队的。比如作为 PO，你完全可以谈评审 MR 的影响，你觉得帮到团队了吗？有没有什么你可以做得更好、让团队运转更顺畅的？ | 反思的主语是 "I"；把贡献里的具体事件拿来评价；改变要是某个问题的直接解法 |

这位同学三项都是 Good，说明**该写的小节都写了、也有一些具体内容**，但三项都差在同一件事上：**具体到可验证的程度**。贡献缺"评审的影响"，角色缺"每次会议 + 截图"，反思缺"针对自己 + 原因"。按 tutor 的评语逐条补，三项各升一档就是 3.2 / 4，升两档是 4 / 4。

---

## 6. Sprint 1 → Sprint 2 Individual Report　下一步看什么

Sprint 2 个人报告 2026-11-07（周六）21:00 截止、Moodle 提交、建议 2 页（不含截图）、迟交每天扣 5%。指南 §3.4 列了八个必答点，正好对应 Sprint 1 的三个评分项：

| Sprint 1 评分项 | Sprint 2 指南 §3.4 的必答点 | 变化 |
|---|---|---|
| Contribution & Evidence（2） | Your contribution to Sprint 2；Evidence of your contribution | 不变：挂 issue / MR / commit。Sprint 2 多了 CI，**写 `.gitlab-ci.yml`、修流水线失败、评审时看 pipeline 结果**都是可写的贡献，证据是 pipeline 链接 |
| Scrum Role and Participation（1） | Your Scrum role；Meeting participation；Lab checkpoints | 不变：角色 + 每次会议 + lab check-in。lab check-in 从 Week 2–3 改为 **Week 7** |
| Reflection（1） | What worked；What did not work；One change for Sprint 3 | 不变：三个问题，针对自己、有原因、改变可验证。**Sprint 1 反思里承诺的那个改变，在 Sprint 2 报告里要交代做没做、效果如何** |

本文第 1–3 节的自查清单在 Sprint 2 照用。真实案例的三条教训（评审放进贡献并写影响、会议每次一行加截图、反思只写自己）在 Sprint 2 的 rubric 里同样有效。
