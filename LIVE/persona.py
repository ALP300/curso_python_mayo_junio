'''







Crear una clase simple
Descripción: Crea una clase Persona con
atributos nombre y edad, y un método 
presentarse que imprima un mensaje con 
el nombre y la edad de la persona.
'''
class Persona:
    def __init__(self, nombre, edad):
     self.nombre= nombre
     self.edad= edad
    
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

persona1= Persona("Leo", 21)
persona2= Persona("Derf", 24)
persona3= Persona("Melanie", 19)
persona4= Persona("Yenifer", 20)
persona5= Persona("Velkoz el más wapo", 18)
persona3.presentarse()

