from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings


class Base(DeclarativeBase):
    pass


DATABASE_URL = (
    f"postgresql+psycopg2://{settings.db_user}:{settings.db_password}"
    f"@{settings.db_host}:{settings.db_port}/{settings.db_name}"
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
    print("Tablas mapeadas")


if __name__ == "__main__":
    init_db()
