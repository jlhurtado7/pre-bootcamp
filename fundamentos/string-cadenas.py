"""
Strings/Cadenas
Objetivos

Emplear varios métodos para concatenar cadenas con otras cadenas así como con otros tipos de datos.
Utilizar la conversión de tipo con tipos numéricos primitivos.
Identificar y utilizar la sintaxis correcta para las cadenas “f”.
Concatenar múltiples variables en una cadena utilizando el método .format() con los argumentos apropiados.
Familiarizarse con los métodos de cadena comúnmente utilizados y dónde encontrar más información.


Cadena literal

Las cadenas son secuencias de caracteres, pueden incluir letras, números, símbolos,
y se colocan entre comillas simples o dobles. Por ejemplo:
"""

print("Esta es una cadenas de caracteres.")



"""
Concatenar cadenas y variables con la función print

Existen distintas maneras en las que podemos imprimir una cadena que contenga información de variables. 
Una de ellas es añadiendo una coma después de la cadena seguido de una variable. 
Esto ocasiona que la función print() agregue un espacio entre los elementos separados por comas.
"""
nombre = "Marcelo"
print("Me llamo", nombre) # Imprime: Me llamo Marcelo

# Otra manera es concatenando el contenido con la ayuda de +.

nombre = "Marcelo"
print("Mi nombre es " + nombre) # Imprime: Mi nombre es Marcelo

"""
A diferencia de la primera forma, esta no agrega ningún espacio entre las cadenas, 
por lo que si queremos alguno es necesario colocarlo explícitamente.

Además de esta diferencia, entre las dos formas de concatenar, 
existe otra distinción muy importante. ¿Qué te parece si intentas concatenar una cadena con un entero usando +? 
¡Nos da un error!

Conversión de tipos (Type Casting) o Conversión de tipo explícito

Python no tiene manera de unir una cadena con un número, pero sí de juntar dos cadenas. 
Entonces es necesario convertir el número a cadena para poder “sumar” ambos valores.
"""

#print("¿Cuántas vocales hay? " + 5) # ERROR: TypeError: can only concatenate str (not "int") to str
print("¿Cuántas vocales hay? " + str(5)) #Imprime: ¿Cuántas vocales hay? 5

# Podemos hacer la conversión también de cadena a número, por ejemplo:

tiempo_preparacion = 1
tiempo_orneador = '2'
#tiempo_total = tiempo_preparacion + tiempo_orneador # ERROR: TypeError: unsupported operand type(s) for +: 'int' and 'str'
tiempo_total = tiempo_preparacion + int(tiempo_orneador) # Imprime: 3
print(tiempo_total)

"""
Interpolación de cadenas

También tenemos la posibilidad de insertar variables en nuestras cadenas, 
una práctica conocida como interpolación de cadenas. Existen distintas maneras de llevar a cabo esta tarea.

 
Cadenas “f” (Interpolación de cadenas literal)

A partir de la versión 3.6 de Python, se pueden utilizar las cadenas “f” para interpolar cadenas. 
La sintaxis es la siguiente: escribimos una f justo después de la comilla inicial. 
Después, dentro de la cadena escribimos la variable dentro de llaves. 
"""

nombre = "Marcelo"
edad = 29
print(f"Mi nombre es {nombre} y tengo {edad} años de edad.")

"""
string.format()

Antes de que se introdujeran las cadenas “f”, esta misma funcionalidad se lograba con el método .format(). 
Para usar este método, escribimos la cadena completa y colocamos llaves ({}) en los espacios en los que queremos 
desplegar el valor de la variable. Después invocamos al método format y pasamos las variables como argumentos 
en el orden que debieran llenarse los parámetros {}. Por ejemplo:

"""

nombre = 'Joel'
edad = 38

print("Mi nombre es {} y tengo {} años de edad".format(nombre,edad)) 
print("Tengo {} de edad y mi nombre es {}".format(edad,nombre))

"""
Nota que el método format lee la cadena de caracteres de izquierda a derecha, y va reemplazando 
las {} con el valor de las variables dadas en orden. Es importante entender que dado a esto,
el número de {} debe ser el mismo número de argumentos dados a la función.

 
%-formatting

Quizás en algún código te puedas topar con un método que se utilizaba antes de que existiera las formas 
vistas antes de interpolación. En lugar de utilizar llaves, 
se utiliza el símbolo % para indicar un parámetro; %s para indicar una cadena y %d para indicar un número. 
Una vez establecida la cadena, se coloca de nuevo % para separar el texto de las variables que serán interpoladas.
 Por ejemplo:
"""

nombre = "Patricio"
edad = 39
print('Mi nombre es %s y tengo %d de edad.' % (nombre, edad)) # imprime nombre y edad 

"""
Métodos de cadenas integrados

Además de .format(), existen muchos métodos más que nos ayudarán a manipular nuestras cadenas. Estos son algunos de ellos:

string.upper(): regresa la cadena con todos los caracteres en mayúscula.
string.lower(): regresa la cadena con todos los caracteres en minúscula.
string.count(substring): regresa el número de recurrencias de una subcadena de una cadena.
string.split(caracter):regresa una lista de valores donde la cadena es dividida en el carácter especificado. En caso de no enviar el carácter, la división se hace en cada espacio.
string.find(substring): regresa el índice del comienzo de la primer recurrencia de la subcadena dentro de una cadena.
string.isalnum(): regresa un booleano dependiendo de si la longitud de la cadena es > 0 y todos los caracteres sean alfanuméricos (solo letras y números). Las cadenas que incluyen espacios y puntuación devolverán False con este método. Métodos similares incluyen .isalpha(), .isdigit(), .islower(), .isupper(),  entre otros. Todos devuelven booleanos.
string.join(lista): regresa una cadena que contiene todas las cadenas de nuestro conjunto (en este caso, una lista) concatenadas.
string.endswith(substring): regresa True o False si los últimos caracteres de la cadena coinciden con la subcadena.
 

Estos son solo algunos de los conceptos básicos de las distintas cosas que podemos realizar con las cadenas. Existen muchas otras cosas más que se pueden hacer con la interpolación y además todos los tipos distintos de datos tienen múltiples métodos integrados. Lo mejor en estos casos es leer y analizar la documentación oficial. Recuerda no intentar memorizar todo, ya que siempre habrá información que puedes buscar con facilidad. Te invitamos a leer un poco de la documentación sobre cadenas aquí.
"""