"""
Task Tracker 最小测试。
Sprint 1 课程还没讲测试、也不要求测试；这里只是用来在 demo 前快速确认三个功能没坏。
运行：pytest -q
"""

import pytest

import app as tasktracker


@pytest.fixture
def client():
    """每个测试前清空任务，拿到一个可以模拟浏览器请求的测试客户端。"""
    tasktracker.reset_tasks()
    tasktracker.app.config["TESTING"] = True
    with tasktracker.app.test_client() as c:
        yield c


def test_index_shows_empty_state(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"My Tasks" in resp.data
    assert b"No tasks yet" in resp.data


def test_add_task_appears_in_list(client):
    resp = client.post("/add", data={"title": "Finish lab_git"})
    assert resp.status_code == 302  # PRG：添加后重定向回首页
    assert resp.headers["Location"].endswith("/")

    page = client.get("/")
    assert b"Finish lab_git" in page.data
    assert tasktracker.tasks == [{"id": 1, "title": "Finish lab_git"}]


def test_add_blank_task_is_ignored(client):
    client.post("/add", data={"title": "   "})
    assert tasktracker.tasks == []


def test_delete_task_removes_only_that_task(client):
    client.post("/add", data={"title": "Task A"})
    client.post("/add", data={"title": "Task B"})
    client.post("/add", data={"title": "Task C"})

    resp = client.post("/delete/2")  # 删除 Task B
    assert resp.status_code == 302

    titles = [t["title"] for t in tasktracker.tasks]
    assert titles == ["Task A", "Task C"]
    page = client.get("/")
    assert b"Task B" not in page.data


def test_delete_unknown_id_is_harmless(client):
    client.post("/add", data={"title": "Only task"})
    client.post("/delete/999")
    assert len(tasktracker.tasks) == 1


def test_task_title_is_html_escaped(client):
    client.post("/add", data={"title": "<script>alert(1)</script>"})
    page = client.get("/")
    assert b"<script>" not in page.data
    assert b"&lt;script&gt;" in page.data
