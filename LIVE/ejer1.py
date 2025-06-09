'''









Escribir un programa que almacene las asignaturas
de un curso (por ejemplo Matemáticas, Física,
Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado 
en cada asignatura y elimine de la lista 
las asignaturas aprobadas. Al final el programa
debe mostrar por pantalla las asignaturas 
que el usuario tiene que repetir.
'''
materias=["Geometría", "Historia", "Lengua"]
aprobadas=[]
for materia in materias:
    nota= float(input("Qué nota has sacado en "+materia+"?:" ))
    if nota>=5:
        aprobadas.append(materia)
for aprobada in aprobadas:
    materias.remove(aprobada)

print("Tienes que repetir: "+str(materias))
    

