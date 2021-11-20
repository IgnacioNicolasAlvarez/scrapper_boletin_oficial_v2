import re
from .logger import loggear

PATTERN_REGEX = r".*:\s([0-9]*.*[0-9]*)$"


def aplicar_regex_title(texto):
    try:
        return re.search(PATTERN_REGEX, texto).group(1)
    except Exception as e:
        print(f"Ha ocurrido un error al aplicar el regex al titulo {texto}:  {str(e)}")
        loggear(
            mensaje=f"Ha ocurrido un error al aplicar el regex al titulo {texto}:  {str(e)}",
            tipo="error",
        )
        exit(1)


