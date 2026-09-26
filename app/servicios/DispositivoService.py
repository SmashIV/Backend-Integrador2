from app.dto.DispositivoDTO import DispositivoCrearDTO
from app.entidades.Dispositivo import Dispositivo
from app.repositorios.DispositivoRepositorio import DispositivoRepositorio

class DispositivoService:
    def __init__(self):
        self.repositorio = DispositivoRepositorio()

    def registrar_dispositivo(self, datos):
        placa_corregida = datos.placa.strip().upper()
        dispositivo_existente = self.repositorio.obtener_byplaca(placa_corregida)
        if dispositivo_existente:
            raise ValueError(f"El dispositivo del camión {placa_corregida} ya está registrado")
        entidad = Dispositivo(
            placa = placa_corregida,
            nombre_chofer= datos.nombre_chofer.strip(),
            estado = datos.estado.strip(),
        )
        return self.repositorio.guardar(entidad)

    def obtener_byid(self, id_dispositivo):
        return self.repositorio.obtener_byid(id_dispositivo)

    def listar_dispositivos(self):
        return self.repositorio.listar_dispositivos()