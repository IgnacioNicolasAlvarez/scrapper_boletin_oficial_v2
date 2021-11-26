import re
from .logger import loggear

PATTERN_TITULO_ID_AVISO = r".*:\s([0-9]*.*[0-9]*)$"


def aplicar_regex_group(texto, pattern):
    try:
        return re.search(pattern, texto).group(1)
    except Exception as e:
        print(f"Ha ocurrido un error al aplicar el regex al titulo {texto}:  {str(e)}")
        loggear(
            mensaje=f"Ha ocurrido un error al aplicar el regex al titulo {texto}:  {str(e)}",
            tipo="error",
        )
        exit(1)


def get_fecha_from_str(texto):
    fecha = re.findall(r"\d{4}-\d{2}-\d{2}", texto)
    if fecha:
        fecha = fecha[0]
        return fecha
    else:
        return None


def get_primera_ocurrencia_texto_split(texto, sep='/'):
    return texto.split(sep)[0]