# COMP9820 Week 3 · 课件整理：Agile Software Architecture and Design for Web Applications

**Lecture 3 · Dr. Basem Suleiman · School of Computer Science and Engineering (CSE), UNSW**
视频：https://youtu.be/IP4fX4hrbzc · 讲义 PDF：`COMP9820_W3_Software_Design_Architecture_Agile_Web_Dev.pdf`（67 页）

> 体例说明
> - 每一页按课上实际放映顺序编号，标题 `### NN · <幻灯片标题>`；正文先给英文原文，`🇨🇳` 为中文翻译，`💬 讲师补充` 为讲师口头讲的、幻灯片上没有的内容（含课堂问答）。
> - 图片由讲义 PDF 渲染（1280×720），比 360p 录像清晰；放映顺序以录像为准。
> - PDF 的 67 页里有 **7 页课上没有放映**（4 张章节过渡页、以及 3 页附录：Event-driven and serverless patterns、Design for non-functional properties、How do we choose an architecture?），放在文末「课上未放映的页面」一节。
> - 自动字幕的常见识别错误已按语义还原（"AI / A I"→API、"design buttons / bets / baton"→design patterns、"bot / bots"→part / parts、"mood"→Moodle、"print"→sprint、"equality"→quality、"biral"→Bidjigal、"ALB"→ELP、"beer evaluation"→peer evaluation、"Xins"→expense、"rooted"→routed、"law cumbling"→low coupling、"civil organizing"→self-organizing）。

---

## 开场（幻灯片之前）

💬 **讲师补充**
- 前两周大家已经进了团队、看到了项目的全貌。**Sprint 1 项目评估的公告已经在 Moodle 发布**，细则在 Moodle 上，今天课的最后会快速介绍。
- 上周讲的 Scrum（敏捷计划、按规则做开发、更新工件、监控进度）正是 Sprint 1 要用的流程：计划 → 构建 → 监控 → 调整。
- 今天换一个话题：**软件架构与软件设计**，特别是 Web 应用的语境——因为你们做的就是 Web 应用。讲师会根据项目进度调整各周内容，保证关键主题在你们需要的那一周讲到。

---

### 01 · COMP9820 Software Project Management — Agile Software Architecture and Design for Web Applications

![](images/01_title.jpg)

**COMP9820 Software Project Management**
Agile Software Architecture and Design for Web Applications
Dr. Basem Suleiman · School of Computer Science and Engineering (CSE)

🇨🇳 COMP9820 软件项目管理——面向 Web 应用的敏捷软件架构与设计。

---

### 02 · Acknowledgement of Country

![](images/02_acknowledgement.jpg)

"I acknowledge the Bidjigal as the Traditional Custodians of the land we are meeting on today. I pay my respects to Elders past and present and recognise the enduring connection of Aboriginal and Torres Strait Islander peoples to Country. I invite us all to reflect on our shared responsibility to honour and respect this land and its stories."

🇨🇳 国土致谢：承认 Bidjigal 人是我们今天所在土地的传统守护者，向过去和现在的长者致敬，并认可原住民与托雷斯海峡岛民与这片土地的长久联系。

---

### 03 · Outline

![](images/03_outline.jpg)

- Key Principles: Software Architecture and Design
- How engineers think about and communicate design
- Agile design: connecting principles to architecture
- Web application components: front end, API, back end and data
- Design principles for non-functional requirements / qualities
- Typical Software Architectural Patterns
- Design decisions within Scrum and CI/CD
- Architecture and design choices and its implications
- Project Work – Sprint 1 Assessment

🇨🇳 本讲大纲
- 核心原则：软件架构与设计
- 工程师怎么思考设计、怎么沟通设计
- 敏捷设计：把原则连到架构上
- Web 应用的组成：前端、API、后端、数据
- 面向非功能需求 / 质量属性的设计原则
- 常见软件架构模式
- Scrum 与 CI/CD 里的设计决策
- 架构与设计选择及其影响
- 项目：Sprint 1 评估

💬 **讲师补充**
- 今天内容很满。这个主题本身可以是一门完整的课（如何设计和架构应用），今天的目标只是让大家 **接触到这些重要概念**，在你们开始搭建应用时建立理解。
- **讲师明确说：不指望你们在项目里大量应用这些内容**——本课程的范围是每个 Sprint 逐步覆盖一些重点。但希望大家带着今天学到的东西，在搭建应用时去思考和反思，为 **capstone 项目 COMP9900** 打基础：在 9900 里，设计与架构是评估的很大一部分（proposal 里有、final report 里有、谈"技术卓越性"时也有）。所以提前在 9820 里讲，而不是等到 9900。
- **这部分内容在 Sprint 1 不会被评估，讲师说 Sprint 2、3 应该也不会。**

---

### 04 · Software architecture, design and patterns

![](images/04_arch_design_patterns.jpg)

Different levels of the same reasoning process

| Architecture | Application design | Design patterns | Implementation |
|---|---|---|---|
| Major parts of the system and their relationships. | Responsibilities, modules, interfaces and dependencies. | Reusable structures for recurring design problems. | Functions, classes, data structures, code and tests. |

The boundary is not rigid.
Architecture focuses on the decisions that are expensive or risky to change later. Design continues inside those architectural boundaries.

🇨🇳 软件架构、设计与模式：同一个推理过程的不同层级

| 架构 | 应用设计 | 设计模式 | 实现 |
|---|---|---|---|
| 系统的主要部分及其关系 | 职责、模块、接口和依赖 | 针对反复出现的设计问题的可复用结构 | 函数、类、数据结构、代码和测试 |

边界不是死的。架构关注的是"以后改起来很贵或风险很大"的决定；设计在架构定下的边界里继续。

💬 **讲师补充**
- **区分架构和设计很重要。** 架构是应用的"最大蓝图 / 路线图"——就像盖楼先有建筑结构，再往里填细节。软件架构 = 系统的主要部分（边界）及其关系，是最高层的抽象。
- 关键词是 **抽象层级** 和 **推理过程**：做设计和架构时我们在做决定，这些决定影响应用的未来——怎么演进、多容易测试、多容易维护。架构看最高层，然后逐步"放大"聚焦到某些方面，这时就进入设计：有哪些职责、模块、接口、依赖。比如要实现一个用户故事，先想它涉及哪些职责 / 功能，再把它们分组成模块，有的要有接口让别的模块来调用……这就是从架构走向设计。
- **设计模式**：多年来开发者在设计应用时反复遇到相同的问题，比如 **安全登录 / 认证**——几乎每个应用都有，设计和实现的思路也都一样，不需要重新发明轮子。设计模式就是针对这类重复问题的可复用结构和指南。
- **实现** 是最底层：函数、类、数据结构、代码，还有测试用例。
- **架构和设计的核心是"决策"，不只是画图。** 图背后的决定才重要：为什么这样拆职责、为什么这样连接。
- 一开始定下的架构和设计会一直跟着你，直到整个应用需要彻底重新设计。大公司常见：五年后发现当初的架构撑不住了。**Facebook 的例子**：信息流（往下滚动要无限加载更多内容）到了某个点，原有架构无法再扩展，不得不从根本上改架构。所以 **早期的大决策会跟很久——要做取舍、要有理由、要想清楚再大量写代码**。

---

### 05 · Design operates at different levels

![](images/05_design_levels.jpg)

- Architecture — Major parts and communication
- Application structure — Responsibilities and boundaries
- Component design — Interfaces and dependencies
- Implementation — Functions, classes and tests

Move between levels as needed. Do not start with code-level detail when the system boundary is unclear.

🇨🇳 设计在不同层级上进行
- 架构：主要部分及其通信
- 应用结构：职责与边界
- 组件设计：接口与依赖
- 实现：函数、类、测试

按需在层级间切换；系统边界还不清楚时，别从代码级细节开始。

💬 **讲师补充**
- 这页是换个角度再强调层级。架构层可以理解成 **"方框和线"**：方框是系统的主要组件，线是它们的通信。后面会看到不同架构风格的例子。
- 应用结构：把大组件拆成小组件，想清楚每个组件里有什么、谁负责什么、**边界到哪**——超出边界就要和另一个组件通信。组件设计：有了职责和组件，就需要 **接口** 让组件之间交互，于是产生了依赖。
- **建议自顶向下**：从代码开始很难看到最高层的抽象。从大图开始——我的主要部分是前端、后端，后端再拆子组件——比从代码开始容易。很多人习惯先写函数、类、测试，越写越多才开始想"怎么分组、怎么组织结构"，最后才到架构。**架构和设计的思考应该在需求之后就开始。**

---

### 06 · How software engineers think about design

![](images/06_engineers_think_questions.jpg)

- What problem are we solving?
- What must change later?
- What belongs together?
- What should stay separate?
- How will we test it?
- What could fail?

🇨🇳 软件工程师怎么思考设计——6 个问题
- 我们在解决什么问题？
- 以后什么必须会变？
- 什么应该放在一起？
- 什么应该分开？
- 我们怎么测试它？
- 什么可能失败？

💬 **讲师补充**
- 设计和架构 **看起来简单（画几个框几条线），实际上很难**——难在"怎么拆、怎么分"这些决定。这 6 个问题是给初学者的指引。
- **解决什么问题 / 应用领域**：有的应用就是普通的"登录、看数据、浏览、保存、购买"；有的是 **事件驱动** 的——事件触发时要有反应。这是两种不同类型的问题。
- **什么会变**：敏捷的核心原则之一就是拥抱变化。设计时要想：数据库会不会增长？业务逻辑会不会加更多规则？以后会不会加更多服务？知道哪些组件会增长 / 变化，从一开始就为变化设计，以后加服务、扩数据就容易。
- **什么放一起**：哪些类 / 组件有逻辑关系，应该放在一个模块里。
- **什么分开**：前端的例子——HTML 描述页面结构，样式作用于它；如果都放在一个文件里，改一个样式就要改整个 HTML 文件。分开之后更容易改、更容易理解，是多个小组件而不是一个复杂的大文件。
- **怎么测试**：回想用户故事——我们把需求定义得很小，就是为了能测试；"能测、能衡量进度"是好用户故事的标志。
- **什么可能失败**：可能把整个应用拖垮的东西是高风险组件 / 类，要有策略把它单独处理，不让它拖垮整个应用。

---

### 07 · Architecture diagrams support communication

![](images/07_architecture_diagrams.jpg)

| 1 Context | 2 Containers | 3 Components | 4 Flow |
|---|---|---|---|
| Who uses the system? | What applications and data stores exist? | What responsibilities sit inside an application? | How does a request move through the system? |

Tools: whiteboard • diagrams.net • Mermaid • PlantUML • C4-based tools

🇨🇳 架构图是用来沟通的

| 1 语境 | 2 容器 | 3 组件 | 4 流程 |
|---|---|---|---|
| 谁在用这个系统？ | 有哪些应用和数据存储？ | 一个应用内部有哪些职责？ | 一个请求怎么在系统里流转？ |

工具：白板、diagrams.net、Mermaid、PlantUML、基于 C4 的工具

💬 **讲师补充**
- **图不等于架构。** 图展示的是系统的主要组件和关系，但背后有推理：有人定义架构时特别强调它是 **一组设计决策**——为什么拆、为什么合、为什么通信是单向不是双向。
- 画架构图的价值是 **让沟通更容易**：只看源码文件很难理解全貌。语境图告诉我们谁在用（从浏览器？手机？别处？）；容器图是有哪些应用和数据存储；组件图是应用内部的职责；流程图是东西从哪个组件流向哪个组件、什么方向。
- 工具是为了提高效率，不要手画。但 **有人陷进工具里，花大量时间把图做得完美**——记住：决策才重要，图只是用来沟通主要组件、怎么划分、怎么交互，以及背后的决策。

---

### 08 · How software engineers think about design

![](images/08_engineers_think_from_need.jpg)

Start from a need, then assign responsibilities and boundaries

| User story | Responsibilities | Components | Interfaces | Quality checks |
|---|---|---|---|---|
| What value must we deliver? | What must the system do? | Where should each responsibility live? | How do components communicate? | Will it remain secure, testable and changeable? |

Example user story
*As a group member, I want to record an expense so that the group knows who paid and what everyone owes.*

🇨🇳 从需求出发，再分配职责和边界

| 用户故事 | 职责 | 组件 | 接口 | 质量检查 |
|---|---|---|---|---|
| 要交付什么价值？ | 系统必须做什么？ | 每个职责放在哪？ | 组件之间怎么通信？ | 是否仍然安全、可测试、可修改？ |

示例用户故事：作为群组成员，我想记录一笔开销，让大家知道谁付了钱、每人欠多少。

💬 **讲师补充**
- 这是在敏捷语境下的思考方式。用户故事已经把需求拆成了可以作为一个小单元实现的小功能，它说清了要交付什么、为什么对用户重要。
- 用户故事帮我们定义 **职责**——为了实现这个故事系统必须做什么，**通常不止一件事、不止一个函数**。然后决定每个职责住在哪个 **组件** 里；**接口** 是组件之间为实现这一个功能怎么通信；**质量检查** 是确保这样设计后仍然安全、性能没问题、容易测试和修改。

---

### 09 · FROM AGILE TO DESIGN – Class Activity

![](images/09_agile_to_design_activity.jpg)

What guides Agile teams in creating software architecture and design?

How does the Agile methodology approach software architecture and design?

🇨🇳 课堂活动：从敏捷到设计
- 什么在指导敏捷团队创建软件架构和设计？
- 敏捷方法论怎么对待软件架构和设计？

💬 **讲师补充**
- 讲师先只放第一个问题："你们团队采用 Scrum，是什么在指导你们做架构和设计？你们会学到设计与架构的知识、一些记法，但敏捷团队决定怎么做设计时，始终参照的是什么？"——课堂一时无人回答，讲师提示"我们讲敏捷时最先讲的是什么？"，然后放出第二个问题。
- 提示：敏捷没有唯一定义，有的是 **一组价值观和原则**，其中有些 **明确谈到了架构和设计**。于是回到下面两页复习。

---

### 10 · Agile Manifesto – Values

![](images/10_agile_manifesto_values.jpg)

- "We are uncovering better ways of developing software by doing it and helping others do it. Through this work we have come to value:"
  - Individuals and interactions over processes and tools
  - Working software over comprehensive documentation
  - Customer collaboration over contract negotiation
  - Responding to change over following a plan
- The items on the left are more valued than those at the right

Agile Manifesto: http://agilemanifesto.org/
© 2001, the above authors. This declaration may be freely copied in any form, but only in its entirety through this notice.

🇨🇳 敏捷宣言——4 条价值观
- "我们通过亲身实践并帮助他人，发现了更好的软件开发方式。通过这项工作我们认为："
  - 个体与互动 高于 流程与工具
  - 可工作的软件 高于 详尽的文档
  - 客户协作 高于 合同谈判
  - 响应变化 高于 遵循计划
- 左边的比右边的更有价值

💬 **讲师补充（课堂互动）**
- 讲师问：从这些价值观里能看出什么对设计和架构有帮助？
- **学生答：简单（simplicity）。** 讲师：很好——我们用简单的方式构建，目标是 **可工作的软件**，哪怕只做一点点功能。想设计架构时，不要从庞大复杂的架构开始，而是从一小组用户故事和功能开始。
- 讲师追问：**谁来做设计和架构？** 项目经理？Team lead？**学生答：软件架构师。** 讲师：对，团队里可能有经验丰富的架构师或资深工程师来 **牵头**（设计和架构需要经验），**但他们不会一个人做**——这就是"个体与互动高于流程与工具"：要很多人一起。谁是这些人？技术人员，加上 **带来业务领域知识的客户**。比如客户告诉你"我们的应用完全依赖事件——股票交易，一有事件就要买卖"，如果不早点、不定期和客户协作，就可能做错设计和架构决策（后面会讲事件驱动架构）。
- **响应变化**：我们不会一开始就花几周几个月做出"完美"的设计和架构，而是从某个起点开始，让它演进、成长——这是个复杂的过程，一次做不对，所以必须 **迭代、增量**。
- 讲师的提醒：**面试时或在业界带团队时**，被问到"你怎么看待设计和架构"，应该引用这 4 条价值观和 12 条原则。

---

### 11 · Agile Principles

![](images/11_agile_principles.jpg)

1. Our highest priority is to satisfy the customer through early and continuous delivery of valuable software.
2. Welcome changing requirements, even late in development. Agile processes harness change for the customer's competitive advantage.
3. Deliver working software frequently, from a couple of weeks to a couple of months, with a preference to the shorter timescale.
4. Business people and developers must work together daily throughout the project.
5. Build projects around motivated individuals. Give them the environment and support they need and trust them to get the job done.
6. The most efficient and effective method of conveying information to and within a development team is face-to-face conversation.
7. Working software is the primary measure of progress.
8. Agile processes promote sustainable development. The sponsors, developers, and users should be able to maintain a constant pace indefinitely.
9. Continuous attention to technical excellence and good design enhances agility.
10. Simplicity--the art of maximizing the amount of work not done--is essential.
11. The best architectures, requirements, and designs emerge from self-organizing teams.
12. At regular intervals, the team reflects on how to become more effective, then tunes and adjusts its behavior accordingly.

Agile Alliance: http://www.agilealliance.org

🇨🇳 敏捷 12 原则（与 Week 2 相同，略译）：1 尽早持续交付有价值的软件；2 欢迎需求变化；3 频繁交付可工作的软件；4 业务人员与开发者每天一起工作；5 围绕有动力的个体建设项目；6 面对面交流最有效；7 可工作的软件是衡量进度的首要标准；8 可持续的匀速开发；**9 持续关注技术卓越与好的设计，能增强敏捷性**；10 简单——最大化"不做的工作"的艺术；**11 最好的架构、需求和设计来自自组织团队**；12 定期反思并调整。

💬 **讲师补充（课堂互动）**
- 讲师问：12 条原则里哪些 **明确** 谈到了设计和架构？
- **学生答：第 9 条**——"持续关注技术卓越和好的设计能增强敏捷性"。讲师：我们关注怎么做技术决策，因为它影响我们有多敏捷、能不能做出可以演进和成长的东西。学生之前提到的"简单"也在第 10 条。
- 讲师再问还有没有很明确的一条——无人答出，讲师指出 **第 11 条**（他说"可能因为我没高亮它"）："最好的架构、需求和设计来自 **自组织团队**"——自组织团队是 **一起做决定** 的团队，不是一个人领导。即使有架构师或资深工程师，让其他人参与决策也能带来很多重要视角。
- 上周讲需求时也提过相关原则（和业务人员一起工作）——这同样有助于协作、及早把设计和架构决策调到正确方向。
- 结论：**你们随时可以回到这些价值观和原则，来推导自己在设计和架构上的思考。**

---

### 12 · FROM AGILE TO DESIGN — Agile principles create technical design responsibilities

![](images/12_section_agile_principles_responsibilities.jpg)

Agile principles create technical design responsibilities

🇨🇳 章节页：敏捷原则产生技术设计责任。

💬 **讲师补充**：上一页已经讲了——总是回到这些原则和价值观来做决定。

---

### 13 · Agile values and design decisions

![](images/13_agile_values_design_decisions.jpg)

| Working software | Design enough structure to deliver a usable increment |
|---|---|
| Responding to change | Keep responsibilities and dependencies easy to change |
| Technical excellence | Use testing, refactoring and clear interfaces to sustain speed |
| Customer collaboration | Use feedback to validate both behaviour and priorities |

The technical choices behind an increment affect how easily the team can respond to change

🇨🇳 敏捷价值观与设计决策

| 可工作的软件 | 设计"刚好够"的结构来交付一个可用的增量 |
|---|---|
| 响应变化 | 让职责和依赖容易改 |
| 技术卓越 | 用测试、重构和清晰的接口来维持速度 |
| 客户协作 | 用反馈来验证行为和优先级 |

一个增量背后的技术选择，决定了团队响应变化有多容易。

💬 **讲师补充**
- **可工作的软件**：设计够用就行，不需要复杂或完整的结构，就能交付一个可用增量（一组非常聚焦的用户故事）。
- **响应变化**：给客户看了评审 / demo，客户说要改——如果职责和依赖是分开的、彼此不严重依赖，改一处不会影响很多别的。例子：我只改登录，不需要改整个用户认证流程。
- **技术卓越**：建立好的测试、大量重构来改进代码和功能，保证它不会限制设计。
- **客户协作**：早点拿反馈，有助于及早理解并确定设计决策的优先级。

---

### 14 · From Agile to Software Design & Architecture

![](images/14_agile_to_design_architecture.jpg)

| Agile → Scrum | Design → Architecture | Build quality in → Software Features |
|---|---|---|
| User stories, acceptance criteria, Sprint planning, iterative delivery. | Translate stories and quality needs into components, responsibilities and boundaries. | Build, Test, Integrate, Refactoring, Deployment (DevOps). |

Turning Agile planning into technical design decisions, and software features to be delivered and deployed

Agile principles make the bridge explicit:
- Continuous attention to technical excellence and good design enhances agility.
- Simplicity helps teams avoid unnecessary work.
- Architectures and designs can emerge through collaboration and feedback.

🇨🇳 从敏捷到软件设计与架构

| 敏捷 → Scrum | 设计 → 架构 | 内建质量 → 软件功能 |
|---|---|---|
| 用户故事、验收标准、Sprint 计划、迭代交付 | 把故事和质量需求翻译成组件、职责和边界 | 构建、测试、集成、重构、部署（DevOps） |

把敏捷计划变成技术设计决策，再变成要交付和部署的软件功能。敏捷原则把这座桥说得很明确：持续关注技术卓越和好设计；简单帮团队避免不必要的工作；架构和设计可以通过协作和反馈涌现。

💬 **讲师补充**
- 这页解释 **本课程的脉络**。讲师坦言安排顺序不容易：先学工具（Git / GitHub / GitLab）？先学 CI/CD？先学需求？先学设计？他的选择是：先学敏捷计划和 Scrum（怎么写用户故事、验收标准、计划 Sprint、所有事件和工件），开始通过 Sprint 做迭代开发；**然后** 把用户故事翻译成要实现的东西，逐步想组件、职责、边界、放在架构的哪一部分（后面会用一个用户故事举例）；**再然后** 从一开始就内建质量。
- 说到软件质量，大家都想到测试；**测试只是 DevOps 的一个组成部分**，DevOps 下面有持续集成、持续交付。CI/CD 的流水线保证每次改动、重构、改设计 / 组件时质量都有保障。

---

### 15 · What you should be able to learn

![](images/15_what_you_learn.jpg)

- Identify the main components of a web application
- Explain the difference between architecture, design principles and design patterns
- Draw a simple architecture or request-flow diagram
- Use separation of concerns, cohesion and coupling to discuss a design
- Relate design decisions to maintainability, testability and extensibility
- Explain how design evolves within Scrum and CI/CD

🇨🇳 学完本讲你应该能
- 识别 Web 应用的主要组件
- 解释架构、设计原则和设计模式的区别
- 画一张简单的架构图或请求流程图
- 用关注点分离、内聚、耦合来讨论一个设计
- 把设计决策和可维护性、可测试性、可扩展性联系起来
- 解释设计如何在 Scrum 和 CI/CD 中演进

💬 **讲师补充**：画图要 **简单**，因为你们的应用本来就简单，目的是让你们开始思考这个过程；设计原则指导你怎么分、怎么合；设计决策要关联到"非功能需求"（有人叫别的名字）——怎么设计才容易维护、测试、扩展。

---

### 16 · How to draw architecture

![](images/16_how_to_draw_architecture.jpg)

Draw enough to answer a question, not every detail

A useful zoom model

| 1. Context | 2. Containers | 3. Components | 4. Code |
|---|---|---|---|
| Who uses the system? What external systems matter? | Web app, API, database, worker, external service. | Modules and responsibilities inside an application. | Classes/functions only when that detail adds value. |

Tools: Whiteboard, diagrams.net, Lucidchart, Miro, Mermaid, PlantUML, Structurizr

For most student web projects, a context diagram + a container diagram is usually enough to start.

Reference: C4 model for visualising software architecture (Simon Brown)

🇨🇳 怎么画架构图：画到能回答问题就够了，不必画每个细节

| 1 语境 | 2 容器 | 3 组件 | 4 代码 |
|---|---|---|---|
| 谁用系统？哪些外部系统重要？ | Web 应用、API、数据库、worker、外部服务 | 应用内部的模块和职责 | 只有当类 / 函数的细节有价值时才画 |

工具：白板、diagrams.net、Lucidchart、Miro、Mermaid、PlantUML、Structurizr。对大多数学生 Web 项目，**一张语境图 + 一张容器图** 就足够起步。参考：C4 模型（Simon Brown）。

💬 **讲师补充**：和前面有点重复——语境、容器（里面住着组件）、组件（模块和职责）、最后实现成代码。**最常画的是语境图和容器图**，通常够用了。

---

### 17 · Design in an Agile development

![](images/17_section_design_in_agile.jpg)

From a user story to Web application components

🇨🇳 章节页：敏捷开发中的设计——从一个用户故事到 Web 应用组件。

💬 **讲师补充**：接下来深入"从用户故事到 Web 应用组件"，仍然带着敏捷思维。

---

### 18 · Agile design is iterative and incremental

![](images/18_agile_design_iterative.jpg)

User need → Small design → Working slice → Feedback → Evolved design

Design decisions become more reliable when the team tests them through working increments.

Good design is not a document handed to developers. It is a set of decisions that makes change safer, clearer and cheaper.

🇨🇳 敏捷设计是迭代、增量的：用户需求 → 小设计 → 可工作的切片 → 反馈 → 演进的设计。当团队通过可工作的增量去检验设计决策时，决策就更可靠。好设计不是交给开发者的一份文档，而是一组让改动更安全、更清晰、更便宜的决策。

💬 **讲师补充**
- 从用户需求（用户故事）开始，做一个小设计，然后构建一个 **可工作的切片（working slice）**——后面会专门举例说明有了用户故事之后怎么做切片。
- **目标是尽早拿到客户 / 用户 / 相关方的反馈** 来演进设计。不做出来、不给他们看，就拿不到早期反馈，也就没法调整设计。
- 设计不是"我给开发团队一堆设计文档 / 图"，还有一组让改动更快、更便宜、更干净的决策。

---

### 19 · A user story becomes a set of responsibilities

![](images/19_user_story_responsibilities.jpg)

As a registered user, I want to submit a request and track its status, so that I know what is happening.

→ Present the form · Validate the request · Apply business rules · Store and retrieve status

🇨🇳 一个用户故事变成一组职责："作为注册用户，我想提交一个请求并跟踪它的状态，这样我就知道发生了什么。" → 展示表单、校验请求、应用业务规则、存储和读取状态。

💬 **讲师补充**
- 实现这个故事 **不是一个函数、一段代码**，而是多个职责：要给用户一个表单（它住在设计 / 架构的某处）；**在把表单提交到后端之前先校验**；校验通过后还要应用业务规则——这个用户是否允许提交、是否有权访问他要的东西；最后要存储和读取状态，这样用户更新了什么系统都有记录。
- 一个用户故事产生了多个职责，住在应用的不同组件里：**有的进前端，有的进后端，后端又有多个组件**，背后还有通信——提交表单会通过 HTTP 请求到应用逻辑，这个请求有格式 / 契约可以遵循。

---

### 20 · Basic web application architecture

![](images/20_basic_web_architecture.jpg)

A browser communicates with server-side software through HTTP

User → Browser (Front-end) → HTTP / API → Back-end (Business logic) → Data

The boundary is also a responsibility boundary: the server must enforce rules and protect data.

🇨🇳 基本的 Web 应用架构：浏览器通过 HTTP 和服务端软件通信。用户 → 浏览器（前端）→ HTTP / API → 后端（业务逻辑）→ 数据。这个边界同时是职责边界：服务器必须执行规则、保护数据。

💬 **讲师补充**
- 用户通常通过浏览器（或手机等设备的界面）交互：看页面、填表单、搜索、登录……请求通过 HTTP / API 发到后端（业务逻辑），后端处理请求、访问或更新数据。
- 虽然用户只是在做"一件事"，但 **职责清楚地分在不同组件里，有清楚的流程**。写代码时要始终用这种思维：前端代码、通过 HTTP API 发请求（请求 / 响应大多由浏览器处理，你不用亲自管，但要理解它怎么工作）、应用逻辑收到 HTTP 请求后开始处理。

---

### 21 · Class Activity: Classify front-end and back-end responsibilities

![](images/21_activity_frontend_backend.jpg)

| | |
|---|---|
| • Validates requests and permissions | • Displays information and accepts input |
| • Applies business rules | • Manages interaction and client-side state |
| • Reads and writes persistent data | • Calls the back end through an API |
| • Integrates external services | • Provides immediate feedback |
| • Returns useful responses and errors | • Handles loading, error and empty states |

🇨🇳 课堂活动：把这些职责分成前端和后端——校验请求和权限 / 应用业务规则 / 读写持久化数据 / 集成外部服务 / 返回有用的响应和错误；显示信息并接收输入 / 管理交互和客户端状态 / 通过 API 调用后端 / 提供即时反馈 / 处理加载、错误和空状态。

💬 **讲师补充（课堂互动）**
- 讲师：这两组是混在一起的还是刚好一组前端一组后端？学生看出 **第二列（右边）像前端**。讲师：对，很多事要在前端做；左边那组全放后端合理吗？合理。
- **这就是实现一个用户故事时要做的决策**：哪些职责进前端、哪些进后端。如果开发者 **把后端的职责做到了前端，就违反了设计原则**（后面会讲），会造成大问题。

---

### 22 · Front end and back end have different responsibilities

![](images/22_frontend_backend_responsibilities.jpg)

| Front-end | Back-end |
|---|---|
| • Displays information and accepts input | • Validates requests and permissions |
| • Manages interaction and client-side state | • Applies business rules |
| • Calls the back end through an API | • Reads and writes persistent data |
| • Provides immediate feedback | • Integrates external services |
| • Handles loading, error and empty states | • Returns useful responses and errors |

🇨🇳 前端和后端职责不同

| 前端 | 后端 |
|---|---|
| 显示信息、接收输入 | 校验请求和权限 |
| 管理交互和客户端状态 | 应用业务规则 |
| 通过 API 调用后端 | 读写持久化数据 |
| 提供即时反馈 | 集成外部服务 |
| 处理加载、错误和空状态 | 返回有用的响应和错误 |

💬 **讲师补充**
- 前端：显示信息、接收输入、管理交互和客户端状态（大多在客户端发生）、通过 API 调后端、在发请求前给即时反馈——**有时在提交之前就做校验，让应用更响应**；处理加载 / 错误 / 空状态（用户提交了东西、或返回了空）。
- 后端：**再校验一次请求**。**重点：即使前端校验过，后端校验仍然是后端的责任**——用户或 **黑客** 可以发送"看起来校验过"但能搞坏代码的东西，可以注入可疑代码、绕过前端校验。
- **为什么前端也要校验？为了性能 / 体验**：不想把请求发到后端再等响应——那要走网络、花时间。用户填了无效的邮箱或密码，能在前端查的就尽量在前端查。
- 后端还要读写数据库来回答查询、有时调用外部服务来满足用户请求，然后返回有用的响应和错误，由前端来处理显示。

---

### 23 · The API is a contract between components

![](images/23_api_contract_between_components.jpg)

| Front-end | API contract | Back-end |
|---|---|---|
| Sends a request with the required data | • Endpoint • Method • Input • Response • Error rules | Validates, processes and returns a response |

🇨🇳 API 是组件之间的契约：前端带着必要数据发请求；契约规定端点、方法、输入、响应、错误规则；后端校验、处理并返回响应。

💬 **讲师补充**
- 前后端中间的 API（应用编程接口）**是一个契约，不只是一个 URL**。契约描述：调用后端服务用哪个 URL / 端点（功能在服务器的哪里）、调用什么方法（可能有很多方法操作数据）、提供什么输入、响应是什么、错误怎么处理。这样处理请求和响应就有了系统性的方式。
- 这个练习的目的：**把正确的职责放进正确的组件，边界设清楚**。理解 API 契约（端点、方法、输入参数、响应长什么样）才能处理请求和响应。
- 讲到这里讲师问有没有问题，没有；说完设计原则这部分再休息。

---

### 24 · DESIGN PRINCIPLES — Good structure can help to make better changes

![](images/24_section_design_principles.jpg)

Good structure can help to make better changes

🇨🇳 章节页：设计原则——好的结构让改动更容易。

💬 **讲师补充**
- 好结构的意义：我们 **预期变化会发生**，预期架构和设计会演进，它不是一次完成的。这个过程很难，因为是增量做的，边走边不断做决定、修正决定。
- **有经验的工程师** 做了很多项目之后才总结出怎么做好决策。通常的路径是初级工程师 → 高级工程师 → 架构师：架构师经历过大量开发，理解从代码到完整架构的全过程，知道早期决策怎么影响后来的设计和架构。
- **关于 AI 的题外话**：现在很多公司用 AI agent 写代码，业界和学术会议都在讨论该教什么、怎么教。常听到"初级工程师不再需要了，AI 能写代码，我们需要更资深的人"。**更资深的人就是理解设计决策和架构决策的人**——和 AI 一起工作时，能判断 AI 写的代码好不好、让它按某种方式改，因为 **不能完全信任 agent 做这些决定**。有人说"一切看起来都很好、能跑"，然后规模上去、用户多了突然就挂了。所以这些早期决策很重要，需要有人来引导 AI agent——这个人必须理解设计原则，也要懂真正好的代码。

---

### 25 · Core design principles

![](images/25_core_design_principles.jpg)

Key principles worth considering for every Sprint

| Separate concerns | Encapsulation | High cohesion | Low coupling |
|---|---|---|---|
| Different responsibilities should not be tangled together. | Hide internal details behind a clear interface. | Keep closely related behaviour together. | Minimise how much one part must know about another. |

| Simple dependencies | Design for change | YAGNI* / simplicity | Refactor continuously |
|---|---|---|---|
| Make dependency direction visible and predictable. | Isolate likely sources of change. | Do not build complexity for imagined future needs. | Improve the design as understanding grows. |

\* You aren't gonna need it

🇨🇳 核心设计原则——每个 Sprint 都值得考虑

| 关注点分离 | 封装 | 高内聚 | 低耦合 |
|---|---|---|---|
| 不同职责不要缠在一起 | 把内部细节藏在清晰的接口后面 | 关系紧密的行为放在一起 | 让一个部分尽量少了解另一个部分 |

| 简单依赖 | 为变化设计 | YAGNI / 简单 | 持续重构 |
|---|---|---|---|
| 依赖方向可见、可预测 | 隔离可能变化的来源 | 别为想象中的未来需求堆复杂度 | 理解加深了就改善设计 |

💬 **讲师补充**
- 设计原则很多，这里只挑一些让你们在 Sprint 开发时放在心上。
- **关注点分离**：前端负责某些事、后端负责某些事，每个职责对应代码里的一个函数之类，但一个在前端一个在后端；后端内部还可以再分。
- **封装**：把内部细节藏在清晰的接口后面。好例子是 **类**：类里有方法和数据，通过类定义的方法来操作数据——别人和这个类"对话"只通过方法。
- **高内聚**：相关行为放一起，**理由是便于修改、把变化局部化**。如果相关行为散在不同组件，改一个行为可能要改很多处，而且 **每一处都要重新测试**，很贵；放在一个组件 / 模块里就容易测试和评估。
- **低耦合**：有人叫"解耦（decoupling）"。高耦合 = 太多组件彼此严重依赖，每个组件要调用很多别的组件才能完成一个功能。**耦合不可能完全避免，目标是最小化** 一个部分必须了解另一个部分的程度——否则改动很贵，做一件事要经过多次调用。
- **简单依赖**：A 调 B、B 调 C……这种 **传递依赖** 要尽量少，让依赖清楚、可见、直接。
- **为变化设计**：架构师会问"什么最常变"，知道了就把它放进一个组件 / 模块来减少改动范围。
- **YAGNI**："你不会需要它"——只实现需要的，保持简单。还有一个 **KISS（Keep it simple, stupid）**：一个东西只做一件小事。开发者常说"以后可能用得上"，于是往一个类 / 函数 / 模块里塞很多职责，后来根本用不上——东西变大、更难维护、更难测试。
- **持续重构**：边做边改进设计。一个用户故事会穿过多层（**垂直切片**），覆盖不同组件的职责，这能让我们早拿反馈、早测试、早发现问题，从而尽早修正设计。

---

### 26 · Separation of concerns

![](images/26_separation_of_concerns.jpg)

One feature can cross layers without mixing responsibilities

UI (Form + feedback) → API (Request/response) → Business logic (Validate expense rules) → Data access (Save/retrieve expense) → Database (Persistent data)

Same user story, distinct responsibilities

A change to the screen layout should not require rewriting persistence. A change to the database should not change the user story.

🇨🇳 关注点分离：一个功能可以穿过多层，但职责不混。界面（表单 + 反馈）→ API（请求 / 响应）→ 业务逻辑（校验开销规则）→ 数据访问（存 / 取开销）→ 数据库（持久化数据）。同一个用户故事，职责各不相同。改页面布局不应该要重写存储；换数据库不应该改变用户故事。

💬 **讲师补充**
- 前端 / 表单只管收集用户的数据和反馈；请求经过 API 发出并在返回时处理响应；业务逻辑只管校验应用规则（这里是开销规则）；访问数据库要 **通过一个专门负责访问数据库的组件**——**业务逻辑不直接调数据库**。
- 这些职责不在一个文件 / 一个模块里。要改数据库访问方式，只改那一部分，其余不受影响；要加业务规则，直接加、调用对应的规则就行，其他部分不动。这样就容易改、容易维护、容易演进。

---

### 27 · Encapsulation and dependency direction

![](images/27_encapsulation_dependency.jpg)

Stable interfaces let internals change

Expense service — Public operations: recordExpense(), getBalances()
— uses → Database adapter (SQL / ORM / repository details)
— uses → Notification adapter (Email / push / webhook details)

Why it helps: Tests can replace adapters with fakes. Infrastructure can change without rewriting business rules.

The goal is not "more layers". The goal is explicit boundaries and fewer surprises.

🇨🇳 封装与依赖方向：接口稳定，内部可以换。Expense service 对外只有 recordExpense() 和 getBalances() 两个操作，它"使用"数据库适配器（SQL / ORM / 仓储细节）和通知适配器（邮件 / 推送 / webhook 细节）。好处：测试时可以用假的适配器替换；换基础设施不用重写业务规则。目标不是"更多层"，而是边界明确、少踩坑。

💬 **讲师补充**
- 不是为了造很多层，而是把实现某组职责的方法 **封装** 在 expense service 里（记开销、取余额，以后可以再加和开销相关的职责）。但它 **不需要处理数据 / 数据库，也不把那些逻辑放进来**——需要记开销时调用数据库层；需要通知时有一个适配器去发推送或邮件。
- **这让测试变容易**：可以把通知适配器换成一个 **mock**，模拟它的行为，即使没有真正的通知服务。数据库也一样。
- **对你们项目的直接建议**：你们刚开始做，**不用太操心后端**——为了简化、聚焦在应用你们学到的东西上，**可以先做前端，后端用一个"假服务"mock 掉，比如一个文件：读文件就返回一个字符串**。决策可以简化，但设计上这段代码 **不在业务逻辑里面，而是在一个单独的适配器 / 组件里**。这样换数据库时不需要改 expense service。

---

### 28 · Separation of concerns and encapsulation

![](images/28_soc_and_encapsulation.jpg)

| Tangled responsibility | Separated responsibility |
|---|---|
| One module • renders the form • validates permissions • calculates fees • writes to the database • sends email | Form / view · Business service · Data access · Notification adapter |

🇨🇳 关注点分离与封装：缠在一起的职责（一个模块画表单、验权限、算费用、写数据库、发邮件）vs 分开的职责（表单 / 视图、业务服务、数据访问、通知适配器）。

💬 **讲师补充**：职责缠在一起会造成很多问题、很难改；分开之后，改适配器就不用把所有东西重新测一遍。

---

### 29 · Cohesion and coupling

![](images/29_cohesion_coupling.jpg)

Keep related things together; keep unnecessary dependencies apart

| High cohesion + low coupling | Low cohesion + high coupling |
|---|---|
| Expense module • create expense • validate split • calculate balances<br>Notification module • email • push notification | UtilityManager • expense calculations • email • database queries • authentication • report formatting • UI helpers |

Design question: "If I change this responsibility, how many unrelated places must I understand and modify?"

🇨🇳 内聚与耦合：相关的放一起，不必要的依赖分开。高内聚 + 低耦合（正例）：开销模块只管建开销、校验分账、算余额；通知模块只管邮件、推送。低内聚 + 高耦合（反例）：一个 UtilityManager 塞了算钱、邮件、查库、认证、报表、UI 工具。设计时问："如果我改这个职责，要看懂并修改多少不相关的地方？"

💬 **讲师补充**
- 目标是左边绿框：高内聚、低耦合——逻辑相关的组件放一起，变化局部化在一个组件内；低耦合让测试和修改容易，只需换掉一个服务。**不要** 低内聚 + 高耦合。
- 始终问自己那个设计问题：改一个职责要动多少不相干的地方？改动应该只落在高度封装 / 高内聚的那一小块代码里。

---

### 30 · Design for change – Class Activity

![](images/30_design_for_change_activity.jpg)

| Architecture 1 | Architecture 2 |
|---|---|
| 12 services · 3 message brokers · custom plugin platform · global multi-region replication · "because we may need it later" | One deployable web app · clear modules · well-defined API boundaries · automated tests · room to extract a service later if evidence appears |

Which Architecture would you choose? Why?

🇨🇳 课堂活动：为变化设计。架构 1：12 个服务、3 个消息队列、自研插件平台、全球多区域复制，理由是"以后可能用得上"。架构 2：一个可部署的 Web 应用、清晰的模块、定义好的 API 边界、自动化测试，有证据再拆服务。你选哪个？为什么？

💬 **讲师补充（课堂互动）**
- **学生答：选 2，理由是"可工作的软件"。** 讲师：好——一个可部署的 Web 应用而不是 12 个服务，可以只部署这一个，然后 **增量** 地往里加东西；模块清楚、API 边界定义好，以后需要了再抽出服务。
- 架构 1 是在 **猜测** 未来需要，但没有证据，加那些东西没有价值。**设计 Sprint 时要简单，用 YAGNI**：不要在一个 Sprint 里想做全部、为没有证据的东西投机。

---

### 31 · Simplicity, YAGNI and design for change

![](images/31_simplicity_yagni.jpg)

Keep today simple; protect the places that are likely to change

| Do not build this on Sprint 1… | Prefer this… |
|---|---|
| Speculative architecture: 12 services · 3 message brokers · custom plugin platform · global multi-region replication · "because we may need it later" | Simple, modular starting point: One deployable web app · clear modules · well-defined API boundaries · automated tests · room to extract a service later if evidence appears |

Design for change means isolating known instability, not predicting every future feature.

🇨🇳 简单、YAGNI 与为变化设计：今天保持简单，保护好可能变化的地方。Sprint 1 别做"投机式架构"，要做"简单、模块化的起点"。为变化设计 = 隔离已知的不稳定点，而不是预测每一个未来功能。

💬 **讲师补充**
- 这和用户故事、Scrum 里讲的一样：**不预测未来，只为我们知道的、确定能在一个增量里交付价值的东西设计**。做到了就能拿到好反馈；用户说要加服务，我们再加——但那是他们 **真的提出了需求** 之后。
- 讲到这里过半，**休息 5 分钟**。

---

### 32 · Architecture of Web applications

![](images/32_section_web_architecture.jpg)

A browser click becomes a chain of responsibilities across the front end, network, back end, data and external services.

🇨🇳 章节页：Web 应用的架构——浏览器上的一次点击，变成一条穿过前端、网络、后端、数据和外部服务的职责链。

💬 **讲师补充**（休息后）：用户在浏览器上点点点、请求东西，背后有一整条 **职责链** 用户看不见；作为工程师你要设计这条链，让设计和架构能安全、容易地完成它。

---

### 33 · The simplest useful web architecture

![](images/33_simplest_web_architecture.jpg)

Client → server → data

| Browser / client | Web / API server | Database | External services |
|---|---|---|---|
| HTML + CSS + JavaScript · User interactions · Local UI state | HTTP endpoints · Business rules · Authentication · Authorisation | Users · Expenses · Groups · Persistent state | Email · Payments · Maps · Identity provider |

(HTTP request / HTTP response between browser and server; query/write to database; API call to external services)

The browser is not "the application". It is one part of a larger system.

Reference: MDN "How the web works"

🇨🇳 最简单但有用的 Web 架构：客户端 → 服务器 → 数据。浏览器 / 客户端（HTML + CSS + JavaScript、用户交互、本地 UI 状态）⇄ HTTP 请求 / 响应 ⇄ Web / API 服务器（HTTP 端点、业务规则、认证、授权）→ 查询 / 写入 → 数据库（用户、开销、群组、持久化状态）；服务器 → API 调用 → 外部服务（邮件、支付、地图、身份提供方）。浏览器不是"应用本身"，只是大系统的一部分。

💬 **讲师补充**
- **浏览器替你做了很多事**：准备发给 Web 服务器的请求 / 响应等幕后工作。你只需要写页面、样式、JavaScript（触发动作、校验输入、处理交互和 UI 状态）。学 Web 开发时会了解 HTTP 协议的各种方法，它描述请求 / 响应怎么和 Web / API 服务器通信。
- Web / API 服务器定义业务规则、认证、授权（谁能访问什么）；有若干 **端点**（URL + 参数）对应不同职责。服务器和浏览器是分开的，通过 HTTP 通信。
- 服务器再去查数据库——**数据库和客户端的直接访问隔开了**。即使一个功能也要经过这些分开的职责，比如查询"符合条件的用户 / 开销 / 群组"（对应你们的 expense splitter）。
- 需要外部服务时（比如扣款、连接真实支付系统、显示地图）通过 API 调用并配置，结果存回数据库。
- 要做快速响应的界面，需要理解浏览器怎么工作，才能优化请求 / 响应的管理。

---

### 34 · Front-end: what belongs in the browser?

![](images/34_frontend_browser.jpg)

Presentation and interaction, not trusted business authority

- Render the interface and data
- Collect user input
- Manage UI state
- Provide immediate validation feedback
- Call back-end APIs
- Handle loading, errors and empty states
- Support accessibility and responsive layout

Example: "Record expense" form — The browser can check that amount looks numeric and show errors instantly.

But the server still validates — A user can bypass JavaScript or call the API directly. Business rules and authorisation must be enforced server-side.

🇨🇳 前端：什么属于浏览器？——展示和交互，不是可信的业务权威。渲染界面和数据、收集输入、管理 UI 状态、提供即时校验反馈、调用后端 API、处理加载 / 错误 / 空状态、支持无障碍和响应式布局。例子："记一笔开销"表单——浏览器可以检查金额是不是数字并立即报错；**但服务器仍然要校验**：用户可以绕过 JavaScript 或直接调 API，业务规则和授权必须在服务端执行。

💬 **讲师补充**：前端做展示和交互，**不要把业务逻辑 / 业务规则放在浏览器里**。前端校验是为了在发请求前给即时反馈；**服务器也会再校验**，确保没有东西绕过前端校验——黑客知道怎么绕过，可能破坏数据库或做未授权的事。

---

### 35 · Back-end: what belongs on the server?

![](images/35_backend_server.jpg)

Business behaviour, security enforcement, persistence and integration

| API boundary | Validation | Authentication | Authorisation |
|---|---|---|---|
| Receive HTTP requests; return structured responses. | Check required data and domain rules. | Establish who the user is. | Decide what that user is allowed to do. |

| Business logic | Persistence | Integration | Observability |
|---|---|---|---|
| Calculate splits, balances and other domain behaviour. | Read/write durable data through a data access layer. | Call external services through controlled adapters. | Log important events and failures. |

🇨🇳 后端：什么属于服务器？——业务行为、安全执行、持久化和集成

| API 边界 | 校验 | 认证 | 授权 |
|---|---|---|---|
| 接收 HTTP 请求，返回结构化响应 | 检查必要数据和领域规则 | 确定用户是谁 | 决定这个用户能做什么 |

| 业务逻辑 | 持久化 | 集成 | 可观测性 |
|---|---|---|---|
| 计算分账、余额等领域行为 | 通过数据访问层读写持久数据 | 通过受控的适配器调用外部服务 | 记录重要事件和失败 |

💬 **讲师补充**
- 后端按 HTTP 协议接收请求、返回结构化响应；做校验；**认证**确保用户是他声称的那个人；**授权**决定他能访问什么——例子：**只能访问自己所在群组的开销，不能看别的群组**。
- 业务逻辑算分账、余额等领域行为；通过数据访问层读写数据库；集成外部服务。
- **可观测性**：每一步都要 **记日志**，出问题时才能知道错在哪（是读库还是写库？）。每个组件都有日志就能定位；当拆分和职责太多时，这件事会变得复杂。

---

### 36 · The API is a contract

![](images/36_api_is_contract.jpg)

A boundary lets front end and back end evolve with less coupling

| Front-end | API contract | Back-end |
|---|---|---|
| Needs to know: endpoint · request format · response format · errors<br>Does not need to know: SQL · server classes · database schema details | POST /expenses<br>{ amount, payer, split }<br>→ 201 Created / validation error | Needs to know: contract · business rules · authorisation · persistence<br>Does not need to know: exact DOM structure · CSS · browser component tree |

Good contracts reduce coupling. They do not eliminate coordination.

🇨🇳 API 是契约：有了边界，前后端可以以更低的耦合各自演进。前端需要知道端点、请求格式、响应格式、错误；不需要知道 SQL、服务器的类、数据库表结构。契约例子：POST /expenses，请求体 { amount, payer, split }，返回 201 Created 或校验错误。后端需要知道契约、业务规则、授权、持久化；不需要知道 DOM 结构、CSS、浏览器组件树。好契约降低耦合，但不消除协调。

💬 **讲师补充**：API 按协议连接前后端——GET 取数据、POST 存数据，遵循一定的结构、状态码和校验规则。**好契约降低耦合，因为代码不在这边也不在那边，而是在契约里**：你知道要发什么、会收到什么。但协调仍然存在——**所以叫低耦合，不叫解耦**。

---

### 37 · Layered architecture

![](images/37_layered_architecture.jpg)

Presentation / API → Application services → Domain / business rules → Data access → Database / external systems

A request usually moves downward, while a response moves back upward.
Each layer has a primary responsibility

🇨🇳 分层架构：展示 / API → 应用服务 → 领域 / 业务规则 → 数据访问 → 数据库 / 外部系统。请求通常往下走，响应往上回。每一层有一个主要职责。

💬 **讲师补充**
- 分层架构是 **关注点分离原则的落地**——你开始看到前面讲的原则活在常见的架构模式里。展示和 API 在浏览器 / 前端；有一层专门定义和实现 **应用服务**，它可能直接回答一些请求，也可能需要先经过领域规则或数据访问。
- **有趣的地方：展示层 / 用户不能直接访问数据访问层或数据库，必须一层层经过。** 有的请求在应用服务层就能回答，直接返回；有的要经过业务逻辑检查规则（可能在访问数据库之前就返回），再到数据库。
- 好处：关注点分离——可以加业务规则、改应用服务、改访问数据库的方法；加一个新数据源只需在数据访问层加一个方法，不影响别的层。
- **安全**：用户尤其是黑客不能直接碰数据库，必须经过所有校验和检查（是否认证、是否有权做这件事）。
- **部署**：各层可以各在一台服务器上（通过 HTTP / API 跨网络调用），也可以全在一台服务器上但作为独立组件存在——**逻辑上分开，物理部署可以不同**。

---

### 38 · Layered architecture: one user story end to end

![](images/38_layered_end_to_end.jpg)

"Record an expense" as a vertical slice

UI (Expense form) → API (POST /expenses) → Service (recordExpense) → Domain (validate split) → Repository (save expense) → DB (rows)

Tests can exist at several seams:
- Domain unit tests for split calculations
- Service tests with a fake repository
- API integration tests
- Small browser/end-to-end tests for critical user journeys

🇨🇳 分层架构：一个用户故事端到端——"记一笔开销"作为垂直切片。界面（开销表单）→ API（POST /expenses）→ 服务（recordExpense）→ 领域（校验分账）→ 仓储（保存开销）→ 数据库（行）。测试可以在多个"缝"上做：领域单元测试（分账计算）、用假仓储测服务层、API 集成测试、针对关键用户路径的少量浏览器 / 端到端测试。

💬 **讲师补充**
- 同一个分层架构换一种画法，聚焦 **一个用户故事从头到尾**：实现"记开销"要做 HTML + CSS 的表单；用户点提交时它知道怎么准备一个 POST 请求到 /expenses；经过服务层调用 recordExpense（可能先检查点什么）；领域组件 **校验分账是否正确** 再存库；仓储做最后的校验并保存。每一层各有职责。
- **测试变容易**：可以分别给 validate split、record expense、save expense 写测试，不需要把所有东西放在一个组件里一起测（那样很复杂）。**可以用假的替换真的**：比如 **不用真数据库，用一个文件来读写**，这样就能测服务层。
- 不同类型的测试 **下周讲**：要保证这些组件集成起来，请求能一路走通，预期行为跨所有组件成立。

---

### 39 · Model-view-controller (MVC)

![](images/39_mvc.jpg)

- **Model** — Defines data and domain behaviour (e.g. updates application state after an item is added)
- **View** — Defines the display (UI) (e.g. user clicks 'add to cart')
- **Controller** — Contains control logic (e.g. receives input from the view and asks the model to update)

View —Sends input from user→ Controller —Manipulates→ Model —Updates→ View (Controller sometimes updates View directly)

A pattern for separating data, presentation and request coordination

🇨🇳 模型-视图-控制器（MVC）：模型定义数据和领域行为（如添加商品后更新应用状态）；视图定义显示 / UI（如用户点"加入购物车"）；控制器包含控制逻辑（接收视图的输入、让模型更新）。视图把用户输入发给控制器，控制器操作模型，模型更新视图（控制器有时直接更新视图）。这是一个把数据、展示、请求协调分开的模式。

💬 **讲师补充**
- 讲师问 **有没有人用过 MVC**——没有人。它很常见，很多课程和 Web 开发里都教。它同样基于关注点分离，三个组件各有专门职责。
- **视图**：事情发生的地方——定义怎么显示、接收用户输入（点"加入购物车"、搜索）并交给控制器；也显示控制器 / 模型返回的结果。
- **控制器**：控制逻辑——收到请求 X（用户想看什么 / 做什么），带着数据，知道该调哪个模型。**控制器不直接访问数据库**，要通过模型。
- **模型**：定义数据和领域行为，比如"把用户要的 X 都取出来"，里面有函数做这件事。
- 我们为每种请求 / URL 定义一个控制器，定义它去哪、调模型里的什么逻辑——三者之间有映射。

---

### 40 · Model-view-controller (MVC) – Web Application

![](images/40_mvc_web_app.jpg)

Web Browser —HTTP requests→ Routes (Forward requests to appropriate controller) → Controller ⇄ Models —Read/write data→ Database
Controller → View (Templates) —HTTP responses→ Web Browser
[Application/Web Server] · [DB Server]

🇨🇳 MVC 的 Web 应用形态：浏览器发 HTTP 请求 → 路由（把请求转发给合适的控制器）→ 控制器 ⇄ 模型 → 读写数据库；控制器 → 视图（模板）→ HTTP 响应回浏览器。路由、控制器、模型、视图在应用 / Web 服务器上，数据库在 DB 服务器上。

💬 **讲师补充**
- 这是讲师 **以前用 Node.js + Express.js 教** 的例子。用户在浏览器点东西发起 HTTP 请求，到 **路由（routes / routers）**：路由知道这类请求该转给哪个控制器——每种请求映射到一个控制器。控制器可能要调模型从数据库取东西（每种逻辑有专门的函数访问数据库），然后用 **视图模板** 生成响应。
- 数据库（比如 MySQL）可以部署在单独的服务器；控制器、路由、视图、模型这些模块在应用 / Web 服务器上。**也可以都放一台服务器，由你决定**——但要想到跨网络调用，以及扩展时的大问题（这里不展开）。

---

### 41 · Model-view-controller (MVC) – Web Application (request flow)

![](images/41_mvc_web_app_flow.jpg)

1. Request comes into application
2. Request gets routed to controller
3. Controller may send request to model for data
4. Model may need to talk to a data source (database) to manipulate data
5. Data source sends result back to model
6. Model responds to controller
7. Controller pass data to view
8. View generate HTTP response and sends back to client

- Database related code should be put in model layer
- Controller should not have knowledge about the actual database
- Modularity allows easy switching between technologies
  - e.g. different view templates, different database management systems

🇨🇳 MVC 请求流程 8 步：请求进入应用 → 路由到控制器 → 控制器向模型要数据 → 模型访问数据源操作数据 → 数据源把结果回给模型 → 模型回给控制器 → 控制器把数据交给视图 → 视图生成 HTTP 响应发回客户端。数据库相关代码放在模型层；控制器不应该知道实际的数据库；模块化让换技术很容易（换视图模板、换数据库管理系统）。

💬 **讲师补充**
- 课上这页是逐步动画：先出现第 1 步，再出现全部步骤。
- 流程：请求进来 → 经路由到控制器 → 控制器需要数据就请求模型，自己能处理就处理 → 模型可能要和数据库 / 数据源打交道 → 数据库把数据给模型 → 模型回控制器 → 控制器把要显示的东西传给视图 → 作为响应发回，浏览器显示。
- 这就是你设计实现时在做的事："我实现路由，收到请求 X 就给控制器 X，请求 Y 给控制器 Y"，有函数做这个映射；控制器根据请求类型和内容决定调不调模型。

---

### 42 · Model-view-controller (MVC) – Web Application (project structure)

![](images/42_mvc_folder_structure.jpg)

Horizontal Structure (a Node.js / Express project):
```
app/
  controllers/   models/   routes/   views/
config/
  env/   config.js   express.js
public/
  config/  controllers/  css/  directives/  filters/  img/  services/  views/  application.js
server.js
package.json
```

🇨🇳 MVC 项目的目录结构（Node.js 示例）：app 下分 controllers / models / routes / views；config 放环境与配置；public 放静态资源（css、img 等）和前端代码；根目录有入口 server.js 和依赖清单 package.json。

💬 **讲师补充**：控制器代码放在 controllers 文件夹、模型在 models、路由在 routes、视图在 views；图片、CSS 各有位置。**每个文件夹就是一个模块，模块下是源码文件**——这就是把架构图上的组件映射到代码结构的方式。

---

### 43 · MVC in modern Web app

![](images/43_mvc_modern.jpg)

The responsibilities may be split across browser and server

| Browser | | Server | |
|---|---|---|---|
| View (HTML/CSS + UI components) | Client logic (Events, state, API calls) | Controller / route (Receives HTTP request) | Model / domain (Data + business rules) → Database (persistent state) |

(HTTP / JSON between browser and server)

Python example: Django describes its approach as Model–Template–View (MTV), similar in style to MVC.

References: MDN MVC; Django documentation glossary

🇨🇳 现代 Web 应用中的 MVC：职责可能分布在浏览器和服务器两边。浏览器：视图（HTML/CSS + UI 组件）、客户端逻辑（事件、状态、API 调用）；通过 HTTP / JSON 到服务器：控制器 / 路由（接收 HTTP 请求）、模型 / 领域（数据 + 业务规则）→ 数据库。Python 例子：Django 把自己的方式叫 Model–Template–View（MTV），风格和 MVC 类似。

💬 **讲师补充**
- Python 里叫 **模型-模板-视图（MTV）**：客户端逻辑、事件、状态、API 调用大多在浏览器端处理；服务端专注控制器把请求路由到某段逻辑，再到模型和数据库。
- **Django 这样的框架开箱就给你这套结构**，不用自己从零实现。很多语言 / 框架采用了这些被广泛认可的设计模式，你只需要知道东西怎么组织、怎么调用、怎么发请求处理响应，日子就轻松了。

---

### 44 · Microservices Architecture

![](images/44_microservices.jpg)

API gateway (entry point) → User service (own logic) → User DB
API gateway (entry point) → Expense service (own logic) → Expense DB

Potential benefits: Independent deployment and scaling · Clear service ownership · Fault isolation when designed well

New complexity: Network failures + latency · Distributed tracing · Data consistency · More CI/CD + operations · Harder cross-service refactoring

- Do not choose microservices because they "sound scalable". Choose them when the benefits justify the operational complexity.
- Independent deployment can help, but distribution has a price

References: Martin Fowler microservices guide; "Monolith First"

🇨🇳 微服务架构：API 网关（入口）→ 用户服务（自己的逻辑）→ 用户库；→ 开销服务 → 开销库。潜在好处：独立部署和扩展、服务归属清晰、设计得好时故障隔离。新增复杂度：网络故障和延迟、分布式追踪、数据一致性、更多 CI/CD 和运维、跨服务重构更难。**别因为微服务"听起来可扩展"就选它**，只在收益能证明运维复杂度值得时才选；独立部署有帮助，但分布式有代价。

💬 **讲师补充**
- 课上这页也是两步显示：先出架构图和两栏要点，再出底部两条结论。
- 微服务 = **把每一个小功能做成一个服务**：比如认证用户（检查用户名密码、允许登录）就是一个服务；用户服务、开销服务各有自己的逻辑。
- **数据也拆成"微数据库"**：用户服务只有用户数据（它只需要这些来认证），开销服务只访问开销库——**用户服务不需要访问开销库**。要组合逻辑（"我群组里的人谁付了什么"）就调用服务 X、Y、Z 来拼出一个大功能。每个服务都有自己的 API；**API 网关** 收到请求后知道该调哪个服务的 API——所以叫网关。
- **好处：可扩展性**——假设用户服务负载不大，但开销服务 **每秒上千个请求** 成了瓶颈，就只把这个服务部署到多台服务器分流，**只扩展瓶颈组件而不是整个应用**。**故障隔离**：一个服务挂了不影响其他。**安全**：攻破一个服务拿不到其他数据库和服务。CI/CD 看起来也更容易，因为构建的都是小组件、独立运行。
- **代价**：服务分布在不同服务器，**追踪很难**（要每个都追）；**网络故障和延迟**；**数据一致性**（跨组件 / 数据库共享和更新数据）。**没有理想方案、没有银弹，只有决策和取舍**——这就是"架构 = 设计决策"的意思。
- 有的公司用了很有收益，但要看你的应用、领域、要解决的问题。**延迟敏感的应用** 不能容忍大量网络 API 调用。

---

### 45 · Architecture choices involve trade-offs

![](images/45_tradeoffs.jpg)

| Question | Why it matters |
|---|---|
| What is changing? | Separate likely points of variation |
| How large is the team? | Avoid operational overhead the team cannot support |
| What must scale? | Scale the relevant component or workload |
| How will we deploy? | Keep the architecture compatible with CI/CD |
| How will we test failures? | Prefer boundaries the team can observe and verify |

🇨🇳 架构选择涉及取舍

| 问题 | 为什么重要 |
|---|---|
| 什么在变？ | 把可能变化的点分开 |
| 团队多大？ | 避免团队撑不起的运维开销 |
| 什么必须扩展？ | 只扩展相关的组件或负载 |
| 怎么部署？ | 让架构和 CI/CD 兼容 |
| 怎么测试失败？ | 优先选择团队能观察、能验证的边界 |

💬 **讲师补充**：前面几页已经在讲取舍。**团队规模很重要**——团队大、组件拆太多（比如微服务），运维开销会变得巨大。知道哪个部分需要扩展有助于选架构。部署：每次构建都要部署到基础设施上，可能要把不同组件部署到不同服务器，这会拖慢交付、让追踪更复杂。

---

### 46 · Architecture also supports non-functional properties

![](images/46_non_functional.jpg)

- Performance — Where might time or resources be spent?
- Scalability — What grows: users, requests, data or integrations?
- Reliability — What happens when a dependency fails?
- Security — Who can perform this action? How is data protected?
- Others — Based on the application domain and stakeholders' needs

🇨🇳 架构还要支撑非功能属性：性能（时间和资源可能花在哪）、可扩展性（什么在增长：用户、请求、数据还是集成）、可靠性（依赖挂了会怎样）、安全（谁能做这个操作、数据怎么保护）、其他（看应用领域和相关方的需求）。

💬 **讲师补充**
- **性能 vs 安全的取舍**：分层架构里如果所有东西包括数据库都放在一台服务器，不用跨网络调用，性能好；但 **安全受影响**——攻破这台服务器就能拿到数据库和一切。分开放到不同服务器就是另一回事。**永远是取舍，不可能全都要。**
- **可扩展性**：用户数、数据量、访问量、负载增加时应用表现如何。例子：100 个用户时处理一个请求约 600 毫秒，**1,000 或 10,000 个用户时还是这个响应时间吗？** 延迟可能会增加。
- **可靠性**：一个组件依赖的另一个组件挂了怎么办——应该有 **故障切换（failover）** 方案：组件自动部署到另一台服务器并启动，用户完全感觉不到故障。
- 其他属性 / 非功能需求：可维护性（今天讲了很多遍）、**可理解性**（队友和你自己能不能看懂并修改代码——全在一个大文件里、到处依赖和调用就很难）、**可测试性**（职责拆好、边界清楚就能定义好的测试用例）、**模块化**（比如 MVC 怎么按文件夹模块化）、**可扩展性 / extensibility**（往一个组件加服务，别的组件代码不用改，它只需要知道有个新服务可以这样调）、**可部署性**（以后加更多东西时部署是否容易）。
- 设计时要想这些，而不是"能跑、够快"就行。代码越大越复杂，这些问题越突出。

---

### 47 · What "good design" buys an Agile team

![](images/47_good_design_buys.jpg)

Quality attributes are not decorations added at the end

| Maintainability | Understandability | Testability |
|---|---|---|
| Change code without widespread rework. | A teammate can locate and reason about the right place to change. | Behaviour can be verified automatically and in isolation. |

| Modularity | Extensibility | Deployability |
|---|---|---|
| Work can be divided into meaningful units with clear ownership. | New behaviour can be added without rewriting unrelated code. | Changes can move through CI/CD with predictable impact. |

These qualities reinforce each other: Clear modules are easier to understand, test, refactor and deploy.

🇨🇳 好设计给敏捷团队带来什么——质量属性不是最后加上去的装饰。可维护性（改代码不用大面积返工）、可理解性（队友能找到并想清楚该改哪）、可测试性（行为能自动、独立地验证）、模块化（工作能拆成归属清晰的单元）、可扩展性（加功能不用重写无关代码）、可部署性（改动能顺着 CI/CD 走、影响可预测）。这些质量互相加强：模块清楚了就更容易理解、测试、重构、部署。

💬 **讲师补充**：这页的内容已在上一页展开讲过（见上一页讲师补充）。

---

### 48 · A vertical slice connects design to delivery

![](images/48_vertical_slice.jpg)

User story → UI interaction → API endpoint → Business rule → Data access → Automated test → CI check

Each sprint can deliver a small end-to-end capability instead of a disconnected technical layer.

🇨🇳 垂直切片把设计和交付连起来：用户故事 → 界面交互 → API 端点 → 业务规则 → 数据访问 → 自动化测试 → CI 检查。每个 Sprint 可以交付一个小而完整的端到端能力，而不是一个孤立的技术层。

💬 **讲师补充**：对你们的 Sprint 来说——实现一个用户故事要覆盖不同组件的不同职责（前面讲过）。每个 Sprint 交付一个小的端到端能力，而不是彼此不连通的技术层。

---

### 49 · Sprint Design and Development – Class Activity

![](images/49_sprint_design_activity.jpg)

| Component design and development | Vertical Slice Design and Development |
|---|---|
| Sprint 1 — database components | Story A — UI → API → rule → DB → test → CI |
| Sprint 2 — Back-end design and development | Story B — UI → API → rule → DB → test → CI |
| Sprint 3 — Front-end design and development | Story C — UI → API → rule → DB → test → CI |

As Agile Teams, which design and development approach would you follow? Why?

🇨🇳 课堂活动：Sprint 的设计与开发。左边按组件分 Sprint（第 1 轮数据库、第 2 轮后端、第 3 轮前端）；右边按垂直切片（每个故事都是 界面 → API → 规则 → 数据库 → 测试 → CI）。作为敏捷团队你会选哪种？为什么？

💬 **讲师补充（课堂互动）**
- 讲师问：Sprint 1 做数据库组件、Sprint 2 做后端、Sprint 3 做前端？还是故事 A、B、C 各自跨所有组件？**学生：显然选切片。**
- 左边要避免——**capstone 项目里也有这种情况**："我们做了全部后端，另一拨人做全部前端，最后再集成"——这叫 **大爆炸集成（big bang integration）**：最后把所有东西放一起，再去找哪里出了问题。
- 正确做法：做故事 A——做表单 UI、调 API、检查规则、检查数据库、测试，然后和其他代码集成；故事 B 同样做完并集成；C、D 也一样，不管是同一个 Sprint 还是不同 Sprint。

---

### 50 · Vertical slices: design for incremental delivery

![](images/50_vertical_slices_incremental.jpg)

| Avoid component-only planning | Prefer vertical increments |
|---|---|
| Sprint 1 — database only · Sprint 2 — back end only · Sprint 3 — front end only | Story A / B / C — UI → API → rule → DB → test → CI |

Each sprint can deliver a small end-to-end capability instead of a disconnected technical layer.

Why? Every Sprint produces integrated, testable behaviour and exposes architecture problems early.

A story should become a thin, working path through the architecture

🇨🇳 垂直切片：为增量交付而设计。避免只按组件计划（第 1 轮只做数据库、第 2 轮只做后端、第 3 轮只做前端）；优先垂直增量（每个故事 界面 → API → 规则 → 数据库 → 测试 → CI）。为什么？每个 Sprint 都产出集成好、可测试的行为，并尽早暴露架构问题。一个故事应该成为穿过架构的一条细细的、能跑的路径。

💬 **讲师补充**：Sprint 1 里用切片做几个故事，就能 **早点从用户 / 客户那里拿反馈**，边做边测试、细化设计和架构——不是一开始做一个大决定就完了。你会有 **明确的证据** 知道哪里需要改、东西怎么工作；要测更大流量也能早测、早发现、早改。**早期的改动让团队的日子好过得多。**

---

### 51 · Emergent architecture in Scrum

![](images/51_emergent_architecture.jpg)

Sprint 1 (Simple web app: UI + API + DB) → Feedback (More rules · More tests · New quality needs) → Sprint 2 (Introduce modules · Isolate persistence · Improve API) → Evidence (Traffic grows · Async work appears) → Later (Extract worker/service only if justified)

Emergent ≠ accidental
Architecture still needs intentional decisions, tests, refactoring and team communication. The difference is that decisions are revisited as evidence grows.

Design enough now, learn from the increment, then improve the structure

Reference: Agile Manifesto principle 11; Scrum inspection and adaptation

🇨🇳 Scrum 中的涌现式架构：Sprint 1（简单 Web 应用：UI + API + DB）→ 反馈（更多规则、更多测试、新的质量需求）→ Sprint 2（引入模块、隔离持久化、改进 API）→ 证据（流量增长、出现异步工作）→ 以后（只有有理由时才抽出 worker / 服务）。**涌现 ≠ 随意**：架构仍然需要有意识的决策、测试、重构和团队沟通，区别只是决策会随证据增加被重新审视。现在设计够用就好，从增量里学习，再改善结构。

💬 **讲师补充**
- 涌现式架构 **不是偶然的**：每次做用户故事、演进设计和架构时都要有决策。现在设计够用，不必完美；从增量和收集到的反馈里学习，下个 Sprint 改进结构。
- **"虽然我们不要求你们展示设计和架构，但希望这种思维指导你们的决策"**：怎么拆职责、组件放哪、在哪实现。
- **Sprint 结束 ≠ 项目或开发结束**，收集到更多反馈后可以继续改进。

---

### 52 · Applying the ideas to your COMP9820 project

![](images/52_applying_to_project.jpg)

1. Before implementation — Agree on a simple system boundary and initial architecture
2. During the sprint — Keep design decisions visible in issues, merge requests and documentation
3. Before merging — Check responsibility boundaries, tests and integration
4. During review — Demonstrate working behaviour and collect stakeholder feedback
5. During retrospective — Record design or process improvements for the next sprint

🇨🇳 把这些想法用到你们的 COMP9820 项目：1 实现前——全组商定一个简单的系统边界和初始架构；2 Sprint 中——把设计决策写在 Issue、MR 和文档里让大家看得见；3 合并前——检查职责边界、测试和集成；4 评审时——演示能跑的行为、收集相关方反馈；5 回顾时——记下下个 Sprint 要做的设计或流程改进。

💬 **讲师补充**：这页课上没有逐条展开，直接进入要点总结。

---

### 53 · Key takeaways (1)

![](images/53_key_takeaways_1.jpg)

Architecture should make the next change easier, not merely look sophisticated

- Architecture organises the major parts of a system.
- Design principles help teams control responsibility and dependencies.
- Web applications separate front-end, API, back-end and data concerns.
- MVC and layered architecture are useful patterns, not universal rules.
- Agile architecture evolves through increments, feedback and refactoring.
- Good design makes software easier to understand, test, maintain and extend.

🇨🇳 要点（1）——架构应该让下一次改动更容易，而不是看起来更高级：架构组织系统的主要部分；设计原则帮团队管住职责和依赖；Web 应用把前端、API、后端、数据分开；MVC 和分层是有用的模式而不是万能规则；敏捷架构靠增量、反馈和重构演进；好设计让软件更容易理解、测试、维护、扩展。

💬 **讲师补充**：两页要点讲师没有逐条念，留给大家自己看——它们总结了今天的关键内容。

---

### 54 · Key takeaways (2)

![](images/54_key_takeaways_2.jpg)

Architecture should make the next change easier, not merely look sophisticated

1. Agile still needs design — Design happens continuously and evolves with feedback.
2. Start with responsibilities — Separate UI, business rules, persistence and integration concerns.
3. Keep boundaries clear — Cohesion, low coupling and encapsulation improve changeability.
4. Patterns are tools — Layered architecture and MVC are useful starting points; modern patterns add trade-offs.
5. Quality drives architecture — Security, testability, scalability and maintainability shape decisions.
6. Prefer simple evolution — A modular starting point can evolve when evidence justifies more complexity.

Good architecture supports working software today and safe change tomorrow.

🇨🇳 要点（2）：1 敏捷仍然需要设计——设计持续发生、随反馈演进；2 从职责开始——把界面、业务规则、持久化、集成分开；3 边界清楚——内聚、低耦合、封装提高可改性；4 模式是工具——分层和 MVC 是好起点，现代模式各有取舍；5 质量驱动架构——安全、可测试、可扩展、可维护决定选择；6 简单演进——模块化的起点在证据证明需要时再加复杂度。好架构 = 今天软件能跑，明天改动安全。

💬 **讲师补充**：这页课上只停留了几秒钟就切到 Sprint 1 评估，内容请自行阅读。

---

### 55 · Sprint 1 Assessments

![](images/55_section_sprint1.jpg)

Sprint 1 Assessments

🇨🇳 章节页：Sprint 1 评估。

💬 **讲师补充**
- Sprint 1 评估已经发布，内容聚焦第 1、2 周（主要是第 2 周）讲的东西。Sprint 1 要做：
  - **Demo（10%）**，在你们的 lab 里演示——这是让学生 **开口讲、沟通自己的工作** 的一种方式，很重要。每个队在自己的 lab 演示，还要 **提交录像作为证据**。
  - **Team Report**，覆盖后面几页讲的所有要点。
  - **Peer Evaluation**：每个成员评价其他成员。目标是 **建设性反馈，不是指责别人的弱点**，而是帮助别人在下个 Sprint 改进。
  - **Individual Report**：你个人怎么反思自己做的工作和贡献。
- **Sprint 1 总共占 30%**。

---

### 56 · Sprint 1: what's due and when

![](images/56_sprint1_due.jpg)

- Demo (10%): live in your Week 4 lab (7–9 October); recording due Sunday 11 October, 9 pm
- Team Report (15%): Sunday 11 October, 9 pm, one submission per team via Turnitin
- Peer Evaluation (1%): opens Wednesday of Week 4, closes Sunday 11 October, 9 pm
- Individual Report (4%): Sunday 18 October, 9 pm

Sprint 1 is 30% of the course. Full details on the "Project Sprint 1 Guidelines" page in Moodle.

🇨🇳 Sprint 1 交什么、什么时候交
- Demo（10%）：第 4 周 lab 现场演示（10 月 7–9 日）；录像 10 月 11 日周日晚 9 点前交
- Team Report（15%）：10 月 11 日周日晚 9 点，每队一份，通过 Turnitin 提交
- Peer Evaluation（1%）：第 4 周周三开放，10 月 11 日周日晚 9 点关闭
- Individual Report（4%）：10 月 18 日周日晚 9 点
Sprint 1 占课程总分 30%。细则见 Moodle 的 "Project Sprint 1 Guidelines" 页面。

💬 **讲师补充**：细则都在 Moodle 的 Project Sprint 1 Guidelines 里。

---

### 57 · The Demo in next week's lab

![](images/57_demo.jpg)

- 10–12 minutes, then questions from your tutor and the other teams
- Every member attends and presents a part; absence without special consideration is 0 for that student
- Show the Shared Expense Splitter features you built, running live on your own machine
- Show how the sprint was run: backlog, issue board, issues, branches, merge requests
- Record the session and submit the MP4 to Moodle (used for cross-marking and special consideration)

Have the app running and your GitLab tabs open before your slot starts

🇨🇳 下周 lab 的 Demo
- 10–12 分钟，然后 tutor 和其他队提问
- 每个成员都要到场并讲一部分；没有 special consideration 的缺席者这项 0 分
- 在自己的电脑上现场运行，展示你们做出来的 Shared Expense Splitter 功能
- 展示 Sprint 是怎么跑的：backlog、看板、Issue、分支、MR
- 全程录像，MP4 交到 Moodle（用于交叉评分和特殊情况）
轮到你们之前就把应用跑起来、GitLab 页面打开。

💬 **讲师补充**
- Demo 是讲给 **tutor 和其他队** 听的——**要想着不同的听众**，这是关键。
- **每个成员必须出席并演示**；有特殊情况不能来的要 **申请 special consideration，才能拿到团队分**。
- 两部分：一是应用——展示实现的功能；二是 **你们应该按 Scrum 做了**，要展示 / 强调 Sprint 是怎么跑的，我们要确认你们作为团队做对了。
- 应用先跑起来、GitLab 标签页先打开——**为了效率**。

---

### 58 · Team Report, Peer Evaluation and Individual Report

![](images/58_reports.jpg)

- Team Report, about 15 pages, five parts:
  - Scrum roles, role allocation and meeting minutes (3%)
  - Sprint planning: user stories, acceptance criteria, points, sprint goal (4%)
  - Sprint tracking: issue board, meetings, Git workflow (3%)
  - Velocity: points committed versus completed, and what it tells you (2%)
  - Retrospective: what went well, what did not, things to try in Sprint 2 (3%)
- Peer evaluation is 1% for submitting on time (there are no late submissions)
- Individual report (4%, W5): your own contribution, evidence from issues and merge requests

🇨🇳 团队报告、互评、个人报告
- Team Report 约 15 页，5 个部分：Scrum 角色、分工和会议记录（3%）；Sprint 计划：用户故事、验收标准、故事点、Sprint 目标（4%）；Sprint 跟踪：看板、会议、Git 流程（3%）；速度：承诺 vs 完成的点数及其说明（2%）；回顾：做得好的、不好的、Sprint 2 要尝试的（3%）
- 互评按时提交得 1%（不接受迟交）
- 个人报告（4%，第 5 周）：你自己的贡献，证据来自 Issue 和 MR

💬 **讲师补充**
- **Velocity 这部分：没有对错，重点是解释和说明理由。** 讲 Scrum 时就说过，很多事不是对错问题，而是你要 **解释并论证**——表明你们正确地按敏捷 / Scrum 做了（Scrum Master 要确保这点），同时能说明理由。比如 **承诺了 15 个故事点、完成了 12 个，解释发生了什么**：这是估算，而且这是你们跑的第一个 Sprint。**我们要看到你们的理解，而不是盲目地走流程**——报告里要能解释、能说清楚。
- **Peer Evaluation 必须按时交，不允许迟交**，除非有批准的 special consideration 或 ELP（Equitable Learning Plan）。
- **Individual Report** 在团队报告 **一周之后**：谈你的贡献和工作证据。它让你持续思考、反思自己在做什么、怎么改进、对团队的贡献是什么——我们通过它评估个人贡献。

---

### 59 · References

![](images/59_references.jpg)

- Agile Manifesto. https://agilemanifesto.org/
- Schwaber, K. and Sutherland, J. The Scrum Guide, 2020. https://scrumguides.org/scrum-guide.html
- MDN Web Docs. Client-server overview. https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview
- MDN Web Docs. HTTP. https://developer.mozilla.org/en-US/docs/Web/HTTP
- C4 model. Introduction and abstractions. https://c4model.com/introduction and https://c4model.com/abstractions
- Pallets Projects. Flask documentation: application lifecycle and project layout. https://flask.palletsprojects.com/en/stable/lifecycle/
- Martin Fowler. Microservices. https://martinfowler.com/articles/microservices.html
- AWS. Event-driven architecture. https://aws.amazon.com/event-driven-architecture/

🇨🇳 参考资料（讲师说：这些是他用到的参考，想看更多内容可以去读）。

---

### 60 · Thank you

![](images/60_thank_you.jpg)

Questions and discussion

🇨🇳 谢谢——提问与讨论。

💬 **讲师补充**
- 感谢大家留到最后并参与。**下周讲软件测试**——很大的主题，是 **Sprint 2 和 Sprint 3 的重要部分**，也是在开始 CI/CD 之前的桥梁：测试是持续集成（CI）的重要组成部分。
- 有问题可以下来找讲师聊。

---

## 课上未放映的页面（PDF 里有，录像里没有出现）

> 4 张章节过渡页课上被直接跳过；3 页附录（PDF 第 65–67 页）讲师没有讲到——其中 **事件驱动架构** 讲师在课堂活动时说"后面会讲"，但最终没有展开。内容仍值得自学，这里照录。

### x1 · Software Architecture and Design — Core principles（章节页）

![](images/x1_section_software_architecture_design.jpg)

🇨🇳 章节页：软件架构与设计——核心原则。

### x2 · Typical Architectural Patterns（章节页）

![](images/x2_section_typical_patterns.jpg)

🇨🇳 章节页：常见架构模式。

### x3 · ARCHITECTURE DECISIONS — Making architecture choices and trade-offs（章节页）

![](images/x3_section_architecture_decisions.jpg)

🇨🇳 章节页：架构决策——做架构选择与取舍。

### x4 · DESIGN IN SCRUM — Design decisions are part of the sprint（章节页）

![](images/x4_section_design_in_scrum.jpg)

🇨🇳 章节页：Scrum 中的设计——设计决策是 Sprint 的一部分。

### x5 · Event-driven and serverless patterns（附录）

![](images/x5_event_driven_serverless.jpg)

Event-driven: Producer (Expense created) —event→ Event router / queue (Expense created) → Notification (send receipt) / Analytics (update dashboard)

Serverless idea: Run small functions or managed services on demand rather than managing long-running servers. Useful for event-triggered tasks, APIs and variable workloads.

- Useful when work is asynchronous, bursty or naturally triggered by events
- Trade-off: asynchronous systems can be harder to trace, test and reason about.

References: AWS event-driven architecture and serverless documentation

🇨🇳 事件驱动与无服务器模式。事件驱动：生产者（"开销已创建"）发出事件 → 事件路由 / 队列 → 通知服务（发收据）/ 分析服务（更新仪表盘）。无服务器：按需运行小函数或托管服务，而不是维护长期运行的服务器；适合事件触发的任务、API 和波动的负载。适用于异步、突发或天然由事件触发的工作；取舍：异步系统更难追踪、测试和推理。

### x6 · Design for non-functional properties（附录）

![](images/x6_design_for_non_functional.jpg)

Architecture is where many quality trade-offs become visible

| Quality | Design question | Typical design responses |
|---|---|---|
| Security | Where are trust boundaries? Who can access what? | Server-side authorisation, least privilege, secure defaults |
| Scalability | What may grow independently? | Stateless APIs, caching, queues, selective decomposition |
| Performance | Where is time spent? | Fewer network calls, efficient queries, caching |
| Reliability | What happens when dependencies fail? | Timeouts, retries, graceful failure, observability |
| Maintainability | How local is a change? | Clear modules, low coupling, automated tests |
| Deployability | Can changes move safely? | Small increments, configuration, CI/CD-friendly boundaries |

🇨🇳 面向非功能属性的设计——架构是很多质量取舍变得可见的地方

| 质量 | 设计问题 | 典型应对 |
|---|---|---|
| 安全 | 信任边界在哪？谁能访问什么？ | 服务端授权、最小权限、默认安全 |
| 可扩展性 | 什么可能独立增长？ | 无状态 API、缓存、队列、有选择地拆分 |
| 性能 | 时间花在哪？ | 更少的网络调用、高效查询、缓存 |
| 可靠性 | 依赖失败了怎么办？ | 超时、重试、优雅降级、可观测性 |
| 可维护性 | 一次改动有多局部？ | 清晰模块、低耦合、自动化测试 |
| 可部署性 | 改动能安全上线吗？ | 小增量、配置化、对 CI/CD 友好的边界 |

### x7 · How do we choose an architecture?（附录）

![](images/x7_how_choose_architecture.jpg)

Use constraints and evidence, not fashion

| Product | What are the highest-value user journeys? |
|---|---|
| Change | Which parts may evolve independently? |
| Operations | How much deployment and monitoring complexity can we support? |
| Team | What can this team understand, test and operate? |
| Quality | Which non-functional properties matter now? |
| Evidence | What have we learned from previous increments? |

For a small Agile web project, start with the simplest architecture that preserves clear boundaries.

🇨🇳 怎么选架构？——看约束和证据，不看潮流。产品：最有价值的用户路径是什么；变化：哪些部分会独立演进；运维：我们撑得起多复杂的部署和监控；团队：这个团队能理解、测试、运维什么；质量：现在哪些非功能属性最重要；证据：前几个增量教会了我们什么。对小型敏捷 Web 项目：从最简单但边界清楚的架构开始。

---

## 本周待办清单

1. **Sprint 1 收尾**：本周末前把 Shared Expense Splitter 的功能做到能现场演示；按讲师建议，后端 / 数据库可以先用简单的"假服务"（如读文件）替代，但要放在单独的组件里。
2. **准备下周 lab 的 Demo（10%）**：10–12 分钟；**每个成员都要到场并讲一部分**（缺席且无 special consideration 得 0）；想着听众是 tutor 和其他队；演示功能 + 演示 Sprint 过程（backlog、看板、Issue、分支、MR）；提前把应用跑起来、GitLab 页面开好；**全程录屏**，MP4 10 月 11 日前交 Moodle。
3. **Team Report（15%）**：约 15 页、5 部分（角色与会议记录 3%、计划 4%、跟踪 3%、速度 2%、回顾 3%），10 月 11 日周日 9 pm 前每队一份经 Turnitin 提交；速度部分要 **解释并论证**（承诺 vs 完成），展示理解而不是走流程。
4. **Peer Evaluation（1%）**：第 4 周周三开放，10 月 11 日 9 pm 关闭，**不接受迟交**；写建设性反馈。
5. **Individual Report（4%）**：10 月 18 日 9 pm；写自己的贡献，证据来自自己的 Issue 和 MR——所以平时就要用自己的账号提交。
6. 设计与架构 **本 Sprint 不评估**，但建议全组先商定一个简单的系统边界（一张语境图 + 一张容器图即可），每个故事按 **垂直切片** 做（UI → API → 规则 → DB → 测试），避免"一人做全部后端、一人做全部前端最后再集成"。
7. 自学 PDF 附录 3 页（事件驱动 / 无服务器、面向非功能属性的设计、怎么选架构）。
8. 下周主题：**软件测试**（Sprint 2、3 的重点，CI 的前置）。
