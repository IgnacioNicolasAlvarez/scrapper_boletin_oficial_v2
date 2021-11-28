from datetime import datetime

from ..core.etl.extractor import (
    crear_advices_raw,
    get_page_text,
    get_title_subtitle_body,
    post_http,
)
from ..core.etl.transformer import (
    crear_advice,
    get_fecha_aviso_from_subtitle,
    get_numero_aviso_from_title,
    get_tipo_aviso_from_subtitle,
)
from ..core.etl.loader import save_en_postgres
from ..utils.logger import loggear

today = datetime.today().strftime("%Y-%m-%d")


def extraer(date: str = today):
    loggear(mensaje="Iniciando scrapper", tipo="info")
    loggear(mensaje="Iniciando extractor", tipo="info")

    page_raw, _ = post_http(date)
    page_text = get_page_text(page_raw)
    titles, subtitles, bodies = get_title_subtitle_body(page_text)

    data_raw = crear_advices_raw(titles, subtitles, bodies)
    loggear(mensaje="Finalizando extractor", tipo="info")
    return data_raw


def transformar(data_raw: list):
    loggear(mensaje="Iniciando transformator", tipo="info")
    data = []
    for advice in data_raw:

        fecha_aviso = get_fecha_aviso_from_subtitle(advice.subtitle)
        tipo_aviso = get_tipo_aviso_from_subtitle(advice.subtitle)
        numero_aviso = get_numero_aviso_from_title(advice.title)
        data.append(crear_advice(fecha_aviso, tipo_aviso, numero_aviso))

    loggear(mensaje="Finalizando transformator", tipo="info")
    return data


def cargar(data_transformed: list):
    loggear(mensaje="Iniciando cargador", tipo="info")
    loggear(mensaje=f"Cargando {len(data_transformed)} avisos", tipo="info")
    for advice in data_transformed:
        save_en_postgres(advice)
    loggear(mensaje="Finalizando cargador", tipo="info")
