"""
Funciones
Objetivos

Comprender qué es una función y su papel en el desarrollo
Aprender la sintaxis básica de una función en Python
Saber qué son los parámetros y argumentos en una función
Entender qué hace la sentencia return en una función
 

Una función es un conjunto de acciones que forman parte de un bloque de código y que al ser invocada o llamada 
ejecuta una serie de instrucciones en el programa. Esta puede ser ejecutada en cualquier momento, la cantidad 
de veces que necesitemos. Y, ¿para qué nos sirve? Si sabemos que vamos a estar constantemente haciendo una serie 
de cosas, una gran manera de eficientizar el código es encapsulando esas instrucciones en una función.

 

Algunas características de las funciones son:

Tienen un nombre
Aceptan parámetros (se colocan entre paréntesis pero son opcionales)
Ejecutan una serie de instrucciones
Regresan algo (regresan None en caso de no existir una sentencia return)
 

Pensemos en las funciones como si fueran recetas de cocina. Si quisiera preparar una receta:

Establecería los ingredientes (variables y valores) necesarios para la receta
Obtendría los ingredientes (enviar argumentos) para comenzar la receta (llamar a la función)
Ejecutaría paso a paso las instrucciones (ejecutar la función) con los ingredientes proporcionados 
(recibir los parámetros) y prepararíamos la comida.
Una vez realizados todos los pasos, la comida que se realizó con la receta está lista para servirse (return)



Entre las ventajas más importantes de las funciones tenemos:

Reducción de código duplicado
Desglose de problemas complejos en problemas pequeños más simples
Mejoría en la claridad y legibilidad del código
 

Sintaxis

A través de la palabra reservada def, del diminutivo define que en español significa definir,  
declaramos una función. Esto indicará que el código siguiente pertenece a una función y podremos 
asignarle un nombre para poder invocarla después. Los parámetros se colocan entre paréntesis ( ), y son 
entradas que una función espera y que podrán ser utilizadas dentro de la función.

Veamos el siguiente ejemplo:
"""

def multiplicacion(num1, num2): #definimos la función multiplación con los parámetros num1 y num2
   resultado = num1 * num2     #instrucciones dentro de la función
   return resultado            #regresamos valor de resultado

"""
En el código anterior creamos la función con la palabra reservada def y la nombramos multiplicacion, 
declarando que necesita dos parámetros de entrada. Algo importante es que la función no será ejecutada 
sino hasta que se invoque o llame. Esto lo hacemos colocando el nombre de la función seguido de paréntesis ( ). 
En caso de que la función lo requiera, como es el caso aquí, entre los paréntesis enviaremos los argumentos que 
la función espera como entrada.
"""
resultado_multiplicacion = multiplicacion(5, 5) #Llamado a la función con argumentos 5 y 5
print(resultado_multiplicacion) #Se guarda en la variable el resultado que la función regresó. Imprime: 25

"""
Tanto los parámetros que se reciben, como la salida que pudiera generarse, son opcionales y van a depender de la 
función que estemos desarrollando. Van a existir funciones que no necesitan parámetros, van a existir funciones 
que no regresan nada. Aún con esto, el código dentro de la función puede alterar por completo nuestro programa, 
a esto se le llama efecto secundario.




Parámetros y Argumentos

Los parámetros son las entradas que tendremos ante nuestra función. Las funciones pueden tener tantos parámetros 
como se necesite, incluso pueden no tener parámetros de entrada. Mira el siguiente ejemplo, en donde definimos 
una función llamada buenos_dias que recibe el parámetro nombre: 
"""

def buenos_dias(nombre):
   print("Buenos días "+nombre)

#Una vez definida la función, podemos invocarla llamándola por su nombre y enviando la cantidad de 
# argumentos requeridos:

buenos_dias("alegría")
buenos_dias("al amor")
buenos_dias("a la vida")
buenos_dias("señor Sol")\

"""
Devolución de valores

En el ejemplo que vimos hace un momento, ejecutamos la función pero no recibimos (fuera de la función) nada de la 
función. En muchas ocasiones para nuestro desarrollo necesitaremos que dicha función nos regrese algún tipo de 
valor para poder ser utilizado más adelante en nuestro desarrollo. Para esto utilizaremos la sentencia return, 
esta me va a permitir devolver un valor ante la llamada a mi función.

Esto va a significar que la llamada a una función será igual a lo que dicha función regrese. ¡Veámoslo trabajar!

Intentemos hacer algunos cambios para la función buenos_dias:
"""

def buenos_dias(nombre):
   return "Buenos días "+nombre
#El valor de retorno de la función es "Buenos días Python", por lo que el valor de mi variable frase será ese

frase = buenos_dias("Python")
print(frase) #Imprime: Buenos días Python

"""
Regresar un valor en las funciones nos va a permitir almacenar dicha información en una variable. En el ejemplo 
anterior, 
asignamos la invocación a la función buenos_dias a la variable frase, enviando como argumento “Python”. 
Cuando hacemos la impresión de frase veremos: “Buenos días Python”, ya que es la información que buenos_dias 
regresó.

 Almacenar estos valores de retorno en variables nos permite usar los resultados de nuestras funciones en el 
 resto de nuestro programa.

Las funciones pueden devolver cualquier tipo de datos: cadenas, números, listas, tuplas, diccionarios inclusive 
otras funciones.
"""