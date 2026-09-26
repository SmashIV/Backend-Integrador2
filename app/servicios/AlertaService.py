from app.repositorios.AlertaRepositorio import AlertaRepositorio

class AlertaService:
    def __init__(self):
        self.repositorio = AlertaRepositorio()

    def listar_alertas_recientes(self, limite:int=10):
        return self.repositorio.obtener_alertas_recientes(limite)