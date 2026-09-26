from fastapi import FastAPI
from app.controladores import TelemetriaController, AlertaController, UsuarioController

#App principal
app = FastAPI(
    title = "Monitoreo Avícola Los Andes",
    description = "API IoT para el monitoreo de aves durante el transporte",
    version = "1.0.0",
)

#Conectar el controlador
app.include_router(TelemetriaController.router, prefix="/api")
app.include_router(AlertaController.router, prefix="/api" )
app.include_router(UsuarioController.router, prefix="/api")

@app.get("/")
def inicio():
    return{
        "mensaje" : "Servidor Monitoreo IoT",
        "documentacion" : "/docs"
    }

