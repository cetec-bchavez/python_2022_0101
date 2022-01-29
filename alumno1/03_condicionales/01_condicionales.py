print('-----Simples------')

venta=4000
comision=0.0
total_venta=0.
#si venta > 3000, comision 10%
#caso contrario 1%

if venta>=3000: 
    comision=0.10
else :  
    comision=0.01

total_venta = venta + (venta*comision)

print('Total venta:', total_venta,', Comision:', comision)


print('------TERMARIO (IF ESLE y cuando exista una asigacion)------')

comision = 0.1 if venta>=3000 else 0.01

total_venta = venta + (venta*comision)

print('Total venta=', total_venta, 'Comision=', comision)

print('------If Elif -------')
""""
* 4 intervalos (0= 2500, 2501=5000, 5000=7500, 7501=10000)
* comision 4 (0.01, 0.02, 0.03, 0.04)

* Orden (Mayor a Menor o Menos a Mayor)
"""

venta= 0

#venta = input('Ingrese ventas:')

if venta>=7500: 
    comision=0.04
elif venta>=5000:  
    comision=0.03
elif venta>=2500:   
    comision=0.02
else :  
    comision= 0.01

total_venta = venta + (venta*comision)

print('Total Venta=', total_venta, 'Comision=', comision)