from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class Telemetria(Base):
    __tablename__ = "telemetria"
    __mapper_args__ = {"eager_defaults": True}

    id_lectura: Mapped[int] = mapped_column(Integer, primary_key=True)
    fecha_hora: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    temperatura: Mapped[float] = mapped_column(Numeric(5, 2))
    humedad: Mapped[float] = mapped_column(Numeric(5, 2))
    gases: Mapped[float] = mapped_column(Numeric(7, 2))
    latitud: Mapped[float] = mapped_column(Numeric(10, 7))
    longitud: Mapped[float] = mapped_column(Numeric(10, 7))
    id_dispositivo: Mapped[int] = mapped_column(ForeignKey("dispositivos.id_dispositivo"))
