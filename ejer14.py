'''
Ejercicio 5
Gestor de Lista de Tareas.
El objetivo es crear un programa que permita al usuario gestionar 
una lista de tareas usando un arreglo y ciclos. 
El programa:
Almacena tareas en un arreglo.
Permite agregar nuevas tareas.
Muestra todas las tareas con su índice.
Permite marcar tareas como completadas.
Usa ciclos para recorrer y mostrar el estado de las tareas.
Este ejercicio combina arrays (para almacenar las tareas),
ciclos (para mostrarlas o modificarlas), 
y un poco de interacción con el usuario para hacerlo dinámico.

'''

tareas=[]
def agregar_tareas():
    tarea= input("Ingresa la tarea a agregar: ")
    if tarea:
        tareas.append({"tarea": tarea, "completada": False})
        print(f"Tarea {tarea} completada")
    else:
        print("No puedes ingresar tarea vacía")
    
def mostrar_tareas():
    if not tareas:
        print("No hay tareas en la lista")
        return 
    else:
        for i, tarea in enumerate(tareas):
            