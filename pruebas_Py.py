

'''
  Pruebas Py
'''


'''
  Ejercicio 1: 
• Crea un programa que pida números infinitamente. Los números introducidos  deben 
ser cada vez mayores El programa finalizará cuando se introduce un número menor que 
el anterior.
'''

comienzo= int(input('\nIntroduce el primer número: '))


while comienzo:
  seguido= int(input('Ahora introduce números cada vez mayores: '))
  comienzo+= 1
  
  if seguido< comienzo:
    print ('\nSolo se permiten números mayores que el anterior. Finalizando.\n')
    break

print('Se acabo el bucle.')


'''
  Ejercicio 2: 
• Crea un programa que pida números positivos indefinidamente. El programa termina 
cuando se introduce un número negativo. Finalmente el programa muestras la suma de 
todos los números introducidos.
'''


numero= int(input('Introduce el primero número: '))
suma= 0

while numero> 0:
  suma= suma + numero
  numero= int(input('Introduce solo números positivos: '))

print(f'La suma de todos los números introducidos es {suma}')