from datetime import datetime

from ..core.etl.extractor import (
    crear_advices_raw,
    get_page_text,
    get_title_subtitle_body,
    post_http,
)
from ..utils.logger import loggear

today = datetime.today().strftime("%Y-%m-%d")


def extraer(date: str = today):
    loggear(mensaje="Iniciando scrapper", tipo="info")
    loggear(mensaje="Iniciando extractor", tipo="info")

    page_raw, _ = post_http(date)
    page_text = get_page_text(page_raw)
    titles, subtitles, bodies = get_title_subtitle_body(page_text)

    data_raw = crear_advices_raw(titles, subtitles, bodies)
    return data_raw


def transformator(data_raw: list):
    loggear(mensaje="Iniciando transformator", tipo="info")
    return data_raw
