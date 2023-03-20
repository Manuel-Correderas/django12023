# Ejercicio 7
class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, nuevo_titular):
        self.__titular = nuevo_titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad
    
    def mostrar(self):
        print("Titular:", self.__titular)
        print("Cantidad:", self.__cantidad)
    
    def ingresar(self, nueva_cantidad):
        if nueva_cantidad > 0:
            self.__cantidad += nueva_cantidad
    
    def retirar(self, nueva_cantidad):
        self.__cantidad -= nueva_cantidad


#Ejemplo

"""cuenta1 = Cuenta("Manuel", 300)

print(cuenta1.cantidad)  # 300

cuenta1.ingresar(700)
cuenta1.retirar(100)

cuenta1.mostrar()  # Titular: Manuel cantidad 900"""