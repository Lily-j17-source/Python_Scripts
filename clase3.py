############LISTAS##################
print("estoy en python")
mi_primer_lista = [1,3.14,"Hola mundo"]
#Asigna la referencia a y
x=[1,2] #se crea ka variable x 
y = x
x[0] = 0
y

##Asignar el valor de x a y
#al hacer el .copy realiza una copia a los valores qe estaban en x
#no modifica los valores de x, solo los de y
#en el anterior, hace una copia de la referencia de 
#lo qe hay en X
x=[1,2]
y = x.copy()
x[0]=0
y


##METODOS DE LSITAS
#append
mi_lista1 = [1,2,3]
mi_lista2 = [1,3]
mi_lista1.append(mi_lista2)
#append, agrega al final de la lista, y modifica la lista original

#extend
mi_lista1 = [1,2,3]
mi_lista2 = [1,3]
mi_lista1.extend(mi_lista2)
#Agrega al final de la lista pero cada elemento en un espacio diferente,
#agrega al final

#remove--elimina el primer argumento qe le pasas como parametro y encuentra
mi_lista1 = [1,2,3]
mi_lista2 = [1,3]
mi_lista1.remove(2)#eliminara el numero 2
#para eliminar el elemento dentro de una lista que esta en una lista
ejemplo_lista = [1,2,3,[1,3]]
#accedo a la lista con indices, luego hago un remove
ejemplo_lista[3].remove(1)
#eliminaria el 1 de la lista dentro de la lista


#index --- busca el valor que le enviamos y busca el indice
#que le corresponde y este metodo no afecta a la lista
mi_lista1 = [1,2,3]
mi_lista2 = [1,3]
mi_lista1.index(3)
#Si hay mas numeros 3 por ejempl, nos regresa solo el primer indice qe encuentra


#count ---Nos regresa cuantas veces esta el elemento en la lista
mi_lista1.count(1) #--solo cuenta las coincidencias

#reverse--voltear la lista y afecta el objeto, pero no regresa nada
#nos devuelve el NOneType
mi_lista1 = [1,2,3,[1,3],3]
#mi_lista1 = [::-1]
#
#print(mi_lista2)
print(mi_lista1)
mi_lista1[::-1].reverse()#mi_lista1.reverse()
print(mi_lista1)


#insert --dado un indice inserttar un nuevo elemento en la lista
#le enviamos la posicion y despues el valor que queremos insertar
mi_lista1 = [1,2,3]
mi_lista1.insert(2,"methodo insert")
#es la operacion inversa al pop

#pop -- busco un elemento y despues lo elimino, recibe el indice del elemento qe
#queremos borrar, cuando ya llame el metodo ya no lo podemos revertir
#afecta la lista principal y tmb da un resultado, en este caso, 
#es el resultado qe se elimino.


#sort -- 
mi_lista1 = [1,2,3]
mi_lista1.sort()
#copy --






##Indices
#[inicio:(fin+1)] #me va a traer el elemento..
 #quiero llegar al elemento 4, pero sin el +1 nos regresa
 #la posicion 3, por eso le ponemos el +1 para qe nos regrese
 #el elemento correcto
##recorrido de 2 en 2
mi_lista1[::2]#--esto se llama barrido
#para recorrer toda la lista con un barrido:
mi_lista1[::]
#para obtener el ultimo elemento:
mi_lista1[len(mi_lista1)-1]#importante poner el -1
#RECORDAR QUE EL INDICE EMPIEZA EN 0, POR LO QE TENEMOS QUE USAR EL -1
#para que nos regresa el ulitmo elemento
mi_lista1[-1]#de elemento 1 al len(mi_lista1)-1, nos regresa el ultimo elemento
#Esto es un barrido, peeero de inicio a fin por eso no lleva ::

x=[1,2,1,2,2,1,1,2,1,2,2]

##

##FOR EN LISTAS
for i in range(10):
    print("cuenta hasta 10",i)
    

lista_con_for = [i for i in range(50)]
#la primera i, es una variable que se puede modificar y agregar a
#una lista, esa lista se llama lista_con_for

###if en listas
lista_con_for = [i for i in range(50) if i % 2 == 0]

##else en listas
x = [i if i % 2 == 0 else "no es par" for i in range (100)]
#a la lista anterior sumarle 1 a los numeros enteros
[i + 1 for i in x if isinstance(i, int)]
#o tmb asi
[i + 1 for i in x if i % 2 == 0] #--marca error xq los impares son str
[x[i] + 1 for i in range(len(x)) if i % 2 == 0]#aqui lo que hacemos es
#recorrer un rango de la longitud de x donde SUPONEMOS que el indice 
#uno es donde estan los no pares, y ahi no le sumamos,
#solo le sumamos 1, cuando es par, y al elemento x[i] de la posicion i
#le sumanos 1
#Lo que va del lado izq del for es lo que va a almacenar en la lista
#Lo que esta de lado der 


#Lista qe guarda solo los primeros 50 valores.
[i for i in range(100) if i < 50]

#
[i if i % 2 == 0 else "no es par" for i in range(100) if i < 50]
