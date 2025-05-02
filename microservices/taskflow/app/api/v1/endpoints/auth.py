from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import crud, schemas
from app.auth.jwt_config import create_access_token
from app.db.session import get_db
from app.core.security import verify_password

router = APIRouter()

@router.post("/token", response_model=schemas.Token)
def login_for_access_token(login_data: schemas.LoginRequest, db: Session = Depends(get_db)):
    # Buscar el usuario por el email (o username si es lo que prefieres)
    user = crud.get_user_by_username(db, username=login_data.username)  # Asumo que LoginRequest ahora usa email
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(
            status_code=400,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Crear un token JWT
    access_token = create_access_token(data={"sub": str(user.id), "username": user.username, "password": user.hashed_password})
    return {"access_token": access_token, "token_type": "bearer"}
