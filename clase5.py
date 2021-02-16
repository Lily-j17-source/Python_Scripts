#precio diario promedio
precio_diario_promedio = [100, 60, 80, 90, 100, 120, 140 ]
a = 0
for i in range(len(precio_diario_promedio)):
    a += precio_diario_promedio[i]
    
print("el promedio es : ", a / len(precio_diario_promedio))
print("##################################################")

#cuantas veces tomo el valor de 100
se_repite = precio_diario_promedio.count(100)
print("el valor de 100 se repite ",se_repite,"veces")


print("##################################################")
se_Repite_con_if = [i for i in precio_diario_promedio if i == 100]
print(se_Repite_con_if)

precio_diario_promedio[1]=70
print(precio_diario_promedio)