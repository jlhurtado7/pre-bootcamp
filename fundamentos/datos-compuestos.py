"""
Tipo de datos compuestos

Estas con colecciones compuestas de los datos primitivos vistos anteriormente.

Listas: Tipo de datos mutable (que puede cambiar) y contiene un conjunto de distintos valores. 
Suele utilizarse para almacenar información relacionada.
"""

listaVacia = []
gatos = ["Garfield", "Silvestre", "Hello Kitty"]
print(gatos[2]) # imprime Hello Kitty
gatos[1] = "Tom" # Remplasa Hello Kitty por Tom
#print(gatos)
gatos.append("Felix") # Agrega un nuevo elemento al final de la lista
gatos.pop() # Elimina el último elemento de la lista
print(gatos)
gatos.pop(1) # Elimina el elemento en la posición 1
print(gatos) # Imprime ['Garfield', 'Tom']  

"""
Tuplas: Tipo de datos inmutable (que no puede cambiar) y contiene un conjunto de distintos valores.
"""

perro = ("Scooby Doo", "Gran Danés", "Scooby Galletas", 7)
print(perro[0]) # Imprime Scooby Doo
#perro[2] = "comida de perro" # Esto no se puede hacer, ya que es inmutable

"""
Diccionarios: Nos permite almacenar contenido a través de una llave y un valor. 
Podemos acceder a sus datos a través de su índice único (que en este caso llamaremos llave o clave). 
Encuentra algunos métodos integrados de los diccionarios aquí.
"""

diccionario = {}

persona = {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False}
persona["nombre"] = 'Valera' # actuliza el valor de la llave nombre si existe
persona['hobbies'] = [ 'jugar videojeugos', 'programación'] # agrega clave y valor si esta no existe
print(persona)

altura = persona.pop('altura') # elimina la clave y el valor de la clave altura

print(altura) # imprime 1.71
print(persona)
print(altura)

"""
Funciones comunes

En caso de no conocer el tipo de dato de una variable o valor, gracias a la función type podemos saberlo fácilmente.
 Por ejemplo:

"""
print(type(3.1416)) #Imprime: <class 'float'>
print(type(persona)) #Imprime <class 'dict'>

"""
En tipos de datos que tienen tamaño (por ejemplo: listas, tuplas, diccionarios, cadenas), 
podemos usar la función len, que es diminutivo de length (tamaño en español) y que nos regresa
 la longitud de este.
"""
print(len(persona)) #Imprime: 4 (la cantidad de pares de clave-valor)
print(len("Me encanta programar")) #Imprime: 20