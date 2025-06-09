'''





Crea una clase base Vehiculo 
con atributos marca y modelo, 
y un método describir. Luego, 
crea una clase derivada Coche 
que herede de Vehiculo y añada
un atributo puertas y un método 
para mostrar el número de puertas.

'''
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca= marca
        self.modelo= modelo
    def describir(self):
        print(f"Vehiculo {self.marca} {self.modelo} ")

class Coche (Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas= puertas
    
    def describir(self):
        print(f"Coche {self.marca} {self.modelo} {self.puertas} ")

vehiculo= Vehiculo("Toyota","Corolla")
vehiculo= Vehiculo("Toyota", "rav4")
coche= Coche("Toyota","Corolla",4)
print(vehiculo.describir())
print(coche.describir())


