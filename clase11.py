##crear la clase lista
#crear metodo append()
#crear metodo extend()
#crear metodo pop()

class lista(object):
    def __init__(self,*valores):
        self.lista_interna = []
        for i in valores:
            self.lista_interna.append(i)
    def __str__(self):
        aux = "["
        for i in sel.lista_interna
            aux += str(i) + ","
        aux += "]"
        return(aux)
    def extend(self, lista):
        for i in lista:
            self.lista_interna.append(i)
    def append(self, lista):
        self.__lista_interna.append(lista)

lista = Lista(1,3,4,5,6)
print(lista)


def prueba(*lista):
    for i in lista:
        print(i)

print(lista.lista_interna)


###############################################
#Transportes
#atributos
#marca
#dimenciones
#capacidad de usuarios
#metodos:
#desplazamiento


##terrestres
#atributos
#numero de llantas (n_llantas)
#tipo de terreno de desplazamiento


##Autos
#A/c
#rin

class Transportes(object):
    def __init__(self,marca,dimenciones,capacidad_Usuario):
        self.marca = marca
        self.dimenciones = dimenciones
        self.capacidad_Usuario = capacidad_Usuario
    def desplazamiento(self):
        print("se esta moviendo el transporte")




class Terrestres(Transportes):
    def __init__(self,marca,dimenciones,capacidad_Usuario,n_llantas):
        super().__init__(marca,dimenciones,capacidad_Usuario)
        self.n_llantas = n_llantas
    def desplazamiento(self):
        print("Se esta moviendo el transporte terrestres")


class Autos(Terrestres):
    def __init__(self,marca,dimenciones,capacidad_Usuario,n_llantas,arranque,rin):
        super().__init__(marca,dimenciones,capacidad_Usuario,n_llantas)
        self.arranque = arranque
        self.rin = rin
    def desplazamiento(self):
        print("se esta moviendo mi Auto")


miAuto = Autos("Nissan",4,5,4,"Estandar","rin")


miAuto.desplazamiento()
miAuto.arranque





##moto
#metodos
#caballito
#revase en corto espacio

##desplazamientoclass Moto(Terrestres):
    def __init__(self):
        super().__init__(n_llantas)
    def caballito(self):
        print("Se hizo un caballito")
    def revase(self):
        print("se hizo un revase en corto espacio")
    def desplazamiento(self):
        print("se esta moviendo la moto")
    

