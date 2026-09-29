from contextlib import contextmanager

from sqlalchemy import URL, create_engine, inspect, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings


class Base(DeclarativeBase):
    pass


DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=settings.db_user,
    password=settings.db_password,
    host=settings.db_host,
    port=settings.db_port,
    database=settings.db_name,
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    bind=engine, autoflush=False, autocommit=False, expire_on_commit=False
)


@contextmanager
def obtener_sesion():
    sesion = SessionLocal()
    try:
        yield sesion
        sesion.commit()
    except Exception:
        sesion.rollback()
        raise
    finally:
        sesion.close()


def init_db():
    import app.entidades.Alerta  # noqa: F401
    import app.entidades.Dispositivo  # noqa: F401
    import app.entidades.Telemetria  # noqa: F401
    import app.entidades.Usuario  # noqa: F401

    Base.metadata.create_all(bind=engine)
    _migrar_contrasena_column()
    print("Tablas mapeadas")


def _migrar_contrasena_column():
    inspector = inspect(engine)
    if "usuarios" not in inspector.get_table_names():
        return
    columna = next(
        (c for c in inspector.get_columns("usuarios") if c["name"] == "contrasena"),
        None,
    )
    if columna is None:
        return
    largo = getattr(columna["type"], "length", None)
    if largo is not None and largo >= 255:
        return
    with engine.begin() as conexion:
        conexion.execute(
            text("ALTER TABLE usuarios ALTER COLUMN contrasena TYPE VARCHAR(255)")
        )


if __name__ == "__main__":
    init_db()
