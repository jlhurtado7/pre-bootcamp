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

print("¿Cuántas vocales hay? " + 5) # ERROR: TypeError: can only concatenate str (not "int") to str
print("¿Cuántas vocales hay? " + str(5)) #Imprime: ¿Cuántas vocales hay? 5

