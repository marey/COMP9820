"""
Task Tracker — Sprint 1 最小实现（Flask 后端）

Sprint 1 要求：能「显示任务列表」+「添加任务」+「删除任务」即可。
不需要：数据库 / 持久化、漂亮 UI、邮件确认、空输入校验（这里只做了最简单的去空格判断）。

一句话理解 Flask：
    一个「路由（route）」= 一个 URL + 一个 Python 函数。
    浏览器发来请求（request）→ Flask 找到匹配的函数 → 函数返回响应（response）。
"""

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# ---------------------------------------------------------------------------
# 数据：Sprint 1 只放在内存里（一个 Python 列表）。
# 重启服务器数据就没了——这是允许的，持久化留到 Sprint 3。
# 每个任务是一个 dict：{"id": 1, "title": "Finish lab_git"}
# ---------------------------------------------------------------------------
tasks: list[dict] = []
_next_id = 1  # 自增 id，删除时靠 id 精确定位，而不是靠列表下标


def _new_id() -> int:
    """返回一个新的、不会重复的任务 id。"""
    global _next_id
    current = _next_id
    _next_id += 1
    return current


def reset_tasks() -> None:
    """清空所有任务（测试时用，保证每个测试互不干扰）。"""
    global _next_id
    tasks.clear()
    _next_id = 1


# ---------------------------------------------------------------------------
# 路由 1：显示任务列表（Starter code 自带）
#   GET /  →  渲染 templates/index.html，并把 tasks 列表传给模板
# ---------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


# ---------------------------------------------------------------------------
# 路由 2：添加任务（Sprint 1 新功能 —— feature-add-task 分支）
#   POST /add  →  从表单读取 title，追加到 tasks，然后重定向回首页
#
# 为什么用 POST 而不是 GET？
#   GET 用来「读取」，POST 用来「改变服务器上的数据」。添加任务会改数据，所以用 POST。
# 为什么处理完要 redirect 而不是直接 render_template？
#   这叫 PRG 模式（Post → Redirect → Get）：避免用户按 F5 刷新时重复提交同一个任务。
# ---------------------------------------------------------------------------
@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    if title:  # 最简单的保护：空字符串不加入（Sprint 1 不强制要求）
        tasks.append({"id": _new_id(), "title": title})
    return redirect(url_for("index"))


# ---------------------------------------------------------------------------
# 路由 3：删除任务（Sprint 1 新功能 —— feature-delete-task 分支）
#   POST /delete/<task_id>  →  按 id 找到任务并移除，然后重定向回首页
#
# <int:task_id> 是 Flask 的「URL 变量」：/delete/3 会把 3 作为整数传给函数参数 task_id。
# ---------------------------------------------------------------------------
@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id: int):
    tasks[:] = [t for t in tasks if t["id"] != task_id]  # 保留 id 不相等的任务
    return redirect(url_for("index"))


if __name__ == "__main__":
    # debug=True：改代码后自动重启，并在浏览器显示详细报错（只在开发时用）
    app.run(debug=True)
