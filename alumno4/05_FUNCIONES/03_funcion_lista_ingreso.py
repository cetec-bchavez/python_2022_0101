def calcular_promedio_lista(valores): #ingrediente
    resultado = 0.0
    #resultado = (valor1+valor2)/2    #proceso
    suma = 0.0
    numero_valores = 0.0
    numero_valores = len(valores)
    
    for valor in valores:
       suma += valor
       
    resultado = suma / numero_valores   
        
    return resultado     #resultado

promedio = 0.0

nota_actual = 0.0
notas = []
nota_actual = input('Ingreso notas = ')
notas.append(float(nota_actual))
promedio = calcular_promedio_lista(notas)

print(promedio)
print(notas)


