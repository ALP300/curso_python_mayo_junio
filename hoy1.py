'''















Calcular la suma de los “n” 
primeros términos de la 
sucesión 1; 2x; 3x2; 
4x3; … para un valor 
de “x” dado. 
'''

def suma_sucesion(x,n):
    suma=0
    for i in range(1, n+1):
        suma+= i*(x**(i-1))
    
    return suma
        
    
x= int(input("Por favor ingresa X: "))
n= int(input("Por favor, ingresa el valor n: "))
print(suma_sucesion(x, n))
    
