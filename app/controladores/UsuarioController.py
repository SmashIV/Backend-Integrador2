from typing import List
from fastapi import APIRouter, HTTPException, status
from app.dto.UsuarioDTO import UsuarioCrearDTO, UsuarioRespuestaDTO, LoginDTO
from app.servicios.UsuarioService import UsuarioService

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])
servicio = UsuarioService()

@router.post(
    "/",
    response_model=UsuarioRespuestaDTO,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar un nuevo usuario",
)
def registrar_usuario(datos:UsuarioCrearDTO):
    try:
        usuario = servicio.registrar_usuario(datos)
        return usuario
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )

@router.get(
    "/{id_usuario}",
    response_model=UsuarioRespuestaDTO,
    summary="Buscar usuario por ID",
)
def buscar_byid(id_usuario):
    usuario = servicio.obtener_byid(id_usuario)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuario con ID {id_usuario} no encontrado"
        )
    return usuario   

@router.get(
        "/",
        response_model=List[UsuarioRespuestaDTO],
        summary="Listar usuarios",
)
def listar_usuarios():
    return servicio.listar_usuarios()

@router.post(
    "/login",
    response_model=UsuarioRespuestaDTO,
    summary="Iniciar sesión y autenticar"
)
def login(credenciales:LoginDTO):
    try:
        usuario_autenticado = servicio.autenticar_usuario(credenciales)
        return usuario_autenticado
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(error)
        )