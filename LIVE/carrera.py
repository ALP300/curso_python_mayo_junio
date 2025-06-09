'''
Simula una carrera entre "corredores" 
(emojis o nombres) donde cada uno avanza
aleatoriamente en una pista de texto.
La audiencia elige los corredores y puede
"apostar" por el ganador.
El programa muestra la pista en cada turno, creando suspenso.
'''
import random
import time

def carrera_texto():
    corredores= []
    for i in range(10):
        corredor= input(f"Elige el nombre del corredor {i+1}: ") or f"Player {i+1}"
        corredores.append({"nombre": corredor, "posicion": 0})
    meta=20
    print("La carrera comienza: ")
    
    while True:
        for corredor in corredores:
            avance= random.randint(1,5)
            corredor["posicion"]+=avance
            pista= "-"*corredor["posicion"]+corredor["nombre"]+"-"*(meta-corredor["posicion"])
            print(pista)
            if corredor["posicion"]>=meta:
                print(f"\n{corredor["nombre"]} gana la ccarrera")
                return 
        print("\n")
        time.sleep(1)

carrera_texto()
   

carrera_texto()
    