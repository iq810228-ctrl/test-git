from fastapi import FastAPI
from app.routes import tasks
from app.database import init_db

app = FastAPI()

init_db()  # 建立資料庫 table

app.include_router(tasks.router)