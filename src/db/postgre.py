from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine

from ..utils.logger import loggear


class Advice(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    number: Optional[int] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None


class Advice_raw(SQLModel, table=False):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: Optional[str] = None
    subtitle: Optional[str] = None
    body: Optional[str] = None

def create_session():
    return Session(bind=engine)


def insert(object):
    with create_session() as session:
        session.add(object)
        loggear(mensaje=f"{object} insertado", tipo="info")
        session.commit()

try:
    engine = create_engine("postgresql+psycopg2://example:example@db:5432/example")
    SQLModel.metadata.create_all(engine)
except Exception as e:
    pass
    

