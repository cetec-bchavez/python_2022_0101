print('------------------------- Función Calculo con Variables----------------------------')
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
notas = [5,10,20,15,20]
promedio = calcular_promedio_lista(notas)

print(promedio)
print(notas)
