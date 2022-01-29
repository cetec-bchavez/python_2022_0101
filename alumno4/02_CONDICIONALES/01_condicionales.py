venta = 5000
comision=0.0
total_venta=0

#si venta > 3000, comision 10%

if venta >=3000 :
    comision=0.10
else :
    comision=0.01

total_venta=venta+(venta*comision)  
print('Total Venta =',total_venta,', Comision = ',comision)
      