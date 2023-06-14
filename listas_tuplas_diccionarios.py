# ESTRUCUTURAS DE DATOS

#SINTAXIS ESTRUCTURAS VACIAS
lista = []
tupla = ()
diccionario ={}
#____________________________________________

#DATOS
usuario="alex"

lista = [10,True,"name",10.8,usuario]#mutable
tupla = (10,False,True,"name",usuario,9.8)#inmutable
diccionario = {"nombre":"alexander", "numero":123}#mutable

#las 3 se pueden recorrer usando ciclo FOR
#____________________________________________

#mostrar datos de las estructuras de datos
print(lista[0])
print(tupla[1])
print(diccionario["nombre"])#en este caso, en vez de la posicion se usa la key y este entrega el valor
#______________________________________

#      METODOS Y FUNCIONES DE LOS DICCIONARIOS

#primero creamos un diccionario 
usuarios ={"user1":"aaron","user2":"cris","user3":"luis","user4":"alfred"}

#GET()
"""
Busca un elemento a partir de su clave y si no lo encuentra 
devuelve un valor por defecto:
"""
print(usuarios.get("user1","elemento no encontrado"))
#_______________
#KEYS()
"""
Genera una lista en clave de los registros del diccionario:
"""
print(usuarios.keys())
#_______________
#VALUES()
"""
Genera una lista en valor de los registros del diccionario:
"""
print(usuarios.values())
#_______________
#ITEMS()
"""
Genera una lista en clave-valor de los registros del 
diccionario:
"""
print(usuarios.items())
#_______________
#POP()
"""
Extrae un registro de un diccionario a partir de su clave y 
lo borra, acepta valor por defecto:
"""
eliminado = usuarios.pop("user1")
print(eliminado)
#_______________
#CLEAR()
"""
Borra todos los registros de un diccionario:
"""
usuarios.clear()
print(usuarios)

#_______________








