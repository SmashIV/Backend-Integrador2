from psycopg2.extras import RealDictCursor
from app.core.database import get_db


class TelemetriaRepositorio:
    def guardar(self, lectura):
        sentencia_sql = """
                        INSERT INTO Telemetria (temperatura, humedad, gases, latitud, longitud, Id_dispositivo)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        RETURNING Id_lectura, fecha_hora;
        """
        conexion = get_db()
        with conexion:
            with conexion.cursor() as cursor:
                cursor.execute(sentencia_sql,(
                    lectura.temperatura,
                    lectura.humedad,
                    lectura.gases,
                    lectura.latitud,
                    lectura.longitud,
                    lectura.id_dispositivo
                ))
                resultado = cursor.fetchone()
                lectura.id_lectura = resultado[0]
                lectura.fecha_hora = resultado[1]
        conexion.close()
        return lectura

    def obtener_ultimas_lecturas(self, limite=10):
        sentencia_sql = """
                        SELECT Id_lectura, fecha_hora, temperatura, humedad, gases, latitud, longitud, Id_dispositivo
                        FROM Telemetria
                        ORDER BY fecha_hora DESC
                        LIMIT %s;
        """
        conexion = get_db()
        with conexion.cursor(cursor_factory = RealDictCursor) as cursor:
            cursor.execute(sentencia_sql, (limite,))
            registros = cursor.fetchall()
        conexion.close()
        resultado = []
        for reg in registros:
            resultado.append(dict(reg))
        return resultado


    def obtener_ultimas_lecturas_byunidad(self, id_dispositivo, limite):
        sentencia_sql = """
                        SELECT id_lectura, id_dispositivo, temperatura, humedad, gases, latitud, longitud, fecha_hora
                        FROM(
                            SELECT id_lectura, id_dispositivo, temperatura, humedad, gases, latitud, longitud, fecha_hora
                            FROM Telemetria
                            WHERE id_dispositivo = %s
                            ORDER BY fecha_hora DESC
                            LIMIT %s
                        ) AS subconsulta
                        ORDER BY fecha_hora ASC;
        """
        conexion = get_db()
        with conexion.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sentencia_sql, (id_dispositivo, limite))
            registros = cursor.fetchall()
        conexion.close()
        resultado = []
        for reg in registros:
            resultado.append(dict(reg))
        return resultado

    def obtener_ultima_lectura_byunidad(self, id_dispositivo):
        sentencia_sql = """
                        SELECT id_lectura, id_dispositivo, temperatura, humedad, gases, latitud, longitud, fecha_hora
                        FROM Telemetria
                        WHERE id_dispositivo = %s
                        ORDER BY fecha_hora DESC
                        LIMIT 1;

        """
        conexion = get_db()
        lectura = None
        with conexion.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sentencia_sql, (id_dispositivo,))
            registro = cursor.fetchone()
            if registro:
                lectura = dict(registro)
        conexion.close()
        return lectura