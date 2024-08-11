# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 19:28:33 2024

@author: PACHECO
"""
import random

def showPresentation():
    print("*********************")
    print("*****El ahorcado*****")
    print("*********************")
    print("Bienvenido al juego del ahorcado\n")
    
def directory():
    file = open("palabras.txt", 'r')
    words = [line.strip() for line in file]
    file.close()
    
    i = random.randrange(0, len(words))
    
    secret_word = words[i].strip().upper() #Uppercase the word
    return secret_word

def init_list(secret_word):
    return  ['_' for word in secret_word]

def attempts():
    attempt = input("\nDigita una letra: ")
    attempt = attempt.strip().upper() #deleting spaces
    return attempt

def hit_attepmt(attempt, hit_words, secret_word):
    index = 0
    for word in secret_word:
        if attempt == word: 
            hit_words[index] = word.upper()
        index += 1

def draw_fork(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
    
def gameover_message(secret_word):
    print("¡Qué lástima! Te has ahorcado")
    print("La palabra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def wins_message():
    print("Felicidades, ¡Has ganado!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
showPresentation()

secret_word = directory()

hit_words = init_list(secret_word)

hit = False
failed = False
mistakes = 0

print(hit_words)

while not hit and not failed:
    attempt = attempts()
    if attempt in secret_word:
        hit_attepmt(attempt, hit_words, secret_word)
    else:
        mistakes += 1
    draw_fork(mistakes)
    failed = mistakes == 7
    hit = "_" not in hit_words
    print(hit_words)
    if hit:
        wins_message()
    elif failed:
        gameover_message(secret_word)

print("\n¡¡Fin del juego!!")