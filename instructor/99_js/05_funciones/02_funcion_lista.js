console.log('--------------------- Funcion Calculo con Variables --------------')

//functioninir Funcion
function calcular_promedio_lista(valores){  // 1) Ingredientes
    let resultado = 0.0
    
    let suma=0.0
    let numero_valores = 0
    //resultado = (valor1 + valor2) / 2 // 2)Proceso
    
    numero_valores = valores.length

    for(valor of valores) // Recorrer Valores
        suma+=valor

    resultado = suma / numero_valores

    return resultado // 3) Resultado
}

let promedio=0.0
let notas = [5,4,7,9,2,3,10] //Fila de Excel, Columna de Excel

promedio = calcular_promedio_lista(notas)

console.log(promedio)
console.log(notas)

console.log('Primera Nota',notas[0]) //Celda de Excel
console.log('Tercera Nota',notas[2]) //Celda de Excel

notas[0]=8 //Celda de Excel
console.log('Nueva Primera Nota',notas[0]) //Celda de Excel