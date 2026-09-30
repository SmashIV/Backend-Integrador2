from datetime import datetime

from sqlalchemy import select

from app.core.database import obtener_sesion
from app.entidades.Alerta import Alerta


class AlertaRepositorio:
    def guardar(self, alerta):
        with obtener_sesion() as sesion:
            sesion.add(alerta)
            sesion.flush()
        return alerta

    def obtener_alertas_recientes(self, limite=10):
        with obtener_sesion() as sesion:
            resultado = sesion.execute(
                select(Alerta).order_by(Alerta.fecha_hora.desc()).limit(limite)
            )
            return resultado.scalars().all()

    def atender_alerta(self, id_alerta, id_usuario):
        with obtener_sesion() as sesion:
            alerta = sesion.get(Alerta, id_alerta)
            if not alerta:
                return None
            alerta.fecha_vista = datetime.now()
            alerta.id_usuario = id_usuario
            sesion.flush()
            return alerta
