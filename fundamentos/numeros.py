"""
Objetivos

Entender los distintos tipos de números en Python
Comparar los tipos de números entre JavaScript y Python

Números

Existen 3 tipos de números básicos en Python:

int: números enteros, positivos o negativos. Por ejemplo: 156
float: números con punto flotante o decimales, positivos o negativos. Por ejemplo: 3.1416
Complejos (complex): pertenecen al conjunto de números reales y son comúnmente identificados con la letra j. 
Por ejemplo: 2+5j. Si no estás seguro de necesitar este tipo de número, puedes ignorarlos por ahora.
 

Type

Como lo vimos en el capítulo anterior, si no estás seguro del tipo de un número podemos usar type para verificarlo.
"""

print(type(1.1)) #Imprime: <class 'float'>
print(type(615)) #Imprime: <class 'int'>
print(type(2j)) #Imprime: <class 'complex'>

"""
Conversión

Todos los objetos en Python tienen métodos que podemos utilizar para convertir de un tipo de número a otro.
"""

entero_a_decimal = float(123)
decimal_a_entero = int(22.5)
entero_a_complejo = complex(35)

print(entero_a_decimal) #Imprime: 123.0
print(decimal_a_entero) #Imprime: 22
print(entero_a_complejo) #Imprime: (35+0j)

"""
Número aleatorio

Para generar un número aleatorio importamos la librería random. Puedes ver la documentación oficial de la librería
"""

import random
num_aleatorio = random.randint(5, 10) #Genera un número aleatorio entre 5 y 10
print(num_aleatorio) #Imprime el número aleatorio generado