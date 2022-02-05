
def calc_promedio_lista(valores):
    resultado = 0
    suma=0
    numero_valores=0
    numero_valores = len(valores)

    for valor in valores:
        suma+=valor

    resultado = suma / numero_valores

    return resultado

notas = [5,3,4,6,5,9,8,7]
promedio=calc_promedio_lista(notas)

print(promedio)
print(notas)

print("Primera nota",notas[0])
print("Segunda nota",notas[1])

#cambiar varible de lista ya defiinida

notas[0]= 8
print("nueva primera nota",notas[0])