from passlib.context import CryptContext
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from app.core.config import settings
from sqlalchemy.orm import Session
from app.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def verify_given_password(given_password, hashed_password):
    return given_password==hashed_password

def get_password_hash(password):
    return pwd_context.hash(password)

class Portador(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> dict:
        """
        Sobrescribe __call__ para verificar el token JWT y validar el usuario y contraseña.
        """
        credenciales = await super().__call__(request)
        token = credenciales.credentials

        # Validamos el token
        payload = self.valida_token(token)

        # Accedemos a la sesión de la base de datos desde request.state.db
        db: Session = request.state.db
        user = db.query(User).filter(User.username == payload.get("username")).first()

        if not user or not verify_given_password(payload.get("password", ""), user.hashed_password):
            raise HTTPException(status_code=403, detail="Credenciales inválidas")

        return {"user": user}  # Retornamos el usuario para uso posterior

    def valida_token(self, token: str):
        """
        Valida el token JWT.
        """
        try:
            return jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        except JWTError:
            raise HTTPException(status_code=403, detail="Token inválido")
