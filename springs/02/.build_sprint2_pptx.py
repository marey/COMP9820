# -*- coding: utf-8 -*-
"""COMP9820 26T3 Sprint 2 Guidelines (Moodle page -> Sprint2_Guidelines_1.md) -> 红黑树课堂 bilingual deck.
    python3 build_sprint2.py CROPS_DIR OUT.pptx
"""
import os, sys
SK = '/Users/rbt/Documents/codes/COMP9820/.claude/skills/rbt_lec_pdf_to_pptx'
sys.path.insert(0, os.path.join(SK, 'scripts'))
from pptx_helpers import Deck, textbox, para, bullets, add_run, EN, CN, B, ZH, WHITE, HL

crops, out = sys.argv[1], sys.argv[2]
d = Deck(template=os.path.join(SK, 'assets', 'rbt_template.pptx'), out=out, crops=crops)
d.set_cover_label('COMP9820 Sprint 2')
CODE = 'Courier New'


def code_slide(en, zh, lines, size=13, sb=2, note=None, note_y=6.35):
    s = d.new_slide(); d.title(s, en, zh)
    tb = textbox(s, 1.19, 1.45, 10.9, 5.3)
    for ln in lines:
        if ln.lstrip().startswith('#'):
            runs = [(ln, dict(size=size, bold=False, color=ZH, font=CODE))]
        elif ' #' in ln:
            c, m = ln.split(' #', 1)
            runs = [(c, dict(size=size, bold=False, color=WHITE, font=CODE)),
                    (' #' + m, dict(size=size, bold=False, color=ZH, font=CODE))]
        else:
            runs = [(ln, dict(size=size, bold=False, color=WHITE, font=CODE))]
        p = para(tb, [], bullet=False, space_before=sb)
        for t, o in runs:
            add_run(p, t if t else ' ', **o)
    if note:
        d.note(s, note, y=note_y, size=13)
    return s


DEADLINE = 'Saturday, 7 November, 9 pm'

# ===================================================================== Outline
d.outline([
    {'en': 'Overview: from the generic Sprint 1 splitter to a variation', 'zh': '概览：Sprint 1 人人一样的通用版 → Sprint 2 为一个具体用户做变体 + CI'},
    {'en': 'Goals for Sprint 2 and the suggested weekly planner', 'zh': '目标与四周计划：Week 5 计划、Week 6 搭 CI、Week 7 做功能、Week 8 交付'},
    {'en': 'Variations 1–7 and the scoping rules', 'zh': '七个变体各自的"灵魂差异"、Sprint 2 先做什么、哪些要先问 tutor'},
    {'en': 'CI pipeline: minimum requirements and a ready-to-use .gitlab-ci.yml', 'zh': 'CI 流水线四条最低要求 + 一份可以直接起步的配置 + 红了怎么办'},
    {'en': 'Agile practice: Git, meetings, peer evaluation, planning & stories', 'zh': 'Git 闭环、每周两次会议、互评四维度、用户故事怎么写才达标'},
    {'en': 'Assessment: Demo 10% · Team Report 15% · Peer Evaluation 1% · Individual 4%', 'zh': '考核四项共 30%，逐项拆到评分点和证据'},
    {'en': 'Plagiarism, AI mode, and what to do this week', 'zh': '学术诚信与 AI 使用规则；最后给出本周行动清单'},
], size=19, cn_size=14, sb=4)

d.content('Sprint 2 Guidelines — COMP9820 Project', '共享费用分摊器：从通用版走向为一个具体用户服务的产品', [
    {'en': 'Shared Expense Splitter', 'zh': '项目仍然是「共享费用分摊器」，Sprint 1 的代码就是 Sprint 2 的起点'},
    {'en': 'Source: Moodle → Assessments Hub → Sprint 2 Guidelines (last modified 27 October 2026)', 'zh': '本课件按 Moodle 页面逐段整理，英文原文照抄，中文给零基础同学讲一遍'},
    {'en': 'Sprint 2 runs Week 5 → Week 8 (three weeks, including Flexibility Week)', 'zh': 'Sprint 2 跨 Week 5–8：三周，中间 Week 6 是没有课的弹性周'},
    {'en': ['All four submissions are due ', B(DEADLINE, 18)], 'zh': '演示录像、团队报告、个人报告、互评全部在 11 月 7 日（周六）晚 9 点到期'},
    {'en': 'One sentence: extend Sprint 1 for one clearly defined user, and let a CI pipeline guard main',
     'zh': '一句话：在 Sprint 1 代码上为一个明确的用户做变体，并用 CI 流水线守住 main'},
], size=18, cn_size=14, sb=10)

# ===================================================================== PART 1
d.section('PART 1 — Overview', '第一部分：概览', 'Sprint 2 要交三样东西：能跑的变体、每个 MR 都跑的流水线、团队协作的证据')

d.content('In Sprint 1, every team built the same generic splitter', 'Sprint 1 人人一样；Sprint 2 各组围绕一个具体场景改造它', [
    {'en': 'In Sprint 1, every team built the same generic Shared Expense Splitter: groups, expenses, splits, net balances, edit and delete, and history.',
     'zh': 'Sprint 1 全班做的是同一道"基础版炒饭"：群组、费用、分摊、净余额、增删改、历史记录'},
    {'en': 'Whereas in Sprint 2, your team adapts its Sprint 1 build for one specific scenario (variation).',
     'zh': 'Sprint 2 不是再做一道新菜，而是为一类特定食客改良这道炒饭——这就是"变体（variation）"'},
    {'en': 'You choose a target user, describe their problem, and write and deliver the user stories that solve it.',
     'zh': '选定目标用户、描述他们的痛点、写出并交付能解决痛点的用户故事'},
    {'en': 'Your Sprint 1 code is the base each variation extends; no additional code will be supplied.',
     'zh': 'Sprint 1 的代码是扩展的基础，课程不再发任何新代码'},
    {'zh': '易混淆：Variation 不是"换项目"，是"同一个基础应用 + 一个具体场景"；Target user 是具体人群（合租的大学生），不是"所有用户"'},
], size=17, cn_size=13, sb=8)

d.content('Alongside the variation: a CI pipeline', '同时引入持续集成流水线：全组的共同安全网', [
    {'en': 'Every push and merge request will be built, linted and tested automatically, so that the team can see at a glance whether main still works.',
     'zh': '每次 push、每个 merge request 都自动构建、lint、测试，全组一眼看出 main 还能不能跑'},
    {'en': 'As more people change more code, the pipeline becomes the shared safety net that lets the team integrate work with confidence.',
     'zh': '改代码的人越多、改动越多，流水线就越是大家放心合并的安全网'},
    {'en': 'By the end of Sprint 2 your team should have:'},
    {'en': 'a working variation that serves a clearly defined user', 'zh': '① 一个能运行、服务于明确用户的变体', 'lvl': 1},
    {'en': 'a CI pipeline that runs on every merge request', 'zh': '② 一条在每个 MR 上都会运行的 CI 流水线（.gitlab-ci.yml）', 'lvl': 1},
    {'en': 'evidence that the work was planned, tracked, reviewed and integrated as a team', 'zh': '③ issue board、MR、会议纪要等能证明团队协作过程的证据', 'lvl': 1},
], size=17, cn_size=13, sb=8)

# ===================================================================== PART 2
d.section('PART 2 — Variations & CI', '第二部分：变体与持续集成',
          '先看 Sprint 2 的五个目标和四周计划，再逐个认识七个变体，最后是 CI 流水线的硬性要求')

d.content('Goals for Sprint 2', 'Sprint 2 的五个目标：敏捷原则、用户故事与 Git、扩展功能、CI、留下证据', [
    {'en': 'Sprint 2 focuses on improving the generic Shared Expense Splitter web application into a specific defined product following your chosen variation.',
     'zh': '重点：按选定的变体，把通用 Web 应用改进成一个定义明确的具体产品，并建立更有针对性的用户故事、用例和成功标准'},
    {'en': 'You will continue practising Agile software team principles, including collaboration, communication, and shared responsibility.',
     'zh': '继续实践敏捷团队原则：协作、沟通、共同负责'},
    {'en': 'Translate new targeted ideas into clear user stories; establish good Git habits through branching, committing, and peer-reviewed merges; deliver an initial set of new features.',
     'zh': '把想法写成清晰的用户故事；分支、提交、同伴评审后合并；交付第一批新功能'},
    {'en': 'Extend the Sprint 1 Shared Expense Splitter by implementing features for the chosen variation.',
     'zh': '在 Sprint 1 代码上实现变体功能'},
    {'en': 'Design and set up a CI pipeline in GitLab that runs automatically on merge requests and on main, and use it as part of everyday development.',
     'zh': '在 GitLab 搭一条在 MR 和 main 上自动运行的流水线，并把它当作日常开发的一部分'},
    {'en': 'By the end of the sprint: working variation features, a working CI pipeline, and evidence that the team planned, tracked and reviewed its work.',
     'zh': 'Sprint 结束时：能跑的变体功能 + 可用的流水线 + 计划 / 跟踪 / 评审的证据'},
], size=16, cn_size=13, sb=6)

s = d.new_slide(); d.title(s, 'Suggested weekly planner for Sprint 2', '建议周计划：Week 5 想清楚，Week 6 搭 CI，Week 7 做功能，Week 8 交作业')
d.picture(s, 'timeline', 1.0, 1.4, 11.3, 5.3)

d.two_col('Weekly planner: the original wording', '周计划原文：每周的任务和会议次数', [
    {'en': [B('Week 5: ', 16), 'Sprint 2 planning: define the target user, personas, use cases and success criteria; write and estimate variation user stories; agree the Sprint Goal; create a Sprint 2 milestone. ≥ 2 team meetings'],
     'zh': 'Week 5 计划：定义目标用户、persona、用例、成功标准；写并估算变体故事；商定 Sprint Goal；建 Sprint 2 milestone；至少 2 次会议'},
    {'en': [B('Week 6: ', 16), '(Flexibility Week: No labs or lectures) Design the CI pipeline; get lint and tests passing in CI; begin implementing variation stories; manage issue board. 0-2 team meetings'],
     'zh': 'Week 6 弹性周没课：设计流水线、让 lint 和测试在 CI 变绿、开始做故事、维护看板；0–2 次会议——没课不等于没事做'},
], [
    {'en': [B('Week 7: ', 16), 'Implement variation stories, with every merge request passing the pipeline before review; add tests for new functionality; manage issue board. ≥ 2 team meetings'],
     'zh': 'Week 7：实现故事，每个 MR 先过流水线再评审；为新功能补测试；维护看板；至少 2 次会议'},
    {'en': [B('Week 8: ', 16), 'Sprint 2 demo in lab; sprint retrospective; team report, individual report and peer evaluation (Saturday, 7 November)'],
     'zh': 'Week 8：lab 演示、回顾会、团队报告、个人报告、互评（11 月 7 日周六）'},
    {'en': 'We will release instructions to help your team achieve the above goals week by week following the relevant lectures.',
     'zh': '说明会紧跟讲座逐周发布，免得用还没教到的内容把大家淹没'},
], size=16, cn_size=13, sb=6)

# --------------------------------------------------------------------- 2.1
d.section('PART 2.1 — Variations', '第二部分（一）：七个变体', '同一个基础应用，七种具体场景；你们组在 Week 4 lab 已经选定，tutor 确认过')

d.content('In Sprints 2 and 3, each team builds out a variation', '变体 = 同一个基础应用，针对一个具体场景改造；Sprint 2、3 都围绕它', [
    {'en': 'In Sprints 2 and 3, each team builds out a variation: the same base application adapted for a specific scenario.',
     'zh': 'Sprint 2 和 Sprint 3 都做这一个变体，所以 Sprint 2 选故事时就要给 Sprint 3 留演进空间'},
    {'en': 'Your team chose its variation in the Week 4 lab, and your tutor confirmed it.',
     'zh': '变体在 Week 4 lab 已选定并由 tutor 确认'},
    {'en': 'Please contact your tutor if you do not know which variation you need to do.',
     'zh': '不知道自己组做哪个，马上联系 tutor'},
    {'en': 'Seven variations: Restaurant Bill · Share House · Group Travel · Club Treasury · Expense Claims · Shared Fund · Usage-Based',
     'zh': '七个变体：餐厅账单、合租房、结伴旅行、社团财务、员工报销、先凑钱基金、按使用量分摊——下面逐个看'},
    {'zh': '记忆法：每个变体都有一个和通用版不同的"灵魂差异"（一次性 / 永不结清 / 多币种 / 钱去哪了 / 角色权限 / 先收后花 / 按使用量）'},
], size=17, cn_size=13, sb=9)

d.content('Variation 1: Splitting a Restaurant Bill', '变体 1 分摊餐厅账单：一次性、一部手机、没账号没历史，账单付清就结束', [
    {'en': 'A one-off settlement made in the two minutes at the end of a shared meal. One person uses one phone, with a paper receipt, no accounts and no saved history. The other variations track a group over time; this one ends when the bill is paid.',
     'zh': '聚餐结束后的两分钟内一次性结算；其他变体都是长期跟踪一个群组，它不是'},
    {'en': 'A diner photographs the receipt, and the app extracts its line items', 'zh': '食客给小票拍照，应用提取每一行菜品——需要 OCR 外部服务，先问 tutor'},
    {'en': 'Each diner claims their own dishes and drinks', 'zh': '每位食客认领自己点的菜和饮料'},
    {'en': 'A shared item, such as an appetiser or a bottle of wine, is divided only among the diners who shared it', 'zh': '共享菜品只在分享它的人之间分'},
    {'en': 'Tip and service charge are applied in proportion to each diner\'s share, with rounding that keeps the total exact', 'zh': '小费、服务费按比例分，四舍五入后总额必须精确'},
    {'en': 'The person holding the phone corrects a line item the photo extraction misread', 'zh': '拿手机的人可以修正识别错的一行'},
    {'en': 'Each diner sees one amount to pay the person who settled the bill', 'zh': '每人看到一个金额，付给结账的人'},
], size=15, cn_size=12, sb=5)

d.content('Variation 2: Share House Running Costs', '变体 2 合租房日常开销：费用按月重复、永不结清、分摊规则持久、室友会变', [
    {'en': 'An open-ended arrangement in which expenses recur month after month, and balances never fully settle. Split rules persist from one month to the next, and the household changes as housemates move in and out.',
     'zh': '没有终点：费用月复一月、余额永远结不清；规则跨月延续；室友搬进搬出'},
    {'en': 'A housemate sets up a recurring expense, such as rent or internet, once', 'zh': '房租、网费只设置一次，之后自动按月生成'},
    {'en': 'Each type of expense keeps its own split rule: rent divided unevenly by room, utilities by headcount, groceries equally', 'zh': '每类费用各有规则：房租按房间不均分、水电按人头、买菜均分'},
    {'en': 'A housemate moves in or out mid-month and that month\'s costs are adjusted', 'zh': '月中搬入搬出，当月费用按天折算——折算规则要想清楚'},
    {'en': 'Each housemate checks a monthly statement of what they paid and what they owe', 'zh': '每人能看月度对账单：付了多少、还欠多少'},
], size=16, cn_size=13, sb=7)

d.content('Variation 3: Group Travel', '变体 3 结伴旅行：固定人群固定时段、多币种、可能离线、最后结算一次', [
    {'en': 'A fixed group over a fixed period, with one settlement at the end. One person usually fronts most of the cost, and expenses arise in more than one currency and sometimes without an internet connection.',
     'zh': '通常一个人垫付大头；费用涉及多种货币，有时在没网的地方发生'},
    {'en': 'A traveller records an expense in the local currency, with the exchange rate captured at the time of the expense', 'zh': '用当地货币记账，并记下当时的汇率（手输即可，实时汇率 API 先问 tutor）'},
    {'en': 'The group sets a budget per day or per category and tracks spending against it', 'zh': '按天或按类别设预算并跟踪'},
    {'en': 'A traveller enters expenses offline and they sync when a connection returns', 'zh': '离线录入、联网后同步——技术难度高，谨慎纳入 Sprint 2'},
    {'en': 'The group settles once at the end of the trip', 'zh': '旅行结束时一次性结算'},
], size=16, cn_size=13, sb=7)

d.content('Variation 4: Club or Society Treasury', '变体 4 社团财务：问"钱去哪了"而不是"谁欠谁"，财务要向会员交代', [
    {'en': 'The question is where the money went, not who owes whom. A committee spends on behalf of members, and the treasurer must account for that spending to members who do not record expenses themselves.',
     'zh': '委员会代会员花钱，会员自己不记账，财务（treasurer）要给出交代'},
    {'en': 'The treasurer sets budget lines and tracks spending against each one', 'zh': '设预算科目并逐项跟踪支出'},
    {'en': 'A committee member requests funds, and the spending is approved before it is committed', 'zh': '先申请、再批准、后花钱——涉及审批流程和角色'},
    {'en': 'Members read a report showing spending by budget line', 'zh': '会员看按科目列出的支出报告'},
    {'en': 'The audit trail shows who changed each record and when', 'zh': '审计记录：谁、何时改了哪条'},
], size=16, cn_size=13, sb=7)

d.content('Variation 5: Employee Expense Claims', '变体 5 员工报销：报销方是组织，用户有不同角色和权限', [
    {'en': 'Reimbursement comes from an organisation, not from other members of a group. Each claim is checked against a company policy and approved by a manager, so users have different roles with different permissions.',
     'zh': '每笔申请对照公司政策检查并由经理批准，所以天然需要"员工 / 经理 / 财务"角色'},
    {'en': 'A staff member submits a claim with a photo of the receipt', 'zh': '员工提交申请并附收据照片'},
    {'en': 'A manager approves or rejects the claim, or delegates approval to another manager while away', 'zh': '经理批准 / 驳回，外出时可委托他人审批'},
    {'en': 'The app applies policy rules such as per-diem caps and disallowed categories', 'zh': '执行政策规则：每日津贴上限、禁报类别'},
    {'en': 'Each claim carries tax and account codes', 'zh': '每笔申请带税务代码和会计科目'},
    {'en': 'Finance staff export approved claims to an accounting package', 'zh': '财务导出到会计软件——真正的登录与角色权限先问 tutor'},
], size=15, cn_size=12, sb=6)

d.content('Variation 6: A Shared Fund with Contributions Up Front', '变体 6 先凑钱再花的共同基金：钱先进池子，再从池子里花', [
    {'en': 'Money is collected before it is spent, as with a group gift, a wedding or a shared holiday house. The app tracks money into a pool and spending out of it, rather than reimbursing someone who has already paid.',
     'zh': '合送礼物、办婚礼、合租度假屋：跟踪进池的钱和出池的钱，而不是给垫付的人报销'},
    {'en': 'A contributor pledges an amount, and the app records payments actually received against each pledge', 'zh': '认捐金额 vs 实际到账分开记'},
    {'en': 'The organiser sets a target and contributors see a running total', 'zh': '设目标金额，出资人看实时累计'},
    {'en': 'The organiser spends from the pool and each expense is visible to contributors', 'zh': '从池中支出，每笔对出资人可见'},
    {'en': 'The organiser handles an over-subscribed or under-subscribed fund, including refunds', 'zh': '超额 / 不足时的处理与退款——退款逻辑要先定义清楚'},
], size=16, cn_size=13, sb=7)

d.content('Variation 7: Usage-Based Cost Sharing', '变体 7 按使用量分摊：份额由使用记录推算，余额以额度结转', [
    {'en': 'Each person\'s share is derived from logged usage, not from a split declared when the expense is recorded, as in a carpool or a holiday house shared between families. Balances carry forward as credits instead of being settled in cash.',
     'zh': '拼车、几家人共享度假屋：谁用得多谁分得多；余额变成"额度"结转，不付现金'},
    {'en': 'A member logs attendance per carpool trip or usage per holiday-house stay', 'zh': '记录每次拼车出席 / 每次入住使用量'},
    {'en': 'The app allocates each cost according to the usage log', 'zh': '按使用记录分配每笔成本'},
    {'en': 'Credits carry forward to later trips or stays instead of being paid out', 'zh': '额度结转到以后的行程'},
    {'en': 'Members view a fairness report covering the whole season', 'zh': '整季公平性报告——"公平"怎么定义要先说清'},
], size=16, cn_size=13, sb=7)

d.content('While working on your variation, keep the following in mind', '做变体时的五条规矩：别改 Sprint 1、没新代码、控范围、按两个 Sprint 规划、不重复', [
    {'en': 'Do not change any Sprint 1 user stories because of your variation. The Sprint 1 build is the base that your variation extends.',
     'zh': '不是一行代码不能动，而是 Sprint 1 的功能必须仍然存在、仍然可用；可以在其上演进'},
    {'en': 'No additional code will be supplied. Each team writes the user stories for its variation and extends its own Sprint 1 code to implement them.',
     'zh': '故事自己写，代码自己扩展'},
    {'en': 'Scope carefully. Some ideas need external services (for example, receipt photo extraction or live exchange rates) or real authentication and roles. Discuss scope with your tutor before committing to these stories in your sprint plan.',
     'zh': '外部服务（OCR、实时汇率）和真实认证角色风险高，进计划前先和 tutor 谈'},
    {'en': 'Plan for two sprints. Your variation continues into Sprint 3, so choose stories for Sprint 2 that deliver a usable core and leave room for the variation to evolve.',
     'zh': 'Sprint 2 只做"没有它变体就不成立"的可用核心，剩下的留给 Sprint 3'},
    {'en': 'No two teams in the same lab share a variation. If your team proposed its own variation, it must be approved by your tutor.',
     'zh': '同一实验班不重复；自提变体必须经 tutor 批准'},
], size=15, cn_size=12, sb=6)

d.two_col('Scope carefully: a usable core now, evolution later', '怎么控范围：三步筛故事，高风险点先问 tutor', [
    {'en': 'Three steps to scope Sprint 2'},
    {'en': 'List every story idea for your variation — the guideline bullets are ideas, not a checklist', 'zh': '先把变体的全部故事点子列出来；指南给的只是"ideas"，不是必做清单', 'lvl': 1},
    {'en': 'Flag each one: needs an external service or real authentication?', 'zh': '逐条标注：要不要外部服务 / 真实登录？要的先谈', 'lvl': 1},
    {'en': 'Order by "without it the variation does not exist"; take the top few', 'zh': '按"没有它变体就不成立"排序，Sprint 2 只拿最前面能凑成可用核心的几条', 'lvl': 1},
    {'en': 'Keep a "Sprint 3" column on the issue board from day one', 'zh': '看板上从第一天就留一列 Sprint 3，把暂不做的故事放进去，报告里也能展示取舍'},
], [
    {'en': 'Talk to your tutor first'},
    {'en': 'Receipt photo extraction (OCR)', 'zh': '变体 1：小票拍照识别', 'lvl': 1},
    {'en': 'Live exchange rates; offline entry and sync', 'zh': '变体 3：实时汇率 API、离线同步', 'lvl': 1},
    {'en': 'Real authentication, roles and approval chains', 'zh': '变体 4 / 5：真正的登录、角色权限、审批流', 'lvl': 1},
    {'en': 'Export to an accounting package; refunds', 'zh': '变体 5 导出会计软件；变体 6 退款逻辑', 'lvl': 1},
    {'en': 'Fairness report definition', 'zh': '变体 7："公平"先给出可计算的定义', 'lvl': 1},
], size=16, cn_size=13, sb=6)

# --------------------------------------------------------------------- 2.2
d.section('PART 2.2 — CI Pipeline', '第二部分（二）：CI 流水线', '四条硬性要求 + 一份能直接起步的 .gitlab-ci.yml；报告里 CI 一节占 4%，是最值钱的部分')

d.fig_top('At a minimum, the pipeline must', '流水线的四条最低要求：文件、触发、内容、main 必须绿', 'pipeline', [
    {'en': 'Be defined in a .gitlab-ci.yml file.', 'zh': '定义在仓库根目录的 .gitlab-ci.yml 里——报告贴文件内容和路径截图'},
    {'en': 'Run automatically on merge requests and on pushes to main.', 'zh': '在 MR 和推送 main 时自动运行——MR 页顶部和 main 的每次 commit 旁都能看到 ✓ / ✗'},
    {'en': 'Run, at a minimum, your linters and your automated test suite, and fail when either fails.', 'zh': '至少跑 linter 和测试，任一失败整条红——至少两个 job：lint、test'},
    {'en': 'Pass on the latest commit on main (by the report deadline).', 'zh': '截止时 main 最新 commit 必须是绿的——Repository → Branches 里 main 旁是绿勾'},
], fig_h=2.0, size=16, cn_size=13, sb=5)

d.content('Design the pipeline yourselves — and run meaningful tests', '流水线设计由团队决定；但只有测试有意义，流水线才有用', [
    {'en': 'In this Sprint, each team must design and set up a CI pipeline in GitLab. Beyond the listed requirements, the design is your team\'s decision.',
     'zh': '除四条最低要求外，怎么设计由你们定——报告要解释"为什么这样设计"'},
    {'en': 'Think about which stages your pipeline needs, in what order they should run, how long a run takes, and what a team member should do when it fails.',
     'zh': '要想清楚：哪些 stage、什么顺序、跑一次多久、红了怎么办——这四个问题就是报告 Design 一段的提纲'},
    {'en': 'The pipeline is only useful if the tests it runs are meaningful. Write tests for the variation features you build in Sprint 2, ideally before or alongside the code.',
     'zh': '只跑 3 个测试的绿流水线说明不了什么；变体的每个新功能都要有测试，最好先写测试'},
    {'en': 'Coverage targets and broader quality assurance are assessed in Sprint 3, but a pipeline that already reports coverage in Sprint 2 will make that work easier.',
     'zh': '覆盖率目标 Sprint 3 才考，但现在就让流水线报告覆盖率，Sprint 3 会轻松很多'},
], size=16, cn_size=13, sb=9)

code_slide('.gitlab-ci.yml: a starting point you can hand in', '一份能直接起步的配置：只在 MR 和 main 触发，lint → test 两个 stage', [
    '# .gitlab-ci.yml  —  放在仓库根目录',
    'image: python:3.12',
    'workflow: # 只保留两种触发：MR 流水线 + main 分支流水线',
    '  rules:',
    '    - if: $CI_PIPELINE_SOURCE == "merge_request_event"',
    '    - if: $CI_COMMIT_BRANCH == "main"',
    'stages: [lint, test] # 先 lint（快、便宜）再 test',
    'default:',
    '  before_script:',
    '    - pip install -r requirements.txt',
    'lint:',
    '  stage: lint',
    '  script: make lint # Makefile: ruff check .',
    'test:',
    '  stage: test',
    '  script: make coverage # pytest --cov=app --junitxml=report.xml',
    "  coverage: '/TOTAL.*\\s+(\\d+%)$/' # MR 页面显示覆盖率数字",
    '  artifacts:',
    '    when: always',
    '    reports: {junit: report.xml} # MR 页面列出失败的测试',
], size=13, sb=2, note='Tools 一段怎么写：GitLab CI + python:3.12 镜像 + ruff + pytest / pytest-cov，分别被 lint / test 两个 job 通过 make 目标调用', note_y=6.45)

d.two_col('When the pipeline goes red', '流水线红了怎么办，以及三个常见误区', [
    {'en': 'What a team member should do'},
    {'en': 'Open the red job, read the log, find the first error', 'zh': '点开红色 job 看日志，找第一条报错', 'lvl': 1},
    {'en': 'Fix on the same feature branch and push again — the pipeline reruns automatically', 'zh': '在同一分支修复再 push，流水线自动重跑；不要为了变绿去删测试', 'lvl': 1},
    {'en': 'If main is red, fixing it is the whole team\'s top priority ("stop the line")', 'zh': 'main 红了全组最高优先级修，这叫 stop the line', 'lvl': 1},
    {'en': 'Screenshot the failure and the fix — the report needs at least one failing pipeline', 'zh': '截图留证：报告 Evidence 一段明确要"至少一次失败 + 怎么处理"', 'lvl': 1},
], [
    {'en': 'Common misunderstandings'},
    {'en': ['Never add ', B('allow_failure: true', 14), ' to lint or test'], 'zh': '它会把红变成黄色警告，MR 照样能合并，等于没有把关', 'lvl': 1},
    {'en': 'A green pipeline ≠ correct code', 'zh': '测试少、测试弱，绿也没意义；所以要为每个新功能写测试', 'lvl': 1},
    {'en': 'stages: decides order; every job belongs to one stage', 'zh': 'stage 管先后，job 干活；同一 stage 的 job 并行', 'lvl': 1},
    {'en': ['Settings → Merge requests → ', B('Pipelines must succeed', 14), '; protect main'], 'zh': '勾上后"先过流水线再评审"由系统强制，报告 Impact 一段就有话说', 'lvl': 1},
], size=16, cn_size=13, sb=6)

# --------------------------------------------------------------------- 2.3 / 2.4
d.section('PART 2.3–2.4 — Agile practice', '第二部分（三）：敏捷实践、计划与用户故事',
          'Git 闭环、每周两次会议、互评四维度，以及一条用户故事怎样才算写好')

d.content('2.3 Agile software team practice: Git, meetings, check-ins', 'Git 实践、参与度与会议、Week 7 的 tutor check-in', [
    {'en': '2.3.1 Git practice — Follow 📝 Git Practice (the page linked on Moodle)', 'zh': '照 Moodle 上的 Git Practice 页做；最小闭环：issue → feature 分支 → 小步 commit → MR 关联 issue → 流水线绿 → 评审 → 合并'},
    {'en': '2.3.2 You are expected to have two team meetings per week (on average) in Weeks 5, 7 and 8; optional in Flexibility Week.',
     'zh': 'Week 5、7、8 每周两次会议，弹性周可选；一个 Sprint 约 6–8 份纪要，是报告附录也是监控证据'},
    {'en': 'You will have project check-ins with your tutor during your Week 7 lab; they are excellent opportunities for your tutor to provide you with both technical and non-technical guidance.',
     'zh': 'Week 7 lab 有 tutor check-in：提前准备问题（范围合不合理、流水线够不够）；个人报告也要写这次 check-in'},
    {'zh': '会议纪要至少写：日期、出席、主持人、每人"做了 / 要做 / 卡住"、决定、行动项（谁、什么、何时）'},
], size=16, cn_size=13, sb=9)

d.content('2.3.3 Peer evaluation: four criteria', '同伴互评：Week 8 周三到周六晚 9 点，只有老师看得到，四个维度', [
    {'en': 'Peer evaluation will open from Week 8 Wednesday until Saturday, 9 pm. The results will only be visible to your tutors and lecturers; your team members will NOT be able to see other members\' inputs.',
     'zh': '组员互相看不见；只用于让 tutor 了解小组运转、更好地支持你们；提交才有分，但不直接影响其他成绩'},
    {'en': [B('Participation', 15), ': level of participation in group work, attendance at meetings, making suggestions, taking responsibility for tasks, being in communication with the team'],
     'zh': '参与度：到会、发言、主动领 issue、在群里回消息'},
    {'en': [B('Dependability', 15), ': how dependable in delivering assigned tasks, on time, with expected levels of quality'],
     'zh': '可靠性：说周三交 MR 就周三交，质量过得去'},
    {'en': [B('Team Wellbeing', 15), ': communicating with members, coordinating meetings, listening to concerns, facilitating discussion, offering suggestions'],
     'zh': '团队氛围：约会议、听顾虑、帮卡住的人、评审语气建设性'},
    {'en': [B('Work contribution', 15), ': how much this team member contributed to the development of the project'],
     'zh': '工作贡献：合并进 main 的 MR、写的测试、搭的 CI——只有本地代码不算'},
], size=15, cn_size=12, sb=6)

d.two_col('2.4 Planning & stories', '写好用户故事的指南：格式、以客户为中心、可测试的验收标准、关联 GitLab', [
    {'en': '1. Write User Stories:'},
    {'en': 'Use "As a... I want... so that..." format', 'zh': '"作为……，我想要……，以便……"', 'lvl': 1},
    {'en': 'Make them customer-centric', 'zh': '念给目标用户听他能听懂；出现 endpoint / refactor 的多半不是用户故事', 'lvl': 1},
    {'en': 'Include specific, testable acceptance criteria', 'zh': '验收标准具体、可测试——每一条都能变成一个测试', 'lvl': 1},
    {'en': 'Where stories were split, explain how and why', 'zh': '拆分过的故事写清怎么拆、为什么拆', 'lvl': 1},
], [
    {'en': '2. Connect to GitLab:'},
    {'en': 'Create GitLab issues for each story', 'zh': '每条故事一个 issue，点数用 label（如 points::3）记录', 'lvl': 1},
    {'en': 'Link stories to your issue board', 'zh': '挂到 Sprint 2 milestone，在看板 To Do / Doing / Review / Done 之间移动', 'lvl': 1},
    {'en': 'Remember:'},
    {'en': 'Quality over quantity', 'zh': '质量重于数量', 'lvl': 1},
    {'en': 'A few well-written stories with clear discovery process > many poor stories', 'zh': '几条写得好、探索过程清晰的故事 > 一堆差故事', 'lvl': 1},
    {'en': 'Show your thinking, not just the final stories', 'zh': '报告里写"列了 9 个点子 → 排序 → 挑 4 个 → 拆了 #19"的过程', 'lvl': 1},
], size=16, cn_size=13, sb=6)

d.content('Example: one Sprint 2 user story that meets the bar', '示例：一条达标的用户故事（变体 2 合租房，Issue #23，3 points）', [
    {'en': [B('As a', 15), ' housemate who pays the internet bill, ', B('I want', 15), ' to set up the bill once as a monthly recurring expense, ', B('so that', 15), ' I don\'t have to re-enter it every month.'],
     'zh': '角色、想要什么、为了什么三段齐全；挂在 Sprint 2 milestone，点数 label 记 3'},
    {'en': 'AC1: Given a group exists, when I create an expense with recurring = monthly, then it appears in this month\'s expense list.',
     'zh': '验收标准 1：创建周期费用后出现在本月列表——可以在界面上验证，也能写成接口测试'},
    {'en': 'AC2: Given a monthly recurring expense exists, when the next month starts, then a copy is generated automatically with the same amount and split rule.',
     'zh': '验收标准 2：下月自动生成同金额、同规则的副本'},
    {'en': 'AC3: Given a recurring expense, when I stop it, then no further copies are generated but past copies remain in history.',
     'zh': '验收标准 3：停止后不再生成，但历史保留'},
    {'en': 'Split from #19 "Recurring expenses" into #23 (create recurring) and #24 (uneven split by room) — each can be delivered and demoed on its own.',
     'zh': '拆分说明：原故事太大，拆成两条可独立交付、独立演示的故事'},
    {'zh': '易混淆：验收标准 ≠ 任务清单。"写一个 POST /expenses 接口"是任务；"创建后出现在列表里"才是用户视角的验收标准'},
], size=15, cn_size=12, sb=5)

# ===================================================================== PART 3
d.section('PART 3 — Sprint 2 Assessment', '第三部分：Sprint 2 考核（占总分 30%）',
          '演示 10%、团队报告 15%、互评 1%、个人报告 4%；考的不只是做了什么，还有怎么计划、协作、跟踪、用 Git、反思')

d.content('Sprint 2 Assessment: four components, 30% in total', '四个组成部分：两项团队、两项个人；同一天截止', [
    {'en': 'The assessment focuses not only on what your team builds, but also on how effectively you plan, collaborate, track your work, use Git, and reflect on your contribution throughout the sprint.',
     'zh': '考的不只是产品，还有计划、协作、跟踪、Git 使用和自我反思'},
    {'en': [B('Demo 10%', 17), ' — Live in your Week 8 lab (Recording due Saturday, 7 November, 9 pm)'], 'zh': '演示：Week 8 lab 现场 + 录像，团队提交'},
    {'en': [B('Team Report 15%', 17), ' — End of Week 8, Saturday, 7 November, 9 pm'], 'zh': '团队报告：PDF 约 20 页，通常 Scrum Master 提交；其中 CI 一节 4%'},
    {'en': [B('Peer Evaluation 1%', 17), ' — Opens Week 8 Wednesday, closes Saturday, 7 November, 9 pm'], 'zh': '互评：Microsoft Forms，按时交就得分，不接受迟交'},
    {'en': [B('Individual Report 4%', 17), ' — End of Week 8, Saturday, 7 November, 9 pm'], 'zh': '个人报告：≤ 2 页，Moodle 个人提交'},
    {'en': 'Together, these components contribute 30% of the overall course assessment.', 'zh': '合计 30%；报告 / 录像迟交每天扣 5%，最多五天。建议 Week 8 周三前写完初稿'},
], size=17, cn_size=13, sb=7)

d.two_col('3.1 Sprint 2 Demo — 10%', '演示：Week 8 lab 现场进行并录像，10–12 分钟，全员到场', [
    {'en': [B('When: ', 16), 'your Week 8 scheduled lab. Recording due end of Week 8 (Saturday, 9 pm)'], 'zh': '时间：Week 8 实验课；录像周六晚 9 点前交'},
    {'en': [B('Format: ', 16), 'Team presentation conducted live during your scheduled lab'], 'zh': '形式：实验课上现场团队展示'},
    {'en': [B('Recording: ', 16), 'The demo must be recorded, both audio (spoken) and video (slides/browser)'], 'zh': '录像：音频 + 屏幕都要'},
    {'en': [B('Submission: ', 16), 'Team submission via Moodle (MP4 or a text file with a link to the video shared on UNSW\'s OneDrive)'], 'zh': '提交：MP4，或放 OneDrive 链接的文本文件'},
    {'en': [B('Late penalty: ', 16), '5% per day up to five days'], 'zh': '迟交每天 5%，最多五天'},
], [
    {'en': 'The Sprint 2 demo is your team\'s opportunity to introduce its variation and show how far the team has taken it. The emphasis is on a working product that serves a clearly defined user, and on how the team\'s CI pipeline supports its development process.',
     'zh': '重点两件事：服务明确用户的可运行产品 + CI 流水线如何支撑开发'},
    {'en': 'The demo will run within 10–12 minutes, followed by questions from the tutor and/or peers.', 'zh': '10–12 分钟 + 提问'},
    {'en': 'All team members are expected to attend and present; non-attendance without Special Consideration will result in a 0 for the absent student.',
     'zh': '全员到场并参与展示；无特殊情况申请而缺席者该项 0 分（按人算）'},
    {'en': 'Each member should understand the team\'s work and be prepared to discuss relevant aspects of the project.', 'zh': '每个人都要能回答关于团队工作的问题'},
], size=15, cn_size=12, sb=5)

d.content('Demo: what your team should be prepared to show', '演示要展示的四样：变体与用户、从 main 运行的新功能、流水线策略、全员参与', [
    {'en': 'Your chosen variation, its target users and the problem it solves for them.', 'zh': '变体是什么、为谁、解决什么痛点——念一遍 persona，说出 3–5 条成功标准'},
    {'en': 'A working demonstration of the variation features built or evolved during Sprint 2. (Features must be shown through the interface, running from main.)',
     'zh': '在浏览器里演示 Sprint 2 的新功能，而且是从 main 分支运行——演示前一晚把 MR 合完，当天 git pull main 再启动'},
    {'en': 'Sprint 1 features and template features, including the Notes example, earn no credit, except where a Sprint 1 feature was evolved for the variation.',
     'zh': 'Sprint 1 功能和模板自带的 Notes 示例不得分；只有为变体演进过的 Sprint 1 功能可以讲，并说清演进了什么'},
    {'en': 'An overview of your CI pipeline strategy: its stages, when it runs and why the team designed it that way, with a recent pipeline run on a merge request.',
     'zh': '打开 GitLab：stage 结构、触发时机、为什么这样设计，再点开一个最近的 MR 看流水线'},
    {'en': 'Participation from all team members during the presentation and Q&A.', 'zh': '每个人都要讲一段、都要能答问'},
], size=16, cn_size=13, sb=6)

d.two_col('Demo: marking criteria and recording', '演示评分四项各 2–3%，录像用于交叉评分与特殊情况处理', [
    {'en': 'Marking Criteria'},
    {'en': [B('Variation and target users (2%)', 15), ': explain the variation, who it is for and the success criteria the team is working towards.'], 'zh': '变体与目标用户 2%', 'lvl': 1},
    {'en': [B('Working features (3%)', 15), ': demonstrate your own Sprint 2 variation features live through the user interface, running from main.'], 'zh': '可运行功能 3%：自己做的、界面上、从 main 跑', 'lvl': 1},
    {'en': [B('CI pipeline strategy (2%)', 15), ': explain the pipeline\'s design and show it running on a merge request.'], 'zh': 'CI 策略 2%：讲设计 + 展示 MR 上的运行', 'lvl': 1},
    {'en': [B('Presentation, teamwork and Q&A (3%)', 15), ': present clearly, with every member able to answer questions about the team\'s work.'], 'zh': '展示与问答 3%：人人能答', 'lvl': 1},
], [
    {'en': 'Recording'},
    {'en': 'We require a recording of your live lab demo for cross-marking and special consideration purposes.', 'zh': '录像用于交叉评分和处理特殊情况申请；Zoom / Teams / OBS 同时录音频和屏幕', 'lvl': 1},
    {'en': 'If your recording exceeds Moodle file upload limits, please upload your recording to your UNSW OneDrive and then upload to Moodle a text document with a link to the recording.',
     'zh': '超过上传限制就传 UNSW OneDrive，Moodle 交一个含链接的文本文件', 'lvl': 1},
    {'en': 'Set the link so anyone at UNSW with the link can view, and check it opens in a private browser window before submitting.',
     'zh': '权限设为 Anyone at UNSW with the link；交之前用无痕窗口测一遍', 'lvl': 1},
], size=15, cn_size=12, sb=5)

d.content('Demo run-of-show: 10–12 minutes', '演示分镜：按评分标准倒推，每段有人负责', [
    {'en': [B('0:00–1:30', 16), '  Variation, persona, the problem, 3–5 success criteria'], 'zh': '变体与目标用户 2%：念 persona、说痛点、列成功标准（成员 A）'},
    {'en': [B('1:30–6:30', 16), '  Live demo of Sprint 2 features in the browser, running from main; name the user story before each feature'], 'zh': '可运行功能 3%：每个功能先说对应哪条故事（成员 B、C 轮流）'},
    {'en': [B('6:30–9:00', 16), '  GitLab: .gitlab-ci.yml stages, why this design, a recent MR pipeline — ideally one failure → fix'], 'zh': 'CI 策略 2%：顺手展示一次失败 → 修复的记录（成员 D）'},
    {'en': [B('9:00–10:30', 16), '  Velocity Sprint 1 → Sprint 2, what the team learned, plan for Sprint 3'], 'zh': '展示与问答 3%：速度对比、学到什么、Sprint 3 打算（成员 E）'},
    {'en': [B('Q&A', 16), '  every member answers'], 'zh': '问答全员上：每个人都要了解整个项目，不只是自己那块'},
    {'zh': '彩排一次并计时；把 main 跑起来的那台电脑提前连好投影'},
], size=16, cn_size=13, sb=7)

d.two_col('3.2 Sprint 2 Team Report — 15%', '团队报告：PDF 约 20 页，写"怎么做的和为什么"，用 GitLab 证据支撑', [
    {'en': [B('Due: ', 16), 'end of Week 8, Saturday, 9 pm'], 'zh': '截止：Week 8 周六晚 9 点'},
    {'en': [B('Submission: ', 16), 'Team submission (usually the Scrum Master) via Moodle (PDF)'], 'zh': '团队提交，通常由 Scrum Master，PDF'},
    {'en': [B('Suggested length: ', 16), 'Approximately 20 pages (including appendices)'], 'zh': '约 20 页含附录；按分值分配篇幅'},
    {'en': [B('Late penalty: ', 16), '5% per day up to five days'], 'zh': '迟交每天 5%'},
    {'en': 'The report documents the variation your team chose, how you planned and monitored the sprint, and how you designed and used your CI pipeline.',
     'zh': '三条主线：变体、Sprint 的计划与监控、CI 流水线的设计与使用'},
    {'en': 'As in Sprint 1, the report should not simply describe what the team did. Explain how and why decisions were made, and support them with evidence from GitLab (screenshots preferred, GitLab links acceptable).',
     'zh': '不要只写"做了什么"，要写"怎么决定的、为什么"，并配 GitLab 截图'},
], [
    {'en': 'The report covers the following areas:'},
    {'en': 'Chosen Variation, Personas, Use Cases and Success Criteria — 3%', 'zh': '变体、persona、用例、成功标准（约 3 页）', 'lvl': 1},
    {'en': 'User Stories, Acceptance Criteria and Points — 2%', 'zh': '用户故事、验收标准、点数（约 3 页）', 'lvl': 1},
    {'en': 'Sprint Monitoring and Burndown/Velocity chart — 3%', 'zh': 'Sprint 监控与速度图（约 3 页）', 'lvl': 1},
    {'en': [B('CI Pipeline — 4%', 15)], 'zh': 'CI 流水线（4–5 页，最值钱）', 'lvl': 1},
    {'en': 'Sprint 2 Retrospective and Review of Sprint 1 Things to Try — 3%', 'zh': '回顾会 + Sprint 1 待尝试事项复盘（约 3 页）', 'lvl': 1},
    {'en': 'Appendix: Sprint 2 meeting minutes', 'zh': '附录：全部会议纪要，并在监控一节引用', 'lvl': 1},
], size=15, cn_size=12, sb=3)

d.content('Variation, personas, use cases and success criteria — 3%', '报告第一节：说清为谁、解决什么、为什么通用版不够、怎么判断成功', [
    {'en': 'Name the variation your team chose and the target user it serves. Describe the problem the variation solves and why the generic Sprint 1 splitter does not already solve it.',
     'zh': '"为什么 Sprint 1 通用版解决不了"是本节得分点，别漏'},
    {'en': 'Include one or more personas representing your target users, and the main use cases the variation supports.',
     'zh': 'persona 写一个具体的人：Mia，24 岁，和 3 个室友合租，每月替大家垫网费，最烦重复录入和月底追着要钱'},
    {'en': 'Then state three to five success criteria for the variation: specific, checkable statements of what the variation must achieve by the end of Sprint 3.',
     'zh': '成功标准要可核查：好的"室友两次点击内看到本月应付金额"；差的"系统易用"'},
    {'en': 'Your Sprint 3 report will evaluate what the team delivered against these criteria, so write them with that evaluation in mind.',
     'zh': 'Sprint 3 报告会逐条对照这些标准评估，所以现在写的时候就想着到时候怎么证明'},
], size=16, cn_size=13, sb=9)

d.content('User Stories, Acceptance Criteria and Points — 2%', '报告第二节：每条故事的全文、issue 号、验收标准、点数，以及 Sprint Goal', [
    {'en': 'Include the full text of each Sprint 2 user story, with its GitLab issue number, acceptance criteria and story points (recorded using the point labels on each issue).',
     'zh': '从 GitLab issue 直接复制：故事全文 + issue 号 + 验收标准 + 点数 label'},
    {'en': 'Identify the Sprint Goal and explain how the selected stories contribute to it and to your success criteria.',
     'zh': 'Sprint Goal 一句话，例如"让合租室友不用每月重复录入固定开销"，再说明每条故事怎么支撑它和成功标准'},
    {'en': 'Where stories were split, explain how and why.', 'zh': '拆分过的故事写拆分理由——这正是"show your thinking"'},
], size=17, cn_size=13, sb=10)

d.two_col('Sprint Monitoring and Burndown/Velocity chart — 3%', '报告第三节：监控证据 + 速度对比；分数给解读，不给数字', [
    {'en': 'What to include'},
    {'en': 'Explain how progress was monitored during Sprint 2, with evidence from the issue board and meetings.', 'zh': '不同日期的看板截图 + 会议纪要引用', 'lvl': 1},
    {'en': 'Include a velocity chart comparing Sprint 1 and Sprint 2: points committed and points completed in each sprint.', 'zh': '速度图：两个 Sprint 各自承诺多少点、完成多少点', 'lvl': 1},
    {'en': 'A story counts towards velocity only if it was merged into main and met its acceptance criteria by the end of the sprint.', 'zh': '做了 80% 的故事算 0，不算 80%', 'lvl': 1},
    {'en': 'UNSW\'s GitLab installation does not generate burndown charts; if you would like to include one, build it from the dates your issues were closed.', 'zh': '燃尽图要自己用 issue 关闭日期画', 'lvl': 1},
], [
    {'en': 'How it is marked'},
    {'en': 'Sprint 1 ran for about three weeks and Sprint 2 for three (including Flexibility Week). State each sprint\'s length when comparing velocity, and explain how you\'ll adjust for Sprint 3, which is a standard two-week sprint.',
     'zh': '比较时写明长度并折算：三周完成 21 点 ≈ 每周 7 点，Sprint 3 只有两周就只能承诺 ~14 点', 'lvl': 1},
    {'en': 'As in Sprint 1, the marks are for the interpretation, not the number.', 'zh': '分给的是解读，不是数字大小', 'lvl': 1},
    {'en': 'Explain how the team used its Sprint 1 velocity when deciding what to commit to, whether that decision was right, and how the team will plan Sprint 3.',
     'zh': '写清：Sprint 1 速度怎么用在 Sprint 2 的承诺上、对不对、Sprint 3 怎么改', 'lvl': 1},
], size=15, cn_size=12, sb=5)

d.content('CI Pipeline — 4%: the most important part of the report', '报告第四节：按五个小标题逐段写满——设计、工具、理由、证据、影响', [
    {'en': [B('Design', 15), ': the stages and jobs in your pipeline, what triggers it, the order the jobs run in, and what happens when a job fails. A diagram of the pipeline is recommended.'],
     'zh': '画一张 stage → job 的图，箭头标触发条件（MR / push main），写清失败时的处理流程'},
    {'en': [B('Tools', 15), ': the tools and configuration your pipeline uses (for example, GitLab CI, Docker images, linters, test runners and coverage tools) and how they relate to the template\'s make targets.'],
     'zh': 'GitLab CI、python:3.12 镜像、ruff、pytest、pytest-cov，以及 make lint / test / coverage 分别被哪个 job 调用'},
    {'en': [B('Rationale', 15), ': why the team designed the pipeline this way, the alternatives the team considered, and any trade-offs, such as pipeline run time against thoroughness.'],
     'zh': '为什么 lint 放前面（快、便宜）；考虑过但没做的（Docker 构建、e2e）及原因；时间 vs 彻底的取舍'},
    {'en': [B('Evidence it runs', 15), ': screenshots or links showing pipelines running on merge requests and on main, including at least one failing pipeline and how the team responded to it.'],
     'zh': 'MR 上的绿、main 上的绿、至少一次红 + 修复它的 commit'},
    {'en': [B('Impact on the team', 15), ': how the pipeline changed the way the team reviewed and merged work during the sprint.'],
     'zh': '例如"评审者不再手动跑测试，评审从 30 分钟降到 10 分钟"、"两次红流水线在合并前拦住了 bug"'},
], size=15, cn_size=12, sb=6)

d.content('Retrospective + review of Sprint 1 "Things to try" — 3%', '报告第五节：Sprint 2 回顾会，并逐条复盘 Sprint 1 的待尝试事项', [
    {'en': 'Conduct and document a Sprint 2 retrospective. Record who facilitated it and how long it took, and cover what went well, what did not go well, and things to try in Sprint 3.',
     'zh': '写明主持人和时长；三栏：做得好、做得不好、Sprint 3 要试'},
    {'en': 'As in Sprint 1, focus on processes rather than deliverables, and explain the "why" behind each item.',
     'zh': '关注流程而非交付物，每一项都解释"为什么"'},
    {'en': 'In addition, assess each "Things to try" item from your Sprint 1 retrospective: did the team carry it out, did it work, and what evidence shows this?',
     'zh': '用表格逐条复盘 Sprint 1 的每个待尝试事项：做了吗 / 有效吗 / 证据是什么'},
    {'en': 'A thing to try that the team did not attempt should be reported honestly, with the reason.',
     'zh': '没做的如实写"没做，因为……"；诚实不扣分，编证据才危险'},
    {'en': 'Meeting minutes: include your Sprint 2 meeting minutes as an appendix, and refer to them in your discussion of sprint monitoring.',
     'zh': '会议纪要放附录，并在监控一节引用'},
], size=16, cn_size=13, sb=7)

d.content('3.3 Sprint 2 Peer Evaluation — 1%', '互评：个人通过 Microsoft Forms 提交，按时交就得 1%，不接受迟交', [
    {'en': 'Due: end of Week 8, Saturday, 9 pm · Submission: Individual submission via Microsoft Forms (link available in Moodle) · Late penalty: No late submissions allowed!',
     'zh': 'Week 8 周三表单开放，周六晚 9 点关闭；建议收到链接当天就填'},
    {'en': 'Each student must complete a peer evaluation for their teammates at the end of Sprint 2. The peer evaluation provides an opportunity to reflect on how effectively each member contributed to the team\'s work and collaborative environment.',
     'zh': '每个人给每位队友填一份，反思各自对团队工作和协作环境的贡献'},
    {'en': 'You will be asked to evaluate each teammate on: Participation · Dependability · Team wellbeing · Work contribution',
     'zh': '四个维度：参与度、可靠性、团队氛围、工作贡献（具体行为见 2.3.3 那页）'},
    {'en': 'Peer evaluation responses are seen by teaching staff only. They are used to help teaching staff identify teams that may require additional support and to understand how collaboration is functioning within the group.',
     'zh': '只有老师看得到；用来发现需要帮助的小组，不是用来互相扣分，所以如实填写'},
    {'en': 'The Sprint 2 Peer Evaluation is worth 1%, with the mark awarded for on-time submission. There are no late submissions for this component; under the assessment outline, a missed peer evaluation receives zero.',
     'zh': '这 1% 最容易拿也最容易丢：交了就有，没交就 0'},
], size=15, cn_size=12, sb=7)

d.two_col('3.4 Sprint 2 Individual Report — 4%', '个人报告：≤ 2 页，写"我"做了什么并用 GitLab 证据支撑，要反思不要罗列', [
    {'en': [B('Due: ', 15), 'end of Week 8, Saturday, 9 pm · ', B('Submission: ', 15), 'Individual via Moodle'], 'zh': '个人通过 Moodle 提交'},
    {'en': [B('Suggested maximum length: ', 15), '2 pages (not including screenshots) · ', B('Late penalty: ', 15), '5% per day up to five days'], 'zh': '最多 2 页正文，截图不算'},
    {'en': 'Each student must submit an individual report describing and reflecting on their own contribution to Sprint 2. This is separate from the Team Report and should focus specifically on your individual work, responsibilities, participation, and learning during the sprint.',
     'zh': '用"我"不用"我们"；团队报告写过的别复制过来'},
    {'en': 'Your contribution should be supported by appropriate evidence. In particular, you should connect your work to relevant GitLab issues, merge requests, and commits where applicable.',
     'zh': '每条贡献后面跟证据：!14（MR）、#23（issue）、commit 短哈希'},
    {'en': 'The report should be reflective rather than simply a list of completed tasks.', 'zh': '不是"我做了 #23、#24"，而是"#24 我低估了点数，因为……，下次……"'},
], [
    {'en': 'Your individual report should address:'},
    {'en': 'Your contribution to Sprint 2', 'zh': '个人完成的工作与承担的职责', 'lvl': 1},
    {'en': 'Evidence of your contribution', 'zh': '关联 issue / MR / commit 等仓库证据', 'lvl': 1},
    {'en': 'Your Scrum role', 'zh': 'Scrum 角色及你如何履行它的职责', 'lvl': 1},
    {'en': 'Meeting participation', 'zh': '会议参与：怎么沟通进度、阻碍、下一步', 'lvl': 1},
    {'en': 'Lab checkpoints', 'zh': 'Week 7 lab check-in 里你的参与和贡献', 'lvl': 1},
    {'en': 'What worked', 'zh': '自己或团队流程中有效的方面', 'lvl': 1},
    {'en': 'What did not work', 'zh': '困难、局限、效果差的做法——要具体', 'lvl': 1},
    {'en': 'One change for Sprint 3', 'zh': '只写一个、具体可验证，如"每个 MR 不超过 200 行"', 'lvl': 1},
], size=14, cn_size=12, sb=3, split=6.4)

# ===================================================================== PART 4 / 5
d.section('PART 4 / 5 — Plagiarism & AI mode', '第四、五部分：学术诚信、AI 使用模式、版权',
          '一条红线记牢：代码和报告只在本组成员与 COMP9820 教学人员之间流通')

d.content('4. Plagiarism & Academic Misconduct Notice', '抄袭与学术不端：仓库保持私有，代码不出组，想法可以聊、代码不能给', [
    {'en': 'Your program must be entirely your group\'s work. Plagiarism detection software may be used to compare all submissions pairwise (including submissions for similar assignments in previous terms), and serious penalties will be applied, including an entry on UNSW\'s plagiarism register.',
     'zh': '所有提交两两比对，还比往届类似作业；处罚含记入 UNSW 抄袭登记册'},
    {'en': 'Do not provide or show your project work to any other person, except for your group and the teaching staff of COMP9820.', 'zh': '别把代码发给隔壁组"参考一下"', 'lvl': 1},
    {'en': 'Do not copy ideas or code from others outside your group.', 'zh': '别抄往届或网上的 Expense Splitter 项目', 'lvl': 1},
    {'en': 'Do not use a publicly accessible repository or allow anyone outside your group to see your code, except for the teaching staff of COMP9820.', 'zh': '仓库不能 Public，也别推到个人 GitHub "备份"', 'lvl': 1},
    {'en': 'If you knowingly provide or show your assignment work to another person for any reason, and work derived from it is submitted, you may be penalized, even if the work was submitted without your knowledge or consent.',
     'zh': '即使对方抄了你不知道，给的人也可能被罚；查官方文档和 Stack Overflow 的通用用法是学习，不算抄袭'},
], size=15, cn_size=12, sb=6)

d.two_col('Penalties, resources, and the Assessment AI Mode', '处罚与资源；本次考核的 AI 模式只允许拼写 / 语法 / 引用这类编辑辅助', [
    {'en': 'The penalties for such an offence may include negative marks, automatic failure of the course and possibly other academic discipline. Assignment submissions will be examined both automatically and manually for such submissions.',
     'zh': '处罚：负分、课程不及格、其他纪律处分；自动 + 人工都查'},
    {'en': 'Academic Integrity and Plagiarism — student.unsw.edu.au/plagiarism', 'zh': '学术诚信与抄袭页面'},
    {'en': 'UNSW Plagiarism Policy (PDF)', 'zh': 'UNSW 抄袭政策'},
    {'en': 'The course reserves the right to reassess whether you meet course outcomes through a similar assessment under significant suspicion of academic misconduct.',
     'zh': '有重大嫌疑时，课程可用类似考核重新评估你'},
    {'en': 'Copyright Notice: reproducing, publishing, posting, distributing or translating this assignment is an infringement of copyright.',
     'zh': '题目本身也受版权保护：别发到公开网站或题库'},
], [
    {'en': '5. Assessment AI Mode: Simple Editing Assistance'},
    {'en': 'You are permitted to use standard editing and referencing functions, such as spell-check, grammar-check and reference managers.',
     'zh': '允许：拼写检查、语法检查、文献管理器', 'lvl': 1},
    {'en': 'You must not use any functions that generate or paraphrase passages of text or other media, whether based on your own work or not.',
     'zh': '不允许：让 AI 生成或改写段落——"润色一遍"也在禁止之列', 'lvl': 1},
    {'en': 'If your Convenor has concerns that your submission contains AI-generated text or media, you may be asked to account for your work; if you cannot demonstrate your understanding you may be referred to UNSW Conduct & Integrity Office.',
     'zh': '被怀疑会约谈让你解释自己写的内容；最稳妥：每句话都能当面复述并给出 GitLab 证据', 'lvl': 1},
    {'en': 'More on Generative AI: student.unsw.edu.au/assessment/ai', 'zh': '生成式 AI 允许使用范围的官方页面', 'lvl': 1},
], size=14, cn_size=12, sb=5)

d.closing(['本周要做（Week 5）：定目标用户和 persona → 写并估算变体用户故事 → 商定 Sprint Goal、建 Sprint 2 milestone → 至少开 2 次有纪要的会',
           '弹性周（Week 6）：把 .gitlab-ci.yml 放进仓库，让 lint + test 在 MR 和 main 上跑绿，勾上 Pipelines must succeed',
           '截止：演示录像、团队报告、个人报告、互评全部 11 月 7 日（周六）晚 9 点；互评不接受迟交'])
d.save()
