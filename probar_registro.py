from app.core.database import get_db

# 1. Abrir la conexión
conexion = get_db()
cursor = conexion.cursor()

# 2. Insertar el camión de prueba número 1
consulta = """
    INSERT INTO Dispositivos (Id_dispositivo, Placa, Nombre_chofer, Estado)
    VALUES (1, 'V1-TEST', 'Carlos Ramos', 'Activo')
    ON CONFLICT (Id_dispositivo) DO NOTHING;
"""

cursor.execute(consulta)
conexion.commit()

print("¡Listo! El camión 1 ya existe en la base de datos.")

# 3. Cerrar todo
cursor.close()
conexion.close()