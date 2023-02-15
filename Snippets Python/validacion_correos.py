'''
    Verificación de Correo Electrónico.
'''

import re
regex= re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
correo= input('Introcude tu correo: ')

if re.fullmatch(regex, correo):
    print("Correo Valido")

else:
    print("Correo Invalido")