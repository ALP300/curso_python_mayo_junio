'''
Escribe un programa que solicite al usuario un número entero y calcule
si es divisible por 3 y por 5.
'''
print("Vereficando si el numero es divisible por 3 o por 5 :) " )
numero=int(input("Ingrese un numero  :"))
if numero%3==0:
    print("El numero es divisible por 3")
elif numero%5==0:
    print("El numero es divisible por 5")
else:
    print("El numero no es divisible por 3 ni por 5")
    

