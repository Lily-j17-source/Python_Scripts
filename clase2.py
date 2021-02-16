###Recordatorio
#Python no tiene i++ pero...
print("inicializando i con un valor de 1")
i = 1
print("sumamos una unidad")
#i es igual al valor que tenia y le suma 1
i += 1
print("El resultado es: ", i)
#tmb se puede poner
print("el resultado es: " + str(i))
#str(i)---> str es la funcion que pasa string a entero
texto_resultado = "El resultado es: {}"
texto_resultado = texto_resultado.format(i)
print(texto_resultado)

#fSTRING, solo viven en el momento que es creado, va por orden
#Lleva la letra f
nombre = "Lily"
apellido = "Juarez"
print(f"bienvenida {nombre}{apellido}")

"""Texto
en 
diferentes
lineas
"""
##EJERCICIO
mi_Empresa = "nS"

descripcionEmpresa = """
Nombre de la empresa: {}
El objetivo es: Crear una aplicación que 
apoye a estudiantes o profesionistas de enfermería 
en la realización del proceso cuidado enfermero 
de los pacientes a su cargo.
"""
descripcionEmpresa = descripcionEmpresa.format(mi_Empresa)
print(descripcionEmpresa)



###Funciones type, len
print("5 es un entero", type(5))
print("'5' es un string", type('5'))
print("true es un bool", type(True))
print("3.333 es un float", type( 3.333))
#EJEMPLO CON VARIABLES
x= 5
print("5 es un entero", type(x))

#OBTENER CARACTERES
sentimiento = "Hola, hoy me siento ..."
sentimiento[1]
sentimiento[len(sentimiento)-1]
#[:] nos trae toda la cadena
#[:3] nos traer los primros 3
#[1:3] nos trae el elemento,1,2
#[3:3] nos regresa vacio
#[::-1]Nos invierte la cadena
#[::-1][:5]nos regresa los ultimos 5
#[::-1:-5]
#si ponemos -5 nos dice los numeros desde el final
#Imprime los impares
#[inicio:termina:incremento]
#[0::2]

palindromo = "ANITALAVALATINA"
print(palindromo)
print(palindromo[::-1])


##METODOS de STRINGS
nombre = "Lily Juarez"
nombre.find("a")
#Regres -1 si no hay
#Si lo encuentra, regresa la primera posicion donde lo encontro
nombre.upper()
print(nombre)
nombre.lower()
print(nombre)
#Estos dos metodos no afectan el valor de la variable
nombre.swapcase()#cambia mays a min, y viceverza

nombre.replace("a","e")#cambia las a del nombre por e

nombre.split(" ")#nos separa cuando encuentre un caracter
#col1,col2,col3 = entrada_datos.split("|")

Texto_entrada = "12|13|14"
lista_texta_entrada = Texto_entrada.split("|")
"|".join(lista_texta_entrada)#join nos une

#isdigit() nos sirve para saber si un elemnto es digito
lista_texta_entrada[0].isdigit()

#isnumeric()






