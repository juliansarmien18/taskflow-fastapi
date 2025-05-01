from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.taskflow import *
from app.schemas.taskflow import *
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=Taskflow)
def create_taskflow(item: TaskflowCreate, db: Session = Depends(get_db)):
    return create_taskflow(db=db, item=item)

@router.get("/{item_id}", response_model=Taskflow)
def read_taskflow(item_id: int, db: Session = Depends(get_db)):
    db_item = get_taskflow(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Taskflow not found")
    return db_item

@router.put("/{item_id}", response_model=Taskflow)
def update_taskflow(item_id: int, item: TaskflowCreate, db: Session = Depends(get_db)):
    db_item = get_taskflow(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Taskflow not found")
    return update_taskflow(db=db, db_item=db_item, item=item)

@router.delete("/{item_id}", response_model=Taskflow)
def delete_taskflow(item_id: int, db: Session = Depends(get_db)):
    db_item = get_taskflow(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Taskflow not found")
    return delete_taskflow(db=db, item_id=item_id)

# Add more routes as needed
