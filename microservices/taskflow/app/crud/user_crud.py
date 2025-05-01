from sqlalchemy.orm import Session
from app import schemas
from app.auth.jwt_config import create_access_token, get_password_hash
from app.models.user_model import User
from app.schemas.user_schema import UserCreate

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def create_user(db: Session, user: UserCreate):
    # Verifica si el email ya está registrado
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise ValueError("El correo ya está registrado")

    # Hashear la contraseña
    hashed_password = get_password_hash(user.password)

    # Crear un nuevo usuario
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Crear token JWT con el id del usuario
    access_token = create_access_token(data={"sub": str(new_user.id)})

    # Crear la respuesta en el formato esperado
    user_response = schemas.UserResponse(
        id=new_user.id,
        username=new_user.username,
        email=new_user.email,
        full_name=new_user.full_name,
        is_active=new_user.is_active,
        is_superuser=new_user.is_superuser
    )

    return schemas.UserWithToken(
        user=user_response,
        access_token=access_token,
        token_type="bearer"
    )
