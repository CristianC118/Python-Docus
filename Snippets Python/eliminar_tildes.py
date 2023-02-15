
# Eliminar Tildes
import unicodedata

def quitar_tildes(cadena):
    sust = dict.fromkeys(map(ord, u'\u0300\u0301\u0302\u0308'), None)
    return unicodedata.normalize('NFKD', cadena).translate(sust)

