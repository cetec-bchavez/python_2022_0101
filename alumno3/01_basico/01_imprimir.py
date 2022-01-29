#mi primera ejecucion
"""
con las comillas podemos escribir mas de tres lineas elaborando program 
en python
2022
"""
print('Python Ejecutandose')
#variables
# nombre - valor
#nombre:tipo = valor

nombre_completo='Galo Garzon'  
edad =  40

print (type (nombre_completo))
print(type(edad))

# 1 clasico (texto + variable)
print('Nombre='+nombre_completo+'y Edad='+ str(edad))

# 2 concatenar texto + variable con cosas
print('Nombre=',nombre_completo,'y Edad=',str(edad))  

# 3 concatenar texto + variable con formato rapido

print (f'Nombre = {nombre_completo} y Edad= {edad}')

# 4 concatenar texto + variable con formato general
mensaje = 'Nombre - {0} y Edad= {1}'
print (mensaje.format (nombre_completo,edad))
print(mensaje.format("Galo Garzon",40))


#futuro / profesionales
"""
nombre_completo:str- 'Galo Garzon'  
edad = int - 40
""" 
