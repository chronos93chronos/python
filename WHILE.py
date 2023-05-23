# -*- coding: utf-8 -*-

#ejercicios bucle while python

"""
Escriba un programa que pregunte una y otra vez si desea 
continuar con el programa, siempre que se conteste exactamente 
sí (en minúsculas).
"""

respuesta = "si"
usuario = input("ingrese respuesta:")

while usuario == respuesta :
    print("desea continuar?")
    usuario = input("re-ingrese respuesta:")

print("se acabo el programa")

#___________________________________________________________________

"""
Escriba un algoritmo que lea del teclado un número entero y que
 compruebe si el número es menor que 10. Si no lo está, debe volver
 a leer el número repitiendo la operación hasta que el usuario escriba
 un valor correcto. Finalmente, debe escribir por pantalla el valor leído
 cuando este sea correcto.
 """

numero = int(input("ingresa un numero:"))

while numero > 10:
    print("numero no corresponde")
    numero = int(input("re-ingresar numero:"))
print("numero correcto", numero)

#___________________________________________________________________
"""
Modifique el algoritmo del problema anterior 
para que, en vez de comprobar que el número 
sea menor que 10, compruebe que se encuentre 
en el rango (0, 20).
"""

numero_usuario = int(input("ingrese numero:"))

while numero_usuario > 20 or numero_usuario <0:
    print("numero no corresponde")
    numero_usuario= int(input("re-ingrese numero:"))
print("numero correcto",numero_usuario)

#___________________________________________________________________
"""
Modifique el algoritmo del problema anterior para 
que cuente las veces que ha leído un número de teclado 
y escriba el resultado por pantalla.
"""

contador = 1
number_user = int(input("ingresa un numero:"))

while number_user > 20 or number_user <0:
     print("numero no corresponde")
     number_user = int(input("re-ingrese numero:"))
     contador += 1
print("numero correcto:",number_user)
print("el numero de intentos fueron:",contador)

#___________________________________________________________________
"""
Modifique el algoritmo del problema anterior para que se realicen 5
 lecturas por teclado como máximo.
  """  
new_contador = 1
eleccion = int(input("ingresar numero:"))

while eleccion > 20 or eleccion <0:
    print("numero no corresponde")
    eleccion = int(input("re-ingresar numero:"))
    new_contador +=1
    
    if new_contador == 5:
     print("limite de intentos")
     break

print("el numero de intentos fueron:",new_contador)

#___________________________________________________________________
"""
Escriba un algoritmo que calcule e imprima la suma de 
los N primeros números enteros positivos. El valor de N 
debe leerse del teclado y ser ingresado por el usuario.
"""
suma = 0
numero = int(input("Ingrese un número"))
while numero>0:
 suma = (numero*(numero+1))/2
 break
print ("Número ingresado:",numero)
print ("Suma total:",suma)


#___________________________________________________________________
"""
Escriba un algoritmo que sume los números ingresados por el usuario 
hasta que el usuario ingrese el número 0 (detener las preguntas ante 
este escenario).
"""
sumatoria = 0
user_number = int(input("ingresa los numeros:"))
while user_number != 0:
    sumatoria += user_number
    user_number = int(input("ingresa los numeros:"))
    
print("la sumatoria total es:",sumatoria)
    
#___________________________________________________________________
"""
Escriba un algoritmo que sume los números ingresados por el usuario
 y cuando la suma sea superior a 100 deje de pedir números y muestre
 el total.
"""
sumaaaar = 0
numero = int(input(u"Ingrese un número"))
while numero!=0:
 sumaaaar += numero 
 if (sumaaaar>100):
  break 
 numero = int(input(u"Ingrese un número")) 
print ("Suma total:",sumaaaar)
#___________________________________________________________________

#___________________________________________________________________

#___________________________________________________________________

#___________________________________________________________________





















