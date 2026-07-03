from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime

class UserRegister (BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

    @field_validator('password')
    @classmethod
    def password_strength(cls, value):
        if len (value) < 8:
            raise ValueError("La contraseña debe tener mínimo 8 caracteres")
        return value.strip()

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"