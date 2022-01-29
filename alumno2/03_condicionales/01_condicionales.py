venta = 4000
comision = 0.0
totalVenta = 0

if venta >= 3000 :
    comision = 0.1
else :
    comision = 0.01

totalVenta = int(venta) + int(venta*comision)

print(f"total venta= {totalVenta} comision= {comision} ")