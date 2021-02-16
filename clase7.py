#############3Clase 7
#diccionarios
ejemplo1={
    'Ale Paez' : {
        'Horas de suenio': 7,
        'Minutos al trabajo': 20
    }
}

horas_suenio_diccionario = {
    'Ale Paez':7,
    'Gabriela Camarillo':6,
    'Emanuel Cianca':7,
    'Gilberto Garcia':3,
    'Liliana Juarez':8,
}

#for llave, valor in horas_suenio_diccionario.items():
    #print(f'{llave} duerme {valor}')

list(horas_suenio_diccionario.keys())

#for llave in horas_suenio_diccionario.keys():
   # print(f'{llave} duerme {horas_suenio_diccionario[llave]}')

#for llave in horas_suenio_diccionario.values():
    #print(valor)



###ZIP
l_nombres2 = ['Ale Paez', 'Gabriela Camarillo', 'Emmanuel Cianca', 'Gilberto Garcia', 'Liliana Juárez']
l_horas = [7, 6, 6, 3, 8]
dict_ejercicio = {}

for i, j in zip(l_nombres2, l_horas):
   # print(f'{i} duerme {j} horas')
    #dict_ejercicio.update({i: j})
    dict_ejercicio[i] = j
    print(f'{i} duerme {j} horas')
    
#mezclar diccionarios y listas
ejemplo_mixto ={"liliana":{"vision computacional":[10,9,7]}}
#ejemplo_mixto["Liliana"]

#ejemplo_mixto["liliana"].get("vision computacional")[i]
#ejemplo_mixto["liliana"].get("vision computacional")[0]
#ejemplo_mixto["liliana"].get("vision computacional")[1]
#ejemplo_mixto["liliana"].get("vision computacional")[2]
############
ejercicio3 = {}
nAlumno=input("Escribe el nombre del alumno: ")
nTiempo = input("Cuanto tiempo tarda en llegar al trabajo?: ")



while nAlumno != "no":
    ejercicio3.setdefault(nAlumno,int(nTiempo))
print(ejercicio3)

