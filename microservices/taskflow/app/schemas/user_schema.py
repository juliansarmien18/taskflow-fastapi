from typing import Optional
from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class UserCreate(BaseModel):
    username: str = Field(..., example="julian")
    email: str = Field(..., example="julian")
    password: str = Field(..., min_length=8, example="prueba1234")
    full_name: Optional[str] = Field(None, example="Julian Sarmiento")

# 📤 Usuario sin contraseña, para respuestas
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str] = None
    is_active: bool
    is_superuser: bool

    class Config:
        orm_mode = True

# 📤 Respuesta que incluye el token
class UserWithToken(BaseModel):
    user: UserResponse
    access_token: str
    token_type: str = "bearer"