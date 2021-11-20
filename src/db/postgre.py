from sqlmodel import Field, SQLModel, create_engine, Session


class Advice(SQLModel, table=True):
    id = Field(int, primary_key=True)
    number = Field(int)
    title = Field(str)
    subtitle = Field(str)
    body = Field(str)


engine = create_engine("postgresql+psycopg2://example:example@db:5432/example")
SQLModel.metadata.create_all(engine)


def create_session():
    return Session(bind=engine)


def insert_advice(Number, Title, Subtitle, Body):
    with create_session() as session:
        advice = Advice(number=Number, title=Title, subtitle=Subtitle, body=Body)
        session.add(advice)
        session.commit()
