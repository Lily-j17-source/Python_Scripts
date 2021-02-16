########################OBJETOS
# EN PYTHON todo son clases y objetos

#para crear una clase usamos :
#class molde(object):


class Acumulador(object):
    x = None
    def __init__(self,x = 0):
        self.x = x
    def sumar_una_unidad(self):
        self.x += 1  
        return self.x
    def restar_una_unidad(self):
        self.x -= 1
    def mostrar_acumulador(self):
        print(self.x)

mi_acumulador = Acumulador()

print(mi_acumulador.x)
print(mi_acumulador.sumar_una_unidad())
mi_acumulador.mostrar_acumulador()

######ejercicio 2 #####
class Producto(object):
    carrito = 0
    def __init__(self,precio_inicial_sin_iva = 100, iva = 0.16):
        self.precio_sin_iva = precio_sin_iva
        self.iva = iva
        self.precio_con_iva = (1 + iva) * precio_sin_iva

    def modificar_precio(self, nuevo_precio_sin_iva):
        self.precio_sin_iva = precio_sin_iva
        self.precio_con_iva = (1 + self.iva) * self.precio_sin_iva
    def mostrar_precio_iva(self):
        print(self.precio_con_iva)
    def comprar_una_unidad(self):
        self.carrito += 1
    def calcular_totales(self):
        self.subtotal = self.precio_sin_iva * self.carrito
        self.impuesto = self.subtotal + self.impuesto
    def mostrar_totales(self):
        print(f"has comprado: {self.carrito}, dando un subtotal de:
        {self.subtotal}, pagas de impuesto: {self.impuesto}, el total que vas a 
        pagar es: {self.total}")


producto1 = Producto(200)
print(producto1.precio_sin_iva)
producto1.modificar_precio(150)
print(producto1.precio_sin_iva)
producto1.mostrar_precio_iva()
producto1.mostrar_totales()
producto1.comprar_una_unidad()
producto1.mostrar_totales()
