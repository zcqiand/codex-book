# 从第 33 章提取
# 来源：Codex 从入门到项目实践

from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.metrics import (
    compute_dashboard_metrics,
    get_daily_sales_last_7_days,
    get_low_stock_alerts,
)

router = APIRouter(prefix="/dashboard", tags=["dashboard"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def dashboard(request: Request, db: Session = Depends(get_db)):
    """数据看板首页：核心指标 + 趋势图 + 预警列表。"""
    metrics = compute_dashboard_metrics(db)
    daily_sales = get_daily_sales_last_7_days(db)
    low_stock = get_low_stock_alerts(db)

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "metrics": metrics,
        "daily_sales": daily_sales,
        "low_stock": low_stock,
    })