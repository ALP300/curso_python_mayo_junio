'''
Implementa un programa en Python que simule 
el proceso de deslizar perfiles
de candidatos. 
'''
import random
import time

def generar_candidato(audiencia_nombre=None):
    nombres=["Leonardo", "Elver", "Isa","Mijhail", "Karibes", "Dan"]
    hobbies=["Tocar piano", "Fútbol", "Bailar", "Viajar", "Caminar", "Invertir"]
    frases=["Crees en el amor a primera vista o paso de nuevo?","Tócame que soy realidad",
            "Nunca dejes que nadie prenda tu brilla","Si fueras una función, sería la que siempre retorna felicidad"]
    nombre= audiencia_nombre if audiencia_nombre else random.choice(nombres)
    edad= random.randint(18,40)
    hobby= random.choice(hobbies)
    frase= random.choice(frases)
    return {
        "nombre": nombre,
        "edad": edad,
        "hobby": hobby,
        "frases": frase
    }
def simulador_tinder():
    print("¡Bienvenido a TEAM TOK! ")
    time.sleep(2)
    candidatos=[]
    likes=[]
    for i in range(3):
        nombre= input(f"Por favor ingresa el nombre del candidato {i+1} o PRESIONAR ENTER: ")
        candidato= generar_candidato(nombre)
        print(f"Candidato {i+1}: ")
        print(f"Nombre: {candidato['nombre']} ")
        print(f"Edad:  {candidato['edad']}: ")
        print(f"Hobby: {candidato['hobby']}: ")
        print(f"Frase: {candidato['frases']}: ")
        time.sleep(2)
        
        decision= input("¿Despliza a la derecha (♥️) o a la izquierda (❌)? (r/l): ").lower()
        if decision=="r":
            print(f"Le diste ♥️ a {candidato['nombre']}! ")
            likes.append(candidato)
        else:
            print(f"❌ Rechazo para {candidato['nombre']}")
        candidatos.append(candidato)
        time.sleep(2)
    
    if likes and random.choices([True, False]):
        match= random.choice(likes)
            
        print(f"\n ¡Es un match con {match['nombre']}")
        print(f"\n Te dice:  {match['frases']}")
        print("Prepárate para la cita! :3")
    else:
        print("NO HUBO MATCH :(")

simulador_tinder()