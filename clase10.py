

#Crear la claseAPARTOElectronico
#estado_general (true, false)
#marca
#dimenciones
#funciona(true, false)
class AparatoElectronico(object):
    def __init__(self,marca,dimensiones,encendido = True,funciona=True):
        self.marca = marca
        self.dimensiones = dimensiones
        self.encendido = encendido
        self.funciona = funciona
    def encender (self):
        self.encendido = True
    def descomponer (self):
        self.funciona = False
    def componer(self):
        self.funciona = True
    def apagar (self):
        self.encendido = False

aparato = AparatoElectronico(True,"sony",[40,60],True)
aparato.encendido
aparato.dimensiones
    


#encender afecta el metodo encendido
#descomponer afecta el atributo estado_general
#componer afecta el atributo estado_general
#apagar afecta el atributo encendido

###############3
#Crear la clase Celular
#Atributos
# wifi
# gsm
# llamada = (True, Falses)

#Métodos
# conectar(, red = {wifi, gsm})
# desconectar(, red = {wifi, gsm})
# realizar_llamada()
# colgar()
# tomar_foto
class Celular(object):
    def __init__(self,wifi,red,llamada = True):
        self.wifi = wifi
        self.red = red
    def conectar(self):
        self.red = "Wifi"
    def desconectar(self):
        self.red = "gsm"
    def realizar_llamada(self):
        self.llamada = "True"
    def colgar(self):
        self.llamada = "False"
    def tomar_foto(self):
        self.totmar_foto = "True"


#necender afecta el atributo encendido
#descomponer afecta el atributo estado_general
#componer afecta el atributo estado_general
#apagar afecta el atributo estado_general
#apagar afecta el atributo encendido
#descomponer_tecla afecta el atributo estado_teclas
