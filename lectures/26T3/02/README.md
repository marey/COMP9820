# COMP9820 · 26T3 · Week 2

**Lecture 2: Software Requirements, Agile Software Development Practices with Scrum**
Dr. Basem Suleiman · 2026-09-22 · https://www.youtube.com/watch?v=wgpJdDhBui0

| 文件 | 内容 |
|---|---|
| `01_课件整理_敏捷_Scrum_用户故事.md` | 70 张幻灯片按放映顺序整理：英文原文 + 🇨🇳 中文翻译 + 💬 讲师口头补充（含两次 Slido 投票的课堂讨论）；附本周待办清单 |
| `02_讲课内容详细总结.md` | 按讲课顺序的内容总结（含课堂互动与课后问答），末尾 15 条核心要点速览 |
| `transcript.txt` | 带时间戳的英文自动字幕（纯文本） |
| `transcript.en.json3` | YouTube 原始字幕（json3） |
| `images/` | 幻灯片图片 `NN_slug.jpg`（1280×720，由讲义 PDF 渲染，比 360p 录像清晰）；`15a_*` / `19a_*` 为两次 Slido 投票结果，从录像 720p 片段截取 |
| `26-T3 COMP9820_Software_Requirements_Scrum.pdf` | 讲师原版讲义（70 页），课上按顺序完整放映 |
| `Week_02.pptx` | 红黑树课堂中英对照版讲义（57 页，把原版 70 页合并整理并加中文批注）；2026-09-27 已按视频内容更新 16 页的中文批注（团队 6 人、Sprint 固定 2 周、Sprint 2 起自主、无项目经理、事件留记录供评分、评审时长、GitLab vs Jira / Code Review 列、Slido 结果、常见错误与讲师例子、无期末考试等）；同日再按班课逐字稿补充 25 页讲师落地建议（需求砍一刀 / Future Tasks、task 改 5 个文件、20 小时 / 2h→4h 估算、一天一个小 Sprint、日报周报、label 管状态、Spec Kit、INVEST.md、登录例子、摆烂组员分配、班课问答等）并新增 p55「Git worktree 与 AI 并行开发」；备份：`Week_02.bak.pptx`（原版）、`Week_02.bak2.pptx`（补充前） |
| `03_班课讲解整理_按幻灯片.md` | 班课逐字稿按 pptx 页码整理的要点，标出「pptx 已有」与「新增」 |
| `20260927115930-26T3_COMP9820第二周班课-逐字稿文本-1.md` | 班课（红黑树课堂）逐字稿原文 |

## 本周要做
1. **完成组队**（本周内；有空位的队伍会由 tutor 直接分配成员）。
2. 组内定 **Product Owner** 和 **Scrum Master**，其余为开发团队；不要设项目经理 / team lead。
3. 按 Scrum 跑 2 周一个的 Sprint：计划会 → 每日站会（15 分钟、三个问题）→ 开发 → 评审（演示）→ 回顾（四列表）；**每个事件都要留记录**，评分会检查。
4. 需求写成 User Story（*As a [role], I want [goal], so that [benefit]*）+ 验收标准，用 INVEST 自查；估算用 **T 恤尺码**；GitLab 里一个 Issue = 一个故事，验收标准拆 Tasks，打 `size-*` 标签，挂 Sprint milestone。
5. 课后看 Planning Poker 视频（幻灯片 49 的链接，讲义在 Moodle）。
6. 记住：Sprint 1 有脚手架，Sprint 2 起自己主导；**没有期末考试，全部项目评估**；作业细则本周发布。

## 说明
- 两份 Markdown 中不含视频时间戳；时间戳只在 `transcript.txt` 里。
- 自动字幕的常见识别错误已按语义还原（ritual→retro、bendown/bendout→burndown、planning boar→planning poker、comet→commit、conextra→Connextra、radio→ready、boasted nodes→post-it notes、3900 900→COMP3900/9900）。
