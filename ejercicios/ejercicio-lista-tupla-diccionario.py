#Ejercicios Listas, Tuplas y diccionarios (Core)
#Objetivo: Utilizar listas, tuplas y diccionarios para realizar un análisis básico de datos de ventas utilizando Python.



#Instrucciones Detalladas


#1 Carga de Datos:
#Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta. Cada venta debe incluir las siguientes claves:
#«fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2024-01-01»).
#«producto»: una cadena de texto que represente el nombre del producto vendido.
#«cantidad»: un número entero que represente la cantidad de productos vendidos.
#«precio»: un número flotante que represente el precio unitario del producto.

ventas = [
    {"fecha": "2025-01-01", "producto": "Producto A", "cantidad": 10, "precio": 5.0},
    {"fecha": "2025-02-01", "producto": "Producto B", "cantidad": 5, "precio": 10.0},
    {"fecha": "2025-02-02", "producto": "Producto A", "cantidad": 8, "precio": 5.0},
    {"fecha": "2025-03-02", "producto": "Producto C", "cantidad": 12, "precio": 7.5},
    {"fecha": "2025-04-03", "producto": "Producto B", "cantidad": 3, "precio": 10.0},
]

#2 Cálculo de Ingresos Totales:
#Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales generados por todas las ventas. 
# Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados.
ingresosTotales = 0
for venta in ventas:
    ingresosTotales += venta["cantidad"] * venta["precio"]
print(f"Ingresos totales generados: {ingresosTotales}")

#3 Análisis del Producto Más Vendido:
#Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y los valores sean 
#la cantidad total vendida de cada producto.
#Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.
VentasPorProducto = {}
for venta in ventas:
    productos = venta["producto"]
    cantidad = venta["cantidad"]
    if productos in VentasPorProducto:
        VentasPorProducto[productos] += cantidad
    else:
        VentasPorProducto[productos] = cantidad
producto_mas_vendido = max(VentasPorProducto, key=VentasPorProducto.get)
cantidad_mas_vendida = VentasPorProducto[producto_mas_vendido]
print(f"Producto más vendido: {producto_mas_vendido} con {cantidad_mas_vendida} unidades vendidas.")


#4 Promedio de Precio por Producto:
#Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas. 
# Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.
#Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.

preciosPorProducto = {}

for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    # Suma total de ingresos por producto y cantidad total vendida
    if producto in preciosPorProducto:
        suma_precios, suma_cantidades = preciosPorProducto[producto]
        preciosPorProducto[producto] = (suma_precios + precio * cantidad, suma_cantidades + cantidad)
    else:
        preciosPorProducto[producto] = (precio * cantidad, cantidad)

# Calcular el precio promedio de venta para cada producto
for producto, (suma_precios, suma_cantidades) in preciosPorProducto.items():
    precioPromedio = suma_precios / suma_cantidades
    print(f"Este es el ptrecio promedio de venta de {producto}: {precioPromedio:.2f}")

#5 Ventas por Día:
#Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
#Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.

ingresosPorDia = {}

for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    if fecha in ingresosPorDia:
        ingresosPorDia[fecha] += ingreso
    else:
        ingresosPorDia[fecha] = ingreso

print("Estos son los ingresos totales por día:", ingresosPorDia)

#6 Representación de Datos:
#Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados. Cada diccionario anidado debe contener:
#«cantidad_total»: la cantidad total vendida del producto.
#«ingresos_totales»: los ingresos totales generados por la venta del producto.
#«precio_promedio»: el precio promedio de venta del producto.
 
resumenVentas = {}

for producto in VentasPorProducto:
    cantidadTotal = VentasPorProducto[producto]
    ingresos_totales = preciosPorProducto[producto][0]
    precioPromedio = ingresos_totales / cantidadTotal
    resumenVentas[producto] = {
        "cantidad_total": cantidadTotal,
        "ingresos_totales": ingresos_totales,
        "precio_promedio": round(precioPromedio, 2)
    }

print("Este es el resumen de ventas por producto:")
for producto, resumen in resumenVentas.items():
    print(f"{producto}: {resumen}")


#Entrega: Presenta tus resultados en un archivo de texto o una hoja de cálculo. Detalla cada paso del análisis y los resultados obtenidos. Asegúrate de incluir:

#La lista de ventas original.
#Los ingresos totales generados.
#El producto más vendido y su cantidad total vendida.
#El precio promedio de venta por producto.
#Los ingresos totales por día.
#El resumen de ventas por producto.