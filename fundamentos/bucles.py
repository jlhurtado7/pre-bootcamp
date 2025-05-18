"""Bucles
Objetivos

Aprender cómo hacer un bucle a través de rangos
Aprender cómo recorrer cadenas
Aprender cómo recorrer listas
Aprender cómo recorrer diccionarios
Aprender cómo usar un bucle while
Aprender el uso de las sentencias break y continue dentro de los bucles
 

Bucles

Probablemente en Fundamentos de la Web o el Pre-bootcamp aprendiste un poco sobre los bucles. Refresquemos nuestra memoria un poco: Un bucle es una estructura de control de flujo que nos permite repetir la ejecución de un bloque de código varias veces, siempre y cuando se cumpla una condicional.

En Python estaremos utilizando los bucles a través de la sentencia for y la sentencia while. 

 

Bucles for con range

Podemos utilizar la función range de Python con la sentencia for para repetir el mismo código cierta cantidad de veces. La función range() puede tener entre 1 y 3 argumentos y en base a esto crea una secuencia de números enteros. Este suele ser utilizado para crear bucles que tienen un punto de inicio definido y un punto de parada para una secuencia de números.

Al aceptar 3 argumentos, tenemos 3 maneras distintas de usar range() en un for.

 

Range con 1 argumento

"""

for i in range(4):
   print(i)
#La secuencia de números comienza en 0 por default; el bucle se detiene cuando llega al fin, es decir al argumento enviado a range 
# (pero excluye ese número); cada iteración aumenta en secuencia 1 por default. Veamos el resultado del código



 

#Range con 2 argumentos



for i in range(2, 8):
   print(i)
#La secuencia de números comienza en 2 (el primer argumento); el bucle se detiene cuando llega al fin (segundo argumento, excluyéndolo); cada iteración aumenta en secuencia 1 por default. Veamos el resultado del código



 

#Range con 3 argumentos



for i in range(2, 10, 3):
   print(i)
#La secuencia de números comienza en 2 (el primer argumento); el bucle se detiene cuando llega al fin (segundo argumento, excluyéndolo); cada iteración aumenta en secuencia 3 (tercer argumento). Veamos el resultado del código



#En caso de necesitar un paso para nuestra secuencia, es necesario enviar los tres argumentos al rango. ¡Los rangos también pueden ser decrementales! Para lograr esto, indicaremos que el paso sea un número negativo.

for i in range(0, 15, 3):
   print(i)
#Imprime: 0, 3, 6, 9, 12

for i in range(10, 1, -3):
   print(i)
#Imprime: 10, 7, 4
 

#Recorrer cadenas con bucles for

#Los bucles pueden ser utilizados para recorrer cualquier secuencia en Python. Gracias a esto podemos iterar cada valor de una cadena a través de un for.

for letra in 'Python':
   print(letra)
#Imprime: 'P', 'y', 't', 'h', 'o', 'n'
 

#Recorrer listas con bucles for

#Para recorrer una lista podemos hacerlo de dos maneras distintas. En caso de necesitar los índices, podemos usar la función range y enviar como parámetro la longitud de la lista. En caso de solo necesitar los valores, podemos directamente hacer el recorrido de la lista.

lista = ['brócoli', 'pepino', 'pimiento']

for i in range( len(lista) ):
   print(i, lista[i])
#Imprime: 0 brócoli, 1 pepino, 2 pimiento

for verdura in lista:
   print(verdura)
#Imprime: brócoli, pepino, pimiento
 

#Recorrer tuplas con bucles for

#Las iteraciones funcionan de la misma manera para las tuplas que lo recorridos que hacemos en una lista.

tupla = ('fresa', 'manzana', 'cereza')

for i in range( len(tupla) ):
   print(i, tupla[i])
#Imprime: 0 fresa, 1 manzana, 2 cereza

for fruta in tupla:
   print(fruta)
#Imprime: fresa, manzana, cereza
 

#Recorrer diccionarios con bucles for

#Los diccionarios también pueden ser recorridos. Al hacer la iteración a través de un diccionario, el iterador es cada una de las claves establecidas en el diccionario.

estudiante = {"nombre": "Gonzalo", "curso": "Python"}

for clave in estudiante:
   print(clave)
#Imprime: nombre, curso
#Ya tenemos las claves, ahora ¿cómo accedemos al valor? ¡Colocando la clave entre corchetes! Veamos:

estudiante = {"nombre": "Gonzalo", "curso": "Python"}

for clave in estudiante:
   print(estudiante[clave])
#Imprime: Gonzalo, Python
#En el capítulo de diccionarios vimos algunos métodos que nos permitían obtener las secuencias con los valores, claves y elementos de un diccionario. Prueba el siguiente fragmento de código para ver su funcionamiento en acción

platillos_tipicos = {"México": "Tacos", "Colombia": "Ajiaco", "Costa Rica": "Casado"}

#Otra forma de iterar a través de las claves
for clave in platillos_tipicos.keys():
   print(clave)
#Imprime: México, Colombia, Costa Rica

#Iteramos a través de los valores
for valor in platillos_tipicos.values():
   print(valor)
#Imprime: Tacos, Ajiaco, Casado

#Iteramos a través de los elementos (clave-valor)
for clave, valor in platillos_tipicos.items():
   print(clave, "=", valor)
#Imprime: México = Tacos, Colombia = Ajiaco, Costa Rica = Casado
 

"""Bucles While

La sentencia while es otra manera en la que podemos crear un bucle; esta va a ser repetida mientras (while en inglés) se cumpla con la condicional dada.

La sintaxis en Python es:
"""
#while condicion:
   #Código que se ejecuta mientras la condición se cumpla
#Veamos el siguiente ejemplo:

num = 0

while num < 4:
   print("bucle while -", num)
   num += 1
#Imprime: bucle while - 0, bucle while - 1, bucle while - 2, bucle while - 3
"""Es importante notar que el bloque de código ejecutado debe de afectar a la condición colocada en el while, ya que de lo contrario podemos caer en un bucle infinito. 

 

Else

Todos los bucles while incluyen una condición, pero ¿qué sucede si la condicional no se cumple y aún queremos ejecutar algo? En estas ocasiones utilizaremos la sentencia else con el bucle.
"""
num = 0

while num < 4:
   print("bucle while -", num)
   num += 1
else:
   print("Acabamos de salir del bucle")

"""
Ten en cuenta que el bloque de código del else sólo se ejecutará si el bucle while se ejecuta con normalidad y su condición deja de cumplirse (ya se que nunca se haya ingresado al bucle o que eventualmente dejó de cumplirse con la condición). Si en cambio nuestro bucle sale prematuramente a través de una declaración break o return, ese bloque de código nunca será ejecutado.

 

Control de Bucles

En capítulos anteriores aprendimos sobre estructuras de control de flujo con las sentencias if y else. Los bucles, breaks y continues también son parte de estas estructuras de control de flujo.

Para tener un mayor control sobre los bucles podemos utilizar las siguientes sentencias.

 

Break

La sentencia break termina de forma definitiva el bucle y continúa con la primera sentencia después del bucle. El break se puede utilizar tanto para bucles for como para while.

El break suele utilizarse cuando sucede alguna condición externa que demanda salir del bucle de manera inmediata.



Por ejemplo:
"""
for letra in "detente":
   if letra == "n":
       break
   print(letra)
#Imprime: d, e, t, e
"""En caso de tener bucles anidados, un break solo saldrá del bucle más cercano.

 

Continue

La sentencia continue regresa el control al comienzo del bucle; de alguna manera a través de continue podemos “saltar” todas las sentencias restantes en la iteración actual del bucle y después continúa de manera normal.

"""

for letra in "detente":
   if letra == "n":
        continue
   print(letra)
#Imprime: d, e, t, e, t, e
"""En el ejemplo anterior, “saltamos” la letra n, pero nuestro bucle continuó funcionando de manera normal.

Observa el comportamiento del else acompañado de una sentencia break"""

x = 6

while x > 2:
   print(x)
   x -= 1
   if x == 3:
       break
else: #Recuerda: Solo se ejecuta en una salida normal, NO en un break
   print("Sentencia final")
