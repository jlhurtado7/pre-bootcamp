"""
Parámetros por defecto y argumentos de palabras clave
Objetivos

Entender el uso de los parámetros por defecto
Practicar el uso del módulo random de Python
 

Parámetros por defecto

En el capítulo anterior definimos algunas funciones que necesitaban recibir una cantidad específica de 
parámetros para que pudieran ejecutarse correctamente. Si quisiéramos permitir que algunos de los 
parámetros no fueran obligatorios, podemos establecer un valor por defecto a estos. El siguiente ejemplo 
es una versión un poco modificada de la función que creamos previamente buenos_dias, donde recibiremos un 
nombre y la cantidad de veces que queremos que se repita la frase. En caso de que no se proporcione el 
nombre tomará el valor de “alegría”, en caso de que no se proporcione la cantidad tomará el valor de 1. ¡Veamos!
"""

def buenos_dias(nombre = "alegría", cantidad=1):
   print(("Buenos días " + nombre) * cantidad)

buenos_dias()           #Imprime: "Buenos días alegría" una sola vez
buenos_dias("al amor")  #Imprime: "Buenos días al amor" una sola vez
buenos_dias(nombre="a la vida")  #Imprime: "Buenos días a la vida" una sola vez
buenos_dias(cantidad=3)  #Imprime: "Buenos días alegría" 3 veces
buenos_dias(nombre="señor Sol", cantidad=2)  #Imprime: "Buenos días señor Sol" 2 veces

#El orden de los argumentos no importa siempre y cuando especifiquemos el parámetro
buenos_dias(cantidad=3, nombre="para vos")  #Imprime: "Buenos días para vos" 3 veces

"""
¿Qué podemos observar ante el ejemplo anterior?

Si no se proporcionan argumentos, se utilizan los valor por defecto
Si se proporciona un solo argumento sin establecer el nombre, el valor proporcionado se utiliza para el primer parámetro, 
y se utiliza el valor por defecto del segundo parámetro
Si se proporciona un solo argumento estableciendo el nombre, el valor proporcionado se utiliza para el parámetro con el 
mismo nombre y se usa el valor por defecto del otro parámetro
Si se proporcionan dos argumentos, ambos sin nombre establecido, los valores serán asignados a los parámetros en ese orden
Si se proporcionan dos argumentos, ambos con nombre establecido, los valores se asignarán al parámetro asociado (sin importar el orden).
"""