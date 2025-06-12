'''
Ejercicio5
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

def completar_tarea():
    if not tareas:
        print("NO EXISTE LA TAREA")
        return 
    mostrar_tareas()
    indice= int(obtener_entrada("Ingresa el número de la tarea a marcar: ")) -1
    if 0<= indice<len(tareas):
        if tareas[indice]["completada"]:
            print("La tarea está completada")
        else: 
            tareas[indice]["completada"]= True
            print("Tarea marcada como completa")
def obtener_entrada(mensaje):
    entrada = input(mensaje)
    return entrada.strip()

def agregar_tarea():
    tarea = obtener_entrada("Ingresa la tarea a agregar: ")
    if tarea:
        tareas.append({"tarea": tarea, "completada": False})
        print(f"Tarea '{tarea}' agregada.")
    else:
        print("No se puede agregar una tarea vacía.")
def mostrar_tareas():
    if not tareas:
        print("No hay tareas en la lista.")
        return
    print("\nLista de Tareas:")
    for i, tarea in enumerate(tareas):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i + 1}. {tarea['tarea']} - {estado}")

if __name__ == "__main__":
    while True:
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Salir")
        opcion = obtener_entrada("Selecciona una opción: ")
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")