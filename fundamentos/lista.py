# Lista
# En ciencia de datos, las listas se utilizan frecuentemente para almacenar series de datos. 
# Por ejemplo, podrías tener una lista que almacena una serie de temperaturas diarias.

# Lista de temperaturas diarias
temperaturas = [22.5, 21.0, 23.3, 25.2, 24.5]

mediaTemeratura = sum(temperaturas)/len(temperaturas)
print(" La media de temperaturas es: ", mediaTemeratura)

#Tuplas

#Las tuplas se usan comúnmente para almacenar datos que no deben cambiar, 
# como coordenadas geográficas o dimensiones de un objeto. También son útiles cuando 
# necesitas devolver múltiples valores desde una función.

# Cordenadas geograficas de una ubicción

cordenadas = (19.426, -99.1332) #logintud y latitud de Ciudad de Mexico
def calcularDistancia(coord1, coord2):
    #Implementcion ficticia para calcular la distancia
    distancia = 10 #valor de ejemplo
    return distancia
distancia = calcularDistancia(cordenadas, (34.0522, -118.2437))
print('Distancia', distancia)

#Diccionarios

#En ciencia de datos, los diccionarios se usan ampliamente para manipular y almacenar datos estructurados. 
# Por ejemplo, podrías tener un diccionario que almacena información sobre un conjunto de datos.

# Diccionario con información sobre un conjunto de datos
dataset_info = {
    "nombre": "Datos de ventas",
    "columnas": ["fecha", "producto", "cantidad", "precio"],
    "filas": 1000,
    "fuente": "Sistema de ventas interno"
}

print("Nombre del conjunto de datos:", dataset_info["nombre"])
print("Número de filas:", dataset_info["filas"])