'''
Adivina el Número Secreto
Descripción: Crea un juego donde el programa
genera un número aleatorio entre 1 y 100, y 
el usuario debe adivinarlo. El programa dará
pistas como "Demasiado alto" o "Demasiado bajo".
MITCH - 4
'''
import random
def adivina_numero():
    numero_secreto= random.randint(1,100)
    intentos=0
    print("Adivina el número secreto del 1 al 100")
    while True:
        numero= int(input("Escribe un número: "))
        intentos+=1
        if numero < numero_secreto:
            print("Demasiado bajo, INTENTA OTRA VEZ")
        elif numero> numero_secreto:
             print("Demasiado alto, INTENTA OTRA VEZ")
        else:
            print(f"GANASTE, el número secreto es: {numero_secreto}")
            break

adivina_numero()