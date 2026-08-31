# COMP9820 · Sprint（"Spring"）任务总览目录

> 说明：讲义中的作业单位是 **Sprint**（敏捷"冲刺"），YouTube 自动字幕常把它误识为 "spring"。本目录整理的即 COMP9820 26T1 项目的三个 Sprint。
> 资料来源：`../lectures/01 ~ 09` 的课件整理（`01_课件整理_*.md`）、讲课总结（`02_讲课内容详细总结.md`）与字幕（`transcript.txt`）。Week 6（Deployment / DevOps）没有讲义文件夹，相关内容以其他周的引用为准。

| 文件 | 内容 |
|---|---|
| [00_Sprint总体概述.md](00_Sprint总体概述.md) | 三个 Sprint 的整体框架：考核结构与权重、截止时间、贯穿所有 Sprint 的固定实践（Git、Standup、Issue Board、Contract、Retro、互评、Demo）、提交规则、AI 与学术诚信政策、三个 Sprint 的演进关系、跨 Sprint 的通用评分逻辑与讲师建议 |
| [01_Sprint1_详细任务.md](01_Sprint1_详细任务.md) | Sprint 1「Foundations & First Flight」（Week 1–3，截止 Week 4 周一 12:00）：目标、周计划、任务清单、交付物、完整评分表（组 25 + 个人 5）、提交与 Demo 规则、课堂 Q&A 要点、任务总结 |
| [02_Sprint2_详细任务.md](02_Sprint2_详细任务.md) | Sprint 2「Quality, CI & Deployment」（Week 4–6，截止 Week 7 周一 12:00）：目标、周计划、实践与期望（周会、Issue Board 进阶、Git/MR、CI pipeline、覆盖率、部署、Standup、Retro）、评分要点、提交与 Demo、任务总结 |
| [03_Sprint3_详细任务.md](03_Sprint3_详细任务.md) | Sprint 3「Ownership, Risk & Portfolio」（Week 7–10，截止 Week 10 周五 17:00）：目标、周计划、README / 风险报告 / 重构与复杂度报告 / 个人 Portfolio 的完整要求、Final Demo 规范、完整评分表（Demo 15 + 过程证据 15 + 个人 10）、提交清单、任务总结 |

## 一图看三个 Sprint

```
Sprint 1 (W1–3)          Sprint 2 (W4–6)              Sprint 3 (W7–10)
Foundations & First      Quality, CI & Deployment     Ownership, Risk & Portfolio
Flight
────────────────────     ─────────────────────────    ──────────────────────────────
Git 分支/MR 习惯          TDD + pytest 自动化测试        持久化 / 复杂度 / 重构报告
Team Contract            GitLab CI pipeline（必做）     风险报告（RISK_REPORT.md）
Issue Board              代码覆盖率（pytest-cov）       README（模板）
用户故事 + 需求工程        部署（Vercel lab，可选）        个人 Portfolio（≤1000 词）
Standup ≥2 次/周          Standup 3 次/周 + 周会         正式 Final Demo（10–15 min + Q&A）
add & delete task        自己故事里的新功能              ≥1 个 meaningful 改进
Retro + 互评              Retro + 互评                   Retro + 互评
组 25 / 个人 5            组 25 / 个人 5                 组 30 / 个人 10
截止 W4 Mon 12:00         截止 W7 Mon 12:00              截止 W10 Fri 17:00
难度：最易                难度：更难                     难度：最难
```
