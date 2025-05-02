from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from app.models import User
from app.core.config import settings
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from app.db import get_db
from jose.exceptions import JWTError


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Crea un token JWT con el id de usuario, username y fecha de expiración.
    """
    to_encode = data.copy()

    # Asegúrate de que el `data` contenga `user_id` y `username`
    user_id = data.get("sub")  # O como lo tengas en tu payload
    username = data.get("username")
    password = data.get("password")# Asegúrate de que `data` tenga el `username`
    
    # Calcula la expiración del token
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.access_token_expire_minutes))

    # Agrega los campos al payload
    to_encode.update({
        "sub": user_id,  # `sub` es un campo estándar que se usa para identificar al sujeto
        "username": username,
        "password": password,# Agregamos el username
        "exp": expire  # Tiempo de expiración
    })

    # Codifica el token
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(request: Request, db: Session = Depends(get_db)) -> User:
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing or invalid Authorization header",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        user_id: str = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token payload")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return user