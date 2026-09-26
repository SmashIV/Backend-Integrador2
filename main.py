from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controladores import TelemetriaController, AlertaController, UsuarioController, DispositivoController

#App principal
app = FastAPI(
    title = "Monitoreo Avícola Los Andes",
    description = "API IoT para el monitoreo de aves durante el transporte",
    version = "1.0.0",
)

#Configuracion de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Conectar el controlador 
app.include_router(TelemetriaController.router, prefix="/api")
app.include_router(AlertaController.router, prefix="/api" )
app.include_router(UsuarioController.router, prefix="/api")
app.include_router(DispositivoController.router, prefix="/api")

@app.get("/")
def inicio():
    return{
        "mensaje" : "Servidor Monitoreo IoT",
        "documentacion" : "/docs"
    }

