###1---Crear dos variables que representen dos productos, asignarles un precio
producto1 = 12
producto2 = 18.50

##2--Aplicar iva(16% del precio)
iva = .16
precio = 100.0
valor_total = precio * (1 + iva)
##3-Calcular el precio total de la compra de dos productos

##4--Calcular el precio total de 4 piezas del producto 1 y 5 piezas del producto 2


##5---Aplicar 2 operaciones con entero
numA = 100
numB = 2
resDivision = numA / numB
print("La division de estos dos numeros es: ",resDivision)

resMultiplica = resDivision * 10
print("la multiplicacion de la division es: ",resMultiplica)


##6--Aplicar 2 operaciones con flotantes

print("--------------------------------------")
##Crear una lista l-compañeros con 5 nombres de compañeros
l_nombres = ['Ale Paez', 'Gabriela Camarillo', 'Emmanuel Cianca', 'Gilberto Garcia', 'Liliana Juárez']
print(l_nombres)

l_dato=[20, 0, 10, 35, 40]
print("minutos",l_dato)

l_dato[2] = 30

l_resultado=[l_nombres[i] for i in range(len(l_nombres)) if l_dato[i] < 26]
print( l_resultado)

l_nombres2 = ['Ale Paez', 'Gabriela Camarillo', 'Emmanuel Cianca', 'Gilberto Garcia', 'Liliana Juárez']
l_horas = [7, 6, 6, 3, 8]
print(l_horas)

l_mas8=[l_nombres2[i] for i in range(len(l_horas)) if l_horas[i] >8]
print(l_mas8)

l_vampiros = [l_nombres2[i] + " es un vampiro" if l_horas[i] < 4 else l_nombres2[i] for i in range(len(l_horas)) if l_horas[i] < 8]
print(l_vampiros)


###################################3333
##Bool
#<menor que
#> mayor que
#>= mayor igua
#<= menor igual
#and , &
#or, |
#true & true = true
#true & false = false
#false & true = false
#false & false = false

########################################
#IF
#if(expresion devuelve true, false):
  #  codigo1
#elif (expresion2 devuelve true, false):

horas_suenio = 8
if horas_suenio < 8:
    print("duermes muy poco")
elif horas_suenio < 4:
    print("eres un vampiro")
else:
    print("que envidia")

# True & True = True
print("True & True", True & True)
# True & False = False
print("True & False", True & False)
# False & True = False
print("False & True", False & True)
# False & False = False
print("False & False", False & False)
# True | True = True
print("True | True", True | True)
# False | True = True
print(F"False | True", False | True)
# True | False = True
print("True | False", True | False)
# False | False = False
print("False | False", False | False)
# if (expresion1 devuelve True, False):
#     código 1
# elif (expresion2 devuelve True, False):
#     código 2
# elif (expresion3 devuelve True, False):
#     código 3
# elif (expresion4 devuelve True, False):
#     código 4
# else:
#     código 5
# if condición:
### cuidado con el orden en esta caso nunca se va ejecutar
##  print("duermes muy poco")
##
horas_suenio = 7
if horas_suenio < 8:
    print("duermes muy poco")
elif horas_suenio < 4:
    print("eres un vampiro")
else:
    print("Que envidia")
### para corregirlo puedes cambiar el orden
horas_suenio = 7
if horas_suenio < 4:
    print("eres un vampiro")
elif horas_suenio < 8:
    print("duermes muy poco")
else:
    print("Que envidia")
### Operaciones jerarquía
