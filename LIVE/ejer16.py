'''
Instrucciones para usar el programa:
Ejecuta el código en tu entorno de Python (puedes copiarlo 
a un archivo .py o usar un editor como VS Code, PyCharm
o incluso una consola interactiva).
El programa muestra un menú con 5 opciones:
Ver catálogo: Lista todos los libros con su título, autor y 
estado (disponible o prestado).
Agregar un libro: Permite añadir un libro nuevo con título y 
autor.
Prestar un libro: Marca un libro como prestado si está 
disponible.
Devolver un libro: Marca un libro como disponible si 
estaba prestado.
Salir: Termina el programa.
Ingresa el número de la opción deseada y sigue las 
instrucciones en pantalla.
'''
def mostrar_opciones():
    print("\n Bienvenido a la biblióteca ")
    print("1. Ver catálogo de libros")
    print("2. Agregar libros")
    print("3. Prestar libros")
    print("4. Devolver los libros")
    print("5. Salir")
    return input("Por favor elige una opción (1-5): ")

def agregar_libros(libros):
    titulo= input("Por favor ingresa el título del libro: ")
    autor= input("Por favor ingresa el autor del libro: ")
    if titulo and autor:
        libros.append({'titulo': titulo, 'autor': autor, 'disponible': True})
        print(f"Libro '{titulo}' agregado correctamente")      
    else: 
        print("Por favor ingresa un valor, los datos no pueden estar vacíos")

def ver_libros(libros):
    if not libros:
        print("No hay libros en el catálogo")
    else:
        print("Catálogo de libros: ")
        for libro in libros:
            print(f"- {libro['titulo']} Autor: {libro['autor']}, Estado {libro['disponible']}")


def main():
    libros=[]
    while True:
        opcion= mostrar_opciones()
        if opcion=="1":
            ver_libros(libros)
        elif opcion=="2":
            agregar_libros(libros)

if __name__=="__main__":
    main()