"""
Diccionarios
ObjetivosCXZBFff

Reconocer la sintaxis de los diccionarios en Python
Aprender cómo crear y consultar diccionarios
Familiarizarse con los métodos integrados de los diccionarios
 

El diccionario en Python es una estructura de datos que nos permite almacenar contenido a través de una llave (o clave) y un valor, a estos pares les llamamos 
ítems o elementos. Si estás familiarizado con lenguajes de programación también son conocidos como objetos, mapas de hash o matrices asociativas. 

Algunas características de los diccionarios son:

Son indexados, es decir que podemos acceder a sus datos a través de su índice (que en este caso llamaremos clave)
Son dinámicos y mutables, es decir que no tienen un tamaño definido y que de manera dinámica podemos agregar o quitar elementos y modificarlos. 
Pueden tener cualquier tipo de dato, es decir que dentro de mi diccionario pudiera yo tener una tupla, una lista, o inclusive otro diccionario.
Son colecciones desordenadas de objetos.
 

Crear Diccionarios

Hasta ahora hemos visto dos tipos de conjuntos en Python: Listas y Tuplas. Las listas las inicializamos con corchetes: [ ], las tuplas las inicializamos con paréntesis: 
( ), y ahora los diccionarios los serán con llaves: { }. Veamos juntos el siguiente ejemplo:
"""

estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación literal
paises = {} #Diccionario vacio
paises ['MEX'] = 'Mexico' # Agregando valores
paises ['COL'] = 'Colombia'# Agregando valores
paises ['CHL'] = 'Chile' # Agregando valores
print(estudiante)
print(paises) 


"""

En el código anterior creamos dos diccionarios de distintas maneras:

Notación Literal: Los pares de clave-valor se encapsulan en las llaves { }; cada par es separado por comas siendo el primer texto la clave, 
seguida de dos puntos : y el valor de este. Por ejemplo: “nombre” representa la clave que corresponde al valor “Alfredo”.
Crear diccionario vacío y agregar valores. Creamos un diccionario vacío colocando las llaves solamente. Para asignar valores colocamos el 
nombre de la variable y entre corchetes [ ] la clave seguida de la asignación del valor. Por ejemplo: paises[“MEX”] = “México”, donde el diccionario es paises,
 la clave es “MEX” y el valor asignado es “México”.
 

Acceder y modificar valores

Para acceder a los valores de un diccionario, puedes utilizar los corchetes [ ] junto con la clave para obtener el valor asignado.
"""

print(estudiante['nombre']) #Accedemos al valor de la clave "nombre"
print(estudiante['curso']) #Accedemos al valor de la clave "curso"

#Las claves establecidas son únicas. En caso de que se realice alguna asignación de una clave ya existente, el valor 
# pasado será sobreescrito por el nuevo valor. De esta manera podemos modificar los valores del diccionario.

estudiante["nombre"] = "Vicente"
print(estudiante["nombre"]) #Imprime: Vicente


"""
Verificar la existencia de una clave

¿Notaste que utilizamos la misma sintaxis para crear un nuevo elemento y modificar el valor de un elemento? Algunas veces necesitaremos 
verificar si existe alguna clave en el diccionario para saber si estamos agregando un valor inicial o bien reemplazando un valor existente.

"""
if 'CRI' in paises:
    print("Desea remplazar el valor?")
else:
    print("No existe la clave")
    paises["Cri"] = "Costa rica"
    print(paises)


"""
Remover elementos
tenemos dos maneras de eliminar un elemento del diccionario:
"""
valor_removido = paises.pop('MEX') #Eliminamos el elemento con clave "CRI" y lo guardamos en la variable valor_removido
del paises['COL'] #Eliminamos el elemento con clave "CRI" sin guardar su valor
print(valor_removido) #Imprime: Costa Rica


"""Sintaxis Multi-línea

Puedes escribir los pares de clave-valor de un diccionario en múltiples líneas para leerlo de una manera más fácil. Esto es muy útil sobre 
todo en diccionarios más largos. Por ejemplo el siguiente diccionario: 
"""
pintor = { "nombre": "Frida Kahlo", "pais": "México", "fecha_nacimiento": "6 de julio de 1907"}

#Puede ser escrito de esta manera:

pintor = {
   "nombre": "Frida Kahlo",
   "pais": "México",
   "fecha_nacimiento": "6 de julio de 1907"
}
"""
Diccionarios anidados

Como mencionamos anteriormente, los valores que podemos utilizar para los diccionarios pueden contener listas, tuplas e inclusive otros diccionarios.
"""
escuela = {
   "nombre": "Coding Dojo LATAM",
   "profesores": [
       {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},
       {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},
       {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}
   ]
}
 

"""Funciones y métodos integrados

A continuación te presentamos algunas funciones que te serán de gran utilidad para los diccionarios:

len(diccionario): regresa el tamaño de un diccionario . 
str(diccionario): crea una representación de cadena (imprimible) de un diccionario. 
type(diccionario): regresa el tipo de la variable. Si la variable es un diccionario, devolverá un tipo de dict. 
 

Veamos también algunos métodos de los diccionarios. La sintaxis puede ser dict.method(tu_diccionario) o tu_diccionario.method(), donde method es el método a utilizar.

.clear(): elimina todos los elementos del diccionario 
.copy(): regresa una copia del diccionario
.get(clave, default=None): regresa el valor establecido para una clave o None si la clave no se encuentra en el diccionario. 
.has_key(clave): regresa verdadero (True) si la clave proporcionada está disponible en el diccionario; de lo contrario, devuelve False. 
.items(): regresa una lista de pares de tuplas (clave, valor) del diccionario. 
.keys(): regresa una lista de claves de diccionario. 
.update(pares_actualizar): agrega y actualiza los pares clave-valor del diccionario enviado al diccionario existente. 
.values(): regresa una lista de valores del diccionario. """