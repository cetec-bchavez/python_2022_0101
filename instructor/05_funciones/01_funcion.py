print('--------------------- Funcion Calculo con Variables --------------')

#Definir Funcion
def calcular_promedio(valor1,valor2):  # 1) Ingredientes
    resultado = 0.0

    resultado = (valor1 + valor2) / 2 # 2)Proceso
    
    return resultado # 3) Resultado


#Utilizar Funcion
nota1=5.0
nota2=6.0

promedio=0.0
suma=0.0

promedio = calcular_promedio(nota1,nota2)

print(nota1,nota2,promedio)

nota1=7.0
nota2=8.0

promedio = calcular_promedio(nota1,nota2)
print(nota1,nota2,promedio)

#Anonimamente
print(9,10,calcular_promedio(9,10))


