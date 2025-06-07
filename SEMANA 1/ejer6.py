'''
Escribe un programa que solicite al usuario tres números y determine
cuál de ellos es el mayor.
'''

num1= float(input("Por favor ingrese el primer número: "))
num2= float(input("Por favor ingrese el segundo número: "))
num3= float(input ("Por favir ingrese el tercer número: "))

if (num1>num2 and num1>num3):
    print(f"El número mayor es  {num1}")
elif(num2>num1 and num2>num3 ):
    print (f"El número mayor es {num2}")
elif(num3>num1 and num3>num2):
    print(f"El número mayor es {num3}")
#else (num1==num2 or num1 == num3 or num2 == num3):
else:
    print("Error! Números inválidos")
