let cantidad=0
let precio=0.0
let total=0.0

//1) Ingresar Datos
//2) Procesar Datos
//3) Mostrar Resultados

function ingresar_datos() {
    //global cantidad,precio,total

    cantidad = parseInt(prompt('Ingresar Cantidad: '))
    precio = parseFloat(prompt('Ingresar Precio: '))
}

function procesar_datos(){
    //global cantidad,precio,total

    total=cantidad * precio
}

function mostrar_resultados(){
    //global cantidad,precio,total
    console.log('Total=',total)
}

ingresar_datos()
procesar_datos()
mostrar_resultados()