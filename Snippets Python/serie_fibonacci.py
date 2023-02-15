
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