from src.db.postgre import Advice_raw
from src.utils.regex import get_fecha_from_str, get_primera_ocurrencia_texto_split


def get_data_title(title_text):
    fecha = get_fecha_from_str(title_text)
    tipo = get_primera_ocurrencia_texto_split(title_text, " ")
    return fecha, tipo



