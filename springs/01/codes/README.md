# Task Tracker — Sprint 1

COMP9820 Sprint 1 最小可运行版本：**显示任务列表 + 添加任务 + 删除任务**。
技术栈按课程要求只用 **Python (Flask) + HTML + CSS**，没有 JavaScript、没有数据库。

## How to Run

```bash
# 1. 进入项目目录
cd springs/01

# 2. 创建并激活虚拟环境（只需第一次）
python3 -m venv .venv
source .venv/bin/activate          # Windows(WSL) 同样；PowerShell 用 .venv\Scripts\Activate.ps1

# 3. 安装依赖
pip install -r requirements.txt

# 4. 启动
python app.py
# 或者：flask --app app run --debug
```

浏览器打开 <http://127.0.0.1:5000> 即可看到页面。

## Project Structure

```
01/
├── app.py                 # Flask 后端：3 个路由（/、/add、/delete/<id>）
├── templates/index.html   # 前端页面（Jinja2 模板）
├── static/style.css       # 样式
├── requirements.txt       # 依赖
├── tests/test_app.py      # （可选）pytest 测试，demo 前自检
├── README.md
└── 教学文档_Sprint1_TaskTracker.md   # 代码讲解 + demo 脚本
```

## Making Your First Changes

| 想改什么 | 去哪里改 |
|---|---|
| 页面标题 "My Tasks" | `templates/index.html` 里的 `<h1>` |
| 按钮颜色 / 布局 | `static/style.css` |
| 添加任务的行为（例如去掉空输入保护） | `app.py` 的 `add_task()` |
| 删除任务的行为 | `app.py` 的 `delete_task()` |
| 新增一个页面 | 在 `app.py` 加一个 `@app.route(...)` 函数 + 在 `templates/` 加一个 html |

改完保存，`debug=True` 会自动重启服务器，刷新浏览器即可看到效果。

## Run the Tests (optional)

```bash
pytest -q
```

## Common Questions

**Q: 刷新后任务没了？**
正常。Sprint 1 数据只放在内存（`app.py` 里的 `tasks` 列表），重启服务器就清空。持久化是 Sprint 3 的事。

**Q: 提交表单后地址栏为什么还是 `/`？**
因为 `/add` 和 `/delete/<id>` 处理完都 `redirect` 回首页（PRG 模式），避免按 F5 重复提交。

**Q: 端口被占用？**
`flask --app app run --port 5001`。

**Q: `ModuleNotFoundError: No module named 'flask'`？**
没激活虚拟环境或没装依赖，回到 How to Run 第 2、3 步。
