import os

import psycopg2

DB_CONFIG = {
    "dbname": os.environ["DB_NAME"],
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "5432")),
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