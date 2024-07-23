# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 18:29:52 2024

@author: PACHECO
"""

import Python_Project2
import Python_Project

print("*********************")
print("*******Juegos*******")
print("*********************")
print("(1) Horca (2) Adivinanza")

game = int(input("Selecciona el juego: "))
if game == 1:
    print("\n")
    Python_Project2.play()
elif game == 2:
    print("\n")
    Python_Project.play()
    
