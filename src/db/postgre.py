from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine
import pendulum

from ..utils.logger import loggear


class Advice(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    numero_aviso: Optional[int] = None
    tipo_aviso: Optional[str] = None
    fecha_aviso: Optional[str] = None
    fecha_consulta: str = pendulum.now(
        "America/Argentina/Buenos_Aires"
    ).to_datetime_string()


class Advice_raw(SQLModel, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: Optional[str] = None
    subtitle: Optional[str] = None
    body: Optional[str] = None


def create_session():
    return Session(bind=engine)


def insert(object):
    try:
        with create_session() as session:
            session.add(object)
            loggear(mensaje=f"{object} insertado", tipo="info")
            session.commit()
    except Exception as e:
        loggear(mensaje=f"Error en insert: {e}", tipo="error")


try:
    engine = create_engine("postgresql+psycopg2://example:example@db:5432/example")
    SQLModel.metadata.create_all(engine)
except Exception as e:
    pass
