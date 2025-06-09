'''




Clase con métodos
Descripción: Crea una clase Rectangulo 
con atributos largo y ancho. Implementa 
métodos para calcular el area y el perimetro.
'''
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo= largo
        self.ancho= ancho
    
    def area(self):
        return self.largo*self.ancho
    def perimetro(self):
        return 2*(self.largo+self.ancho)

rect= Rectangulo(5,3)
rect2= Rectangulo(8,3)
print(f"Area es: ", rect.area())
print(f"El perímetro es: ", rect2.perimetro())