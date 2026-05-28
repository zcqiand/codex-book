# 从第 31 章提取
# 来源：Codex 从入门到项目实践

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Supplier, Product

router = APIRouter(prefix="/api/suppliers", tags=["suppliers"])

@router.get("/")
def list_suppliers(db: Session = Depends(get_db)):
    return db.query(Supplier).all()

@router.post("/", status_code=201)
def create_supplier(name: str, contact_person: str = "", phone: str = "",
                     db: Session = Depends(get_db)):
    supplier = Supplier(name=name, contact_person=contact_person, phone=phone)
    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    return supplier

@router.get("/{supplier_id}")
def get_supplier(supplier_id: int, db: Session = Depends(get_db)):
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if not supplier:
        raise HTTPException(404, "供应商不存在")
    return supplier

@router.patch("/{supplier_id}/status")
def update_supplier_status(supplier_id: int, status: str,
                            db: Session = Depends(get_db)):
    supplier = db.query(Supplier).filter(Supplier.id == supplier_id).first()
    if not supplier:
        raise HTTPException(404, "供应商不存在")
    supplier.status = status
    db.commit()
    return supplier