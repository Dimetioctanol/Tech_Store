from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.user import User
from app.models.role import Role
from app.schemas.user import UserRegister, UserLogin, TokenResponse, UserResponse
from app.core.security import hash_password, verify_password, create_access_token

#Verificar email
def register_user(data: UserRegister, db:Session) -> UserResponse:
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail = "El email ya está registrado"
        )
    
    #Rol 'customer' por defecto

    role = db.query(Role).filter(Role.name == "customer").first()
    if not role:
        raise HTTPException(
            status_code= status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Rol por defecto no encontrado"
        )
    

    user = User(
        first_name = data.first_name,
        last_name = data.last_name,
        email = data.email,
        password_hash = hash_password(data.password),
        role_id = role.id
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)

def login_user(data: UserLogin, db:Session) -> TokenResponse:
    #Buscar usuario

    user = db.query(User).filter(User.email == data.email).first()

    #Verificar credenciales

    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Credenciales incorrectas"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= "Credenciales incorrectas"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code= status.HTTP_403_FORBIDDEN,
            detail= "Usuario inactivo"
        )
    

    token = create_access_token({"sub": str(user.id), "role": user.role.name})
    return TokenResponse(access_token=token)
    