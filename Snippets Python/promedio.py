

# importa el modulo de statistics de python , el cual  permite realizar operaciones como suma,promedio,media etc. 
from statistics import mean

# capturar los valores correspondiente a cada mes
budgetEnero= int(input('Ingrese el presupuesto de Enero: '))
budgetFebrero= int(input('Ingrese el presupuesto de Febrero: '))
budgetMarzo= int(input('Ingrese el presupuesto de Marzo: '))

# hallar el promedio, dentro de '[]' se puede agregar los valores de los meses separados por comas
mean = mean([budgetEnero, budgetFebrero, budgetMarzo])

# imprime el promedio
print(f'el promedio de los meses es {mean}')