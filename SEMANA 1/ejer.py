"ponerse al dia con el lenguaje de programación Python"
'''
"sebastian estuvo aqui"

Escribe un programa que solicite al usuario dos números y muestre su
suma, resta, multiplicación, división, división entera y residuo (módulo).
'''
num1= float(input("Por favor ingresa el número 1: "))
num2= float(input("Por favor ingresa el número 2: "))
suma= num1+num2
resta= num1-num2
multiplicación= num1*num2
if num2!=0:
    div= num1/num2
    div_Entera= num1//num2
    modulo= num1%num2
else:
    print("No se puede dividir por cero")

print(f"La suma es: {suma} ")
print(f"La resta es: {resta} ")
print(f"La multiplicación es: {multiplicación} ")
print(f"La división es: {div} ")
print(f"La división entera es: {div_Entera} ")
print(f"El módulo es: {modulo} ")