import hmac

from pwdlib.exceptions import PwdlibError

from app.core.seguridad import password_hash
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
            contrasena = password_hash.hash(datos.contrasena),
            rol = datos.rol,
        )
        return self.repositorio.guardar(entidad)

    def obtener_byid(self, id_usuario):
        return self.repositorio.obtener_byid(id_usuario)

    def listar_usuarios(self):
        return self.repositorio.listar_usuarios()

    def autenticar_usuario(self, datos):
        usuario = self.repositorio.obtener_byemail(datos.email)
        if not usuario:
            raise ValueError("Credenciales inválidas")

        try:
            contrasena_valida = password_hash.verify(datos.contrasena, usuario.contrasena)
        except PwdlibError:
            contrasena_valida = hmac.compare_digest(
                datos.contrasena,
                usuario.contrasena,
            )
            if contrasena_valida:
                self.repositorio.actualizar_contrasena(
                    usuario.id_usuario,
                    password_hash.hash(datos.contrasena),
                )

        if not contrasena_valida:
            raise ValueError("Credenciales inválidas")
        return{
            "id_usuario":usuario.id_usuario,
            "nombre":usuario.nombre,
            "email":usuario.email,
            "rol":usuario.rol,
        }
