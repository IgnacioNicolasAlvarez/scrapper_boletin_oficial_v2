import re

PATTERN_REGEX = r'^.*\s([0-9]{2}.[0-9]{3})$'

def aplicar_regex_title(texto):
    return re.match(PATTERN_REGEX, texto).group(1)