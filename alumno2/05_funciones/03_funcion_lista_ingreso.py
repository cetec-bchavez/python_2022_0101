def calc_promedio_lista(valores):
    resultado = 0
    suma=0
    numero_valores=0
    numero_valores = len(valores)

    for valor in valores:
        suma+=valor

    resultado = suma/numero_valores

    return resultado

promedio=0
nota_actual=0
notas = [] #[5,3,4,6,5,9,8,7]

nota_actual=input("ingrese nota: ")   #solo para un dato, celda o variable

notas.append(float(nota_actual))

promedio=calc_promedio_lista(notas)



print(promedio)
print(notas)

#print("Primera nota",notas[0])
#print("Segunda nota",notas[1])