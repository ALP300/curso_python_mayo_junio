'''
Juego de Piedra, Papel o Tijera
Descripción: Implementa un juego clásico de
Piedra, Papel o Tijera donde la audiencia 
elige una opción y el programa responde 
con una elección aleatoria.
'''
import random
def piedra_papel_tijera():
    opciones=["piedra", "papel", "tijera"]
    eleccionComputadora= random.choice(opciones)
    eleccion_usuario= input("Elige Piedra, Papel, Tijera: ")
    if eleccion_usuario not in opciones:
        print("Opción inválida!")
        return 
    print(f"La computador eligió {eleccionComputadora}")
    
    if eleccion_usuario== eleccionComputadora:
        print("¡EMPATE!")
        
    elif (eleccionComputadora=="tijera" and eleccion_usuario=="piedra") or \
         (eleccionComputadora=="piedra" and eleccion_usuario=="papel")  or \
         (eleccionComputadora=="papel" and eleccion_usuario=="tijera"):
                print("¡GANASTE!")
    
    else:
        print("¡Perdiste!")
        
piedra_papel_tijera()