###############EJERCICIO DE DICCIONARIOS

#cREAR UN DICCIONARIO
ejercicio_Diccionario = {}
id = 1

#FUNCION PARA REGISTRAR UN USUARIO EN DICCIONARIO(DATA), NOMBRE, EDAD
#CIUDAD DE RESIDENCIA
#CADA QUE SE INSERTA UN USUARIO SE LE DA UN ID, ES DECIR, CONTENDRA NOMBRE, EDAD
#,CIUDAD DE RESIDENCIA
#nombre = input("Ingresa el nombre del usuario: \n")
#edad = input("Ingresa la edad del usuario: \n")
#ciudad_Residencia = input("Ingresa la ciudad de residencia del usuario: \n")

def nuevoUsuario (nombre, edad, ciudad_Residencia):
    global ejercicio_Diccionario
    global id 
    id +=1
    #id = len(ejercicio_Diccionario) + 1
    #valor = ejercicio_Diccionario.setdefault(id,{nombre,edad,ciudad_Residencia})
    valor = ejercicio_Diccionario.update({"id":[id],"nombre":nombre,"edad":edad,"residencia":ciudad_Residencia})
    print(id)
    return id,ejercicio_Diccionario

print(id)
nuevoUsuario("lily","26","San luis")
nuevoUsuario("lil","22","San luis")
nuevoUsuario("liliana","20","San luis")

#print(ejercicio_Diccionario)


#VALIDAR QUE NO EXISTA YA EN EL DICCIONARIO

#FUNCION PARA MOSTRAR LOS DATOS DEL USURAIO, SE RECIBE UN ID

#FUNCION PARA MODIFICAR LOS DATOS

#FUNCION PARA MOSTRAR TODOS LOS USUARIOS REGISTRADOS
def muestraTodos():
    global ejercicio_Diccionario
    for key in ejercicio_Diccionario:
        print (key, ":", ejercicio_Diccionario[key])


muestraTodos()
#FUNCION PARA FILTRAR POR EDAD

#FUNCION PARA ELIMINAR UN USUARIO POR ID
def elimina_Usuario(id):
    global ejercicio_Diccionario
    valor = ejercicio_Diccionario.pop(id)
    print("el usuario eliminado fue el del id: ", valor)
