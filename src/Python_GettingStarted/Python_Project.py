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
attempts = 3
attempt = 1

while(attempts >= attempt):
    #print("Intenton {} de {}".format(attempt, attempts))
    print(f"Intento {attempt} de {attempts}")
    input_str = input("Digita un numero: ")
    input_number = int(input_str)
    print("El número que digitaste: ", input_number)
    
    acerto = secret_number == input_number
    mayor = input_number > secret_number
    menor = input_number < secret_number
    
    if(acerto):
        print("¡Acertaste!")
        attempt = 3
    else:
        if(mayor):
          print("El número no corresponde! El número que ingresaste es mayor.")  
        elif(menor):
            print("El número no corresponde! El número que ingresaste es menor.")
    attempt += 1
        
print("El juego ha concluído!")