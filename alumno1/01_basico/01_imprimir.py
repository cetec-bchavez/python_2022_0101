
#Mi primera ejecucion
print('Python Ejecutandose')

#Variables
# nombre = valor 
nombre_completo= 'Pancho Villa'
edad = 20

print(type(nombre_completo))
print(type(edad))

#clasico (texto + variables)
print('nombre: '+nombre_completo+', edad: '+str(edad))

#concatenar Texto + Variables con comas
print('Nombre: ',nombre_completo, ' edad: '+str(edad))

#concatenar Texto + Variables con formato rapido
print(f'Nombre: {nombre_completo}, edad: {edad} ')

#concatenar Texto + Variables con formato general
mensaje = 'Nombre: {0}, edad: {1}'
print(mensaje.format(nombre_completo,edad))

# nombre: tipo = valor
#futuro mas profesional
"""
nombre_completo2:str 'panchito v'
edad:int '20'
"""