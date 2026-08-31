# Sprint 2 — Quality, CI & Deployment（详细任务）

> 周期：Weeks 4–6 · 截止：**Week 7 Monday 12:00（2026-03-30）** · 权重：Group **25%** + Individual **5%**
> 来源：Week 4 开场 Project Sprint 2 Guidelines 走读（§1–§7）+ 休息期间关于功能与评分基线的 Q&A；Week 4 讲座（TDD、pytest、CI pipeline）；Week 5 讲座（覆盖率、可维护性、Sprint 2 rubric 难度说明）；Week 7 回顾（Week 6 deployment lab、Sprint 2 结束）。
> ⚠️ **资料缺口说明**：Week 4 讲座时指南的 §4.5 Code coverage and quality、§4.6 Deployment、§5 详细评分表均标注 "coming soon"（讲师承诺次日定稿）；Week 6（Deployment/DevOps）没有讲义文件夹。本文件中评分细则以已公布的要求 + 后续讲座透露的标准（如 Sprint 3 沿用的 "Sprint 2 bar"：CI 绿、后端覆盖率 > 70%）整理，**最终 rubric 以课程网站为准**。

---

## 目录

1. [概览与目标](#1-概览与目标)
2. [建议周计划（Suggested Weekly Planner）](#2-建议周计划suggested-weekly-planner)
3. [实践与期望（§4 原文 + 讲师解释）](#3-实践与期望4-原文--讲师解释)
4. [任务清单（按交付物）](#4-任务清单按交付物)
5. [技术要点速查：TDD / pytest / CI / Coverage / 可维护性](#5-技术要点速查tdd--pytest--ci--coverage--可维护性)
6. [评分标准（已知信息）](#6-评分标准已知信息)
7. [提交与 Demo（§6）](#7-提交与-demo6)
8. [课堂 Q&A 要点汇总](#8-课堂-qa-要点汇总)
9. [Sprint 2 任务总结](#9-sprint-2-任务总结)

---

## 1. 概览与目标

**指南原文（🚀 1. Overview）**

> With Sprint 1 behind them, the Procrastination Warriors have a working Task Tracker and solid team habits. Sprint 2 shifts the focus from *building* to *building well*: automated testing, continuous integration, code quality, and getting the app ready to run in a real environment. By the end of Sprint 2, your team should have a tested, quality-checked, and deployed Task Tracker, with clear evidence of ongoing collaboration and planning.

**🎯 2. Sprint 2 Goals（原文）**
- Practice **quality-first** development: tests written (ideally before or alongside code), coverage tracked, and code kept clean.
- Set up and use a **CI pipeline** (e.g. GitLab CI) that runs tests and quality checks on merge requests and main.
- Improve **issue board** usage: link issues to MRs, use labels and milestones, and use the board for sprint planning and tracking.
- Hold **weekly team meetings** and document them (e.g. in repo or Wiki); use standups and the issue board to keep progress visible.
- (Pending) **Deploy** the application (e.g. GitLab Pages, a simple host, or another approved platform) and demonstrate it in the Week 7 lab.
- Deliver **new features** (beyond add/delete) as planned in your user stories, with tests and CI in place.

**讲师定位**
- 重点从"做出来"转为"**做得好**"：自动化测试、持续集成、代码质量、部署。
- 团队管理要求与 Sprint 1 相同但**期望更高**；Sprint ritual（standup、retro、互评、demo、推 main 提交）与 Sprint 1 相同。
- **功能由你们自己的用户故事决定**（Sprint 1 所有组做同样的 add/delete 是因为还没学故事）；课程不规定"加登录/加用户"；Sprint 末按**给用户带来的价值**评分。
- **Sprint 2 rubric 比 Sprint 1 更有挑战**：工作量更大、质量要求更高，拿 HD 更难。
- 曾考虑只按测试/CI 评分不要求新功能，但不写新功能就无法练"测试先于实现"、pipeline、协作——所以仍以好的最终产品为目标。

---

## 2. 建议周计划（Suggested Weekly Planner）

| Week | Focus | Tasks（原文） |
|---|---|---|
| 4 | Testing & CI | Weekly meeting; add unit/integration tests; set up CI pipeline (run tests on push/MR); update issue board with testing tasks; standups. |
| 5 | Coverage & quality | Weekly meeting; improve code coverage; refactor for clarity/maintainability; run coverage and lint in CI; plan deployment; standups. |
| 6 | Deployment & polish | Weekly meeting; deploy app; fix deployment issues; finish features and tests; sprint retro & teamwork evaluation; standups. |

Relevant lectures: Week 4 (Testing, CI), Week 5 (Coverage, Refactoring), Week 6 (DevOps).

讲师："和 Sprint 1 一样，按这个周计划走，sprint 末就不会有问题。"

---

## 3. 实践与期望（§4 原文 + 讲师解释）

### 4.1 Weekly meetings
> - Hold **at least one full team meeting per week** during Sprint 2 (Weeks 4–6).
> - Document each meeting (e.g. agenda, decisions, action items) in a timestamped place in your repo (e.g. `meetings/`, Wiki, or `MEETING_MINUTES.md`).
> - Use meetings to: align on CI/deployment approach, assign issues, review progress on the issue board, and address blockers.

💬 Sprint 1 只要求 standup；Sprint 2 起**每周至少一次全员会议**——可直接在 live class 上开（人齐省时间），但**不是说不用课外开会**。会后要 meeting minutes；不爱写文档可用 Teams 录制 + AI 纪要。只要求：开了会、有 action items、有计划。**每周一次是最低要求。**

### 4.2 Issue board – advanced use
> - Use the **issue board** as the single place for sprint work: **Labels**: e.g. bug, feature, testing, deployment, documentation. **Milestones**: e.g. "Sprint 2" or "Week 4 – CI". **Link MRs to issues**: "Closes #X" in merge request descriptions. **Assignees** and **due dates** where useful.
> - Keep the board up to date (e.g. move issues across To Do / In Progress / Done) so your tutor can see how work is tracked.

💬 Sprint 1 提过 MR 关联 issue 但没要求；**Sprint 2 要求 MR 链接 issue**（描述里 `Closes #X`，合并后自动关闭）。Milestones 和 labels **可选**。

### 4.3 Git and merge requests
> - Continue **Sprint 1 Git practice**: work on feature branches, no direct commits to **main**, merge via Merge Requests (MRs).
> - **At least one MR per person** into **main** during Sprint 2, with peer review and approval.
> - MRs should reference the CI pipeline (e.g. "pipeline passed") and, where relevant, link to issues.

💬 要求同 Sprint 1，但讲师口头表示**不再像 Sprint 1 那样严格要求"每人一个 MR"**（那是为了人人练到），按团队实际情况规划。（网页文本仍写着 at least one MR per person。）

### 4.4 CI pipeline
> - **Required**: A CI pipeline (e.g. GitLab CI) that: Runs on push and/or on merge requests. Executes your test suite. Optionally: runs coverage, failing tests or quality checks should block merging when configured.
> - Configuration (e.g. `.gitlab-ci.yml`) must be in the repo and working at submission time.

### 4.5 Code coverage and quality — *coming soon*（Week 5 讲座内容）
- 安装 `pytest-cov` 并加进 `requirements.txt`（便于 pipeline 里跑）；`pytest --cov --cov-report=term-missing` / `--cov-report=html`。
- 根据 Missing 行补测试（把 Sprint 1 已有实现但没测试的 add/delete 补回来）；**不追求 100%**；覆盖边界/错误路径（空输入、非法 index）而不只 happy path；关注分支覆盖。
- 重构提升可维护性：7 个设计问题（DRY / KISS / over-under design / coupling / YAGNI / conventions）；**没有强测试套件不要重构**。
- 周计划提到 "run coverage and lint in CI"。
- 后续 Sprint 3 rubric 把 "Backend code coverage above 70%" 作为 "Sprint 2 bar" 的延续——可视为 Sprint 2 的目标线。

### 4.6 Deployment — *coming soon*（Week 6 讲座；标 Pending）
- 目标原文："(Pending) Deploy the application (e.g. GitLab Pages, a simple host, or another approved platform) and demonstrate it in the Week 7 lab."
- Week 6 有 **deployment lab**，平台为 **Vercel**（Week 7 学生问"是否必须只部署到 Vercel"）。Week 9 讲师："如果你还没做 deployment lab，我强烈建议你试一下——看到自己的应用上线很有意思。"
- 到 Sprint 3 明确**不强制部署**（UNSW IP 考虑），localhost 即可。

### 4.7 Participation and standups
> **Standups**: 3 standups per week, including at least one in the lab with your tutor. Standups can be documented in your chosen place (e.g. MS Teams channel or repo); your tutor may ask to see evidence.

💬 Sprint 1 每周 2 次，Sprint 2 每周 **3 次**；不是视频会，在 Teams 频道发消息即可；最多 15 分钟，通常 5 分钟够。

### 4.8 Sprint retro and teamwork evaluation
> Run a **Sprint 2 retrospective** (what went well, what to improve, action items for Sprint 3). Complete the teamwork evaluation after Sprint 2 is due (link will be sent after Sprint 2 is due). Store the retro summary (and any updated team contract) in the repo.

💬 Sprint 2/3 的 retro **必须在截止前交**（Sprint 1 的迟交例外仅一次）。契约更新：Quality Standards 里 **Sprint 2 正式定义 Definition of Done**。

---

## 4. 任务清单（按交付物）

### ☑ A. 新功能（来自自己的用户故事）
- [ ] 从 `stories.md` 里挑本 Sprint 的故事（只规划下一个 Sprint），每个故事一个 issue（含 UAC）。
- [ ] **按 TDD 实现**：从故事写核心测试 → 写最少代码通过 → 重构 → 补边界（如"空任务不添加"可作为一个故事）。
- [ ] 先提交测试、再提交实现——**git 历史就是"测试先于实现"的证明**。
- [ ] Feature 分支 + MR（描述写 `Closes #X`、注明 pipeline passed）+ peer review + 作者合并；main 不直接改。

### ☑ B. 自动化测试（pytest）
- [ ] `pip install pytest`（Mac `pip3`），`pytest` 与 `Flask` 写进 `requirements.txt`。
- [ ] 建 `tests/`（如 `tests/test_app.py`）与根目录 `conftest.py`（文件名固定）：`client` fixture，**每个测试前重置数据**（测试之间不能互相影响）。
- [ ] 测试命名 `test_*`；用 `assert`；`response.data` 是 bytes → `b"..."`；可用 class 分组。
- [ ] 本地 `pytest` / `pytest -v` 全绿。

### ☑ C. CI pipeline（必做）
- [ ] 仓库根目录 `.gitlab-ci.yml`（文件名必须完全一致）：
  ```yaml
  stages:
    - test

  test:
    stage: test
    image: python:3.11
    before_script:
      - pip install -r requirements.txt
    script:
      - pytest
  ```
- [ ] 可用 GitLab **Build → Pipeline editor**（有模板 + 语法检查；YAML 对缩进极严格）。
- [ ] push / MR 触发后确认 **绿勾**；红叉看 job 日志定位。
- [ ] 可选：`only: - main` 只在 main 跑；加覆盖率/lint。
- [ ] 规则：**main 永远绿**——reviewer approve 前、作者 merge 前都确认 pipeline passed。
- [ ] 提交时配置必须**存在且能工作**。

### ☑ D. 覆盖率与代码质量
- [ ] `pip3 install pytest-cov`，加入 `requirements.txt`；跑 `pytest --cov --cov-report=term-missing` 与 `--cov-report=html`（`htmlcov/index.html`）。
- [ ] 按 Missing 行补测试；目标线参考 >70%（Sprint 3 延续标准）；不刷廉价测试。
- [ ] 在有测试保护的前提下重构：问 7 个设计问题；清晰 > 聪明；不写"将来可能用到"的代码。

### ☑ E. 周会（每周 ≥1 次，Weeks 4–6）
- [ ] 会议纪要（议程、决策、行动项）存仓库 `meetings/`（或 Wiki / `MEETING_MINUTES.md`），带时间戳。
- [ ] 用途：对齐 CI/部署方案、分配 issue、review board 进度、处理 blocker。

### ☑ F. Standups（每周 3 次）
- [ ] Teams 频道三问 + action items；至少 1 次在 lab 当着 tutor。

### ☑ G. Issue Board 进阶
- [ ] MR ↔ issue 链接（`Closes #X`，必做）；labels / milestones / assignee / due date（可选）；To Do / In Progress / Done 保持最新。

### ☑ H. 部署（Pending / 可选）
- [ ] 完成 Week 6 deployment lab（Vercel）；若部署成功在 Week 7 lab 展示。

### ☑ I. Retro + 互评 + 契约更新
- [ ] Sprint 2 retro（截止前交，含 Sprint 3 的 action items）；retro 摘要与更新的契约（含 DoD）存仓库。
- [ ] 截止后完成 Moodle Teamwork Evaluation。

### ☑ J. 提交与 Demo
- [ ] Week 7 周一 12:00 前推 main；**不要最后一刻集中 push**（共享 runner 排队）。
- [ ] Week 7 lab 全员到场 demo。

---

## 5. 技术要点速查：TDD / pytest / CI / Coverage / 可维护性

### TDD
- 定义：写一个描述期望行为的**失败测试**（Red）→ 写**最少**代码让它通过（Green）→ 重构（Refactor）→ 重复。
- **The Rule**：Don't write any production code unless you have a failing test. 测**行为**不测实现（黑盒）。
- 常见误解：不是"先写完所有测试再写所有代码"；TDD 是增量的。
- 顺序"由内向外剥洋葱"：Core（index 显示任务）→ Happy path（add）→ Special cases（空/空白输入不添加）→ More behaviour（delete；非法 index 不崩溃）。
- 为什么先写测试：从用户价值先设计再实现；测试是活文档；减少偏见；安全重构；快速反馈。**全绿 ≠ 没 bug**（只说明你测的都对）。
- 再自信也先写测试；先让测试过再重构。

### pytest 示例
```python
# conftest.py
import pytest
import app as app_module
from app import app

INITIAL_TASKS = ["Complete Flask tutorial", "Learn Python basics", "Build a web app"]

@pytest.fixture
def client():
    app_module.tasks = list(INITIAL_TASKS)
    with app.test_client() as c:
        yield c
    app_module.tasks = list(INITIAL_TASKS)
```
```python
# tests/test_app.py
def test_index_shows_tasks(client):
    response = client.get("/")
    assert b"Complete Flask tutorial" in response.data

class TestIndex:
    def test_index_loads(self, client):
        response = client.get("/")
        assert b"Task Tracker" in response.data
```
- Add：POST `/add` 后 GET `/` 检查文本出现；Empty：POST 空任务后数量不变；Delete：访问 `/delete/<i>` 后任务消失、非法 index 不崩溃。

### CI（GitLab）
- CI = 自动把多个贡献者的变更集成到单一项目，让合入 main 更**频繁、稳定**；简化说：每次 commit/MR 自动跑 pytest，并在 GitLab 显示绿勾/红叉。
- **Runner** = 专门跑 pipeline 的另一台电脑；CSE 为 COMP9820 项目配了共享 runner（个人项目可能没有）。
- 概念：stages（build → test → deploy，前一阶段过了才进下一阶段）、job、`image`（全组同一 Python 版本）、`before_script`（装依赖）、`script`（`pytest`；非零退出即失败）。
- 总结流程：写测试 → 写实现 → push + MR → 看到绿勾 → 放心合并。
- 进一步阅读：GitLab CI 文档、Atlassian CI 教程。

### Coverage
- Test coverage（功能被测多少，人判断）vs **Code coverage**（测试执行了多少代码，可量化）。最有用的是**没执行的部分**。
- 报表列：Stmts / Miss / Cover / Missing；HTML 报告 Files / Functions / Classes 视图，绿=执行过、红=缺失。
- 管理视角（Theory X vs Y）：指标是对话起点不是记分板；"必须 90%"命令必然导致廉价测试与失调；AI 让刷数字更容易——**不合并不理解的 AI 代码**。
- 工具补充：**diff-cover** 只算 diff 行覆盖率（Week 7 学生推荐）。

### 可维护性（7 个设计问题）
1. 唯一事实来源？（DRY）2. 尽可能简单？（KISS，clear > clever，"没写的代码没 bug"）3. 过度/不足设计？（重复两次可接受）4./5. 相关靠近、无关分开？（耦合，避免 spaghetti）6. 在臆测必要性？（YAGNI，功能来自需求工程——没人要就不做"导出 PDF"）7. 遵循惯例？（Flask 流行；别用 C 写 Web）。
- 重构 = 不改外部行为地重组代码；**没有强测试套件不要重构**；AI 可辅助但设计决策与审批由人负责。

---

## 6. 评分标准（已知信息）

指南 §5 原文：

> **📝 5. Sprint 2 Submission and Marking Rubric** — Detailed criteria coming soon.
> **5.2 Individual marking (overview)** — Detailed criteria coming soon.

已知框架与讲师说明：
- 权重：Group **25** + Individual **5**（Assignments Overview）。
- 组分考察点（由 §2 Goals、§4 要求与 Week 7 demo 内容推断）：新功能及其**测试**（TDD 证据在 git 历史）、**CI pipeline**（提交时存在且工作、main 绿）、**覆盖率与代码质量**、**周会纪要**、**issue board 进阶使用**（MR 链接 issue）、**Git/MR 实践**、**retro + 互评**、（pending）部署。
- 个人分考察点：Git commit/branch/MR 贡献、standup 参与（每周 3 次）——与 Sprint 1 / Sprint 3 结构一致。
- **功能数量不是评分依据**：讲师故意不设最低功能数基线，评"给用户带来的价值"与过程质量；评分细则在 Week 4 周二晚定稿（本资料未收录）。
- Sprint 3 沿用的 "Sprint 2 bar"（可作参考标准）：CI green on main、tests cover important behaviour、**backend code coverage above 70%**、MR reviewable、issues 有 AC、MR `Closes #n`。
- 讲师警告：**Sprint 2 rubric 比 Sprint 1 更难拿 HD**；Sprint 3 更难。

---

## 7. 提交与 Demo（§6）

> - **Sprint 2 deadline: Week 7 Monday 12:00 (midday)**.
> - **Submission**: Push your final work to the main branch on GitLab before the deadline. The latest commit on main before the deadline will be marked. Late submissions are not accepted unless special consideration applies (see course website).
> - **Demo**: During the **Week 7 lab**, your team will demonstrate: New features and how they are tested. CI pipeline (e.g. show a pipeline run, coverage report). Where meeting minutes, retro, and issue board live.
> - **Attendance**: All team members must attend the Sprint 2 demo. Absence may result in 0 for this sprint unless special consideration is approved.
> **✍️ 7. Plagiarism and academic integrity** — The same rules as Sprint 1 apply...

---

## 8. 课堂 Q&A 要点汇总

| 问题 | 答案 |
|---|---|
| Sprint 2 到底做什么功能？ | 你们自己故事里的功能；课程不规定；按用户价值评分。 |
| 有没有最低功能数基线？ | 讲师故意不按数量；征求学生意见后次日定稿 rubric。 |
| 需要写文档证明"测试先于实现"吗？ | 不需要，git 历史就是文档（先提交测试再提交实现）。 |
| 明天按 TDD 做，下一步？ | 看用户故事，用故事写核心测试；先主要用例再补边界。 |
| 先写完所有测试再写实现？ | 不是；核心测试 → 实现 → 随时补测试。 |
| 测试过了但想重构？ | 先用最少努力让测试通过，再重构。 |
| 很确定怎么写，能先写代码再补测试？ | 不能，再自信也先写测试。 |
| standup 15 分钟要开视频会？ | 不用，Teams 频道发消息即可；"15 分钟"只是强调要快。 |
| 每周会议可以在课上开、不用课外开？ | 可以在课上开省时间，但没说不用课外开；每周一次是最低要求。 |
| pipeline 能按 feature 出覆盖率报告？ | 讲师不确定，鼓励研究；最低限度看 feature 分支的覆盖率。 |
| pytest 全绿能说软件正确吗？ | 不能——测试可能不全面；TDD 揭示 bug 不防止 bug。 |
| AI 对重构有帮助吗？ | 有（如语言迁移），但审查量巨大；脑子里要有架构；不合并不理解的代码。 |
| Sprint 1 成绩？ | Moodle Grades，平均 > HD；Sprint 2/3 rubric 更难。 |

---

## 9. Sprint 2 任务总结

**一句话**：在 Sprint 1 的团队习惯之上，把"质量"变成习惯——用 TDD + pytest 为自己故事里的新功能写测试，用 `.gitlab-ci.yml` 让每次 push/MR 自动跑测试并保持 main 永远绿，用 pytest-cov 找测试缺口并在测试保护下重构，同时升级团队流程（周会 + 纪要、3 次/周 standup、MR 链接 issue、DoD 写进契约），并尝试把应用部署到真实环境。

**核心要求速记**
- 截止 **W7 Mon 12:00**，推 main 即提交，无迟交；W7 lab 全员 demo（功能 + 测试、pipeline/coverage、文档位置）。
- **必做**：CI pipeline（`.gitlab-ci.yml` 在根目录、提交时能工作）、MR `Closes #X`、每周 ≥1 次周会 + 纪要、每周 3 次 standup（1 次在 lab）、feature 分支 + peer-reviewed MR、retro（截止前）+ 互评。
- **应做**：TDD（测试先于实现，git 历史为证）、`tests/` + `conftest.py`、覆盖率跟踪（参考 >70%）、有测试保护的重构、labels/milestones、部署（pending/可选）。
- **不做**：直接改 main、合并红叉、用 AI 刷廉价测试、合并不理解的 AI 代码、最后一刻集中 push。

**讲师给的 Sprint 2 "拿分策略"**
1. 按周计划：W4 测试 + CI，W5 覆盖率 + 重构，W6 部署 + 收尾 + retro。
2. 从故事出发写测试，先核心后边界；每次改完就跑 pytest。
3. 把 CI 绿勾变成合并前的硬门槛（reviewer 与作者各确认一次）。
4. 覆盖率报告用来找缺口，不是 KPI；补齐 add/delete 的测试。
5. 会议纪要/commit message 必须真实——AI 生成的低质量记录会拉低分数。
