# Ejercicio 8
class Cuenta:
    def __init__(self, titular, cantidad=0, edad=0):
        self._titular = titular
        self._cantidad = cantidad
        self._edad = edad
    
    def ingresar(self, cantidad=0):
        if cantidad > 0:
            self._cantidad += cantidad
    
    def retirar(self, cantidad=0):
        if self._cantidad >= cantidad:
            self._cantidad -= cantidad
        else:
            print("No se puede retirar la cantidad especificada")
    
    def mostrar(self):
        print("Titular:", self._titular)
        print("Cantidad:", self._cantidad)

    @property
    def titular(self):
        return self._titular
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @property
    def edad(self):
        return self._edad
    
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad, bonificacion, edad):
        super().__init__(titular, cantidad, edad)
        self._bonificacion = bonificacion
    
    def es_titular_valido(self):
        if self.edad >= 18 and self.edad < 25:
            return True
        else:
            return False
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("El titular no es válido para realizar esta operación")
    
    def mostrar(self):
        print("Cuenta Joven")
        print("Bonificación:", self._bonificacion)
        super().mostrar()

    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self._bonificacion = bonificacion

"""
#EJEMPLOS
# Cuenta normal
cuenta_normal = Cuenta("Manuel", 1000,34)

# Operamos en la cuenta normal
cuenta_normal.ingresar(100)
cuenta_normal.retirar(900)
cuenta_normal.mostrar()

# Cuenta joven
cuenta_joven = CuentaJoven("Eugenia", 1000, 1000,18)

# Operamos en la cuenta joven
cuenta_joven.ingresar(1000)
cuenta_joven.bonificacion
cuenta_joven.retirar(700)
cuenta_joven.mostrar()

# ¿El titular de la cuenta joven es válido?
print("¿Es el titular válido?", cuenta_joven.es_titular_valido())

# Cuenta joven titular no válido error
cuenta_joven = CuentaJoven("Nina", 3000, 0,25)
cuenta_joven.ingresar(1000)
cuenta_joven.bonificacion
cuenta_joven.retirar(2000)
cuenta_joven.mostrar()
print("¿Es el titular válido?", cuenta_joven.es_titular_valido())"""
