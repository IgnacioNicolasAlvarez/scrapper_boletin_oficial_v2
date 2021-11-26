def reemplazar(cadena, buscar, reemplazar, fuction=None):
    if fuction:
        return fuction(cadena.replace(buscar, reemplazar))
    return cadena.replace(buscar, reemplazar)

def trim(cadena):
    return reemplazar(cadena, " ", "", fuction=str.strip)