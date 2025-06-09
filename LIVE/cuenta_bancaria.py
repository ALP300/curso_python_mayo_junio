'''



Crea una clase CuentaBancaria con un 
atributo privado saldo. Implementa 
métodos para depositar, retirar y 
consultar el saldo, asegurándote de 
que el saldo no pueda ser negativo.
'''
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo= saldo_inicial if saldo_inicial>=0 else 0
    
    def depositar(self, cantidad):
        if(cantidad>0):
            self.__saldo+=cantidad
            print(f"DEPOSITADO {cantidad}. NUEVO SALDO {self.__saldo}")
        else:
            print("Por favor ingresa un número positivo")
    def retirar(self, cantidad):
        if(cantidad>0) and cantidad<=self.__saldo:
            self.__saldo-=cantidad
            print(f"DEPOSITADO {cantidad}. NUEVO SALDO {self.__saldo}")
        else:
            print("Por favor ingresa un número positivo")
    def consultar_saldo(self):
        return self.__saldo

cuenta= CuentaBancaria(400)
cuenta.depositar(500)
cuenta.retirar(300)
cuenta.consultar_saldo()