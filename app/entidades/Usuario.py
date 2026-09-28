from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(70))
    email: Mapped[str] = mapped_column(String(120), unique=True)
    contrasena: Mapped[str] = mapped_column(String(30))
    rol: Mapped[str] = mapped_column(String(20), default="Operador")
