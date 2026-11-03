# Sprint 1 Team Report Grading Criteria　Sprint 1 团队报告评分标准与解读（满分 10 分，rubric 原始分 15 分）

> **来源**：本目录 `Sprint1-TeamReport.pdf`（Moodle「Assessments Hub → Sprint 1 - Team Report」提交页的 Submission status + Feedback + Grade breakdown，导出于 2026-10-31）
>
> **截止**：Due: Sunday, 18 October 2026, 9:00 PM（Week 5 周日 21:00，与 Demo 录像、个人报告同一天）
>
> **提交物**：一组一份 PDF（示例文件名 `COMP9820_Team_Report_<组名>.pdf`）；Moodle 显示 Grading status: Released，Graded on: Thursday, 29 October 2026
>
> **分数换算**：rubric 五项原始满分 3 + 4 + 3 + 2 + 3 = **15 分**，Moodle 按比例折成 10 分。案例组原始 10.2 / 15 = **6.8 / 10**。下文各项的分值都是 rubric 原始分。
>
> **配套**：Sprint 2 团队报告的要求见 [Sprint2_Guidelines.md](../02/Sprint2_Guidelines.md) §3.2（五个部分、约 20 页）；Demo 评分标准见 [Sprint1-Demo_评分标准.md](Sprint1-Demo_评分标准.md)；个人报告评分标准见 [Sprint1-IndividualReport_评分标准.md](Sprint1-IndividualReport_评分标准.md)；项目背景（Shared Expense Splitter、GitLab 流程）见 [Sprint2_Guidelines_1.md](../02/Sprint2_Guidelines_1.md)
>
> 💡 **关于案例**：第 7 节的真实反馈来自 26T3 一个小组的评分页，组名已隐去。五项里两项 Very good、三项 Good，拿了 6.8 / 10。tutor 对每一项都写了"要进下一档该补什么"，是写 Sprint 2 团队报告时最直接的修改清单。
>
> ⚠️ **原文缺字说明**：Moodle 导出的 PDF 右边缘被裁掉了评语的最后几个字母（如 "as soo" / "it wou" / "fir"）。本文按上下文补全并用〔〕标出，其余原文一字不改。

---

## 一页总结

**考什么**：5 个评分项，每项 6 档（None / Very poor / Poor / Good / Very good / Excellent）。**Sprint Planning 一项占 4 / 15**，其余 Scrum Roles & Minutes、Sprint Tracking、Retrospective 各 3 分，Velocity 2 分。五项共同的评分逻辑：**不是"做了什么"，而是"证据在哪、为什么这样做"**。会议纪要、issue board 截图、MR 评审评论、速度数字的解释、回顾的原因，每一项都在问"能不能被没在场的人验证"。

| # | 评分项 | 原始满分 | 档位分值 | 拿满分的关键词 | 最容易丢分的地方 |
|---|---|---|---|---|---|
| 1 | Scrum Roles, Role Allocation and Minutes（Scrum 角色、角色分配与会议纪要） | 3 | 0 / 0.6 / 1.2 / 1.8 / 2.4 / 3 | 角色职责清楚并说明**工作怎么分**；从 Week 2 起**每周两次**纪要、格式一致；每条 action item 有 **owner + due date**；变成开发工作的 action item **链接到 issue**；纪要**跟进上次的 action item**；报告引用纪要；说明角色分配**实际运作得如何、中途改过什么、为什么** | action item 没 owner（卡在 1.8）；due date 全写 "as soon as possible"；纪要看起来是事后补的（格式统一、内容空泛、没跟进）；纪要里没有延误的记录 |
| 2 | Sprint Planning（Sprint 计划） | 4 | 0 / 0.8 / 1.6 / 2.4 / 3.2 / 4 | story 格式正确、**可测试**、用 GitLab **point label** 估算、带 issue 号；估算方法和 Sprint Goal 清楚；解释选的 story **如何服务 Goal**；backlog **已排优先级且没有预分配给 Sprint 2**；计划过程**从头到尾可追溯**：feature list → user story → 怎么拆 → 为什么这样选 | 验收标准含糊 / 不可测试；没 issue 号；story points 没说怎么估的；Sprint Goal 一句话带过；backlog 没排优先级 |
| 3 | Sprint Tracking（Sprint 跟踪） | 3 | 0 / 0.6 / 1.2 / 1.8 / 2.4 / 3 | board 截图或 issue 历史来自 sprint 的**多个时间点**；story → issue → branch → **他人评审的 MR** 可追溯；纪要里有进度检查；**每条** Sprint 1 story 从计划追到 main；评审有**导致修改的评论**；说明团队**如何用 board、会议、Git 发现并处理问题** | 只有一张 sprint 末的 board 截图（1.2）；MR 自己批准、没评论；MR 和 issue 不是超链接；story 追不到实现 |
| 4 | Velocity（速度） | 2 | 0 / 0.4 / 0.8 / 1.2 / 1.6 / 2 | 数字**和 board 一致**、story 表完整；解释**具体**：哪些 story 比估算大 / 小、为什么；是否过度承诺；多少工作带进 Sprint 2；这个数字**如何决定 Sprint 2 的承诺**；诚实评估估算的**一致性和偏差原因**（验收标准不清、环境搭建时间）；**具体改变估算或计划的方法**，而不只是调数字 | 部分完成的 story 也算进去（0.8）；总数和 board 对不上；解释只有一两句泛泛的话；Sprint 2 的速度数字给了但没说怎么用 |
| 5 | Retrospective（回顾） | 3 | 0 / 0.6 / 1.2 / 1.8 / 2.4 / 3 | 三块都有、记录**主持人和时长**；条目关于**过程**而不是交付物；每条有**原因**；每个问题对应一条 Sprint 2 **可检查**的行动；证据来自 sprint 本身（纪要、board、MR 历史）；每条行动有 **owner 或验证方式**；区分**团队能控制和不能控制**的原因 | 只写"发生了什么"不写"为什么"（卡在 1.8）；Sprint 2 行动太笼统（"consider the user's viewpoint"）；缺主持人 / 时长；条目是"我们完成了 X 功能"这类交付物 |

**五条分水岭**：

1. **Scrum Roles 1.8 → 2.4 → 3**：1.8 是"纪要接近每周两次、有决定和 action item，但部分 action item 没 owner"；2.4 要求**每条 action item 有 owner 和 due date**、开发类 action item 链接 issue、报告引用纪要；3 分要求**缺席的成员看纪要就知道决定了什么、下一步做什么**、纪要跟进上次的 action item、并说明角色分配实际运作和中途调整的原因。
2. **Sprint Planning 2.4 → 3.2 → 4**：2.4 是"story 基本合格，但估算方法 / 发现过程 / Goal 与 story 的联系薄，或 backlog 没排序"；3.2 要求**可测试 + point label + issue 号 + 估算方法和 Goal 清楚 + backlog 排序且不预分配**；4 分要求**整个计划过程可追溯**：feature list 怎么变成 story、怎么拆、为什么这样选。
3. **Sprint Tracking 1.8 → 2.4 → 3**：1.8 是"大部分工作走了 branch + MR，但证据只来自一两个时间点、评审薄、有些 story 追不到实现"；2.4 要求**多个时间点的 board 截图**、大部分 story 追到**他人评审的 MR**、纪要有进度检查；3 分要求**每条 story** 可追溯、评审评论**导致了修改**、并说明团队怎么用 board / 会议 / Git **发现并处理问题**。
4. **Velocity 1.2 → 1.6 → 2**：1.2 是"数字对、表完整，但解释泛泛，Sprint 2 的数字没说怎么用"；1.6 要求**点名具体 story** 的估算偏差和原因、判断是否过度承诺、说明带入 Sprint 2 的工作量、以及数字如何决定 Sprint 2 承诺；2 分要求**诚实评估估算一致性和偏差原因**，并提出**调数字以外的具体改变**。
5. **Retrospective 1.8 → 2.4 → 3**：1.8 是"三块都有、主持人时长有，但 why 薄、行动太笼统"；2.4 要求**每条有原因**、每个问题对应一条**可检查**的行动；3 分要求证据来自 sprint 本身、每条行动有 **owner 或验证方式**、区分**可控和不可控**的原因。

**rubric 里的硬门槛**（碰到就被锁在低档）：

| 门槛 | 锁在哪一档 |
|---|---|
| 没有角色、没有纪要 | Scrum Roles = None（0） |
| 纪要只有一两次，或看起来是事后补写（统一、空泛、无跟进） | Scrum Roles ≤ 0.6 |
| story 没有验收标准、不是 "As a… I want… so that…" 格式、没 story points、没 Sprint Goal | Sprint Planning ≤ 0.8 |
| 跟踪一节没有任何证据 | Sprint Tracking = None（0） |
| 只有一张 sprint 末的 board 截图 + 几个 MR，评审缺失或自己批准 | Sprint Tracking ≤ 1.2 |
| 只有一个速度数字，没有 story 表、没有解释 | Velocity ≤ 0.4 |
| 回顾只是功能总结 | Retrospective = None（0） |
| 三块缺一块、没有 Sprint 2 行动、没写主持人和时长 | Retrospective ≤ 0.6 |

> 🎯 **一句话总结**：团队报告拿高分 = **纪要每周两次、每条 action item 有人有期限 + story 可测试带 issue 号、计划过程可追溯 + 多个时间点的 board 截图和有评论的 MR + 速度数字点名 story 解释偏差 + 回顾每条有原因、每个行动可检查**。五项都在问同一个问题：没在场的人能不能靠这份报告验证你们做了什么、为什么。

---

## 0. Submission Status　提交信息（Moodle 页面）

| 字段 | 原文 | 中文 |
|---|---|---|
| Due | Sunday, 18 October 2026, 9:00 PM | 2026 年 10 月 18 日（周日）21:00 截止 |
| Group | *(组名)* | 以组为单位提交 |
| Submission status | Submitted for grading | 已提交待评分 |
| Grading status | Released | 成绩已发布 |
| Time remaining | Assignment was submitted 2 hours 40 mins early | 提前 2 小时 40 分钟提交 |
| Last modified | Sunday, 18 October 2026, 6:19 PM | 最后修改时间 |
| File submissions | `COMP9820_Team_Report_<组名>.pdf` | 一组一份 PDF |
| Submission comments | Comments (0) | 无提交备注 |
| Grade | 6.80 / 10.00 | 案例组得分（原始 10.2 / 15） |
| Graded on | Thursday, 29 October 2026, 10:44 AM | 评分日期 |

> ⚠️ **三份 Sprint 1 提交同一天截止**（Demo 录像、团队报告、个人报告都是 10 月 18 日周日 21:00）。Sprint 2 的团队报告 11 月 7 日（周六）21:00 截止，通常由 Scrum Master 通过 Moodle 提交 PDF，建议约 20 页（含附录），迟交每天扣 5%、最多五天（见 Sprint 2 指南 §3.2）。

---

## 1. Scrum Roles, Role Allocation and Minutes　Scrum 角色、角色分配与会议纪要（0–3 分）

| 分数 | 档位 | 原文描述 | 中文 |
|---|---|---|---|
| 0 | None | the section is missing. There are no roles and no meeting minutes. | 该节缺失；没有角色，也没有会议纪要 |
| 0.6 | Very poor | roles are named with no explanation of who did what, or are missing. Only one or two sets of minutes, or minutes with no decisions or action items, or minutes that look written after the fact (uniform, vague, with no follow-up). | 角色只有名字、没说谁做了什么，或缺失；纪要只有一两次，或没有决定和 action item，或**看起来是事后补写的**（格式统一、内容空泛、没有跟进） |
| 1.2 | Poor | roles are listed but responsibilities are vague. Minutes exist, but well short of two a week or in an inconsistent format, and they record discussion without clear decisions or owners. The report doesn't refer to them. | 列了角色但职责含糊；有纪要，但**远少于每周两次**或格式不一致，记录了讨论却没有明确的决定或负责人；报告没有引用纪要 |
| 1.8 | Good | roles and responsibilities are clear. Minutes come close to two a week from Week 2, in a consistent format, and record decisions and action items. Some action items lack owners. | 角色和职责清楚；从 Week 2 起纪要**接近每周两次**、格式一致、记录了决定和 action item；但**部分 action item 没有负责人** |
| 2.4 | Very good | roles and responsibilities are clear and explained, including how work was shared. Minutes are regular and consistent, and record decisions and action items with owners and due dates. Action items that became development work link to issues, and the report draws on the minutes. | 角色和职责清楚并有解释，包括**工作是怎么分的**；纪要定期、格式一致，决定和 action item 都有**负责人和截止日期**；变成开发工作的 action item **链接到 issue**；报告引用了纪要 |
| 3 | Excellent | everything at Very good. Each set of minutes has all the required attributes; a member who missed the meeting would know what was decided and what to do next. Minutes follow up earlier action items. The report explains how role allocation worked in practice, including any changes made during the sprint and why. | 在 Very good 的基础上，每次纪要都有全部必需属性，**缺席的成员看纪要就知道决定了什么、下一步做什么**；纪要**跟进此前的 action item**；报告说明角色分配**实际运作得如何**，包括 sprint 中途的调整和原因 |

### 怎么拿分

这一项的核心是**会议纪要能不能当"没在场的人的工作指南"**。rubric 从 0 到 3 在查六件事：

| 维度 | 0.6 / 1.2 分的样子 | 1.8 分 | 2.4 分 | 3 分 |
|---|---|---|---|---|
| 频率 | 一两次 / 远少于每周两次 | 从 Week 2 起接近每周两次 | 定期 | 同左 |
| 格式 | 不一致 / 事后补写 | 一致 | 一致 | 每次都有全部必需属性 |
| 决定 | 只有讨论 | 有决定 | 有决定 | 缺席者看了就知道决定了什么 |
| Action item | 没有 / 没 owner | 有，部分没 owner | **owner + due date** | 跟进上次的 action item |
| 与 GitLab 的关系 | 无 | 无 | 开发类 action item 链接 issue | 同左 |
| 角色 | 只有名字 | 职责清楚 | 解释工作怎么分 | 实际运作如何、中途怎么改、为什么 |

真实案例卡在 1.8，tutor 的两段评语正好是 1.8 → 2.4 → 3 的两道坎：

| tutor 评语 | 对应 rubric | 修法 |
|---|---|---|
| please be specific when it comes to action items & its owner, try not to group all the user stories as one and say "each respective user story", be specific, we want someone who has attended the meeting to know exactly what everyone is doing. furthermore, having "as soo〔n〕 as possible" for all the due dates doesn't provide much value or prioritisation so it woul〔d〕 be hard for someone who didn't attend the meeting to know what they should work on fir〔st〕（action item 和负责人要具体，不要把所有 story 打包写成"各自的 user story"；due date 全写 "as soon as possible" 没有价值也没有优先级，没来的人不知道先做什么） | 2.4 要求 "action items with owners and due dates"；3 分要求 "a member who missed the meeting would know … what to do next" | action item 表格固定四列：**做什么（具体到 issue 号）/ 谁 / 哪天前 / 状态**。一个 story 一行，不合并；due date 写具体日期，按日期排序就是优先级 |
| you need to reflect on previous action items and minutes, for example you guys mention th〔at〕 due to merge conflicts and poor communication, you guys were delayed, but there doesn't seem to be any detail of that within the minutes & the action items should reflect any delays.（要回顾上次的 action item 和纪要；你们提到因为合并冲突和沟通不畅延误了，但纪要里没有任何记录，action item 也应该反映延误） | 3 分要求 "Minutes follow up earlier action items" | 每次纪要第一项固定是"上次 action item 复查"：逐条写**完成 / 延期（新日期 + 原因）/ 取消**。报告里说的每个问题（合并冲突、沟通不畅）都要能在某次纪要里找到当天的记录 |

> ⚠️ **"minutes that look written after the fact" 直接锁在 0.6**。tutor 判断的依据就是：每次格式一模一样、内容空泛、没有一条"上次说的 X 做了没"。纪要要在会议当天写进 GitLab wiki 或 repo，带 commit 时间戳就是最好的证据。
>
> ⚠️ **"two a week from Week 2"** 是明确的数量要求。Sprint 1 约三周，从 Week 2 起算至少 4–6 次纪要。少于这个数就从 1.8 往下掉。

### 自查

- [ ] 从 Week 2 起每周至少两次纪要，文件名带日期，格式一致（日期 / 出席 / 上次 action item 复查 / 讨论 / 决定 / 新 action item）
- [ ] 每条 action item 有具体内容（issue 号）、负责人、具体日期，没有 "ASAP"、没有"各自的 story"
- [ ] 每次纪要第一项是上次 action item 的逐条复查，延期的写新日期和原因
- [ ] 开发类 action item 链接到对应 issue
- [ ] 报告正文至少引用三次纪要（"见附录 B，10 月 7 日会议决定……"）
- [ ] 角色一节写了职责、工作怎么分、中途有没有调整、为什么
- [ ] 报告里提到的每个问题（延误、冲突）都能在某次纪要里找到当天的记录

---

## 2. Sprint Planning　Sprint 计划（0–4 分）

| 分数 | 档位 | 原文描述 | 中文 |
|---|---|---|---|
| 0 | None | the section is missing. There are no user stories and no planning. | 该节缺失；没有 user story，也没有计划 |
| 0.8 | Very poor | stories are missing their acceptance criteria, aren't written as "As a… I want… so that…" or can't be read in the report. There are no story points, no Sprint Goal and no visible planning process. | story 没有验收标准、不是 "As a… I want… so that…" 格式，或在报告里读不到；没有 story points、没有 Sprint Goal、看不到计划过程 |
| 1.6 | Poor | some stories are well formed, but many acceptance criteria are vague or untestable, and stories lack GitLab issue numbers. Points appear without an explained estimation approach. The Sprint Goal, discovery process or backlog is missing or covered in one line. | 部分 story 格式正确，但很多验收标准**含糊或不可测试**，story 没有 GitLab issue 号；有 points 但**没说明估算方法**；Sprint Goal、需求发现过程或 backlog 缺失或只有一行 |
| 2.4 | Good | stories are mostly well formed and readable, with issue numbers, points and mostly testable acceptance criteria. There's a clear Sprint Goal. The estimation approach, discovery process or link between the goal and the selected stories is thin, or the backlog isn't prioritised. | story 大多格式正确、可读，有 issue 号、points 和大多可测试的验收标准；Sprint Goal 清楚；但**估算方法、发现过程或 Goal 与所选 story 的联系薄**，或 **backlog 没排优先级** |
| 3.2 | Very good | stories are well formed, testable, estimated with GitLab point labels and tagged with issue numbers. The estimation approach and Sprint Goal are clear, and the report explains how the selected work serves the goal. The backlog is prioritised and not pre-assigned to Sprint 2. | story 格式正确、**可测试**、用 GitLab **point label** 估算、带 issue 号；估算方法和 Sprint Goal 清楚，报告解释了所选工作**如何服务 Goal**；backlog **已排优先级且没有预分配给 Sprint 2** |
| 4 | Excellent | everything at Very good, with the planning process traceable from start to finish. The report shows how the feature list became user stories, how stories were split where needed, and the reasons for its main choices. | 在 Very good 的基础上，计划过程**从头到尾可追溯**：报告展示 feature list 如何变成 user story、需要时如何拆分、以及主要选择的理由 |

### 怎么拿分

这是分值最高的一项（4 / 15）。rubric 在查一条链：**需求 → feature → user story → 验收标准 → 估算 → Sprint Goal → 选哪些 story → backlog 排序**。真实案例拿 3.2，tutor 一句话指出 3.2 和 4 的差距：

| tutor 评语 | 对应 rubric | 修法 |
|---|---|---|
| to move into the next band, i would suggest you elaborate what the requirements would be from the user's perspective from a expense splitter -> how that becomes a feature -> what the acceptance criteria AND how do we test it who is responsible for it（要进下一档，建议展开：从用户视角看费用分摊的需求是什么 → 怎么变成一个 feature → 验收标准是什么、怎么测试、谁负责） | 4 分要求 "how the feature list became user stories, how stories were split where needed, and the reasons for its main choices" | 加一节"从需求到 story"，用一两个例子走完整条链（见下表），再加一张 story 总表列出每条的验收标准、测试方法、负责人 |

4 分的"可追溯"写法，一个例子就够：

| 环节 | 示例 |
|---|---|
| 用户视角的需求 | 合租的三个人想知道这个月谁欠谁多少 |
| 变成 feature | 群组内按人计算净余额 |
| 拆成 story | #7 "As a member I want to see each member's net balance so that I know who owes whom"；拆出 #8 "部分成员分摊的费用"，因为 #7 一条做不完 |
| 验收标准（可测试） | 三人均分 100 元，付款人余额 +66.67，其余两人各 −33.33；所有余额之和为 0 |
| 怎么测 | pytest：`test_net_balance_sums_to_zero`、`test_partial_split` |
| 估算 | Planning poker，#7 = 3 points（label `points::3`），理由：涉及两张表的聚合 |
| 为什么选进 Sprint 1 | Sprint Goal 是"能用的通用分摊器"，没有净余额就不算能用 |
| 负责人 | C（issue assignee） |

> ⚠️ **"testable" 是 2.4 和 3.2 的分界**。"用户能看到余额"不可测试，"三人均分 100 元后余额之和为 0"可测试。每条验收标准都要能直接翻译成一个 pytest 用例。
>
> ⚠️ **"not pre-assigned to Sprint 2"**：backlog 里 Sprint 1 没做的 story 保持在 backlog 并排好优先级，不要提前打上 Sprint 2 的 milestone。Sprint 2 的计划会在 Sprint 2 开头做。

### 自查

- [ ] 每条 story 是 "As a… I want… so that…" 格式，带 GitLab issue 号
- [ ] 每条验收标准能对应一个具体的测试用例（数字、输入、期望输出）
- [ ] story points 用 GitLab point label 记录，报告说明估算方法（planning poker / T-shirt size / 相对估算）
- [ ] Sprint Goal 一句话，并逐条说明选的 story 如何服务它
- [ ] 至少一个例子走完"需求 → feature → story → 拆分 → 验收标准 → 测试 → 估算 → 负责人"全链
- [ ] 拆过的 story 写了怎么拆、为什么拆
- [ ] backlog 按优先级排序，截图里 Sprint 1 没做的 story 没有预分配给 Sprint 2

---

## 3. Sprint Tracking　Sprint 跟踪（0–3 分）

| 分数 | 档位 | 原文描述 | 中文 |
|---|---|---|---|
| 0 | None | the section is missing, or it describes tracking with no evidence of any kind. | 该节缺失，或描述了跟踪但**没有任何证据** |
| 0.6 | Very poor | the section claims the team tracked its work, but the only evidence is one or two links or screenshots that show little. There's no sign of review, or merge requests lack comments and links to issues. | 声称团队跟踪了工作，但唯一的证据是一两个几乎看不出什么的链接或截图；没有评审的迹象，或 MR 没有评论、没有关联 issue |
| 1.2 | Poor | a single end-of-sprint board screenshot and a few merge requests, with little link between planned stories and the work done. Reviews are missing or self-approved, and the minutes don't mention progress checks. | **只有一张 sprint 末的 board 截图**和几个 MR，计划的 story 和实际工作之间几乎没有联系；评审缺失或**自己批准自己**；纪要没提进度检查 |
| 1.8 | Good | screenshots or links showing the board or issue history, issues and merge requests show most work going through branches and merge requests. Gaps remain: evidence from only one or two points in the sprint, thin reviews, or some stories that can't be traced to their implementation. | 有 board 或 issue 历史的截图 / 链接，issue 和 MR 显示大部分工作走了 branch + MR；但有缺口：**证据只来自 sprint 的一两个时间点**、评审薄、或有些 story 追不到实现（原文第一句缺主句动词，原文如此） |
| 2.4 | Very good | board screenshots or issue history from several points in the sprint show tasks moving through it. Most stories trace through issues and branches to merge requests reviewed by another member. The minutes show progress checked at meetings. | 来自 sprint **多个时间点**的 board 截图或 issue 历史显示任务在流动；大部分 story 能从 issue、branch 追到**由另一名成员评审的 MR**；纪要显示会议上检查了进度 |
| 3 | Excellent | everything at Very good, with every Sprint 1 story traceable from plan to main. Reviews are substantive, with comments that led to changes. The section explains how the team used the board, meetings and Git to spot and deal with problems during the sprint, as well as what happened. | 在 Very good 的基础上，**每条** Sprint 1 story 都能从计划追到 main；评审有实质内容，**评论导致了修改**；本节说明团队如何用 board、会议和 Git **在 sprint 中发现并处理问题**，而不只是发生了什么 |

### 怎么拿分

这一项和 Demo 的 Sprint Process Evidence 考的是同一条链（story → issue → branch → MR → main），区别是报告要用**截图**证明，而且要证明**整个 sprint 期间**都在跟踪，不是最后一天补的。真实案例卡在 1.8，tutor 的三条要求对应 rubric 的三个缺口：

| tutor 评语 | 对应 rubric | 修法 |
|---|---|---|
| please link MR & issues as hyperlinks（MR 和 issue 要做成超链接） | 1.8 的 "some stories that can't be traced to their implementation" | story 表加两列：issue 链接、MR 链接；PDF 里保留可点击的超链接 |
| it wou〔ld〕 be nice to see multiple screenshots of the iss〔ue〕 board, so yes the empty one is nice, but i wou〔ld〕 like one mid sprint with issues in the backlog, progress etc & another one towards the end o〔f〕 the sprint, showing the progress（希望看到多张 issue board 截图：空的那张不错，但还要一张 sprint 中期的、一张 sprint 末的，显示进度） | 2.4 要求 "board screenshots or issue history from several points in the sprint" | 固定三张 board 截图：**sprint 开始（全在 Backlog）、中期（Doing / Review 有卡片）、结束（Done）**，每张带日期。做法是每周会议时顺手截一张存进 repo |
| please show evidence of merge request reviewing, with exa〔mple〕 comments（展示 MR 评审的证据，附评论示例） | 2.4 要求 "reviewed by another member"；3 分要求 "comments that led to changes" | 挑 2–3 个 MR 截图评论区：reviewer ≠ author、评论指出具体问题、作者回复、之后的 commit。配一句"评审发现 X，作者在 commit abc123 修复" |

> ⚠️ **"a single end-of-sprint board screenshot" 锁在 1.2**。一张全是 Done 的 board 证明不了跟踪，只能证明做完了。tutor 要看的是 issue **移动的过程**。
>
> ⚠️ **3 分的 "spot and deal with problems"**：找一个 sprint 中真实发生的问题（某个 MR 卡在 Review 三天、某条 story 估算偏小），写清**怎么从 board / 会议 / Git 发现的、当时怎么处理的、结果如何**。这和第 5 节回顾、第 1 节纪要里的记录要能对上。

### 自查

- [ ] 三张带日期的 board 截图：sprint 开始、中期、结束
- [ ] story 表每行有 issue 超链接和 MR 超链接
- [ ] 2–3 个 MR 的评审截图：reviewer 不是作者、有具体评论、评论后有修改 commit
- [ ] 每条 Sprint 1 story 都能追到 main 上的 merge commit
- [ ] 纪要里每次会议有"进度检查"一项，报告引用
- [ ] 写了至少一个"从 board / 会议 / Git 发现问题 → 处理 → 结果"的例子

---

## 4. Velocity　速度（0–2 分）

| 分数 | 档位 | 原文描述 | 中文 |
|---|---|---|---|
| 0 | None | the section is missing, or it gives no velocity figure and no discussion. | 该节缺失，或没有速度数字也没有讨论 |
| 0.4 | Very poor | a velocity figure with no supporting story table and no interpretation. | 只有一个速度数字，没有 story 表支撑，也没有解释 |
| 0.8 | Poor | points committed and completed and a story table are present, but there are counting errors, such as partial stories counted or totals that don't match the board. The interpretation is a sentence or two of generic comment. | 有承诺 / 完成的 points 和 story 表，但**计数有错**（如把部分完成的 story 算进去、总数和 board 对不上）；解释只有一两句泛泛的话 |
| 1.2 | Good | the figures are counted correctly and match the board, and the story table is complete. The interpretation touches on estimation or commitment but stays general, and there's a Sprint 2 velocity figure with little on how the team will use it. | 数字计算正确、和 board 一致，story 表完整；解释提到了估算或承诺但**停留在一般性**；给了 Sprint 2 的速度数字但几乎没说团队怎么用它 |
| 1.6 | Very good | the figures are correct and consistent with the board. The interpretation is specific: it names stories that were larger or smaller than estimated and why, judges whether the team over-committed, and states how much work carried into Sprint 2. It explains how the figure will shape the Sprint 2 commitment. | 数字正确、与 board 一致；解释**具体**：点名哪些 story 比估算大或小、为什么；判断团队是否过度承诺；说明多少工作带进 Sprint 2；解释这个数字**如何决定 Sprint 2 的承诺量** |
| 2 | Excellent | everything at Very good, with an honest assessment of how consistently the team estimated and what caused the gaps, such as unclear acceptance criteria or setup time. It also names concrete changes to estimation or planning for Sprint 2, beyond adjusting the number. | 在 Very good 的基础上，诚实评估团队估算的**一致性**和偏差的**原因**（如验收标准不清、环境搭建时间）；并提出 Sprint 2 对估算或计划的**具体改变**，而不只是调整数字 |

### 怎么拿分

Sprint 2 指南原话：**"the marks are for the interpretation, not the number"**。数字对只值 1.2，剩下 0.8 全在解释。真实案例拿 1.6，tutor 的评语指向 1.6 → 2 的最后一步：

| tutor 评语 | 对应 rubric | 修法 |
|---|---|---|
| pretty good, to move up into the next band, i would've liked you to be more specific about how the sprint 2 tasks are more complex -> th〔us〕 needing extra story points for example with receipt image recognition, you would need to implement OCR -> talk about what this would involve & how this would affect your other planned stories & how you guys would plan around this? what would you guys do different〔ly〕 to accommodate these added complexities?（要进下一档，希望更具体地说明 Sprint 2 的任务为什么更复杂、因此需要更多 points。比如收据图像识别需要 OCR：这涉及什么、怎么影响其他计划的 story、怎么围绕它做计划、你们会做什么不同的事来应对这些复杂度） | 2 分要求 "concrete changes to estimation or planning for Sprint 2, beyond adjusting the number" | 不要只写"Sprint 2 承诺 20 points"。挑 1–2 条 Sprint 2 最复杂的 story，写：**为什么复杂（技术依赖）→ 估多少、怎么估的 → 它挤占了哪些 story → 计划上的具体改变**（先做 spike、拆成两个 story、把它排到 sprint 前半段） |

2 分的速度一节，结构可以是：

| 部分 | 内容 |
|---|---|
| 数字 | 承诺 N points、完成 M points；story 表（issue 号 / points / 状态 / 是否合并到 main 且满足验收标准）；**只算合并到 main 且通过验收标准的** |
| 偏差 | 点名：#7 估 3 实际相当于 5，原因是验收标准没写清部分成员分摊；#4 估 2 实际 1，原因是模板已有大半 |
| 一致性 | 三周里估算偏差的方向：前期普遍偏小（环境搭建没算进去），后期准确 |
| 过度承诺？ | 承诺 N 完成 M，差额是哪两条 story，带进 Sprint 2 |
| Sprint 2 怎么用 | 以 M 为基准；但 Sprint 2 的 OCR story 复杂度更高，先做一个 1 point 的 spike 验证库可用，再估主 story；承诺量按 M 减去 spike |
| 估算方法的改变 | 验收标准必须先写完再估；环境 / 依赖搭建单独一条 story 计点 |

> ⚠️ **"partial stories counted" 是 0.8 的典型错误**。做了 80% 但没合并到 main 的 story 算 0 points。宁可速度数字难看，也不要被 tutor 对照 board 发现对不上。

### 自查

- [ ] 承诺 / 完成的 points 和 board 上 issue 的 label、状态一一对得上
- [ ] 只有合并到 main 且满足验收标准的 story 计入完成
- [ ] 至少点名两条 story 的估算偏差和原因
- [ ] 明确回答"是否过度承诺"和"带入 Sprint 2 的工作量"
- [ ] Sprint 2 的承诺量有推导过程，并针对最复杂的 story 说明技术依赖和计划调整
- [ ] 写了至少一条估算方法本身的改变，不只是改数字

---

## 5. Retrospective　回顾（0–3 分）

| 分数 | 档位 | 原文描述 | 中文 |
|---|---|---|---|
| 0 | None | the section is missing, or it's only a summary of the features the team built. | 该节缺失，或只是团队所做功能的总结 |
| 0.6 | Very poor | the section lists outcomes, such as "we finished the expense feature" or "we didn't deliver the frontend", with no causes. One or more of the three areas is missing, there are no actions for Sprint 2, and it doesn't say who facilitated or how long it took. | 只列结果（如 "we finished the expense feature"、"we didn't deliver the frontend"），没有原因；三块缺一块或更多；没有 Sprint 2 的行动；没写谁主持、用了多久 |
| 1.2 | Poor | all three areas appear, but most items describe deliverables, not process, or give generic causes such as "communication could be better". Sprint 2 actions are vague intentions, and the facilitator or duration may be missing. | 三块都有，但大部分条目说的是**交付物而不是过程**，或原因泛泛（如 "communication could be better"）；Sprint 2 的行动是含糊的意向；主持人或时长可能缺失 |
| 1.8 | Good | all three areas are covered, with the facilitator and duration recorded. Most items are about process, but the "why" is thin, and some Sprint 2 actions are too general to check. | 三块都有，记录了主持人和时长；大部分条目关于过程，但 **"为什么"薄**，部分 Sprint 2 行动**太笼统、无法检查** |
| 2.4 | Very good | items focus on process and explain their causes, such as the frontend team being blocked by a late API contract. Each problem leads to a specific Sprint 2 action the team could check, and the facilitator and duration are recorded. | 条目聚焦过程并解释原因（如前端被迟到的 API 契约阻塞）；**每个问题对应一条团队可以检查的 Sprint 2 行动**；记录了主持人和时长 |
| 3 | Excellent | everything at Very good, with the retrospective's evidence drawn from the sprint itself, such as minutes, the board or merge request history. Each Sprint 2 action names an owner or a way to tell whether it worked, and the section separates causes the team controls from those it doesn't. | 在 Very good 的基础上，回顾的证据来自 sprint 本身（纪要、board 或 MR 历史）；每条 Sprint 2 行动有 **owner 或验证方式**；区分**团队能控制和不能控制**的原因 |

### 怎么拿分

回顾三块：**什么顺利、什么不顺利、Sprint 2 试什么**，外加主持人和时长。rubric 反复出现的两个词是 **process**（过程不是交付物）和 **why**（原因不是现象）。真实案例卡在 1.8，tutor 的评语就是 "why is thin" 和 "too general to check" 的具体版本：

| tutor 评语 | 对应 rubric | 修法 |
|---|---|---|
| you guys were very descriptive in what happened, but it would be nice if you could elaborate more on why things happened, for example, what was the thought process behin〔d〕 keeping the sprint 1 features to be limited (in order to prevent it from happening again) or w〔hy〕 wasn't the demo rehearsed? was it a time management issue? if so, how can we mitigat〔e〕 that in the future?（你们把发生了什么写得很详细，但要多写为什么：比如把 Sprint 1 功能限制在很少的思路是什么？为什么 demo 没排练？是时间管理问题吗？如果是，以后怎么避免？） | 1.8 的 "the 'why' is thin"；2.4 要求 "explain their causes" | 每条"不顺利"写成三段：**现象 → 原因 → 根因**。"demo 没排练" → "周五才合完最后一个 MR" → "MR 评审排队，没有规定评审响应时间"。根因才是 Sprint 2 行动的来源 |
| with the sprint 2 improvements, we can be a little bit more specific, what does "consider the user's viewpoint" actually mean, how will you guys d〔o〕 that? you guys need to be more detailed（Sprint 2 的改进要更具体："考虑用户视角"到底是什么意思、怎么做？要更详细） | 1.8 的 "too general to check"；2.4 要求 "a specific Sprint 2 action the team could check"；3 分要求 "an owner or a way to tell whether it worked" | 每条行动写成：**做什么（可观察的动作）/ 谁负责 / 怎么知道做到了**。"考虑用户视角" → "每条 story 的验收标准由 PO 从 persona 的角度写一条使用场景，B 负责检查；Sprint 2 末统计有多少条 story 做到了" |

> ⚠️ **"evidence drawn from the sprint itself" 是 2.4 和 3 的分界**。回顾里的每个问题都要能指向一条纪要、一张 board 截图或一个 MR："10 月 9 日纪要记录 C 的 MR !11 等了三天没人评审"。这也是第 1 节 tutor 说的"纪要里要有延误记录"的另一面。
>
> ⚠️ **"separates causes the team controls from those it doesn't"**：把原因分两栏。能控制的（评审响应时间、验收标准写法）配行动；不能控制的（成员生病、UNSW GitLab 没有 burndown）写应对方式。

### 自查

- [ ] 写了主持人、日期、时长
- [ ] 三块都有，每块至少两条，条目都是过程（评审、会议、估算、沟通），不是功能
- [ ] 每条"不顺利"有现象 → 原因 → 根因
- [ ] 每条 Sprint 2 行动有可观察的动作、负责人、验证方式
- [ ] 每个问题至少指向一条纪要 / 截图 / MR 作为证据
- [ ] 原因分成"团队可控"和"不可控"两类

---

## 6. 推荐报告结构（Sprint 1 约 15–20 页，含附录）

按分值分配篇幅：Planning 4 分最多，三个 3 分项次之，Velocity 2 分最少。证据（纪要、截图）全部进附录，正文引用。

| 节 | 篇幅 | 内容 | 对应评分项 |
|---|---|---|---|
| 1. Team & Roles | 1 页 | 角色表（姓名 / 角色 / 职责 / 中途调整与原因）；工作怎么分 | 1 |
| 2. Sprint Planning | 3–4 页 | Sprint Goal；需求 → feature → story 的追溯示例；story 总表（issue 链接 / 格式 / 验收标准 / 测试方法 / points / 负责人）；估算方法；拆分说明；排序后的 backlog 截图 | 2 |
| 3. Sprint Tracking | 2–3 页 | 三张带日期的 board 截图；story → MR 追溯表；2–3 个评审示例截图；一个"发现问题 → 处理 → 结果"的例子；引用纪要的进度检查 | 3 |
| 4. Velocity | 1–2 页 | 承诺 / 完成表；偏差点名；一致性；过度承诺判断；Sprint 2 承诺推导；估算方法改变 | 4 |
| 5. Retrospective | 2 页 | 主持人 / 时长；三块；每条现象 → 原因 → 根因；行动表（动作 / 负责人 / 验证）；可控 vs 不可控 | 5 |
| Appendix A: Meeting minutes | 不限 | 每次纪要全文，格式一致，含上次 action item 复查 | 1、3、5 |
| Appendix B: GitLab evidence | 不限 | board 截图、MR 评审截图、Contributors 图 | 3 |

> 💡 **纪要是五项里三项的证据来源**（角色、跟踪、回顾）。Sprint 2 从第一次会议起就按固定模板写、当天提交到 repo，报告里的问题和延误都能回指到某次纪要，三项一起受益。

---

## 7. 真实反馈案例　6.8 / 10（原始 10.2 / 15）

| 评分项 | 得分 | 档位 | tutor 评语 | 中文 | 教训 |
|---|---|---|---|---|---|
| Scrum Roles, Role Allocation and Minutes | 1.8 / 3 | Good | please be specific when it comes to action items & its owner, try not to group all the user stories as one and say "each respective user story", be specific, we want someone who has attended the meeting to know exactly what everyone is doing. furthermore, having "as soo〔n〕 as possible" for all the due dates doesn't provide much value or prioritisation so it woul〔d〕 be hard for someone who didn't attend the meeting to know what they should work on fir〔st〕 - you need to reflect on previous action items and minutes, for example you guys mention th〔at〕 due to merge conflicts and poor communication, you guys were delayed, but there doesn't seem to be any detail of that within the minutes & the action items should reflect any delays. | action item 和负责人要具体，不要把所有 story 打包成"各自的 user story"；due date 全写 "as soon as possible" 没有价值也没有优先级，没来的人不知道先做什么。要回顾上次的 action item：你们提到因合并冲突和沟通不畅延误了，但纪要里没有任何记录，action item 也应该反映延误。 | action item 四列：**具体内容 / 谁 / 哪天 / 状态**；每次纪要先复查上次的 action item；报告里提的问题要能在纪要里找到当天记录 |
| Sprint Planning | 3.2 / 4 | Very good | to move into the next band, i would suggest you elaborate what the requirements would be from the user's perspective from a expense splitter -> how that becomes a feature -> what the acceptance criteria AND how do we test it who is responsible for it | 要进下一档，建议展开：从用户视角看费用分摊的需求是什么 → 怎么变成 feature → 验收标准是什么、怎么测、谁负责。 | 差的 0.8 是"计划过程可追溯"：加一个从需求走到负责人的完整示例 |
| Sprint Tracking | 1.8 / 3 | Good | please link MR & issues as hyperlinks - it wou〔ld〕 be nice to see multiple screenshots of the iss〔ue〕 board, so yes the empty one is nice, but i wou〔ld〕 like one mid sprint with issues in the backlog, progress etc & another one towards the end o〔f〕 the sprint, showing the progress - please show evidence of merge request reviewing, with exa〔mple〕 comments | MR 和 issue 要做成超链接；希望看到多张 board 截图：空的那张不错，但还要一张 sprint 中期的、一张 sprint 末的；请展示 MR 评审的证据，附评论示例。 | 三张带日期的 board 截图；story 表带超链接；2–3 个评审评论截图 |
| Velocity | 1.6 / 2 | Very good | pretty good, to move up into the next band, i would've liked you to be more specific about how the sprint 2 tasks are more complex -> th〔us〕 needing extra story points for example with receipt image recognition, you would need to implement OCR -> talk about what this would involve & how this would affect your other planned stories & how you guys would plan around this? what would you guys do different〔ly〕 to accommodate these added complexities? | 不错。要进下一档，希望更具体地说明 Sprint 2 的任务为什么更复杂、因此需要更多 points：比如收据图像识别要做 OCR，这涉及什么、怎么影响其他 story、怎么围绕它做计划、你们会做什么不同的事来应对？ | 差的 0.4 是"调数字以外的具体改变"：针对最复杂的 story 写技术依赖、对其他 story 的影响、计划调整 |
| Retrospective | 1.8 / 3 | Good | you guys were very descriptive in what happened, but it would be nice if you could elaborate more on why things happened, for example, what was the thought process behin〔d〕 keeping the sprint 1 features to be limited (in order to prevent it from happening again) or w〔hy〕 wasn't the demo rehearsed? was it a time management issue? if so, how can we mitigat〔e〕 that in the future? - with the sprint 2 improvements, we can be a little bit more specific, what does "consider the user's viewpoint" actually mean, how will you guys d〔o〕 that? you guys need to be more detailed | 你们把发生了什么写得很详细，但要多写为什么：把 Sprint 1 功能限制在很少的思路是什么？为什么 demo 没排练？是时间管理问题吗？以后怎么避免？Sprint 2 的改进要更具体："考虑用户视角"到底是什么意思、怎么做？要更详细。 | 每条问题写到根因；每条行动写动作 / 负责人 / 验证方式 |

这个组五项都有内容、都没有缺项，所以没有一项掉到 1.2 以下。丢掉的 4.8 分（原始）分布很均匀：**每一项都差"再具体一层"**。纪要差 owner 和日期，计划差一个完整的追溯示例，跟踪差中期截图和评审评论，速度差技术复杂度的分析，回顾差根因和可检查的行动。按 tutor 的评语逐项补一档就是 13.2 / 15 = 8.8 / 10。

值得注意的是，这个组的 Demo 只拿了 3.5 / 10（见 [Sprint1-Demo_评分标准.md](Sprint1-Demo_评分标准.md) 第 5 节：全程没展示 GitLab、超时），而团队报告 6.8 / 10 说明过程本身是做了的。**报告里有的 board、MR、纪要，demo 时没有拿出来给 tutor 看**。Sprint 2 的 demo 脚本应该直接从团队报告第 3 节的截图里取材。

---

## 8. Sprint 1 → Sprint 2 Team Report　下一步看什么

Sprint 2 团队报告 2026-11-07（周六）21:00 截止、占 15%、约 20 页（含附录）。指南 §3.2 的五个部分与 Sprint 1 的五个评分项对照：

| Sprint 1 评分项 | Sprint 2 指南 §3.2 的部分 | 变化 |
|---|---|---|
| Scrum Roles, Role Allocation and Minutes（3） | Meeting minutes（附录，并在 Sprint Monitoring 里引用） | 纪要不再单独计分，但是 Sprint Monitoring 和 Retrospective 的证据来源。**action item 的 owner / 日期 / 复查**这三条要求照旧 |
| Sprint Planning（4） | Chosen Variation, Personas, Use Cases and Success Criteria（3%）+ User Stories, Acceptance Criteria and Points（2%） | 拆成两块：前面多了**变体、persona、用例、3–5 条成功标准**；story 部分要求不变（issue 号、验收标准、point label、Sprint Goal、拆分说明）。tutor 要的"从用户视角 → feature → story"的追溯，正好用 persona 和用例来写 |
| Sprint Tracking（3） | Sprint Monitoring and Burndown/Velocity chart（3%） | 跟踪和速度合并。要求**board 和会议的证据**不变；新增 Sprint 1 vs Sprint 2 的速度对比图，并说明两个 sprint 的长度（约三周 vs 三周含弹性周） |
| Velocity（2） | 同上 | "marks are for the interpretation, not the number" 原话保留。要写 Sprint 1 速度**怎么用来决定 Sprint 2 承诺、决定对不对、Sprint 3（两周）怎么调** |
| — | **CI Pipeline（4%）** | 新增、分值最高：design / tools / rationale / evidence（含至少一次失败）/ impact |
| Retrospective（3） | Sprint 2 Retrospective and Review of Sprint 1 Things to Try（3%） | 回顾要求不变（主持人、时长、过程、why）。新增：**逐条评估 Sprint 1 回顾里的 "things to try"：做了没、有没有效、证据是什么**。所以 Sprint 1 回顾里"考虑用户视角"这种无法检查的行动，在 Sprint 2 报告里会再被问一次 |

本文第 1–5 节的自查清单在 Sprint 2 照用。真实案例的五条教训（action item 要有人有日期、计划要可追溯、board 截图要多个时间点、速度要分析复杂度、回顾要写根因和可检查的行动）在 Sprint 2 的 rubric 里同样有效。
