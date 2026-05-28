# 从第 29 章提取
# 来源：Codex 从入门到项目实践

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///ecommerce.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # FastAPI 异步需要
    echo=False,                                 # 生产环境关闭 SQL 回显
)

@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    """每次连接时激活 WAL 模式和外键约束。"""
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA journal_mode=WAL")
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """FastAPI 依赖注入：每个请求获取独立 session，请求结束后关闭。"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()