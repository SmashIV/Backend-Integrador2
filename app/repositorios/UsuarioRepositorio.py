from typing import List, Optional
from psycopg2.extras import RealDictCursor
from app.core.database import get_db
from app.entidades.Usuario import Usuario

class UsuarioRepositorio:
    def guardar(self, usuario):
        sentencia_sql = """
                        INSERT INTO Usuarios (nombre, email, contrasena, rol)
                        VALUES (%s,%s,%s,%s)
                        RETURNING id_usuario;
        """
        conexion = get_db()
        with conexion:
            with conexion.cursor() as cursor:
                cursor.execute(sentencia_sql,(
                    usuario.nombre,
                    usuario.email,
                    usuario.contrasena,
                    usuario.rol,
                ))
                resultado = cursor.fetchone()
                usuario.id_usuario = resultado[0]
        conexion.close()
        return usuario

    def obtener_byemail(self, email):
        sentencia_sql = """
                        SELECT id_usuario, nombre, email, contrasena, rol
                        FROM Usuarios
                        WHERE email = %s; 
        """
        conexion = get_db()
        usuario = None
        with conexion.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sentencia_sql, (email,))
            registro = cursor.fetchone()
            if registro:
                usuario = dict(registro)
        conexion.close()
        return usuario

    def obtener_byid(self, id_usuario):
        sentencia_sql = """
                        SELECT id_usuario, nombre, email, rol
                        FROM Usuarios
                        WHERE id_usuario = %s;
        """
        conexion = get_db()
        usuario = None
        with conexion.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sentencia_sql, (id_usuario,))
            registro = cursor.fetchone()
            if registro:
                usuario = dict(registro)
        conexion.close()
        return usuario

    def listar_usuarios(self):
        sentencia_sql = """
            SELECT id_usuario, nombre, email, rol
            FROM Usuarios
            ORDER BY id_usuario;
        """
        conexion = get_db()
        with conexion.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sentencia_sql)
            registros = cursor.fetchall()

        conexion.close()
        resultado = []
        for reg in registros:
            resultado.append(dict(reg))
        return resultado