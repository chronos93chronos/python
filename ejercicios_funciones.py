# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import math
"""
Created on Thu Jun  8 17:10:23 2023

Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el
mayor de ellos. 
"""

numero_1 = int(input("ingresar numero 1:"))
numero_2 = int(input("ingresar numero 2:"))
mayor_numero = 0
def max_number():
    global numero_1
    global numero_2
    global mayor_numero
    if numero_1 > numero_2:
        mayor_numero = numero_1
    else:
        mayor_numero = numero_2
       
max_number()
print(mayor_numero)

#________________________________________________
"""
Mismo ejercicio que el anterior, pero ahora con 3 numeros
"""

num_1 = int(input("ingresar num 1:"))
num_2 = int(input("ingresar num 2:"))
num_3 = int(input("ingresar num 3:"))
max_number = 0

def identificar_max_number():
    global num_1
    global num_2
    global num_3
    global max_number
    if num_1 > num_2:
        max_number = num_1
    else:
        max_number = num_2
    
    if max_number > num_3:
        max_number = max_number
    else:
        max_number = num_3

identificar_max_number()
print("el maximo numero es:", max_number)

#___________________________________________________
"""
Realiza una función llamada area_rectangulo
(base, altura) que devuelva el área del rectangulo 
a partir de una base y una altura. 
Calcula el área de un rectángulo de 15 de base 
y 10 de altura:
"""    

def area_rectangulo():
    base = float(input("ingresar base:"))
    altura = float(input("ingresar altura:"))
    area = base * altura
    print("el area de la figura es de:",area)

area_rectangulo()

#__________________________________________________
"""
El área de un círculo se obtiene al elevar el
 radio a dos y multiplicando el resultado por el 
 número pi. Puedes utilizar el valor 3.14159 
 como pi o importarlo del módulo math:
"""
def area_circulo():
    radio = float(input("ingresar radio:"))
    radio = radio ** 2
    area = radio * math.pi
    print("el area de la circunferencia es:",area)

area_circulo()    
    
    
    
