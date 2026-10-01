# COMP9820 · 26T3 · Week 3

**Lecture 3: Agile Software Architecture and Design for Web Applications**
Dr. Basem Suleiman · 2026-09-29 · https://youtu.be/IP4fX4hrbzc

| 文件 | 内容 |
|---|---|
| `01_课件整理_软件架构与设计_敏捷Web开发.md` | 课上放映的 60 页按放映顺序整理：英文原文 + 🇨🇳 中文翻译 + 💬 讲师口头补充（含 4 次课堂活动的问答）；文末附 PDF 里有但课上未放映的 7 页（4 张章节页 + 3 页附录），以及本周待办清单 |
| `02_讲课内容详细总结.md` | 按讲课顺序的内容总结（含课堂互动与讲师对项目 / 评分的要求），末尾 18 条核心要点速览 |
| `transcript.txt` | 带时间戳的英文自动字幕（纯文本） |
| `transcript.en.json3` / `transcript.en-orig.json3` | YouTube 原始字幕（json3） |
| `images/` | 幻灯片图片 `NN_slug.jpg`（1280×720，由讲义 PDF 渲染，比 360p 录像清晰）；`x1`–`x7` 为课上未放映的页面 |
| `COMP9820_W3_Software_Design_Architecture_Agile_Web_Dev.pdf` | 讲师原版讲义（67 页）；课上放映 60 页，4 张章节页被跳过，第 65–67 页附录未讲 |
| `Week_03.pptx` | 红黑树课堂中英对照版讲义（63 页）；2026-10-01 已按视频内容更新中文批注：纠正 4 处"Team Report 要放架构图"的说法（讲师明确本 Sprint 不评估设计与架构）、标注事件驱动页课上未讲，并补充 18 条讲师口头要点（本周定位与 9900、Facebook 例子、课堂活动答案、校验两次的理由、AI 题外话、KISS / 低耦合≠解耦、后端可先用假服务 mock、分层安全、微服务只扩瓶颈、非功能属性三个例子、大爆炸集成、Velocity 要解释论证等）；备份：`Week_03.bak.pptx`（更新前） |

## 本周要做
1. **Sprint 1 收尾**：本周末前把 Shared Expense Splitter 做到能现场演示；后端 / 数据库可先用简单"假服务"（讲师建议：比如读文件）替代，但放在单独组件里。
2. **下周 lab Demo（10%）**：10–12 分钟；每个成员到场并讲一部分（无 special consideration 缺席得 0）；演示功能 + Sprint 过程（backlog、看板、Issue、分支、MR）；提前把应用跑起来、GitLab 页面开好；全程录屏，MP4 10 月 11 日前交 Moodle。
3. **Team Report（15%）**：约 15 页五部分，10 月 11 日周日 9 pm 经 Turnitin 每队一份；速度部分要解释论证（承诺 vs 完成）。
4. **Peer Evaluation（1%）**：第 4 周周三开放、10 月 11 日 9 pm 关闭，不接受迟交。
5. **Individual Report（4%）**：10 月 18 日 9 pm；自己的贡献，证据来自自己的 Issue 和 MR。
6. 设计与架构本 Sprint 不评估，但建议每个故事按垂直切片做，避免"后端组 / 前端组最后再集成"。
7. 下周主题：软件测试（Sprint 2、3 的重点）。

## 说明
- 两份 Markdown 中不含视频时间戳；时间戳只在 `transcript.txt` 里。
- 自动字幕的常见识别错误已按语义还原（"AI"→API、"design buttons / bets / baton"→design patterns、"bot"→part、"mood"→Moodle、"print"→sprint、"equality"→quality、"ALB"→ELP、"Xins"→expense、"rooted"→routed、"law cumbling"→low coupling）。
- 课上两处动画（MVC 请求流程 8 步逐步出现、微服务页底部两条结论后出现）在图片中以 PDF 完整页呈现。
