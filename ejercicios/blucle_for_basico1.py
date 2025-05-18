"""Bucles for: Básico 1 (Core)
Objetivos

Practicar el uso de sentencias básicas for en Python
Poner en práctica los algoritmos básicos en Python
 

Crea un archivo de Python llamado bucle_for_basico1.py y realiza lo presentado a continuación:
"""
#Básico: imprime todos los números enteros del 0 al 100.
for numeros in range(101):
    print(numeros)
#Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
for multiplos in range(2,501,2):
    print(f"Estos son los múltiplos de 2: {multiplos}")
    

#Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”
for num in range(1,101):
    if num % 10 == 0:
        print("baby")
    elif num % 5 == 0:
        print("ice ice")
    else:
        print(num)


#Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante).
suma = 0
for numGigante in range(0,5001,2):
    suma += numGigante
print(f"La suma de los números pares del 0 al 500,000 es: {suma} esl el numero gigante")

#Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.
for numPositivo in range(2024,0,-3):
    print(numPositivo)


#Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, 
# imprime los números enteros que sean múltiplos de multiplo. Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, 
# el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas).
numInicial = 3
numFinal = 10
multiplo = 2

for n in range(numInicial, numFinal + 1):
    if n % multiplo == 0:
        print(f"El numero entero es {n}")

#Crea el archivo un Python llamado bucle_for_básico1.py
#Codifica el ejercicio 1. Básico
#Codifica el ejercicio 2. Múltiples de 2
#Codifica el ejercicio 3. Contando Vanilla Ice
#Codifica el ejercicio 4. Wow. Número gigante a la vista
#Codifica el ejercicio 5. Regrésame al 3
#Codifica el ejercicio 6. Contador dinámico