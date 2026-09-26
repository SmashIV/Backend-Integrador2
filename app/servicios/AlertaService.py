from app.repositorios.AlertaRepositorio import AlertaRepositorio

class AlertaService:
    def __init__(self):
        self.repositorio = AlertaRepositorio()

    def listar_alertas_recientes(self, limite:int=10):
        return self.repositorio.obtener_alertas_recientes(limite)

    def atender_alerta(self, id_alerta:int, id_usuario:int):
        alerta = self.repositorio.atender_alerta(id_alerta, id_usuario)
        return alerta