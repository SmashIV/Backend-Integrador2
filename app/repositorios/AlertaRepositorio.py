from psycopg2.extras import RealDictCursor
from app.core.database import get_db
from app.entidades.Alerta import Alerta

class AlertaRepositorio:
    def guardar(self, alerta):
        sentencia_sql = """
                        INSERT INTO Alertas (tipo_alerta, id_lectura, fecha_vista, id_usuario)
                        VALUES (%s, %s, %s, %s)
                        RETURNING id_alerta, fecha_hora;
        """

        conexion = get_db()
        with conexion:
            with conexion.cursor() as cursor:
                cursor.execute(sentencia_sql,(
                    alerta.tipo_alerta,
                    alerta.id_lectura,
                    alerta.fecha_vista,
                    alerta.id_usuario,
                ))
                resultado = cursor.fetchone()
                alerta.id_alerta = resultado[0]
                alerta.fecha_hora = resultado[1]
        conexion.close()
        return alerta

    def obtener_alertas_recientes(self, limite=10):
        sentencia_sql = """
                        SELECT id_alerta, tipo_alerta, fecha_hora, fecha_vista, id_lectura, id_usuario
                        FROM Alertas
                        ORDER BY fecha_hora DESC
                        LIMIT %s;
        """
        conexion = get_db()
        with conexion.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sentencia_sql,(limite,))
            registros = cursor.fetchall()
        conexion.close()
        resultado = []
        for reg in registros:
            resultado.append(dict(reg))
        return resultado
