
# SALIR DEL INTERPRETE PYTHON "quit()"

print ("----------------------------------------------")

(50 - 5 * 6) / 4 # LOS "()" PUEDEN USARSE PARA AGRUPAR

8 / 5 # LA DIVISIÓN SIEMPRE DEVUELVE UN NÚMERO DE PUNTO FLOTANTE

print ("----------------------------------------------")

"""
# EN EL MODO INTERACTIVO LA ÚLTIMA EXPRESIÓN IMPRESA SE ASIGNA
A LA VARIABLE "_" (SIRVE PARA SEGUIR SUMANDO)
tax = 12.5 / 100

price = 100.50

price * tax

price + _

round (_, 2)
"""

print ("----------------------------------------------")

"""
SE UTILIZA "r" ANTES DE LA PRIMERA COMILLA PARA EVITAR USAR
CARACTERES ESPECIALES CUANDO SE UTILIZA BARRA INVERTIDA.
"""

print("hambre\nombres")  # SIN "r"

print(r"hambre\nombres")  # CON "r"... LA "r" VA PEGADA A LAS ""

print ("----------------------------------------------")

# LAS CADEBAS SE PUEDEN CONCATENAR (PEGAR JUNTAS) CON EL OPERADOR +
3 * "su" + 3 * "ba" + 3 * "ru"

# DOS O MÁS CADENAS LITERALES (ES DECIR, LAS ENCERRADAS ENTRE
    # COMILLAS) UNA AL LADO DE OTRA
"Py" "thon"

texto = ("PON VARIAS CADENAS DE TEXTO "
"PARA UNIRLAS.")

print (texto)

# PARA CONCATENAR VARIABLES Y UN LITERAL SE USA "+"
varible = "Py"

varible + "thon"

# LAS CADENAS DE TEXTO ESTAN INDEXADAS
word = "Python"

word[:6]

print ("----------------------------------------------")

#   SERIE  FIBONACCI
#   LA SUMA DE DOS ELEMENTOS DEFINE EL SIGUEINTE

a, b = 0, 1

while a < 40:

    print (a, end=", ")

    a, b = b, a + b

else:

    print (a)
"""print () # CON ESTO CERRAMOS LA FUNCIÓN "end="
            # CERRAR CON CONDICIONAL "if/else" SIRVE DE IGUAL FORMA
            PERO MEJOR"""


def fibonacci(n):

    a, b = 0, 1

    while a < n:

        print (a, end=" ")

        a, b = b, a + b

#fibonacci(int(input()))
print ()# CON ESTO CERRAMOS LA FUNCIÓN "end="


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []

    a, b = 0, 1

    while a < n:

        result.append(a)

        a, b = b, a+b
    return result

#f100 = fib2(100)
#f100
print ()# CON ESTO CERRAMOS LA FUNCIÓN "end="


"""
    Nota (No entiendo del todo*):
        Debido a que ** tiene una prioridad mayor que `-, -3**2 se
        interpretará como -(3**2), por lo tanto dará como resultado
        -9. Para evitar esto y obtener 9, puedes usar (-3)**2.
"""

print ("----------------------------------------------")

#   FUNCIÓN "sum()" con "range()"
sum (range(4)) # 0 + 1 + 2 +3

# LA SENTENCIA "break" TERMINA UN BUCLE MÁS ANIDADO
# LA DECLARACIÓN "continue" ES LO CONTRARIO A "break"
for n in range(0, 100):

    for x in range(2, n):

        if n % x == 0:

            print(n, 'es igual', x, '*', n//x)

            break

    else:

        # Si el bucle falló sin encontrar un factor
        print(n, 'es un número primo')

print ("----------------------------------------------")

"""
        - Correcta Documentación
        - Notacion Camello
        - Minusculas con Guiones Bajos
        - "self" PARA NOMBRAR ARGUMENTOS
"""

# AlGUNAS COSAS SOBRE LISTAS

print ("----------------------------------------------")

squares1 = []
for x in range(10):
    squares1.append(x**2)

print (squares1)

#------------------------------#

squares2 = list(map(lambda x: x**2, range(10)))
print  (squares2)

#------------------------------#
# Más práctico y solo una línea de código
squares3 = [x**2 for x in range(10)]
print (squares3)

#------------------------------

combo1 = [(x, y) for x in [1,2,3] for y in [4,5,6] if x != y]
print (combo1)

#------------------------------#

combos2 = []
for x in [1,2,3]:
    for y in [4,5,6]:
        if x != y:
            combos2.append((x, y))

print (combos2)

print ("----------------------------------------------")

"""
    Las comprensiones de Listas pueden contener expresiones
complejas y funciones anidadas:
"""
from math import pi

[str (round (pi, i)) for i in range (1, 6)]

#------------------------------#

#Comprensión Anidada
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print (matrix)
list(zip(*matrix))

#------------------------------#
"""    Intrucción "del"
    Sirve para quitar un item de una LISTA, TUPLA y DICCIONARIO.
    Así también sirve para eliminar variables.
"""
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[4]
print (a)
print (a)
#del a
print(a)

print ("----------------------------------------------")

"""
- Mejores aplicaciones de acuerdo a la estructura utilizada:

            Lista, Tupla, Diccionario:
        Lista:
    - Usado en formato JSON.
    - Útil para operaciones de matriz.
    - Utilizado en bases de datos.

        Tupla:
    - Se usa para insertar registros en la base de datos a tráves
-de una consulta SQL a la vez...
Ej.: (1, "sravan", 35).(2."geek", 35)
    - Se usa entre paréntesis.

        Diccionario:
    - Se utiliza para crear un marco de datos con listas.
    - Usado en JSON.
"""

print ("----------------------------------------------")

# Técnicas de iteración:


lados = {"arriba,": "abajo", "izquierda,": "derecha"}

# .items() sirve para devolver Clave:Valor de un Diccionario
for s, q in lados.items():
    print (s, q)


# enumerate() sirve para obtener el índice de posición junto a su valor
for s, q in enumerate(["tic", "tac", "toc"]):
    print (s, q)


# zip() sirve para iterar dos más secuencias al mismo tiempo
preguntas = ['nombre', 'búsqueda', 'color favorito']

respuestas = ['lancelot', 'el Santo Grial', 'azul']

for p, r in zip(preguntas, respuestas):

    print('Cual es tu {0}? es {1}.' .format(p, r))
"""         .format sirve para  incluir en una cadena, texto
            y caractéres de formateo, que representan un tipo
            en particular de datos, tales como entero, cadena
            o flotante"""
