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

for attempt in range(1,4):
    
    #print("Intenton {} de {}".format(attempt, attempts))
    print(f"Intento {attempt} de 3")
    input_str = input("Digita un numero: ")
    input_number = int(input_str)
    if input_number < 1 or input_number > 100:
        print("Digita un número mayor que 0 o menor igual a 100.")
        continue
    print("El número que digitaste: ", input_number)
    
    acerto = secret_number == input_number
    mayor = input_number > secret_number
    menor = input_number < secret_number
    
    if(acerto):
        print("¡Acertaste!")
        break
    else:
        if(mayor):
          print("El número no corresponde! El número que ingresaste es mayor.")  
        elif(menor):
            print("El número no corresponde! El número que ingresaste es menor.")
        
print("El juego ha concluído!")