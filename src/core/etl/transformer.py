from src.utils.regex import (
    get_fecha_from_str,
    get_primera_ocurrencia_texto_split,
    aplicar_regex_group,
    PATTERN_TITULO_ID_AVISO,
)
from src.utils.logger import loggear
from src.db.postgre import Advice


def get_fecha_aviso_from_subtitle(subtitle):
    try:
        return get_fecha_from_str(subtitle)
    except Exception as e:
        print(
            f"Ha ocurrido un error al aplicar el regex al titulo {subtitle}:  {str(e)}"
        )
        loggear(
            mensaje=f"Ha ocurrido un error al aplicar el regex al titulo {subtitle}:  {str(e)}",
            tipo="error",
        )


def get_tipo_aviso_from_subtitle(subtitle):
    try:
        return get_primera_ocurrencia_texto_split(subtitle, " ")
    except Exception as e:
        print(
            f"Ha ocurrido un error al aplicar el regex al titulo {subtitle}:  {str(e)}"
        )
        loggear(
            mensaje=f"Ha ocurrido un error al aplicar el regex al titulo {subtitle}:  {str(e)}",
            tipo="error",
        )


def get_numero_aviso_from_title(title):
    try:
        return aplicar_regex_group(title, PATTERN_TITULO_ID_AVISO)
    except Exception as e:
        print(f"Ha ocurrido un error al aplicar el regex al titulo {title}:  {str(e)}")
        loggear(
            mensaje=f"Ha ocurrido un error al aplicar el regex al titulo {title}:  {str(e)}",
            tipo="error",
        )


def crear_advice(fecha_aviso, tipo_aviso, numero_aviso) -> Advice:
    try:
        return Advice(
            fecha_aviso=fecha_aviso, tipo_aviso=tipo_aviso, numero_aviso=numero_aviso
        )
    except Exception as e:
        print(
            f"Ha ocurrido un error al crear una instancia de Advice con los argumentos: {fecha_aviso}, {tipo_aviso}, {numero_aviso}:  {str(e)}"
        )
        loggear(
            mensaje=f"Ha ocurrido un error al crear una instancia de Advice con los argumentos: {fecha_aviso}, {tipo_aviso}, {numero_aviso}:  {str(e)}",
            tipo="error",
        )
