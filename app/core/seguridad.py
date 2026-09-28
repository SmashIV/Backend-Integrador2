from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash
from pwdlib.hashers.bcrypt import BcryptHasher

from app.core.config import jwt_settings

password_hash = PasswordHash([BcryptHasher()])


def crear_token_acceso(datos_usuario):
    expiracion = datetime.now(timezone.utc) + timedelta(
        minutes=jwt_settings.expire_minutes
    )
    payload = {
        "id_usuario": str(datos_usuario["id_usuario"]),
        "nombre": datos_usuario["nombre"],
        "rol": datos_usuario["rol"],
        "email": datos_usuario["email"],
        "exp": expiracion,
    }
    return jwt.encode(payload, jwt_settings.secret, algorithm=jwt_settings.algorithm)


def verificar_token(token):
    try:
        return jwt.decode(
            token, jwt_settings.secret, algorithms=[jwt_settings.algorithm]
        )
    except jwt.PyJWTError:
        return None