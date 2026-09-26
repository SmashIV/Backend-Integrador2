from app.dto.UsuarioDTO import UsuarioCrearDTO
from app.entidades.Usuario import Usuario
from app.repositorios.UsuarioRepositorio import UsuarioRepositorio

class UsuarioService:
    def __init__(self):
        self.repositorio = UsuarioRepositorio()

    def registrar_usuario(self, datos:UsuarioCrearDTO):
        usuario_existente = self.repositorio.obtener_byemail(datos.email)
        if usuario_existente:
            raise ValueError(
                f"El correo '{datos.email}' ya se encuentra registrado"
            )
        entidad = Usuario(
            nombre = datos.nombre,
            email = datos.email,
            contrasena = datos.contrasena,
            rol = datos.rol,
        )
        return self.repositorio.guardar(entidad)

    def obtener_byid(self, id_usuario):
        return self.repositorio.obtener_byid(id_usuario)

    def listar_usuarios(self):
        return self.repositorio.listar_usuarios()