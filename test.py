import psycopg2
import psycopg2

# Coloca aquí los datos de tu PostgreSQL local:
DB_CONFIG = {
    "dbname": "Monitoreo_Integrador",
    "user": "postgres",         
    "password": "david352",  
    "host": "localhost",
    "port": 5432
}

try:
    print("Conectando a PostgreSQL...")
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print("\n ¡CONEXIÓN EXITOSA!")
    print(f"Versión instalada: {version[0]}\n")
    cursor.close()
    conn.close()
except Exception as error:
    print("\n HUBO UN ERROR AL CONECTAR:")
    print(error)