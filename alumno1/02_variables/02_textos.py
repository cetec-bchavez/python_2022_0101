from dataclasses import replace

nombre = 'cec'
nombre_mayus = nombre.upper()
print(nombre_mayus)


print('--------------ANONIMAMENTE----------------')
print('cec'.upper())

print('-----OTROS-----')
nombre = 'cec'
print(nombre.replace('cec', 'cetec'))
#nombre = nombre.replace('centro', 'universidad')
print(nombre)

nombre2 = ('Maria, Ana, Juana')
palabras = nombre.split(' ')
palabras_nombre = nombre2.split(',')
print(palabras)
print(palabras_nombre)

for palabra in palabras_nombre :       
    print('palabra actual - ',palabra)

print('---------Ejercicio Pregunta-----------')
nombre3 = ('Ana Saes,Juana Saes,Jose Delgado')
palabras_nombres3 = nombre3.split(',')

for palabra in palabras_nombres3 :  
    print('Mujer completo -', palabra) 
    print('Mujer nombre simple -', palabra.split(' ')[0])
    print('Mujer apellido simple -', palabra.split(' ')[1])

print('------ Tarea ------')

nombre4 = ('Jhoselyn Llano,Miranda Lopez,Carlos Sadness,Alexander Delgado')
palabras_nombre4 = nombre4.split(',')

for palabra in palabras_nombre4 :   
    print('Nombres completos= ',palabra)
