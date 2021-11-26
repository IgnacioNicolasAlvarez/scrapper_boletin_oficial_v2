from datetime import datetime, timedelta

from prefect import Flow, task
from prefect.schedules import IntervalSchedule

from ..utils.logger import loggear
from . import scrapper

schedule = IntervalSchedule(
    start_date=datetime.utcnow() + timedelta(seconds=1),
    interval=timedelta(days=1),
)


@task
def extract(date=None):
    try:
        loggear(mensaje="Iniciando Extraccion", tipo="info")
        if date:
            data = scrapper.extraer(date)
        else:
            data = scrapper.extraer()
        loggear(mensaje="Finalizando Extraccion", tipo="info")
        return data
    except KeyboardInterrupt:
        loggear(mensaje="Error en ingreso de fecha", tipo="error")
        exit(1)


@task
def transform(data_raw):
    try:
        loggear(mensaje="Iniciando Transformacion", tipo="info")
        # transformacion
        data_transformed = data_raw
        loggear(mensaje="Finalizando Transformacion", tipo="info")
        return data_transformed
    except Exception as e:
        loggear(mensaje=f"Error: {e}", tipo="error")
        exit(1)


@task
def load(transformed_data):
    try:
        loggear(mensaje="Iniciando Carga", tipo="info")
        scrapper.save_data(transformed_data)
        loggear(mensaje="Finalizando Carga", tipo="info")
    except Exception as e:
        loggear(mensaje=f"Error: {e}", tipo="error")
        exit(1)


def run(date=None):

    with Flow("Scrapper Boletin Oficial", schedule=schedule) as flow:
        result_extract = extract(date=date)
        result_transform = transform(result_extract)
        load(result_transform)

    flow.run()
