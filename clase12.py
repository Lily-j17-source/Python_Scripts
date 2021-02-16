#Crear la clase hogar, craerle por lo menos 3 metodos y 3 atributos, considera
#adicionalmente el atributo numeor de cuartos y el de superficie en M2
##Crear la clase Departamento que hereda de la clase hogar, crearle por lo menos
#3metodos y atributos

###Utilizar __add__ en hogar que sume los cuartos de la casa o un departamento
###Utilizar __len__ para devolver las dimenciones de la casa o depa

class Hogar(object):
    def __init__(self,calle,numero,cp,familia):
        calle = calle
        numero = numero
        cp = cp
    def direccion (self):
        print("La direccion de tu hogar es:{calle},{numero},{cp}")
    def familia(self):
        print("En este hogar vive la familia:{familia}")
    def __add__(self, other):
        return self.ncuartos + other.ncuartos
    




class Departamento(Hogar):
    def __init__(self,calle,numero,cp,familia,npiso,ncuartos,superficie):
        super().__init__(calle,numero,cp,familia)
        npiso =  8
        ncuartos = ncuartos
        superficie = superficie
    def altura(self):
        print(f'Este Departamento se encuentra en elpiso:{npiso}')

    def __len__(self):
        return(self.superficie)

depa1 = Departamento("Libertad",109,78430,"Juarez",8,2,42)
depa1.altura()
print(depa1.npiso)
print(isinstance(depa1,Hogar))



##################################
#Errores:

try:
    resultado = 10/0
except:
    print("no se puede realizar")


try:
    lista = [1,2,3,4,5]
    lista[10]
Exception as e:
    print('El error que te ocurrio es: {e}')



try:
    colores = {'rojo':'red','verde':'green','negre':'black'}
    colores['blanco']
except:
    print("Key no encontrada")



try:
    resultado = 15 + "20"
Exception as e:
    print(f'El error que te ocurrio es: {e}')