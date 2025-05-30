'''
Crea un programa que tome una lista de números y calcule la suma de todos sus elementos.
'''
numeros=[4,2,5,6]
numeros.append(7)
print(numeros)
suma=0
for num in numeros:
    suma+=num

print(f"La suma de los elementos es: {suma}") 

tupla= (1,2,"HOLAAA",3.5)

print(tupla)

diccionario={"nombre": "Ana", "edad":14, "ciudad": "Lima"}
diccionario["dirección"]= "Avenida manzanitas"
del diccionario["ciudad"]
print(diccionario)
print(diccionario["edad"])
