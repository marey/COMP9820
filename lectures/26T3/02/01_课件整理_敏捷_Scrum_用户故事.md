# COMP9820 Week 2 · 课件整理：Software Requirements & Agile Development with Scrum

**Lecture 2 · Dr. Basem Suleiman · School of Computer Science and Engineering (CSE), UNSW**
视频：https://www.youtube.com/watch?v=wgpJdDhBui0 · 讲义 PDF：`26-T3 COMP9820_Software_Requirements_Scrum.pdf`（70 页）

> 体例说明
> - 每一页按放映顺序编号，标题 `### NN · <幻灯片标题>`；正文先给英文原文，`🇨🇳` 为中文翻译，`💬 讲师补充` 为讲师口头讲的、幻灯片上没有的内容（含课堂问答）。
> - 两次 Slido 投票的结果截图不在 PDF 里，从录像中截取，编号 15a / 19a。
> - 自动字幕的常见识别错误已按语义还原（如 "ritual"→retro、"bendown/bendout chart"→burndown chart、"planning boar"→planning poker、"comet"→commit、"conextra"→Connextra、"radio"→ready、"boasted nodes"→post-it notes、"3900 900"→COMP3900/9900）。

---

## 开场（幻灯片之前）

💬 **讲师补充**
- 教室显示设备出了问题（上周是摄像头问题），开场延迟了几分钟；线上同学请确认能听到声音。
- **Week 1 回顾与组队要求**：上周 lab 的活动就是为了帮大家有目的地组队。目前仍有不少队伍少于 3–4 人。**本周必须完成组队**——如果队伍还有空位，tutor 会直接把人分配进去。
- 上周已经开始练版本控制：用 git 命令改本地仓库、用 git remote 和 GitLab 协作（以前课程用 GitHub，现在用 GitLab）。
- 今天讲 **敏捷开发实践与 Scrum**——这正是你们项目 **三个 Sprint** 要用的方法，而且 **评分会检查你们是否按 Scrum 的方式正确地做**。
- 讲师问：有没有人在别的课做过完整的 Scrum Sprint？有人做过，但不确定是否以团队方式做——所以本课程会让大家以团队方式走完三个 Sprint。
- 今天的顺序：先讲敏捷开发实践（价值观、原则），自然引出在敏捷计划中怎么写软件需求（User Stories）。

---

### 01 · COMP9820 Software Project Management — Software Requirements, Agile Software Development Practices with Scrum

![](images/01_title.jpg)

**COMP9820 Software Project Management**
Software Requirements, Agile Software Development Practices with Scrum
Dr. Basem Suleiman · School of Computer Science and Engineering (CSE)

🇨🇳 COMP9820 软件项目管理——软件需求、使用 Scrum 的敏捷软件开发实践。

---

### 02 · Acknowledgement of Country

![](images/02_acknowledgement_of_country.jpg)

I acknowledge the Bidjigal as the Traditional Custodians of the land we are meeting on today. I pay my respects to Elders past and present and recognise the enduring connection of Aboriginal and Torres Strait Islander peoples to Country. I invite us all to reflect on our shared responsibility to honour and respect this land and its stories.

🇨🇳 国土致谢：承认 Bidjigal 人是我们今天所在土地的传统守护者，向过去和现在的长者致敬，并认可原住民与托雷斯海峡岛民与这片土地的长久联系。

---

### 03 · Outline

![](images/03_outline.jpg)

- Agile Software Development Practices
  - Agile Manifesto, and Principles
  - Scrum; Team Roles, Events, Artefacts, Planning, Estimation & Monitoring
- Agile Development (Software Requirements)
  - User Stories
- Revisit – Git Team practices

🇨🇳 本讲大纲
- 敏捷软件开发实践
  - 敏捷宣言与 12 条原则
  - Scrum：团队角色、事件、产物、计划、估算与监控
- 敏捷开发中的软件需求
  - 用户故事（User Stories）
- 回顾：Git 团队协作实践

---

### 04 · Agile Software Development – Values & Principles

![](images/04_section_agile_values_principles.jpg)

**Agile Software Development – Values & Principles**（章节页）

🇨🇳 章节：敏捷软件开发——价值观与原则。

💬 **讲师补充**
- "敏捷"没有一个明确的定义，最接近定义的就是 **敏捷价值观**——它规定了软件开发团队如何协作。
- 之后学 Scrum 时，你会不断回头看这些价值观和原则：为什么团队这样组织、为什么有这个角色那个角色，答案都在这里。

---

### 05 · Agile Manifesto – Agile Values

![](images/05_agile_manifesto_values.jpg)

"We are uncovering better ways of developing software by doing it and helping others do it. Through this work we have come to value:"
- **Individuals and interactions** over processes and tools
- **Working software** over comprehensive documentation
- **Customer collaboration** over contract negotiation
- **Responding to change** over following a plan

The items on the left are **more valued** than those at the right
Agile Manifesto: http://agilemanifesto.org/ · © 2001, the above authors. This declaration may be freely copied in any form, but only in its entirety through this notice.

🇨🇳 敏捷宣言——四条价值观
"我们通过亲身实践并帮助他人实践，正在发掘更好的软件开发方式。由此我们建立了如下价值观："
- **个体与互动** 高于 流程与工具
- **可工作的软件** 高于 详尽的文档
- **客户协作** 高于 合同谈判
- **响应变化** 高于 遵循计划

左边的条目比右边的 **更受重视**（不是右边不重要）。

💬 **讲师补充**
- 宣言不是凭空来的：一群软件从业者在瀑布式开发里挣扎了很多年，才总结出这套让团队更好协作的方式。
- **最常见的误解**：一说"我们做敏捷"，就以为不用工具、不用流程、不写文档、不签合同、不做计划。**错**——只是左边比右边更重要。我们仍然写文档、用工具、走流程，只是 **轻量化**。
- 第 1 条：不像瀑布那样花几个月把一切定义到"完美"、走一套僵硬冗长的流程；流程是灵活的，重点是人如何用流程和工具把软件做出来。
- 第 2 条：写了一大堆没人看的文档有什么意义？我们要做的是对最终用户、客户、相关方有价值的东西。
- 第 3 条：瀑布式开发是先花大量时间拟法律合同、让客户签字再开工；改需求就要加钱。敏捷是迭代地和客户一起工作，弄清楚他们真正想要什么。
- 第 4 条：**软件的本质是演进**。软件运行在有客户、用户、环境的世界里，变化一定会发生；我们要 **响应变化**，而不是说"计划定了不能改"。
- 右边的东西正是过去多年让人痛苦的根源；左边是从业者提出的解法。

---

### 06 · Agile Principles (1)

![](images/06_agile_principles_1.jpg)

1. Our highest priority is to **satisfy the customer** through **early** and **continuous delivery** of **valuable software**
2. **Welcome changing requirements**, even late in development. Agile processes harness change for the customer's competitive advantage
3. **Deliver working software frequently**, from a couple of weeks to a couple of months, with a preference to the **shorter timescale**
4. **Business people** and **developers** must **work together daily** throughout the project

Agile Alliance: http://www.agilealliance.org

🇨🇳 敏捷原则（1–4）
1. 最高优先级：通过 **尽早、持续地交付有价值的软件** 让客户满意
2. **欢迎需求变更**，哪怕在开发后期；敏捷流程把变化变成客户的竞争优势
3. **频繁交付可工作的软件**，几周到几个月一次，**越短越好**
4. **业务人员和开发者** 在整个项目期间 **每天一起工作**

💬 **讲师补充**
- 12 条原则是在价值观之上进一步指导团队怎么工作的。
- "有价值的软件"= 能给最终用户/客户带来好处的软件，这是建软件的第一优先级。
- 需求变更通常来自最终用户或客户，接受变化才能做出他们想要的东西。
- 不要花很长时间设计、开发、写文档才交付；交付能用的东西、**尽早收集反馈、尽早处理**再往前走。
- 业务人员懂业务领域（例如审批采购订单有什么规则），这些输入要由业务人员带给开发者，开发者不该自己编规则；"daily" 强调的是频率——贯穿整个项目。

---

### 07 · Agile Principles (2)

![](images/07_agile_principles_2.jpg)

5. Build projects around **motivated individuals**. Give them the **environment and support** they need, and **trust** them to get the job done
6. The most efficient and effective method of **conveying information** to and within a development team is **face-to-face conversation**
7. **Working software** is the primary **measure of progress**
8. Agile processes promote **sustainable development**. The sponsors, developers, and users should be able to maintain a **constant pace** indefinitely

🇨🇳 敏捷原则（5–8）
5. 围绕 **有干劲的个体** 组建项目；给他们所需的 **环境和支持**，并 **信任** 他们能完成工作
6. 团队内外 **传递信息** 最高效的方式是 **面对面交谈**
7. **可工作的软件** 是衡量进度的 **首要标准**
8. 敏捷流程提倡 **可持续开发**：出资方、开发者和用户应能无限期地保持 **稳定的节奏**

💬 **讲师补充**
- 第 5 条给开发团队很大的自由和信心：不由项目经理或其他角色发号施令，而是通过环境、支持和信任来赋能——Scrum 方法会具体规定怎么做到。
- 第 6 条点出了 **项目最常见的失败原因：沟通**。沟通不到位会做出客户不要的功能、或者对实现方式理解不一致而产生 bug。面对面远好于聊天和邮件——你们应该也体会过靠文字沟通产生的误解。
- 第 7 条：进度不是看写了多少页文档、多少张设计图，而是做出了客户想要的、能跑的东西——哪怕功能很小，"这些做完了，下一个"。
- 第 8 条：**匀速开发**。不是一周把大部分活干完、后面几周越干越少，而是每天/每周都稳定推进，这才能维持良好进度。

---

### 08 · Agile Principles (3)

![](images/08_agile_principles_3.jpg)

9. **Continuous attention** to **technical excellence** and **good design** enhances agility
10. **Simplicity** – the art of maximizing the amount of work not done is essential
11. The best architectures, requirements, and designs emerge from **self-organizing teams**
12. At regular intervals, the **team reflects** on how to become more **effective**, then **tunes and adjusts its behavior** accordingly

🇨🇳 敏捷原则（9–12）
9. **持续关注技术卓越和良好设计** 能增强敏捷性
10. **简单**——最大化"不做的工作量"的艺术——至关重要
11. 最好的架构、需求和设计来自 **自组织团队**
12. 团队 **定期反思** 如何更高效，然后 **调整自己的行为**

💬 **讲师补充**
- 第 9 条：每做一小块软件都要注意技术层面，这样才灵活。
- 第 10 条：不要把事情复杂化，保持简单、清晰、目标明确。**今天就会学到一种比你们习惯的方式简单得多的写需求方法**。
- 第 11 条：团队不是被业务人员告知"必须这样做"，而是自己决定最好的做法。**项目安排：Sprint 1 会给你们一些脚手架（scaffolding）；从 Sprint 2 起，由你们接管，自己定义需求、自己主导。**
- 第 12 条：团队要反思的不是技术，而是团队本身、所遵循的流程：有没有障碍、有没有问题——这些都会影响团队进度和目标的达成。

---

### 09 · Agile Software Development Model

![](images/09_agile_development_model.jpg)

**Agile Software Development Model** — Iterative & Incremental development
（图：Agile Lifecycle 循环——Start → Development phases (Build functionality) → Integrate & Test → Review → Feedback → Approve? → Release / Record & Make changes → Adjust & Track (Reprioritize features) → Next iteration）
https://blog.capterra.com/agile-vs-waterfall/

🇨🇳 敏捷软件开发模型——**迭代 + 增量** 开发。一轮循环：开始 → 开发功能 → 集成与测试 → 评审 → 反馈 → 是否通过？通过就发布，不通过就记录并修改 → 调整与跟踪（重新排列功能优先级）→ 下一轮迭代。

💬 **讲师补充**
- 上周讲过两种软件开发过程模型；敏捷模型就是本课程采用的那一种，常被称为 **迭代增量开发模型**。
- 对照价值观和原则看这张图：每次小迭代里定义要做什么、构建、集成、测试，然后评审——由客户和技术团队给反馈，决定好不好、要不要改。这个循环是建立在 12 条原则和价值观之上的。
- 让整个团队真正做到并遵循这个流程是有挑战的，虽然看起来简单。后面用 Scrum 详细讲每个循环里到底应该发生什么。

---

### 10 · Scrum Software Development

![](images/10_scrum_overview.jpg)

An agile method for **managing software development** focused on **delivering products of the highest value**

**Teams and roles**
- Product Owner, Scrum Master, Dev Team

**Events**
- Sprint, Sprint Planning, Daily Scrum, Sprint Review, and Retrospective

**Artefacts**
- Product Backlog, Sprint Backlog, Increment
- Project estimation and Sprint estimation
- Rules govern the relationships between roles, events and artifacts
- All the above components are essential for Scrum success

🇨🇳 Scrum 软件开发：一种用于 **管理软件开发** 的敏捷方法，专注于 **交付最高价值的产品**。
- **团队与角色**：Product Owner（产品负责人）、Scrum Master、开发团队
- **事件**：Sprint、Sprint Planning（冲刺计划会）、Daily Scrum（每日站会）、Sprint Review（冲刺评审）、Retrospective（回顾会）
- **产物**：Product Backlog（产品待办列表）、Sprint Backlog（冲刺待办列表）、Increment（增量）；项目估算与 Sprint 估算
- **规则** 把角色、事件、产物串起来；以上所有组成部分对 Scrum 的成功缺一不可

💬 **讲师补充**
- 敏捷方法有很多种。讲师问有没有人做过 **极限编程（XP）** 或游戏开发——有做游戏的同学用过 XP。XP 也是敏捷方法之一；各方法共享一部分价值观和原则。
- 本课程采用 **Scrum**：业界广泛使用，你们的 **capstone 项目 COMP9900** 也用它。
- "最高价值"是什么意思？举例：**Microsoft Word** 有海量功能，大多数人从未碰过甚至不知道；真正对我有价值的是写、编辑、修改、保存这些核心功能——设计和构建应该从这些开始。如果一开始就什么都做，客户可能会困惑："这么多东西，哪个才是重点？"
- **WhatsApp** 一开始只做一件事：即时消息，然后把它做得越来越可靠、越来越快，加了发文件/图片；视频通话是在获得主流用户之后才加的。敏捷教我们：**从客户最感兴趣、价值最大的功能开始**。
- 前面说敏捷也做文档，Scrum 里的 **产物（artifacts）就是轻量、聚焦的文档**。

---

### 11 · The Scrum Team

![](images/11_section_scrum_team.jpg)

**The Scrum Team**（章节页）

🇨🇳 章节：Scrum 团队。

---

### 12 · Scrum Team – The Product Owner

![](images/12_scrum_team_product_owner.jpg)

**Product Owner (PO)** maximize the **value** of the **product** and the **work**
- Talks to customer/clients, understand requirements and its priorities
- **Managing** the **Product Backlog** (only person)
  - Can assign it to the development team, but still accountable

**Managing the product backlog:**
- Record product backlog items and order it
- Optimize the value of the work the development team performs
- Ensure transparency and clarity of the product backlog
- Ensure the development team understands product backlog

🇨🇳 Scrum 团队——产品负责人（PO）：让 **产品** 和 **团队工作** 的价值最大化
- 与客户沟通，理解需求及其优先级
- **唯一** 负责管理 Product Backlog 的人（可以让开发团队帮忙，但责任仍在 PO）
- 管理 Product Backlog 的具体内容：记录条目并排序；优化开发团队所做工作的价值；确保 Backlog 透明、清晰；确保开发团队理解 Backlog

💬 **讲师补充**
- PO 对多数人是个新角色。PO 是 **为最终用户/客户代言** 的人：我们要做的这个功能对他们有没有好处？能不能解决他们日常工作中的问题？PO 要把自己放到用户的位置上思考。
- 客户往往只会告诉你 **问题**（"我总是很难把所有文件一起上传"），而不会告诉你怎么解决——**把问题变成合适的功能** 是 PO 要发挥创造力的地方。
- 开发过程中会发现原来没想到的功能，PO 把它们加进 Backlog；同时要聚焦有价值的事，别做太多没价值的。
- **透明** 非常重要：如果把开发团队排除在外，他们会问"为什么加这个功能？""为什么有人告诉我们做什么？"——透明才能让团队自组织、保持动力。
- **你们每个组都会有一个 PO**。当 PO 就要知道自己的职责并在每个 Sprint 里执行。这也是在积累可以写进简历、面试时能讲的经历——"我是 PO，我做了 X 和 Y"，业内的人一听就懂，这是一套 **正式语言**。

---

### 13 · Scrum Team – The Development Team

![](images/13_scrum_team_development_team.jpg)

- **Self-organizing**: turns Product Backlog into increments of potentially releasable functionality
- **Two-pizza team** (4-9 members)
- **Cross-functional**: skills mix necessary to create a product
- Whole team is **accountable (often no sub-teams)**
- Less emphasis on **titles** for Dev team members

🇨🇳 Scrum 团队——开发团队
- **自组织**：把 Product Backlog 变成可发布的功能增量
- **两个披萨团队**：4–9 人
- **跨职能**：具备做出产品所需的技能组合
- **整个团队共同负责**（通常不分子团队）
- **不强调头衔**

💬 **讲师补充**
- 自组织 = 大家一起管理、一起做决定、和 PO 讨论、互相讨论，而不是被命令。
- "两个披萨（美国尺寸）能喂饱的团队"，通常 4–9 人。团队越大，成员间的互动和讨论越复杂；太小又可能做不出东西。业界小团队也大约 6–9 人。**你们是 6 人一组，和 capstone 一样**，正好获得这种体验。
- 跨职能：有人擅长前端、有人擅长后端、设计等等。**这就是 Week 1 lab 组队时让你们考虑技能搭配的原因**，而不是随机组队。
- 通常不分子团队：不是架构师决定、其他人接受，而是整个团队一起做决定。
- 弱化头衔：人人参与、人人负责，不让某些人比别人"更重要"。这些做法让团队自组织、有动力、都贡献、**透明**——你不希望有人因为"凭什么他是 lead 来指挥我们"而藏着掖着。**有两个领导通常就会有冲突**；团队要有凝聚力、协作。

---

### 14 · Scrum Team – The Scrum Master

![](images/14_scrum_team_scrum_master.jpg)

**Scrum Master (SM)** Keeps the team focused on **using Scrum properly**
- Everyone **understands Scrum rules** and **values** (**coaching**)
- Remove roadblocks
- Helps those outside the Scrum team which of their interactions with the Scrum team are/aren't helpful
- **Maximize the value** created by the Scrum team through changing team interactions

🇨🇳 Scrum 团队——Scrum Master（SM）：让团队专注于 **正确地使用 Scrum**
- 让每个人 **理解 Scrum 的规则和价值观**（**辅导/教练**）
- 清除障碍
- 帮助团队外的人了解他们与团队的哪些互动有帮助、哪些没有
- 通过改变团队互动方式 **最大化团队创造的价值**

💬 **讲师补充**
- 既然团队要采用 Scrum，就需要有人确保大家 **正确地** 遵循这些实践——辅导团队、监督团队。
- 推荐参考书：幻灯片末尾列的 **《Learning Agile》**（Stellman & Greene），讲义大量内容取自此书，想深入理解可以读。
- 光看 Scrum 觉得都很容易；真正作为团队用 Git/GitLab、做 CI/CD 等实践时就会发现困难：有人不相信这套方法——"为什么每天都要开站会？"站会是重要的 Scrum 事件，有目的、有结构；即使勉强做了但做得不对，也会削弱 Scrum 的收益。**做得不对，站会就会变成负担**。
- **每个组都会有一个 SM**。SM 的职责是让团队正确地采用和实施 Scrum 和敏捷实践，让收益和生产力最大化。
- 清除障碍的例子：大家都很忙约不到开会时间——SM 说"这个我来解决，我来找一个大家都行的时间"，团队就不用为此操心。

---

### 15 · Scrum Team — Which structure better describes the Scrum team?（Slido 投票）

![](images/15_slido_scrum_team_structure.jpg)

**Scrum Team** — Which structure better describes the Scrum team?
- **Team A**：Developer/Architect、Scrum Master、Product Owner、Team Lead 围绕同一颗星（共同目标）交流
- **Team B**：Developer/Architect、Project Manager、Business User、Team Lead 各自脑中想着不同的星

Slido.com --> # 3301735

🇨🇳 Scrum 团队——哪种结构更符合 Scrum 团队？Team A：所有人围绕一个共享的目标互相沟通；Team B：每个人各想各的，且有 Project Manager 这一角色。（Slido 投票，房间号 3301735）

---

### 15a · Slido 结果：Which team better describes the Scrum team structure?

![](images/15a_slido_result_team_A_vs_B.jpg)

| 选项 | 得票 |
|---|---|
| Team A | **79%** |
| Team B | 14% |
| Both Team A and Team B | 7% |

共 28 票。

💬 **讲师补充（课堂讨论）**
- 讲师问为什么选 A、B 有什么问题。**学生答：开放的沟通（open communication）**。讲师：100% 正确——**沟通和互动是关键**。A 里团队成员始终在讨论，有 **清晰的共同愿景**；B 里每个人对功能或项目有不同理解，各自按自己的想法实现——这非常危险。团队要在同一页上、一起讨论、一起决策、整个团队共同负责。
- 再看角色：**B 里有 Project Manager，而 Scrum 里没有项目经理**。Scrum 的标准角色只有开发团队、Scrum Master、Product Owner。实践中有些公司会做变体（比如设一个 team lead），那是他们觉得更符合自身需要；但 **项目经理** 是偏业务的人，告诉开发团队"你要做这个、要在这个时间做完"——开发者会觉得"他们不懂技术，这比他们想的更花时间，却怪我们没按时做完"。很多项目延期或超支就是因为以为项目经理什么都懂、告诉大家做什么就行。
- B 里的 Business User 也不怎么和团队沟通，而我们要求业务人员也给团队输入。
- 这看起来不难，真正实施时会发现和以前的习惯不一样，**需要团队每个人转变思维方式**。SM 要确保团队里没有人扮演项目经理。
- 讲师的真实经历：在 capstone（COMP3900/9900）有同学项目结束时发邮件说"我是项目经理"——**Scrum 开发里没有这个角色**。面试时如果说"我在 Scrum 敏捷团队里当项目经理"，对方会立刻知道这不是 Scrum 的角色；**评分时我们看的就是你是否理解并正确应用这些**。

---

### 16 · The Scrum Events

![](images/16_section_scrum_events.jpg)

**The Scrum Events**（章节页）

🇨🇳 章节：Scrum 事件——Scrum 的第二根支柱。

---

### 17 · Scrum Events – The Sprint

![](images/17_scrum_events_sprint.jpg)

A development **iteration** (one cycle)
- Useable and potentially **releasable product increment** is created

**Time-boxed** (typically 2-4 weeks)
- Too long sprints may lead to changes in the definition

Sprints have **consistent durations** during the product development

Sprint Planning, Daily Scrum (Stand-ups), the Development Work, the Sprint Review and the Sprint Retrospective

🇨🇳 Scrum 事件——Sprint（冲刺）
- 一个开发 **迭代**（一个周期）：产出可用、可发布的 **产品增量**
- **时间盒**（通常 2–4 周）；Sprint 太长，中途定义可能就变了
- 整个产品开发期间各 Sprint **时长一致**
- 一个 Sprint 内含：Sprint 计划会、每日站会、开发工作、Sprint 评审、Sprint 回顾

💬 **讲师补充**
- 敏捷是迭代增量开发，所以把开发切成一个个 Sprint/迭代。每个迭代都要做出 **能用的东西**——哪怕只有一两个功能，做完就可以发布，客户就能受益。不是做一大堆用户不感兴趣的功能。发布出去的就是一个 **增量（increment）**。
- 敏捷里 **一切都有时间盒**，时间盒让我们 **有纪律**、按周期走。前面讲"匀速开发"，所以每个 Sprint 必须同样长：定了两周就每个 Sprint 都两周。
- 常见 2–4 周，最长 4 周；再长就违背敏捷了——做了一大堆才给客户看。做得少、更早给客户看，就能 **更早拿到反馈、以更低成本修正**、更早协作。
- **你们的项目 Sprint 定为 2 周**，以配合 10 周的学期。

---

### 18 · Scrum Events – Sprint Planning

![](images/18_scrum_events_sprint_planning.jpg)

Identify the **Sprint Goal** (items from the "Product Backlog")
Identify **work to be done** to deliver this
**Two-parts meeting** (SM, PO, and Dev team)
- **Before meeting**: PO prepares prioritized list of most valuable items
- **Meeting part 1**: PO & Dev team select items to be delivered at the end of the sprint based on their value and on the team's estimate of how much work needed
- **Meeting part 2**: Dev team figure out the individual tasks they'll use to implement those items

**Output:** *Sprint Backlog*

🇨🇳 Scrum 事件——Sprint 计划会
- 确定 **Sprint 目标**（从 Product Backlog 中选条目）；确定要交付它 **需要做的工作**
- **两部分会议**（SM、PO、开发团队都参加）
  - **会前**：PO 准备好按优先级排好的最有价值条目清单
  - **第 1 部分**：PO 与开发团队根据 **价值** 和 **团队估算的工作量**，选出本 Sprint 结束时要交付的条目
  - **第 2 部分**：开发团队把这些条目拆成实现所需的 **具体任务**
- **产出：Sprint Backlog**

💬 **讲师补充**
- 每个 Sprint 开始都要先计划：先定一个 **目标**，例如"这个 Sprint 做用户认证"，然后把高度相关的功能放进来，Sprint 结束时能说"用户可以认证了"。
- 计划通过会议进行——这又回到"沟通与互动是关键"。**不是项目经理和 PO 开会做决定再通知开发团队**，团队是会议的一部分。
- PO 会前准备的是"对本 Sprint 目标最有价值"的优先级清单，因为 PO 最清楚哪些功能对用户更重要。
- 第 1 部分按价值和估算选条目（估算后面会讲，是关键环节）；第 2 部分把每个功能/用户故事拆成更小的任务。
- 产出 Sprint Backlog：本 Sprint 要做的功能清单，Sprint 结束时应全部实现并达成 Sprint 目标。

---

### 19 · Scrum – Team Structure — Which team organization better describes the Scrum Sprint/iteration planning?（Slido 投票）

![](images/19_slido_sprint_planning_structure.jpg)

**Scrum – Team Structure** — Which team organization better describes the Scrum Sprint/iteration planning?
- **Team C**：Project Manager 拿着甘特图式计划，单向分派任务给各成员
- **Team D**：所有成员围着任务板（To Do / In Progress / Done + 燃尽图）互相讨论

Slido.com --> # 3301735

🇨🇳 Scrum 团队结构——哪种组织方式更符合 Scrum 的 Sprint/迭代计划？C：项目经理一个人拿着计划分配任务；D：全员围着任务板一起计划。（Slido 房间号同上）

💬 **讲师补充**
- 讲师说明：这题不是问团队结构，而是问 **计划/迭代的过程** 由谁怎么做；二维码同上。

---

### 19a · Slido 结果：Which team organization better describes the Scrum Sprint planning?

![](images/19a_slido_result_team_C_vs_D.jpg)

| 选项 | 得票 |
|---|---|
| Team C | 48% |
| Team D | **52%** |
| Both Team C and Team D | 0% |

共 31 票。

💬 **讲师补充（课堂讨论）**
- 结果很接近。**学生答：Scrum 里不存在项目经理。** 讲师：非常好。
- 传统项目里项目经理替团队做计划：用 Microsoft Project 之类的工具建好所有任务、什么时候交付，然后"告诉"开发团队——实际上是在 **独断计划决策**。项目经理的利益可能是按客户要求的时间交付，于是给团队施压"你们必须做到"。团队感到不被参与、不是决策的一部分，结果往往交付不出有价值的东西。
- 敏捷的计划是 **所有团队成员一起参与**，决定本 Sprint 放什么；每个 Sprint 都和 PO、SM 一起做计划。SM 要确保团队按原则做计划，别做错。
- **正确答案是 Team D**。没有 team lead 之类的头衔告诉团队做什么；每个人都对"为什么做这个功能、要多久、这个 Sprint 放不放得下"有发言权；后面讲估算时也是全员参与。
- 这两道题想说的就是：**别把传统方式带进来**，要换思维。SM 要告诉大家"我们这样做，效果会更好"。如果不按敏捷正确地做，人们就会说"敏捷没用"——其实是有成员不相信、或做得不对；这些问题通常 **隐藏到很晚才暴露**。上周讲团队动力学时提到有人会妥协"好吧我接受"，明知没在正确地做 Scrum——**要透明地把这些讨论出来**。

---

### 20 · Scrum Events – Daily Scrum Meeting (Stand-ups)

![](images/20_scrum_events_daily_scrum.jpg)

- To ensure **problems and obstacles are visible** to the team
- **Timeboxed *15 minutes*** (same time and place each day)
- **All team members** including SM and PO must attend
- Each briefly **answers three questions**:
  - What did I do yesterday that helped the development team meet the Sprint Goal?
  - What will I do today to help the development team meet the Sprint Goal?
  - do I see any obstacles that prevent me or the Dev team to meeting the Sprint Goal?
- **No problem-solving** during the meeting
  - Follow-up meetings if further discussion is required

🇨🇳 Scrum 事件——每日站会
- 目的：让 **问题和障碍对团队可见**
- **限时 15 分钟**（每天同一时间、同一地点）
- **所有成员** 包括 SM 和 PO 必须参加
- 每人简短回答三个问题：昨天为达成 Sprint 目标做了什么？今天要做什么？有没有阻碍我或团队达成目标的障碍？
- 站会上 **不解决问题**；需要深入讨论的另开后续会议

💬 **讲师补充**
- 一说"我做敏捷"大家都知道"站会"，也都会问：**真的每天要开吗？真的要站着吗？** 站着就是为了 **短、切题**——坐下很可能就拖长了；SM 要确保控制在 15 分钟。
- 时长可随团队规模略有变化（4–9 人），因为每个人都要回答三个问题。
- 前两个问题让大家知道 **谁在做什么**，这就是 **透明**：你听到"我在做这个功能的后端"，而你做前端，就知道要去找他聊。第三个问题：有人遇到问题就简单提一下，不讲细节；别人可能说"这影响到我，会后聊"或"我遇到过同样问题，告诉你怎么解决"——**但细节在后续会议里谈**。
- 一旦在站会里聊细节，其他人会觉得"让我干活去吧，这问题跟我没关系"，觉得坐在会议里什么都没做。开一个小时的站会，人就会厌烦、觉得太多——这就是"实施错了然后出问题"的典型。保持 15 分钟、只答三个问题，就能保持轻量和生产力。
- SM 应帮助做后续跟进，确保团队真的在分享和讨论重要信息。

---

### 21 · Scrum Events – Development Work

![](images/21_scrum_events_development_work.jpg)

- Dev team Builds the items in the *Sprint Backlog* into working software
- Should inform the PO if they are overcommitted or can add extra items if time allows
- Must **update the Sprint backlog** and keep it **visible** to everyone

🇨🇳 Scrum 事件——开发工作
- 开发团队把 Sprint Backlog 里的条目做成可工作的软件
- 承诺过多要告诉 PO；时间充裕可以加条目
- 必须 **更新 Sprint Backlog** 并让所有人 **可见**

💬 **讲师补充**
- 有了计划、有了每日站会，开发工作就是真正把 Sprint 里定义的功能做出来。
- PO 要确保团队 **不跑偏**：不会做着做着切到别的功能，也不会把功能做成客户不需要的样子——PO 确保功能的实现方式确实给用户带来价值。
- 更新 Sprint Backlog 是为了让每个人都知道进度："这个任务我负责，我在做/我做完了"。后面会演示怎么做。

---

### 22 · Scrum Events – Sprint Review

![](images/22_scrum_events_sprint_review.jpg)

Informal meeting at end of the Sprint (max. 4-hours)
- **Dev team demonstrates working software to customers/stakeholders**
  - Items done – completed, tested & accepted by the product owner
  - Only functional working software – not architecture, database design etc.
- **Stakeholders share** their feedback, ideas, feelings, thoughts about the demo
- The Product Owner explains "Done" and "Not Done" items

**Output:** *revised Product Backlog and probable items for next iteration*

🇨🇳 Scrum 事件——Sprint 评审：Sprint 结束时的非正式会议（最多 4 小时）
- **开发团队向客户/相关方演示可工作的软件**："完成"= 做完、测过、PO 验收；只演示能运行的功能，不讲架构、数据库设计等
- **相关方分享** 对演示的反馈、想法、感受
- PO 说明哪些"完成"、哪些"未完成"
- **产出：修订后的 Product Backlog，以及下个迭代的候选条目**

💬 **讲师补充**
- Sprint 结束有两个主要事件：评审和回顾。评审就是 **演示** 团队设计和实现的东西。
- "最多 4 小时"取决于 Sprint 长度：4 周的 Sprint 评审可以长一些；**2 周的 Sprint 大约 1–2 小时**。团队自己定时长，但不能开放式无限拖；SM 负责控时，避免不必要的讨论。
- 演示的目的不是"汇报"，而是让客户/用户说"很好我满意"或"我需要改"。在每个 Sprint 结束时做，意味着 **尽早收集反馈、尽早协作**，而不是全部做完才给他们看。反馈可以变成新功能或改进，进入下一次计划。
- 要邀请 **能影响决策的相关方**（stakeholders）——产品是否就绪、能否发布，他们说了算；不邀请就等于把决策者排除在外。
- 产出：要么全部完成、客户满意，可以进入下一个发布；要么有些需要改进，进入下一个 Sprint。

---

### 23 · Scrum Iteration (Sprint) Process

![](images/23_scrum_iteration_process.jpg)

**Scrum Iteration (Sprint) Process**
（左图：Iteration #1 → #2 → #3 层层叠加的循环，每轮产出增量；右图：Backlog 1 → 2 → 3 → 4，每轮取一部分去做，Backlog 逐渐减少）
\* **Product Backlog**: set of all features and sub-features (items) needed to build the product

🇨🇳 Scrum 迭代过程。Product Backlog = 构建产品所需的全部功能和子功能（条目）的集合。

💬 **讲师补充**
- 开发经过一个个迭代/Sprint：Sprint 1 结束做出一些功能，Sprint 2 再加一些，Sprint 3 再加——最终产品就是软件的 **增量** 累积。
- 同时看 Product Backlog：开始时是你要做的全部功能；第一轮做完两个，这两个就没了；随着推进 Backlog **应该在下降**。但也可能在 Sprint 中往里加（比如发现要修的问题）。总体应该逐渐减少，并且要 **持续更新 Product Backlog 和 Sprint Backlog**。

---

### 24 · Scrum Events – Retrospectives

![](images/24_scrum_events_retrospectives.jpg)

Opportunity for the **Scrum team to inspect itself and create plan for improvements**
- **Inspect** how the last Sprint went with regards to **people, relationships, process, and tools**;
- Identify and order the major **items that went well** and **potential improvements**;
- Create a plan for **implementing improvements** to the way the Scrum Team does its work

🇨🇳 Scrum 事件——回顾会：**团队自我检视并制定改进计划** 的机会
- **检视** 上一个 Sprint 在 **人、关系、流程、工具** 方面的情况
- 找出并排序 **做得好的** 和 **可改进的**
- 制定 **落实改进** 的计划

💬 **讲师补充**
- 回顾会对很多人是新东西：团队坐在一起，**不谈开发、不谈功能**——那些在评审和开发中已经谈过了。回顾会 **纯粹关于人、关系、流程和工具**：我们做得怎么样？什么顺利？什么出了问题？作为团队怎么改进？工具应该帮我们，而不是让日子难过。
- 产出是改进计划，比如换更好的工具、把工具配置得更利于协作。

---

### 25 · Scrum Events – Retrospectives（会议形式）

![](images/25_scrum_events_retrospective_meeting.jpg)

**Retrospective meetings** (max. 1-2 hours)
The SM and the Dev. team (maybe product owner)
Each person answer **two questions**:
- What went well during the Sprint?
- What can be improved in the future?

The **SM notes improvements** that should be added to the Product Backlog (non-functional items)
- E.g., set-up a better build server, adopting design principles, changing office layout

**Output:** *identified improvements to be implemented in the next Sprint (adaptation)*

🇨🇳 回顾会议（最多 1–2 小时）
- 参加者：SM 和开发团队（PO 可选）
- 每人回答 **两个问题**：这个 Sprint 什么做得好？将来什么可以改进？
- **SM 记录改进项**，加入 Product Backlog（属于非功能性条目），例如：搭建更好的构建服务器、采用设计原则、改变办公布局
- **产出：下个 Sprint 要落实的改进（适应/adaptation）**

💬 **讲师补充**
- Scrum 和敏捷 **明确规定** 了回顾怎么开，不是随意的。一切都有时间盒：1–2 小时，太长人们就会说"没用、太多了"；Sprint 短的话时间也相应缩短。
- SM 的核心工作是识别团队的障碍和问题并和团队一起解决。
- 注意：**和站会一样，每个人都要回答问题**，不是由 lead 说——每个人都参与，这让你感到归属感、是过程的一部分，而不是被告知做什么。
- 例子：有人说构建服务器又慢又老崩，我们需要修——这就成了下个 Sprint 的改进项。这就是团队的 **自我适应、自组织**：团队自己决定哪里不好、怎么改，下次就改进。
- **你们要在每个 Sprint 结束时做回顾。**

---

### 26 · Sprint Retrospective - Example for Sprint 1

![](images/26_retrospective_example_sprint1.jpg)

| Last retrospective's To Try | What went well | What didn't go so well | To Try |
|---|---|---|---|
| First sprint so N/A | Met sprint goal | Duplicated work (2 team-members accidentally working on same task without knowing) | |

🇨🇳 Sprint 1 回顾示例（四列表格）：上次的 To Try——第一个 Sprint，不适用；做得好——达成了 Sprint 目标；不太好——重复劳动（两名成员不知情地做了同一个任务）；To Try——待填。

💬 **讲师补充**
- 做得好：达成 Sprint 目标，很棒。不太好：两个人意外地做了同一个任务——这可能是 **沟通问题**、或者对谁做什么不清楚、或者 **可见性** 不够。

---

### 27 · Sprint Retrospective - Example for Sprint 1（补上 To Try）

![](images/27_retrospective_example_sprint1_to_try.jpg)

| Last retrospective's To Try | What went well | What didn't go so well | To Try |
|---|---|---|---|
| First sprint so N/A | Met sprint goal | Duplicated work (2 team-members accidentally working on same task without knowing) | ensure everyone sends daily scrum updates if absent from the daily scrum meeting; Adam checks that everyone's present, and reminds any absentees to email status update to team |

🇨🇳 To Try：确保缺席站会的人也要发每日更新；Adam 负责点名，提醒缺席者给团队发邮件汇报状态。

💬 **讲师补充**
- 下个 Sprint 要针对这个问题：确保更新到位、确保大家在站会上分享"我在做这个、接下来做那个"——这样别人就能说"等等，我也在做这个"。

---

### 28 · Sprint Retrospective - Example for Sprint 2

![](images/28_retrospective_example_sprint2.jpg)

| Last retrospective's To Try | What went well | What didn't go so well | To Try |
|---|---|---|---|
| Ensure everyone sends daily scrum updates if absent from the daily scrum meeting. (Adam checks that everyone's present, and reminds any absentees to email status update to team) → *This worked well. Everyone knows what everyone else is doing - no more duplicate work* | Met sprint goal; No more duplicated work | Software unit demonstrated was buggy | Write unit tests for each unit developed (all members to follow up on that) |

🇨🇳 Sprint 2 回顾示例：上次的 To Try 原样搬过来并标注"效果很好，大家都知道彼此在做什么，不再重复劳动"；做得好——达成目标、不再重复；不太好——演示的软件单元有 bug；To Try——每个开发的单元都写单元测试（全员跟进）。

💬 **讲师补充**
- 下一个 Sprint 要回头看：上次定的 To Try **有没有帮团队解决问题**？没有就换别的办法。这是一个闭环。
- **评分要求：我们会要求你们把回顾（以及前面讲的其他事件）记录下来**，以证明你们是按正确的方式实施 Scrum 的。请注意这些细节。

> 💬 讲到这里课间休息约五分钟。休息时一位同学询问：他们所在的线下 tutorial 后来改成了线上，怎么加入？讲师答：该 lab 由 Daniel 负责，给 Daniel 发邮件说明你们已换到线上 tutorial，他（或 tutor）会把你们加进去；讲师也会跟进邮件。

---

### 29 · Scrum Artifacts

![](images/29_section_scrum_artifacts.jpg)

**Scrum Artifacts**（章节页）

🇨🇳 章节：Scrum 产物。

💬 **讲师补充**
- 产物可以理解为 **我们的文档**：在开发、计划过程中产生的东西。

---

### 30 · Scrum Artifacts – Product Backlog (PB)

![](images/30_scrum_artifacts_product_backlog.jpg)

Set of **all features and sub-features** (items) needed to build the product (the "Plan" for multiple iterations)
- Features, functions, requirements, enhancements and fixes from previous Sprints
- Expressed as User Stories

**Maintained by the PO** in collaboration with customers and team
The source of the **product (software) requirements**
- Evolves over the time and never complete (dynamic)

The **items ordered by priority**
- To deliver value to the customer in each iteration, put the most important things early

🇨🇳 Scrum 产物——Product Backlog（PB）
- 构建产品所需的 **全部功能和子功能** 的集合（多次迭代的"计划"）：功能、需求、改进、以及上个 Sprint 遗留的修复；**以用户故事表达**
- **由 PO 维护**，与客户和团队协作
- 它就是 **产品（软件）需求的来源**；随时间演进，**永远不算完成**（动态）
- **条目按优先级排序**：为了每个迭代都给客户交付价值，最重要的放前面

💬 **讲师补充**
- PB 描述我们要实现的功能/需求，也包括从上个 Sprint 发现的问题所需的改进和修复。通常写成 **用户故事**——这是最有效、最贴合敏捷的方式，今天后半段详细讲。
- 强调 PO 的责任：确保团队在协作、和客户一起定义 PB——**不是由一个人或一个来源强加的**。
- "我们在做什么？"看 PB 就知道——用很简单的方式描述。
- **和瀑布最大的区别**：瀑布是花几个月把需求细化成一份不太会变的软件规格说明书；PB **可以也应该演进**。为什么？一开始通过和相关方/用户/客户开 **工作坊**（比如用便利贴）收集大部分需求、理解他们的问题、定义功能，形成 PB——但它 **不完整，也永远不会完整**。
- 需要转变的思维：不是"定义好了就不能改"。轻量的需求定义方式假设"先定义我们知道的、先干起来，推进中会发现更多、再重新定义和细化"。**如果你的 PB 没有在演进，那就有问题**——说明你试图一次把它定义完美。
- 演进的来源：开发团队真正动手时会问"这里怎么设计？要采集什么信息？"PO 因为和客户谈过问题，能回答；不确定就去问客户。
- **优先级/价值**：核心功能构成 **最小可行产品（MVP）**——有了这些功能软件就能被客户使用；其他功能"有更好"，没有产品依然可用。给每一项标上"高度重要"或"nice to have"，先做有价值的——这就是 PB 排序的精髓。

---

### 31 · Scrum Artifacts – Sprint Backlog (SB)

![](images/31_scrum_artifacts_sprint_backlog.jpg)

Set of **PB items selected for the Sprint**, and a plan for delivering the product increment and realize the Sprint Goal
- The Dev. team to forecasts next items to be implemented
- Includes high-priority improvement identified from previous Sprint
- The Dev. team adds new work to the SB
- The estimated remaining work is updated once an item is completed
- Visible to anyone and to be modified by the Dev. team

🇨🇳 Scrum 产物——Sprint Backlog（SB）：**为本 Sprint 选出的 PB 条目**，加上交付产品增量、实现 Sprint 目标的计划
- 开发团队预测接下来要实现的条目
- 包括上个 Sprint 识别出的高优先级改进
- 开发团队可以往 SB 里加新工作
- 每完成一项就更新"剩余估算工作量"
- 对所有人可见，由开发团队修改

💬 **讲师补充**
- PB 描述所有要实现的功能并随时间演进；SB 描述 **我们选中要在下个 Sprint 里做的** 那些条目。每个 Sprint 都有自己的一组条目。

---

### 32 · Sprint Backlog – Example

![](images/32_sprint_backlog_example_task_board.jpg)

Typically divided into 3 sections; **"To Do", "In Progress", "Done"**
Tools to support Sprint planning and monitoring; e.g., Jira
（图：任务板，卡片分布在 To Do 与 In Progress 两列，Done 为空）

🇨🇳 Sprint Backlog 示例：通常分三栏——**待办、进行中、已完成**；用 Jira 等工具支持 Sprint 计划与监控。

💬 **讲师补充**
- 先讲最简单的组织方式：三列。Sprint 1 定义了这些功能（有时功能会再拆成任务），全部放在 To Do。开始开发时分配谁做什么：开发者 1 开始做某功能，就把它移到 In Progress。
- 看这块 **任务板（task board / sprint task board）** 就知道任何时刻谁在做什么、进度如何：图里几项在进行中、Done 还是空的——还没交付任何东西。
- 关键是它 **对整个团队可见、透明**，谁做什么不是秘密——这就是团队自组织的意义。

---

### 33 · Agile Planning (Requirements) — User Stories

![](images/33_section_agile_planning_user_stories.jpg)

**Agile Planning (Requirements)** — **User Stories**（章节页）

🇨🇳 章节：敏捷计划（需求）——用户故事。

💬 **讲师补充**
- 讲完 Sprint 和 PB，现在讲 **需求**。需求通常在 **每个 Sprint 开始时** 定义：你在计划时说"这些是我们要做的需求"。

---

### 34 · Requirements – Agile Software Development Model

![](images/34_requirements_agile_model.jpg)

**Requirements – Agile Software Development Model**
（同第 9 页的 Agile Lifecycle 循环图，强调"Start / Next iteration"处的需求定义）
https://blog.capterra.com/wp-content/uploads/2016/01/agile-methodology-720x617.png

🇨🇳 需求在敏捷开发模型中的位置：在每轮迭代开始/计划时定义本轮要做的需求。

💬 **讲师补充**
- 一开始（比如通过和客户的工作坊）定义所有已知需求形成 PB；然后每个 Sprint 开始时 **从中选出** 进入本 Sprint 的需求。

---

### 35 · User Stories

![](images/35_user_stories_intro.jpg)

- A method for describing software requirements, tasks or issues
- It helps **agile software development teams** capture a **simplified** and **high-level** description of a **requirement** from an **end user** perspective
- Focuses on **value (benefit)** delivered, not technical implementation
- Agile Development (Planning)
  - Ligh-weight planning – iterative and incremental
  - Small enough to build and test within a single Sprint
  - Captured in Product backlog and Sprint Backlog

🇨🇳 用户故事
- 一种描述软件需求、任务或问题的方法
- 帮助 **敏捷团队** 从 **最终用户** 视角写出 **简化、高层次** 的需求描述
- 聚焦于交付的 **价值（好处）**，而不是技术实现
- 在敏捷计划中：轻量级计划（迭代、增量）；小到能在一个 Sprint 内构建并测试；记录在 PB 和 SB 里

💬 **讲师补充**
- 传统方式一个功能要写很多页；这里非常轻量，遵循敏捷原则——假设需求会演进、迭代地做。
- 用户故事从 **要使用该功能的用户** 的视角描述需求，关注 **价值/好处**，不关注怎么实现——我们想的是用户要什么、为什么要。
- 一个用户故事只写 **一件事**，不要塞太多东西；要小到一个 Sprint 内做完并测完。

---

### 36 · User Story – Format

![](images/36_user_story_format_connextra.jpg)

A user story often follows the following **Connextra** format/template:
**As a [who] I want to [what] so that [why]**
- As a **<type of user>** – this is the **WHO**
  - Who are we building this for? Who is the user?
- I want **<some feature>** – this is the **WHAT**
  - What are we building? What is the intention?
- So that **<some reason>** – this is the **WHY**
  - Why are we building this? What is the value for the customer?

🇨🇳 用户故事格式——**Connextra 模板**：**作为【谁】，我想要【什么】，以便【为什么】**
- 作为 **<某类用户>**——**WHO**：为谁做？用户是谁？
- 我想要 **<某功能>**——**WHAT**：做什么？意图是什么？
- 以便 **<某原因>**——**WHY**：为什么做？对客户的价值是什么？

💬 **讲师补充**
- 很简单，三个要素：**who、what、why——三个 W**。
- 想清楚 **用户是谁** 有助于更好地设计和实现功能。
- "what" 必须是 **一件事**，不要"我想做这个、这个、还有那个"。
- 讲师问：为什么需要 "why"？**学生答：给团队动力（motivation）。** 讲师：很好——团队理解了用户为什么要这个功能，就能更好地设计和实现；不理解价值，可能做出来的东西并不能给用户带来价值。理解价值让你始终聚焦在最终用户的好处上。

---

### 37 · User Story – Format（Role / Goal / Benefit）

![](images/37_user_story_format_role_goal_benefit.jpg)

- As a **[role]**, I want **[goal]**, so that **[benefit]**
- **Role**: who is asking for this
- **Goal**: what they want to do
- **Benefit**: why it matters to them
（右图："The User Story Template" 插画：ROLE / GOAL / BENEFIT）

🇨🇳 另一种表述：作为 **[角色]**，我想要 **[目标]**，以便 **[收益]**。角色——谁在提这个需求；目标——他们想做什么；收益——为什么对他们重要。

💬 **讲师补充**
- 有人用略微不同的说法：**Role、Goal、Benefit——可以记成 RGB**；另一种是三个 W。**lab 里会用这一页**。

---

### 38 · User Stories – Examples

![](images/38_user_story_examples.jpg)

- Example:
  - As an **online shopper**, I want to **add an item to my cart**, so that **I can purchase it**
  - As a **group member**, I want to **record an expense**, so that **my group knows who paid**

🇨🇳 示例：
- 作为 **网购用户**，我想 **把商品加入购物车**，以便 **购买它**
- 作为 **小组成员**，我想 **记录一笔开销**，以便 **组里知道谁付了钱**

💬 **讲师补充**
- 第一个例子非常简单清晰。读了它你就能实现功能并确保帮用户完成结账购买——**如果只说"要加入购物车"而不说为什么，我不知道他也许只是想存到心愿单**。知道目的才能做对。
- **你们的项目是一个分摊开销的应用（expense splitter）**，第二个例子就来自它。注意它很 **具体**：不是"作为用户"，而是"作为共享开销的小组里的成员"；只说了一件想做的事；以及价值是什么。

---

### 39 · Writing Good User Stories (INVEST)

![](images/39_writing_good_user_stories_invest.jpg)

- **I**ndependent: can be worked on without waiting on another story
- **N**egotiable: details can be discussed, not fixed in stone
- **V**aluable: delivers real value to a user
- **E**stimable: the team can size it
- **S**mall: fits comfortably in one sprint
- **T**estable: has a clear way to verify it's done

agilealliance.org/glossary/invest/

🇨🇳 写好用户故事的标准（INVEST）
- **独立**：不用等别的故事就能开工
- **可协商**：细节可以讨论，不是铁板一块
- **有价值**：给用户带来真实价值
- **可估算**：团队能估出大小
- **小**：一个 Sprint 内轻松完成
- **可测试**：有明确的方法验证是否完成

💬 **讲师补充**
- 学生写用户故事的 **常见错误**：（1）太泛——写"作为用户"，不说是系统管理员、学生还是什么角色；要 **具体**；（2）"我需要用这个和这个和那个来搜索"——堆了太多东西，把事情复杂化；要简单清晰。
- INVEST 是衡量用户故事好坏的一种方法：可估算指知道大概要多少时间；可测试指完成时能验证，不是开放式任务。

---

### 40 · Your Turn – What do you think of this User Story?

![](images/40_your_turn_user_story.jpg)

**Your Turn – What do you think of this User Story?**
> I want to cover the expense when I join a group activity and store that in the databased persistently

🇨🇳 轮到你：这条用户故事写得怎么样？"我想在参加小组活动时承担费用，并把它持久化存进数据库。"

💬 **讲师补充**
- 讲师问：如果你的队友写了这条，而你要去实现它，你觉得怎么样？缺了什么？**学生答：角色（the role）。** 讲师：很好，没有角色。

---

### 41 · Poor vs Good User Story

![](images/41_poor_vs_good_user_story.jpg)

> I want to cover the expense when I join a group activity and store that in the databased persistently
- Poor User Story: vague, no role, no value stated, technical implementation, other?

> As a group member, I want to split an expense unevenly, so that the split matches how group members shared the expense
- A better User Story: specific, testable, and tied to a real need

🇨🇳 差的 vs 好的用户故事
- 差：含糊；没有角色；没说价值；混进了技术实现（存数据库）；还有别的吗？
- 好："作为小组成员，我想不均等地拆分一笔开销，以便拆分结果与成员实际分摊方式一致"——具体、可测试、对应真实需求

💬 **讲师补充**
- 那条差的故事只说了想做什么，却在谈 **数据库**——用户故事是用 **高层、非技术** 的语言写的，和你协作的业务人员也应该能看懂，不需要去想"数据库是指什么"。（"databased" 是幻灯片上的笔误。）
- 你需要 **评估** 自己的用户故事好不好。好的那条：没有混杂，我能为它定义测试用例，它对应真实需求，用户是谁很清楚。

---

### 42 · Acceptance Criteria

![](images/42_acceptance_criteria.jpg)

- **Acceptance criteria (*satisfaction conditions*)**, provide a detailed scope of end users requirements
- Help the development team understand the **value of the user story** and **set expectations** as to when a team should consider something **done**
- Acceptance Criteria Goals
  - **clarify** what the team should **build** before they start
  - **ensure** everyone has a **common understanding** of the **functionality**
  - help the team members know **when the story is complete**
  - help **verify** the expected behaviour via automated tests

🇨🇳 验收标准（满足条件）：细化最终用户需求的范围
- 帮助开发团队理解 **用户故事的价值**，并 **设定预期**——什么时候可以认为 **完成**
- 目的：开工前 **说清要做什么**；确保所有人对功能有 **共同理解**；让成员知道 **故事何时算完成**；通过自动化测试 **验证** 预期行为

💬 **讲师补充**
- 验收标准回答"怎么评估这个用户故事做完了/完成了"。需求可能是开放的，不设一组标准就会一直有悬而未决的问题。
- 在敏捷里这尤其重要：Sprint 有固定时间，必须能衡量"我们完成了"。
- 后面讲 **CI/CD（持续集成/持续交付）** 时，**测试是关键**——每个实现的功能都要测试。所以要定义一组标准，并 **把这些标准变成测试用例**。

---

### 43 · Acceptance Criteria (cont'd)

![](images/43_acceptance_criteria_should_include.jpg)

Acceptance criteria should include:
- **Negative** scenarios of the functionality
- **Functional** and **non-functional** use cases
- **Performance** concerns and guidelines
- What the system/feature intends to do
- **User experience** aspects

🇨🇳 验收标准应包含：功能的 **反面场景**；**功能性与非功能性** 用例；**性能** 要求与准则；系统/功能要做什么；**用户体验** 方面。

💬 **讲师补充**
- 学过测试的话，不只考虑正常情况，还要考虑异常情况：**反面场景**——输入不符合预期怎么办？应该输入数字却输入了字符串，功能要能处理。
- **非功能性**：用户能登录，但花了 3 分钟，可以接受吗？不行——功能上能登录，但时间太长，不能算完成；时间是非功能需求。
- 性能总会出现；**用户体验**：用户能完成操作，但界面不直观、花了很久才弄明白怎么做——这些都是判断功能是否"完成"时要考虑的常见方面。

---

### 44 · Acceptance Criteria (cont'd) — Example

![](images/44_acceptance_criteria_example.jpg)

Example:
- As an online banking customer, I want a strong password, so that my credit card information is secure

Acceptance Criteria:
- The password must be at least eight (8) characters
- The password must contain at least one character from each of the following groups:
  - lower case alphabet
  - upper case alphabet
  - digit
  - special characters (!, @, #, $, %, ^, &, *)

🇨🇳 示例：作为网上银行客户，我想要一个强密码，以便我的信用卡信息安全。验收标准：至少 8 个字符；必须包含以下每组至少一个字符——小写字母、大写字母、数字、特殊字符。

💬 **讲师补充**
- 注意角色很具体："网上银行客户"。什么叫强密码？要定义规则，确保用户创建密码时遵循这些规则。
- 测试这个功能时，要 **测试这些规则的组合**。

---

### 45 · User Stories（小结）

![](images/45_user_stories_tips.jpg)

- Keep them short
- Keep them simple
- Write them from the **user perspective**
- Make the **value/benefit** of the story clear
- Describe only **one piece of functionality**
- Write stories as a **team**
- Use **acceptance criteria** to show a **Minimum Viable Product (MVP)**, that is, is a **working** and **usable** product

🇨🇳 用户故事小结：写短；写简单；从 **用户视角** 写；把 **价值/收益** 写清楚；只描述 **一个功能**；**团队一起写**；用 **验收标准** 界定 **最小可行产品（MVP）**——一个能工作、能用的产品。

💬 **讲师补充**
- 讲师问在进入最后一部分（计划、估算与监控）之前有没有问题；没有。

---

### 46 · Scrum – Planning, Estimation, and Monitoring

![](images/46_section_planning_estimation_monitoring.jpg)

**Scrum – Planning, Estimation, and Monitoring**（章节页）

🇨🇳 章节：Scrum——计划、估算与监控（本讲最后一部分）。

---

### 47 · Scrum – Planning and Iteration Estimation

![](images/47_planning_and_iteration_estimation.jpg)

- PO works with the customer to set the **priority of PB items**
- In an iteration, the team divides the PB items into **individual tasks**
- The dev. team **defines tasks and estimates the size/effort** for each item
  - Product Owner/customers are not allowed to change the estimates
- The list of tasks is flexible
- Dev. team tracks all "tasks" on a Task Board (To Do, in-progress, Done)
- Dev. team tracks progress with a burn-down chart

🇨🇳 Scrum——计划与迭代估算
- PO 与客户一起设定 **PB 条目的优先级**
- 每个迭代里，团队把 PB 条目拆成 **具体任务**
- 开发团队 **定义任务并估算每项的大小/工作量**；PO 和客户 **不能改估算**
- 任务列表是灵活的
- 开发团队在任务板上跟踪所有任务（待办/进行中/完成）
- 开发团队用燃尽图跟踪进度

💬 **讲师补充**
- PO 挑出下个 Sprint 优先实现的条目后，团队可能把一个用户故事拆成子任务。例子：登录功能——（1）做前端界面让用户输入信息；（2）做后端存储信息并验证用户；（3）把两者集成。三个子任务实现一个功能。
- 拆完就要想：选了这个故事和这些子任务，**要花多长时间/多少精力**？

---

### 48 · Estimation – Size of User Story

![](images/48_estimation_size_of_user_story.jpg)

- **Ideal days**
  - The amount of time a user story will take to develop
  - Express the estimate as a whole (i.e., 2 ideal days)
- **Story points**
  - Metric for the size of a user story, feature, or other piece of work
  - A point value to each item is assigned
  - Estimation scale:
    - *Fibonacci series*; 1, 2, 3, 5, 8, …
    - *Subsequent number as twice the number that precedes it*: 1, 2, 4, 8, …

🇨🇳 估算——用户故事的大小
- **理想天数**：开发一个用户故事需要的时间；用整数表示（如 2 个理想天）
- **故事点**：衡量用户故事/功能/工作 **大小** 的指标；给每个条目一个点数；刻度：**斐波那契数列** 1, 2, 3, 5, 8, …；或 **每次翻倍** 1, 2, 4, 8, …

💬 **讲师补充**
- 估算的做法和以前不太一样。有人说"这个功能我要两天"——**两天怎么算？** 10 小时？24 小时？48 小时？很含糊。一天 8 小时工作，有 1 小时午餐不算；被人打断、回邮件、处理紧急问题的时间也不算。所以要说 **理想天数**：真正花在上面、不含干扰的时间。
- 这仍然比较复杂。更便于跟踪进度的是 **故事点**：给每个故事一个数字表示它的 **大小**，这个数字帮团队估算一个 Sprint 能完成多少故事/多少点。**它是估算，永远不会 100% 准确。**
- 常用斐波那契数列（1 是能做的最小的事）；或者后一个数是前一个的两倍——大小逐级增大。

---

### 49 · Estimation Technique – Planning Poker

![](images/49_estimation_planning_poker.jpg)

- Gamified technique to estimate effort/relative size of development in Agile development
- Agile teams to estimate is by playing planning poker

**Agile Estimating and Planning: Planning Poker - Mike Cohn**（视频链接）

🇨🇳 估算技巧——计划扑克：一种游戏化的技术，用来估算敏捷开发中的工作量/相对大小；敏捷团队通过"打扑克"来估算。参考：Mike Cohn 的 Planning Poker 视频。

💬 **讲师补充**
- 课上没时间展开，**视频链接在幻灯片上（幻灯片已放到 Moodle）**，请课后看，它用很好的例子解释了真实团队怎么做。
- 做法：团队成员讨论每个用户故事该给多少故事点，**人人参与但互不影响**——每个人先自己想，然后像出牌一样同时亮出数字。有人说 3、有人说 8，就讨论"为什么你觉得是 8？"——"这个要做很多测试、还要搭数据库"——"哦我没想到，那再想想"。再想、再亮牌，直到达成一致。
- 这样每个人都参与决定估算，并决定按大小下个 Sprint 该做什么——**不是项目经理或某个人独断**。

---

### 50 · Sprint Planning – Story Points

![](images/50_sprint_planning_story_points.jpg)

- Start with the most valuable user stories from the product backlog
- Take a story in that list (ideally the smallest one)
- Discuss with the team whether that estimate is accurate
- Keep going through the stories until the team have accumulated enough points to fill the Sprint

🇨🇳 Sprint 计划——用故事点
- 从 PB 里最有价值的用户故事开始
- 取其中一条（最好是最小的一条）作为基准
- 和团队讨论这个估算准不准
- 一条条过下去，直到累计的点数填满一个 Sprint

---

### 51 · User Story Estimation – T-Shirt Sizing Method

![](images/51_estimation_tshirt_sizing.jpg)

- Uses sizes: **XS, S, M, L, XL**
- **Simple, fast, and beginner-friendly**
- No false precision; good for early-stage teams
- This course's **standard method** for story point examples

atlassian.com/agile/project-management/estimation

🇨🇳 用户故事估算——T 恤尺码法
- 用尺码 **XS、S、M、L、XL**
- **简单、快、适合新手**
- 不会造成"精确"的假象；适合早期团队
- **本课程用于故事点示例的标准方法**

💬 **讲师补充**
- 另一种常见、易于理解的方式：说这个故事是 XS/S/M/L/XL。通常也会给每个尺码对应一个数字，这样 S 和 L 就有区别。
- 这些数字的意义在于 **之后跟踪进度**："我们推进了多少"——马上会讲为什么重要。

---

### 52 · Example: A Complete User Story

![](images/52_example_complete_user_story.jpg)

- **Story**: As a group member, I want to record an expense with a payer, amount, and split, so that the group knows what everyone owes
- **Acceptance criteria**:
  - Expense has a payer, an amount, and a split method
  - Equal split divides the amount evenly across all members
  - Custom split allows entering each member's share
  - Amounts that don't divide evenly are handled without losing or gaining money
- **Story point**: size-M
- In GitLab: one Issue, four Tasks for the criteria, `size-M` label, assigned to the Sprint 1 milestone

🇨🇳 示例：一个完整的用户故事
- **故事**：作为小组成员，我想记录一笔开销（付款人、金额、分摊方式），以便组里知道每个人欠多少
- **验收标准**：开销有付款人、金额和分摊方式；均分把金额平均分给所有成员；自定义分摊允许输入每人份额；除不尽的金额要处理好，不多不少
- **故事点**：size-M
- **在 GitLab 里**：一个 Issue，四个 Task 对应四条验收标准，打 `size-M` 标签，挂到 Sprint 1 milestone

💬 **讲师补充**
- 基于用户故事和验收标准，团队一起决定它是 M 号。估算是团队一起做的，用来决定我们能做多少——**记住它只是估算**。

---

### 53 · Summary of Scrum

![](images/53_summary_of_scrum.jpg)

**Summary of Scrum**（图：*Agile Software Development with Scrum*, Ken Schwaber & Mike Beedle）
- Product backlog → prioritized list of product features – based on customer input → this could be the "current working view of the release"
- Backlog item(s) selected for current Sprint → team defines and estimates the tasks
- Sprint: a 30-day iteration (**2 to 4 weeks**) · should deliver some working code · may deliver documents and models
- Scrum: 15 minute daily meeting. Team members answer three basic questions: what did I do in the last 24 hours? what are the obstacles? what will I do in the next 24 hours?
- New functionality demonstrated at the end of every Sprint – customers should give feedback

🇨🇳 Scrum 总览图：Product Backlog（按客户输入排好优先级的功能列表）→ 选出本 Sprint 的条目，团队定义并估算任务 → 一个 2–4 周的 Sprint，每 24 小时一次 15 分钟站会（三个问题）→ Sprint 结束演示新功能，客户给反馈。

💬 **讲师补充**
- 把所有东西放在一起的快速总结：所有要做的功能按优先级排好；挑出条目进入下个 Sprint 并拆成子任务；2–4 周一个 Sprint（你们是 2 周）；每 24 小时一次站会；Sprint 结束有新功能，要评审、要回顾。

---

### 54 · Scrum – Tracking and Monitoring Progress

![](images/54_section_tracking_monitoring_progress.jpg)

**Scrum – Tracking and Monitoring Progress** — Burndown chart, Velocity, The Sprint/Task board（章节页）

🇨🇳 章节：Scrum——跟踪与监控进度：燃尽图、速度（velocity）、Sprint/任务板。

---

### 55 · Planning – Running a Sprint Using SPs, Tasks, and a Task Board

![](images/55_running_a_sprint_sps_tasks_taskboard.jpg)

**First half** of the Sprint planning
- Story points and velocity to figure out what will go into the Sprint

**Second half** of the Sprint planning
- Plan out the actual work for the team is to add cards for individual tasks
- Tasks can be written code, create design and architecture, and all those other things that teams really do every day to build and release software

🇨🇳 计划——用故事点、任务和任务板跑一个 Sprint
- **计划会前半段**：用故事点和速度决定本 Sprint 放什么
- **后半段**：规划实际工作——为每个任务加卡片；任务可以是写代码、做设计和架构，以及团队为构建和发布软件每天真正要做的一切

💬 **讲师补充**
- 计划时要给用户故事分配故事点，并弄清 **团队能做多少**。

---

### 56 · Burndown Charts

![](images/56_burndown_charts.jpg)

- Tracks the completion of development work throughout the Sprint;
- Should be visible to everyone in the team (e.g., whiteboard, wall chart, online tool)
- First half of the Sprint planning
  - Story points and velocity to figure out what will go into the Sprint
- Good estimation and planning should help the team to burn stories relatively with similar pace

🇨🇳 燃尽图
- 跟踪整个 Sprint 期间开发工作的完成情况
- 对团队所有人可见（白板、墙图、在线工具）
- 计划会前半段用故事点和速度决定 Sprint 内容
- 好的估算和计划能让团队以相对均匀的节奏"烧掉"故事

💬 **讲师补充**
- 燃尽图是帮团队跟踪和监控进度的一种方式，依赖你定义的故事点。

---

### 57 · Burndown Charts based on Story Points

![](images/57_burndown_chart_story_points.jpg)

（图：纵轴 story points 0–27，横轴 day 0–day 30；灰色斜线为 **Ideal burndown**；实际折线从 24 点出发，约第 5 天降到 17 点）
*Two stories worth 7 points burned off*

🇨🇳 基于故事点的燃尽图：两个故事共 7 点被"烧掉"。

💬 **讲师补充**
- 例子是 30 天（4 周）的 Sprint。纵轴是故事点：假设本 Sprint 选的用户故事故事点总和是 24。随着推进，完成并测试了一些故事，就把剩余点数往下减：图里大约 5 天完成两个故事、烧掉 7 点。
- 理想情况是沿着理想线 **在结束时降到零**；但现实不会那么理想——因为我们在 **估算**，没人确切知道能做多少。**如果没按计划走，不要觉得糟糕**，你在估算、在学习。有些用户故事可能会延到下个 Sprint。

---

### 58 · Estimating Progress – Velocity

![](images/58_estimating_progress_velocity.jpg)

- A measure of a team's rate of progress
- Sum the number of story points assigned to each user story that the team completed during the iteration

Example:
- A team completed 3 stories, 5 SPs each → velocity = 15

🇨🇳 进度估计——速度（velocity）：衡量团队推进速率；= 本迭代内团队 **完成** 的用户故事的故事点之和。例：完成 3 个故事，每个 5 点 → 速度 = 15。

💬 **讲师补充**
- 燃尽图看的是 **一个 Sprint 内** 故事点的燃烧；速度看的是 **团队每个 Sprint 能完成多少故事点**。

---

### 59 · Tools for Tracking Progress

![](images/59_section_tools_for_tracking_progress.jpg)

**Tools for Tracking Progress** — Burndown chart, The Task board（章节页）

🇨🇳 章节：跟踪进度的工具——燃尽图、任务板。

---

### 60 · Tool Support for Agile SW Development

![](images/60_tool_support_jira.jpg)

- **JIRA** is a software tool for planning, tracking and managing software development
  - Supports different agile methodologies including Scrum and Kanban
- Jira supports Scrum Sprint planning, stand ups (daily scrums), Sprints and retrospectives
- Including backlog management, project and issue tracking, agile reporting
  - E.g., Burndown and velocity charts, Sprint report
- Scrum boards visualize all the work in a given Sprint

https://www.atlassian.com/software/jira/agile

🇨🇳 敏捷开发的工具支持：**Jira** 是用于计划、跟踪和管理软件开发的工具；支持 Scrum 和看板等；支持 Sprint 计划、站会、Sprint、回顾；包括 Backlog 管理、项目与问题跟踪、敏捷报表（燃尽图、速度图、Sprint 报告）；Scrum 看板可视化一个 Sprint 内的所有工作。

💬 **讲师补充**
- 有工具帮你实施敏捷——站会、跟踪监控、燃尽图、速度、Sprint 任务板等；Jira 是其中之一。
- **本课程简化处理：用 GitLab**，不会深入所有工具，给你们选择的自由。**Capstone 项目用 Jira** 并把很多东西集成在一起。
- 工具的意义是让生活轻松，而不是用 Excel 表格手工做这些。

---

### 61 · Jira Agile – Scrum Board

![](images/61_jira_scrum_board.jpg)

**Jira Agile – Scrum Board**（Jira 看板截图：To Do / In Progress / Done 列，卡片带标签与负责人）
https://www.atlassian.com/software/jira/agile

🇨🇳 Jira 的 Scrum 看板。

💬 **讲师补充**
- 在 Jira 里可以建 Sprint/Scrum 看板，就是前面说的 to do / in progress / done。**有些团队会再加一列 "Code Review"**：在说"完成"之前必须有人审查代码，作为质量保证——这是开发团队的 **最佳实践**。
- 看板显示谁做了什么、进度如何，并用颜色区分；工具里还有更多功能，甚至可以记录站会。

---

### 62 · Jira Agile – Sprint Planning

![](images/62_jira_sprint_planning.jpg)

**Jira Agile – Sprint Planning**（Jira Backlog 视图截图：上方为当前 Sprint 的条目，下方为 Backlog）
https://www.atlassian.com/software/jira/agile

🇨🇳 Jira 里的 Sprint 计划界面。

💬 **讲师补充**
- 可以做 Sprint 计划："Sprint 2 我们选了这些条目/任务"；Product Backlog 显示所有要实现的任务或功能。它把一切记录下来并可视化，你不用自己手工维护。

---

### 63 · Burndown Charts（Jira）

![](images/63_jira_burndown_chart.jpg)

- "**Burndown**" chart tracks the amount of estimated effort remaining in a sprint
  - Maintained daily by the Scrum Master
- ① estimation in story points（纵轴）· ② amount of work left（红线）· ③ Guideline; ideal progress（灰线）

https://www.atlassian.com/agile/tutorials/burndown-charts

🇨🇳 燃尽图跟踪 Sprint 内剩余的估算工作量，由 SM 每日维护。① 纵轴：故事点估算；② 红线：剩余工作量；③ 灰线：理想进度参考线。

💬 **讲师补充**
- 用工具的话燃尽图是 **自动** 的：有人把故事从 to do 移到 done，工具就扣掉相应点数并画到图上，不用手工做。

---

### 64 · Velocity Chart

![](images/64_jira_velocity_chart.jpg)

- *Velocity* tracks the amount of work from Sprint to Sprint
  - Velocity chart graphically shows project/team's velocity
（图：Sprint 1–5 的柱状图，蓝色 = Commitment，绿色 = Work completed）
https://confluence.atlassian.com/jirasoftwareserver/velocity-chart-938845700.html

🇨🇳 速度图：跟踪各 Sprint 之间的工作量；图形化显示项目/团队的速度。蓝色 = 承诺，绿色 = 实际完成。

💬 **讲师补充**
- 每个 Sprint 完成了多少故事点：**绿色是完成的，蓝色是承诺的**。Sprint 1 估计约 17 点，完成 17——完美；Sprint 2 比较激进，估了约 20，完成不到 15。
- 速度显示承诺了多少、完成了多少，衡量团队推进情况。重要的是 **不要一个 Sprint 做很少、另一个做太多**——回想原则里的 **匀速开发**，要保持一致；忽多忽少不是健康的信号。

---

### 65 · Version Control – Remote Collaboration

![](images/65_section_version_control_remote.jpg)

**Version Control – Remote Collaboration** — Git / GitLab Collaboration (revisit)（章节页）

🇨🇳 章节：版本控制——远程协作（Git/GitLab 回顾）。

---

### 66 · Version Control – Local and Remote（本地）

![](images/66_version_control_local.jpg)

**YOUR MACHINE**: working directory → (`git add`) → staging area → (`git commit`) → local repo
LOCAL MACHINE

🇨🇳 本地：工作目录 →（git add）→ 暂存区 →（git commit）→ 本地仓库。

💬 **讲师补充**
- 上周讲过：在本地机器上改东西，改动在 **工作目录**；想加到 **暂存区** 用 `add`；想提交暂存区的改动，用 `commit`，它进入 **本地仓库**——在你的机器上，不在远程。

---

### 67 · Version Control – Local and Remote（加上 GitLab）

![](images/67_version_control_local_and_remote.jpg)

**YOUR MACHINE**: working directory → `git add` → staging area → `git commit` → local repo
**GITLAB**: remote repo ← `git push` / → `git pull`

🇨🇳 本地 + 远程：本地仓库 → git push → GitLab 远程仓库；git pull 把远程改动拉回本地。

💬 **讲师补充**
- 团队协作时多一步：我在本地完成了改动（实现了功能或修了 bug），就 **push** 到 GitLab 上的主仓库，所有人都能看到——改动不再只在我的机器上。这是你们会经常经历的最重要场景之一。

---

### 68 · Version Control – Branching and Merging

![](images/68_version_control_branching_merging.jpg)

（图：绿色 **Master** 主线；蓝色 **Your Work** 分支三个提交后合并回主线；橙色 **Someone Else's Work** 分支一个提交后合并回主线）
A branch lets you work on the same files without disturbing each other.
(The diagram says `Master`; in our repositories, that branch is called `main`.)

🇨🇳 分支与合并：分支让你和队友修改同一批文件而互不干扰。（图里叫 Master，我们的仓库里这个分支叫 `main`。）

💬 **讲师补充**
- 每个人在软件的某个版本上工作：你可以 **建分支**，把工作拿到本地实现改动并本地提交——每次提交产生一个版本，发现出错可以回到之前的版本。
- 做完、测完了，就把分支 **合并（merge）** 到 main/master，把你的改动和别人的改动合在一起。
- 分支是 **并行** 发生的，合并时会变复杂。讲 **CI/CD** 时会学习帮团队处理这些情况的实践和场景，避免陷入过于复杂的修复。版本控制是来帮你的：push 后发现问题，可以回退、修好再 push/merge。

---

### 69 · References

![](images/69_references.jpg)

- Andrew Stellman, Margaret C. L. Greene 2014. *Learning Agile: Understanding Scrum, XP, Lean and Kanban* (1st Edition). O'Reilly, CA, USA.
- Ian Sommerville. 2016. *Software Engineering* (10th ed.) Global Edition. Pearson, Essex England
- Agile Alliance. https://agilealliance.org/
- Agile Manifesto: https://agilemanifesto.org/
- Atlassian Tutorials. https://www.atlassian.com/agile/tutorials/

🇨🇳 参考文献（讲师特别推荐第一本 *Learning Agile*，讲义大量内容取自此书）。

---

### 70 · Thank you!

![](images/70_thank_you.jpg)

**Thank you!**

💬 **讲师补充（结束语与课后问答）**
- 希望已经覆盖了做 Scrum 开发需要的大部分重要内容；有问题可以下来聊。
- **课后问答**
  - 学生问：**作业（assignment）信息什么时候出？** 讲师：正在修改中，很快会发；本周先把大家安排进团队、把项目启动起来，计划本周把最终版整理出来。
  - 学生问：**有期末考试吗？** 讲师：**没有期末考试，全部是项目作业（all project work）。**

---

## 📋 本周待办清单

1. **完成组队**：本周内确保自己在一个团队里；队伍有空位的会由 tutor 直接分配成员。（换到线上 tutorial 的同学，邮件联系负责该 lab 的 tutor Daniel 加入线上组。）
2. **在组内确定 Scrum 角色**：一名 **Product Owner**、一名 **Scrum Master**，其余为开发团队；**不要设"项目经理"或"team lead"**。
3. **按 Scrum 事件跑 Sprint（2 周一个）**：Sprint 计划会（两部分）、每日站会（15 分钟、三个问题、不解决问题）、开发、Sprint 评审（演示）、回顾（两个问题、四列表格）——**每个事件都要留下记录**，评分会检查是否按 Scrum 正确执行。
4. **写需求用 User Story**：格式 *As a [role], I want [goal], so that [benefit]*；角色要具体、一条只写一件事、不写技术实现；用 **INVEST** 自查；每条配 **验收标准**（含反面场景、非功能/性能、用户体验），并能转成测试用例。
5. **估算用 T 恤尺码**（本课程标准）：在 GitLab 里 **一个 Issue = 一个用户故事**，验收标准拆成 Tasks，打 `size-S/M/L` 标签，挂到对应 Sprint milestone；维护 To Do / In Progress / Done 看板，Sprint 中持续更新。
6. **课后观看 Planning Poker 视频**（幻灯片 49 上的链接，讲义已放 Moodle）。
7. **Git 协作复习**：working directory → add → staging → commit → local repo → push 到 GitLab；开分支做功能，测完再 merge 回 `main`。
8. 记住：**Sprint 1 有脚手架，Sprint 2 起由团队自己定义需求、自己主导**；**没有期末考试，全部为项目评估**；作业细则本周发布。
9. 延伸阅读：*Learning Agile*（Stellman & Greene），Agile Manifesto / Agile Alliance / Atlassian tutorials。
