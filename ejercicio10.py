'''









*
**
***
****
*****
******
Imprimir un triángulo de asteriscos
Descripción: Pide un número N 
y dibuja un triángulo de asteriscos con N filas.
'''
def triangulo_asteriscos():
    n= int(input("Ingrese el número de filas N: "))
    for i in range(1,n+1 ):
        print("*"*i)

triangulo_asteriscos()