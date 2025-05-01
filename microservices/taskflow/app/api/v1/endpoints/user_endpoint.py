from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.taskflow import *
from app.schemas.taskflow import *
from app.db.session import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/create-user/", response_model=schemas.UserWithToken)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))