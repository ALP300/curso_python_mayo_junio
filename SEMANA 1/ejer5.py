'''
Escribe un programa que tome una calificación numérica de un
estudiante (entre 0 y 100) y le asigne una letra según la siguiente tabla:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Menos de 60: F
'''
nota= int(input("Ingrese la calificación del estudiante: "))
if(nota>=90): 
    print("Tu calificación es A")
elif(nota>=80):
    print("Tu calificación es B")
elif(nota>=70):
    print("Tu calificación es C")
elif(nota>=60):
    print("Tu calificación es D")
else:
    print("Tu calificación es F")