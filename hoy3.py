'''


Generar múltiplos de un número 
entre 1 y 100
Descripción: Pide un número al 
usuario y muestra todos sus múltiplos 
entre 1 y 100.
'''

def multiplos_1_100():
    n= int(input("Por favor, ingresa un número: "))
    print(f"Múltiplos de {n} entre 1 al 100")
    for i in range(1,100):
        if i%n==0:
            print(i, end=" ")
    print()

            #7 3 8 4 6 2
multiplos_1_100()