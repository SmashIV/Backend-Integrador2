from typing import List, Optional
from psycopg2.extras import RealDictCursor
from app.core.database import get_db
from app.entidades.Dispositivo import Dispositivo

class DispositivoRepositorio:
    def guardar(self, dispositivo):
        sentencia_sql = """
                        INSERT INTO Dispositivos (placa, nombre_chofer, estado)
                        VALUES (%s, %s, %s)
                        RETURNING id_dispositivo;
        """
        conexion = get_db()
        with conexion:
            with conexion.cursor() as cursor:
                cursor.execute(sentencia_sql, (
                    dispositivo.placa,
                    dispositivo.nombre_chofer,
                    dispositivo.estado,
                ))
                resultado = cursor.fetchone()
                dispositivo.id_dispositivo = resultado[0]
        conexion.close()
        return dispositivo

    def obtener_byplaca(self, placa):
        sentencia_sql = """
                        SELECT id_dispositivo, placa, nombre_chofer, estado
                        FROM Dispositivos
                        WHERE placa = %s;
        """
        conexion = get_db()
        dispositivo = None
        with conexion.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sentencia_sql, (placa,))
            registro = cursor.fetchone()
            if registro:
                dispositivo = dict(registro)
        conexion.close()
        return dispositivo

    def obtener_byid(self, id_dispositivo):
        sentencia_sql = """
                        SELECT id_dispositivo, placa, nombre_chofer, estado
                        FROM Dispositivos
                        WHERE id_dispositivo = %s;
        """
        conexion = get_db()
        dispositivo = None
        with conexion.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sentencia_sql, (id_dispositivo,))
            registro = cursor.fetchone()
            if registro:
                dispositivo = dict(registro)
        conexion.close()
        return dispositivo

    def listar_dispositivos(self):
        sentencia_sql = """
                        SELECT id_dispositivo, placa, nombre_chofer, estado
                        FROM Dispositivos
        """
        conexion = get_db()
        with conexion.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sentencia_sql)
            registros = cursor.fetchall()

        conexion.close()
        resultados = []
        for reg in registros:
            resultados.append(dict(reg))
        return resultados