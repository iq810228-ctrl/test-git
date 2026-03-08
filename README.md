FastAPI Task CRUD API
這是一個使用 FastAPI 建立的任務管理 API，實現任務的新增、查詢、更新、刪除(CRUD)功能
此專案示範：

使用 FastAPI 建立 RESTful API

使用 SQLAlchemy 操作資料庫

使用 Pydantic 進行資料驗證

使用 SQLite 儲存資料


Tech Stack

Python
FastAPI
SQLAlchemy
SQLite
Uvicorn


API Endpoints
| HTTP 方法 |     路徑      |    功能     |
|-----------|--------------|-------------|
| POST      | /tasks/      | 新增任務     |
| GET       | /tasks/      | 取得所有任務 |
| GET       | /tasks/{id}  | 取得單一任務 |
| PUT       | /tasks/{id}  | 更新任務     |
| DELETE    | /tasks/{id}  | 刪除任務     |

操作範例
1.新增任務(Create)

Request JSON:
{
  "title": "買牛奶",
  "description": "晚上下班順路買"
}

Response JSON:
{
  "title": "買牛奶",
  "description": "晚上下班順路買",
  "id": 1,
  "completed": false
}

Request JSON:
{
  "title": "寫履歷",
  "description": "完成 FastAPI 專案"
}

Response JSON:
{
  "title": "寫履歷",
  "description": "完成 FastAPI 專案",
  "id": 2,
  "completed": false
}

2.取得所有任務（Read All）

Response JSON:
[
  {
    "title": "買牛奶",
    "description": "晚上下班順路買",
    "id": 1,
    "completed": false
  },
  {
    "title": "寫履歷",
    "description": "完成 FastAPI 專案",
    "id": 2,
    "completed": false
  }
]

3.取得單一任務（Read One）

Response JSON:
{
  "title": "買牛奶",
  "description": "晚上下班順路買",
  "id": 1,
  "completed": false
}

4.更新任務（Update）

Request JSON:
{
  "title": "買牛奶",
  "description": "改成早上買",
  "completed": true
}

Response JSON:
{
  "title": "買牛奶",
  "description": "改成早上買",
  "id": 1,
  "completed": true
}
 
5.刪除任務（Delete）

Request：DELETE /tasks/1

Response JSON:
{
  "detail": "Task deleted"
}

Request：DELETE /tasks/999
Error: Not Found

Response JSON:
{
  "detail": "Task not found"
}


如何執行專案

安裝套件
pip install fastapi uvicorn sqlalchemy

啟動 API server
uvicorn app.main:app --reload

開啟 Swagger 文件
http://127.0.0.1:8000/docs