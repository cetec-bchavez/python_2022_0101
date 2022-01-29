print("CONDICIONAL SIMPLE")
venta = 4000
comision = 0.0
totalVenta = 0

if venta >= 3000 :              
    comision = 0.1
else :
    comision = 0.01

totalVenta = int(venta) + int(venta*comision)

print(f"total venta= {totalVenta} comision= {comision} ")


print("---Condicional ternario(para IF Else con UNA SOLA asignacion)---")

comision=0.1 if venta>=3000 else 0.01

totalVenta = int(venta) + int(venta*comision)
print(f"total venta= {totalVenta} comision= {comision} ")

print("---Ejercicio  IF  ELIF---") #para evitar usar muchos if else

venta= 3000

if venta>7500:
    comision=0.04 
elif venta>7500:
    comision=0.03
elif venta>2500:
    comision=0.02
else:
    comision=0.01

totalVenta = int(venta) + int(venta*comision)
print(f"total venta= {totalVenta} comision= {comision} ")





#   py.exe .\alumno2\03_condicionales\01_condicionales.py
