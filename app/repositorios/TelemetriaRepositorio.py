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
