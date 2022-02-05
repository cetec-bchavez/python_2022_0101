print('--------------------- Funcion Calculo con Variables --------------')

#Definir Funcion
def calcular_promedio_lista(valores):  # 1) Ingredientes
    resultado = 0.0
    
    suma=0.0
    numero_valores = 0
    #resultado = (valor1 + valor2) / 2 # 2)Proceso
    
    numero_valores = len(valores)

    for valor in valores : # Recorrer Valores
        suma+=valor

    resultado = suma / numero_valores

    return resultado # 3) Resultado


promedio=0.0

nota_actual=0.0
notas = [] #[5,4,7,9,2,3,10]

nota_actual = input('Ingrese Nota: ') # 1 dato, 1 celda, 1 variable, texto-string

notas.append(float(nota_actual))

promedio = calcular_promedio_lista(notas)

print(promedio)
print(notas)

print('Primera Nota',notas[0])
#print('Tercera Nota',notas[2])