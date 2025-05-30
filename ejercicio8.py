'''







Contar números pares e impares
entre dos números
Descripción: Pide al usuario dos 
números A y B (donde A < B) y 
cuenta cuántos números son pares 
y cuántos impares en ese rango.
'''

def contar_pares_impares():
    a= int(input("Ingresa el número A: ")) #10
    b= int(input("Ingresa el número B: ")) #20
    if a>=b:
        print("ERROR: A debe ser menor que B")
        return 
    pares=0
    impares=0
    
    for i in range(a,b+1):
        if i%2==0:
            pares+=1
        else:
            impares+=1
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    
contar_pares_impares()