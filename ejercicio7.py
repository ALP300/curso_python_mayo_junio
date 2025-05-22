'''















Calcular la suma de los “n” 
primeros términos de la 
sucesión 1; 2x; 3x2; 
4x3; … para un valor 
de “x” dado. 
'''

def suma_sucesion(n,x):
    suma=0
    for i in range(1,n+1):
        suma+= i *(x**(i-1))
    return suma

n= int(input("Por favor ingresa el n: "))
x= int(input("Por favor ingresa el x: "))
print(suma_sucesion(n,x))


