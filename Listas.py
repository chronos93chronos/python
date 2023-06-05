# -*- coding: utf-8 -*-

#            LISTAS

numeros = [10,70,110,90,80] # se crea una lista

print(len(numeros))# se usa LEN para ver la longitud de la lista . en javascript se escribe LENGTH

"""
append()
Añade un ítem al final de la lista:
"""
numeros.append(69)
print(numeros)
#_____________________________________________________
"""
clear()
Vacía todos los ítems de una lista:
"""
num = [1,2,3,4,5]
num.clear()
print(num)
#_____________________________________________________
"""
extend()
Une una lista a otra:
"""
lista_1 = [10,20,30]
lista_2 = [40,50,60]

lista_1.extend(lista_2)
print(lista_1)

#_____________________________________________________
"""
count()
Cuenta el número de veces que aparece un ítem:
"""
nombres = ["ale","luis","alfred","ale"]

print(nombres.count("ale"))

#_____________________________________________________
"""
index()
Devuelve el índice en el que aparece un ítem (error si no aparece):
"""
profesiones = ["doctor","arquitecto","odontologia"]
print(profesiones.index("doctor"))

#_____________________________________________________
"""
insert()
Agrega un ítem a la lista en un índice específico:

Primera posición (0):
"""

posiciones = [10,30,40,90,110]

posiciones.insert(5,200 )
print(posiciones)
print(posiciones.index(200))
print(len(posiciones))

#_____________________________________________________
"""
pop()
Extrae un ítem de la lista y lo borra:
"""
datos = [100,200,300,400]
datos.pop(1)
print(datos)
#_____________________________________________________
"""
remove()
Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos:
"""
datitos = [10,10,10,20,30]

print(datitos.remove(10))
print(datitos)
#_____________________________________________________
"""
reverse()
Le da la vuelta a la lista actual:
"""
escala = [1,2,3,4,5,6,7,8,9,10]
print(escala)
escala.reverse()
print(escala)
#_____________________________________________________

"""
sort()
Ordena automáticamente los ítems de una lista por su valor de menor a mayor:
"""
notas = [7,4,5,4,9,8,11,56,4,-7,-100,4,5]
notas.sort()
print(notas)
#_____________________________________________________
"""
sort()
ordenar de MAYOR A MENOR usando: reverse=True
"""
cuenta = [100,50,700,-100,564,48512,8,0]

cuenta.sort(reverse=True)
print(cuenta)
#_____________________________________________________

"""
copy()
hace una copia de la lista seleccionada, sin afectar la original
"""
colores = ["rojo","azul","negro","blanco"]

colores_copia = colores.copy()
colores_copia.insert(0, "marron")
print(colores)
print(colores_copia)

#_____________________________________________________

"""
DEL
La del palabra clave se utiliza para eliminar objetos. 
En Python, todo es un objeto, por lo que la del palabra 
clave también se puede usar para eliminar variables, 
listas o partes de una lista, etc.
"""
ejemplo = [20,30,50,60]

del ejemplo[0]
print(ejemplo)
#_____________________________________________________

"""
copiando listas de otra y manejando los datos copiados
NOTA: [inicio:fin]
"""
nba=["bulls","miami","lakers","raptors","denver"]
conferencia = nba[0:3]
print(conferencia)

#_____________________________________________________
#                 OPERADOR IN Y NOT IN
"""
IN: verifica si el valor ingresado se encuentra dentro de la lista
y si esta, devuelve True

NOT IN: verifica si el valor ingresado NO se encuentra
dentro de la lista, si no se encuentra, devuelve True

Sintaxis: valor in nombre_lista
          valor not in nombre_lista
"""
equipos = ["madrid","city","barca","chelsea"]

if equipos in "madrid":
    print("si esta")
else:
    print("no esta")














