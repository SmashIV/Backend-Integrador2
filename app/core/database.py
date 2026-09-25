import psycopg2 
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "dbname": "Monitoreo_Integrador",
    "user" : "postgres",
    "password" : "david352",
    "host" : "localhost",
    "port" : 5432
}

def get_db():
    conexion = psycopg2.connect(**DB_CONFIG)
    return conexion

def init_db():
    conexion = get_db()
    cursor_db = conexion.cursor()

    cursor_db.execute("""
    CREATE TABLE IF NOT EXISTS Dispositivos (
        Id_dispositivo INT PRIMARY KEY,
        Placa VARCHAR (7) NOT NULL,
        Nombre_chofer VARCHAR (70) NOT NULL,
        Estado VARCHAR(20) NOT NULL DEFAULT 'Activo'
    );
    """)

    cursor_db.execute("""
    CREATE TABLE IF NOT EXISTS Telemetria (
        Id_lectura SERIAL PRIMARY KEY,
        Fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        Temperatura NUMERIC (5,2) NOT NULL,
        Humedad NUMERIC (5,2) NOT NULL,
        Gases NUMERIC (7,2) NOT NULL,
        Latitud NUMERIC (10,7) NOT NULL,
        Longitud NUMERIC (10,7) NOT NULL,
        Id_dispositivo INT NOT NULL REFERENCES Dispositivos(Id_dispositivo)
    )
    """)

    cursor_db.execute("""
    CREATE TABLE IF NOT EXISTS Usuarios(
        Id_usuario SERIAL PRIMARY KEY,
        Nombre VARCHAR(70) NOT NULL,
        Email VARCHAR(120) NOT NULL UNIQUE,
        Contrasena VARCHAR(30) NOT NULL,
        Rol VARCHAR(20) NOT NULL DEFAULT 'Operador'
    )
    """)

    cursor_db.execute("""
    CREATE TABLE IF NOT EXISTS Alertas(
        Id_alerta SERIAL PRIMARY KEY,
        Tipo_alerta VARCHAR(60) NOT NULL,
        Fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        fecha_vista TIMESTAMP NULL,
        Id_lectura INT NOT NULL REFERENCES Telemetria(Id_lectura),
        Id_usuario INT REFERENCES Usuarios(Id_usuario)
    )
    """)

    conexion.commit()
    cursor_db.close()
    conexion.close()
    print("Tablas mapeadas")

if __name__ == "__main__":
    init_db()



