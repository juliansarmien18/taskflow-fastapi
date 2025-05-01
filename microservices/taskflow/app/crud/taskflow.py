from sqlalchemy.orm import Session
from microservices.taskflow.app.models.taskflow import *
from microservices.taskflow.app.schemas.taskflow import *

def get_taskflow(db: Session, item_id: int):
    return db.query(Taskflow).filter(Taskflow.id == item_id).first()

def create_taskflow(db: Session, item: TaskflowCreate):
    db_item = Taskflow(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_taskflow(db: Session, db_item: Taskflow, item: TaskflowCreate):
    db_item.name = item.name
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_taskflow(db: Session, item_id: int):
    db_item = db.query(Taskflow).filter(Taskflow.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return db_item
