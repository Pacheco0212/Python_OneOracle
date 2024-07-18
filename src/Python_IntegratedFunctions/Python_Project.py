# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 21:31:42 2024

@author: PACHECO
"""

#Python project
#Built-in Functions

import random

print("*********************")
print("**Adivina el numero**")
print("*********************")
print("Elige nivel de dificultad")
print("(1) Novato (2) Intermedio (3) Avanzado")

level = int(input("Nivel: "))
if level == 1:
    attempts = 20
elif level == 2:
    attempts = 10
elif level == 3:
    attempts = 5
    

#secret_number = round(random.random()*100)
secret_number = random.randint(1, 100)
score = 1000
#print(secret_number)

for attempt in range(1, attempts+1):
    
    #print("Intenton {} de {}".format(attempt, attempts))
    print(f"Intento {attempt} de {attempts}")
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
        print(f"¡Acertaste! Tu puntaje es: {score}")
        break
    else:
        if(mayor):
          print("El número no corresponde! El número que ingresaste es mayor.")  
        elif(menor):
            print("El número no corresponde! El número que ingresaste es menor.")
        lostPoints = abs(secret_number - input_number)
        score = score - lostPoints
        
print("El juego ha concluído!")