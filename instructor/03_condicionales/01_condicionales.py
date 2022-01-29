print('---------------------- SIMPLE -------------------')

venta=4000
comision=0.0
total_venta=0.
#Si venta > 3000 , comision 10%
#Caso contrario 1%


if venta>=3000 :
    comision=0.10
else :
    comision=0.01

total_venta = venta + (venta*comision)

print('Total Venta=',total_venta,', Comision=',comision)

# Accion + parametro/valor

# cd carpeta
# python archivo.py

print('---------------------- TERNARIO (If Else Simple + 1 Asignacion)-------------------')

comision = 0.1 if venta>=3000 else 0.01

total_venta = venta + (venta*comision)

print('Total Venta=',total_venta,', Comision=',comision)

print('---------------------- If Elif -------------------')
"""
* Venta 4 intervalos (0-2500,2501-5000,5001-7500,7501-10000)
* Comision 4 (0.01,0.02,0.03,0.04)

* REQUISITO
* Orden (Mayor a Menor o Menor a Mayor)
"""

venta=1000


if venta>7500 :
    comision=0.04

elif venta>5000:
    comision=0.03

elif venta>2500:
    comision=0.02

else :
    comision=0.01

"""
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
"""

total_venta = venta + (venta*comision)

print('Total Venta=',total_venta,', Comision=',comision)