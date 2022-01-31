console.log('---------------------- SIMPLE -------------------')

let venta=4000
let comision=0.0
let total_venta=0.
//Si venta > 3000 , comision 10%
//Caso contrario 1%


if (venta>=3000) 
    comision=0.10
else 
    comision=0.01

total_venta = venta + (venta*comision)

console.log('Total Venta=',total_venta,', Comision=',comision)

// Accion + parametro/valor

// cd carpeta
// python archivo.py

console.log('---------------------- TERNARIO (If Else Simple + 1 Asignacion)-------------------')

comision = venta>=3000? 0.1 : 0.01

total_venta = venta + (venta*comision)

console.log('Total Venta=',total_venta,', Comision=',comision)

console.log('---------------------- If Elif -------------------')
/*
* Venta 4 intervalos (0-2500,2501-5000,5001-7500,7501-10000)
* Comision 4 (0.01,0.02,0.03,0.04)

* REQUISITO
* Orden (Mayor a Menor o Menor a Mayor)
*/

venta=1000


if (venta>7500) 
    comision=0.04

else if (venta>5000)
    comision=0.03

else if (venta>2500)
    comision=0.02
    
else
    comision=0.01

/*
if venta>7500 :
    comision=0.04

else:
    if venta>5000:
        comision=0.03
    else:
        if venta>2500:
            comision=0.02
        else:
            comision=0.01
*/

total_venta = venta + (venta*comision)

console.log('Total Venta=',total_venta,', Comision=',comision)