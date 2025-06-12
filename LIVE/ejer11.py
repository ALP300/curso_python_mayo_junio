'''


Simulador de votaciones
Descripción: Crea un programa que simule una 
votación donde la audiencia elige candidatos
y vota. Muestra los resultados con porcentajes
y un gráfico simple de barras usando asteriscos.

'''


from collections import Counter

def simulador_votaciones(candidatos, num_votos):
    votos=[]
    for i in range(num_votos):
        voto= input(f"Voto {i+1}: Ingresa el nombre del candidato: ")
        if voto in candidatos:
            votos.append(voto)
        else:
            print("Candidato no válido, voto descartado") 

    conteo= Counter(votos)
    total_votos= len(votos)
    print("Resultado de la votación")
    for candidato, cantidad in conteo.items():
        porcentaje= (cantidad/total_votos)*100
        print(f"{candidato}: {porcentaje} {'*'* cantidad}")
        
candidatos= input("Ingresa los nombres de los candidatos (separado por comas): ").split(',')
candidatos=[c.strip() for c in candidatos]
num_votos= int(input("Por favor, ingresa el número de votantes: "))
simulador_votaciones(candidatos, num_votos)
    

