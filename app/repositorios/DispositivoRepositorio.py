from sqlalchemy import select

from app.core.database import obtener_sesion
from app.entidades.Dispositivo import Dispositivo


class DispositivoRepositorio:
    def guardar(self, dispositivo):
        with obtener_sesion() as sesion:
            sesion.add(dispositivo)
            sesion.flush()
        return dispositivo

    def obtener_byplaca(self, placa):
        with obtener_sesion() as sesion:
            resultado = sesion.execute(
                select(Dispositivo).where(Dispositivo.placa == placa)
            )
            return resultado.scalar_one_or_none()

    def obtener_byid(self, id_dispositivo):
        with obtener_sesion() as sesion:
            return sesion.get(Dispositivo, id_dispositivo)

    def listar_dispositivos(self):
        with obtener_sesion() as sesion:
            resultado = sesion.execute(select(Dispositivo))
            return resultado.scalars().all()
