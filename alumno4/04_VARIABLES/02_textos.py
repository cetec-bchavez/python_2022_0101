
from posixpath import split


nombre_mayusculas = ''
nombre = "Eduardo Clavijo"
nombre_mayusculas = nombre.upper()

print(nombre_mayusculas)

print('------------------ANOMIMO--------------')
print(nombre_mayusculas)
print(nombre.upper())

print(nombre.replace('Eduardo','Abel'))

#nombre = (nombre.replace('Eduardo','Abel'))

nombre2= 'Maria,Ana,Juan'
palabras = nombre,split('')
palabras_nombres=nombre2.split(',')

print(palabras)
print(palabras_nombres)

for palabra in palabras_nombres :
    print('Nombres =',palabra)

nombres3= 'Eduardo Clavijo,Gaby Clavijo'
palabras_nombres3=nombres3,split(',')

    
    
    
    


