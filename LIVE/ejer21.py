'''
Ejercicio 10
Escribir un programa que permita gestionar la base de 
datos de clientes de una empresa. Los clientes se 
guardarán en un diccionario en el que la clave de 
cada cliente será su NIF, y el valor será otro diccionario 
con los datos del cliente (nombre, dirección, teléfono, 
correo, preferente), donde preferente tendrá el valor 
True si se trata de un cliente preferente. El programa
debe preguntar al usuario por una opción del siguiente 
menú: (1) Añadir cliente, 
(2) Eliminar cliente, 
(3) Mostrar cliente, 
(4) Listar todos los clientes, 
(5) Listar clientes preferentes, 
(6) Terminar. En función de la opción elegida el 
programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario 
con los datos y añadirlo a la base de datos.

Preguntar por el NIF del cliente y eliminar sus datos de
la base de datos.

Preguntar por el NIF del cliente y mostrar sus datos.

Mostrar lista de todos los clientes de la base datos con
su NIF y nombre.

Mostrar la lista de clientes preferentes de la base de
datos con su NIF y nombre.

Terminar el programa.


print("Nif: ", nif)
for clave, valor in clientes[nif].items():
'''
clientes={}
opcion=''
while opcion!='6':
    if opcion=='1':
        nif= input("Por favor ingresa el nif: ")
        nombre=  input("Por favor ingresa el nombre: ")
        dirección= input("Por favor ingresa la dirección: ")
        telefono= input("Por favor ingresa el teléfono: ")
        correo= input("Por favor ingresa el correo: ")
        preferente= input("¿El cliente es preferente (S/N): ")
        cliente= {'nombre': nombre, 'dirección': dirección, 'telefono': telefono, 'correo': correo, 'preferente': preferente=='S'}
        clientes[nif]=cliente
    if opcion=='2':
        nif= input("Por favor ingresa el nif del cliente a eliminar: ")
        if nif in clientes:
            del clientes[nif]
        else:
            print("El nif ingresado no existe! ")
           
                

