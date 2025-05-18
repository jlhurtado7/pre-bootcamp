#1
def cantidad_de_vocales():
    return 5
print(cantidad_de_vocales()) # me devuelve 5

"""#2
def cantidad_de_glaciares_argentina():
    return 16968
print(cantidad_de_dias_o_meses_o_semanas_en_anio() + cantidad_de_glaciares_argentina())# error
"""
#3
def anio_independencia_chile():
    return 1810
    return 1851
print(anio_independencia_chile()) # imprime ambos valores, pero solo el primero es el correcto, el segundo no se ejecuta

#4
def cantidad_de_departamentos_colombia():
    return(32)
    print(33)
print(cantidad_de_departamentos_colombia()) # imprime 32, el segundo no se ejecuta

#5
def altura_machu_picchu():
    print(2438)
x = altura_machu_picchu()
print(x) # imprime None, ya que la función no tiene un return, solo un print

#6
"""def suma(a, b):
    print(a+b)
print(suma(10, 5) + suma(4, 3)) # imprime None, ya que la función no tiene un return, solo un print
"""
#7
def concatenar(a, b):
    return str(b) + str(a)
print(concatenar(7, 15)) # imprime 157, ya que convierte ambos valores a string y los concatena

#8
def paises_latinoamerica_o_lenguas_indigenas():
    a = 560
    print(a)
    if a < 180:
        return 33
    else:
        return 46
    return 21
print(paises_latinoamerica_o_lenguas_indigenas()) # imprime 560, ya que la función no tiene un return, solo un print
#9
def cantidad_de_dias_o_meses_o_semanas_en_anio(a, b):
    if a < b:
        return 365
    else:
        return 12
    return 52
print(cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3)) # imprime 365, ya que la función no tiene un return, solo un print
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4)) # imprime 365, ya que la función no tiene un return, solo un print
print(cantidad_de_dias_o_meses_o_semanas_en_anio(7, 4) + cantidad_de_dias_o_meses_o_semanas_en_anio(1, 3)) # imprime 365, ya que la función no tiene un return, solo un print

#10
def sumatoria(a, b):
    return a + b
    return 157
print(sumatoria(3, 4)) # imprime 7

#11
a = 150
print(a)
def funcion():
    a = 350
    print(a)
print(a)
funcion()
print(a) # imprime 150, ya que la función no devuelve nada

#12
a = 150
print(a)
def funcion():
    a = 350
    print(a)
    return a
print(a)
funcion()
print(a) # imprime 150, ya que la función no devuelve nada

#13
a = 150
print(a)
def funcion():
    a = 350
    print(a)
    return a
print(a)
a = funcion()
print(a) # imprime 350, ya que la función devuelve el valor de a

#14
def funcion1():
    print(3)
    funcion2()
    print(2)
def funcion2():
    print(1)
funcion1()

#15
def funcion1():
    print(3)
    a = funcion2()
    print(a)
    return 4 # imprime 4
def funcion2():
    print(1)
    return 0
b = funcion1()
print(b) # imprime 4,   ya que la función devuelve el valor de a