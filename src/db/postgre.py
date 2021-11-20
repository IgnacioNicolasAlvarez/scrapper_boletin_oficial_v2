from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine

from ..utils.logger import loggear


class Advice(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    number: Optional[int] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None


def create_session():
    return Session(bind=engine)


def insert_advice(Number, Title, Subtitle):
    with create_session() as session:
        advice = Advice(number=Number, title=Title, subtitle=Subtitle)
        session.add(advice)
        loggear(mensaje=f"Aviso {Number} insertado", tipo="info")
        session.commit()


engine = create_engine("postgresql+psycopg2://example:example@db:5432/example")
SQLModel.metadata.create_all(engine)
