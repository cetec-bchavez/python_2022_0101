class Factura {
    //Variables Columnas, Variables Complejas
    producto=''
    cantidad=0
    precio=0.0
    total=0.0

    //Mecanico, PRIMEROS VALORES Ejm. Factura('Mouse',5.0,7.0,0.0)
    constructor(productox,cantidadx,preciox,totalx){

        this.producto=productox
        this.cantidad=cantidadx
        this.precio=preciox
        this.total=totalx
    }

    calcular_total(){
        this.total = this.cantidad * this.precio
    }
}


let facturas=[] //Hoja Calculo completa (columnas, y filas de datos)
let factura1 = new Factura('Mouse',5.0,7.0,0.0) // Fila factura1
let factura2 = new Factura('Teclado',7.0,6.0,0.0) // Fila factura2

//Columnas se cambian a Celdas
factura1.producto='Mouse Genius' // Apuntamos a una Celda (producto) de fila factura1
factura2.producto='Teclado Inx' // Apuntamos a una Celda (producto) de fila factura2

factura1.calcular_total()
factura2.calcular_total()

facturas.push(factura1)
facturas.push(factura2)

console.log('------------- Datos Factura 1 --------------')
console.log(factura1.producto,factura1.total)

console.log('------------- Datos Factura 2 --------------')
console.log(factura2.producto,factura2.total)


console.log('------------- Datos Facturas TODOS --------------')

for(let facturax of facturas) 
    console.log(facturax.producto,facturax.total)
    //console.log(facturax)