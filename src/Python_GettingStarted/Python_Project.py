# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 19:02:40 2024

@author: PACHECO
"""
#Python project

print("**********************")
print("  Adivina el numero")
print("**********************")

secret_number = 55
input_str = input("Digita un numero: ")
input_number = int(input_str)
print("El número que digitaste: ", input_number)

acerto = secret_number == input_number
mayor = input_number > secret_number
menor = input_number < secret_number

if(acerto):
    print("¡Acertaste!")
else:
    if(mayor):
      print("El número no corresponde! El número que ingresaste es mayor.")  
    elif(menor):
        print("El número no corresponde! El número que ingresaste es menor.")
    
print("El juego ha concluído!")