'''
Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
Los clientes se guardarán en un diccionario en el que la clave de cada cliente 
será su NIF, y el valor será otro diccionario con los datos del cliente 
(nombre, dirección, teléfono, correo, preferente), donde preferente tendrá 
el valor True si se trata de un cliente preferente. El programa debe preguntar 
al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, 
(3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, 
(6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.
'''
clientes={}
opcion= ' '
while opcion!='6':
    if opcion=='1':
        nif= input("Introduce el NIF del cliente: ") #123
        nombre= input("Introduce el nombre del cliente: ") #Pepe
        dirección= input("Introduce la dirección del cliente: ") #AAAAA
        teléfono= input("Introduce el teléfono del cliente: ")# 12343254325
        correo= input("Introduce el correo del cliente: ") #LEO@GMAIL.COM
        preferente= input("¿Es un cliente preferente (S/N): ") #S
        cliente= {'nombre': nombre, 'dirección': dirección, 'teléfono': teléfono, 'correo': correo, 'preferente': preferente.upper() == 'S'}
        clientes[nif]= cliente
    if opcion=='2':
        nif= input("Por favor ingresa el NIF: ")
        if nif in clientes:
            del clientes[nif]
        else: 
            print("No existe el nif en los clientes")
            
    if opcion=='3':
        nif= input("Introduce el NIF del cliente: ")
        if nif in clientes:
            print('NIF: ', nif)
            for clave, valor in clientes[nif].items():
                print(clave, ': ', valor)
        else: 
            print("No existe el nif en los clientes")
    
    if opcion=='4':
        print("Lista de cliente: ")
        for clave, valor in clientes.items():
            print(clave, ': ', valor["nombre"])
            
    if opcion=='5':
        print("Lista de clientes preferentes: ")
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, ': ', valor["nombre"])
            
    print("\n" + "="*40)
    print("   GESTIÓN DE CLIENTES - MENÚ PRINCIPAL")
    print("="*40)
    print("1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")
    print("="*40)
    opcion = input("Elige una opción (1-6): ")