nombre_mayus = ''
nombre = 'Centro de Capacitacion'

nombre_mayus = nombre.upper()

print(nombre_mayus)


print('--------------------- ANONIMAMENTE -------------------------')

nombre = 'Centro de Capacitacion'

print('Centro de Capacitacion'.upper())
print(nombre.upper())

print('--------------------- OTROS -------------------------')

print(nombre.replace('Centro','Universidad'))
#nombre = nombre.replace('Centro','Universidad')
print(nombre)

nombre2='Maria,Ana,Veronica,Luizana,Luis,Carlos'

palabras = nombre.split(' ')
palabras_nombres = nombre2.split(',')

print(palabras)
print(palabras_nombres)

for palabra in palabras_nombres :
    print('Mujer Actual = ',palabra)    


print('--------------------- Ejercicio 1 Pregunta -------------------------')

for palabra in palabras_nombres :
    if palabra != 'Luis' and palabra != 'Carlos' :
        print('Mujer Actual = ',palabra)
    else :
        print('Hombre Actual = ',palabra)

print('--------------------- Ejercicio 2 Nombre Completo -------------------------')

nombres3='Maria Perez,Ana Sanchez,Veronica Gutierrez,Luizana Perez,Luis Perez'
palabras_nombres3 = nombres3.split(',')

for palabra in palabras_nombres3 :
    print('Mujer Completo = ',palabra)
    print('Mujer Nombre Simple = ',palabra.split(' ')[0])
    print('Mujer Apellido Simple = ',palabra.split(' ')[1])
    """
    nombre_simple = palabra.split(' ')[0]
    apellid_simple = palabra.split(' ')[1]

    print('Mujer Nombre Simple = ',nombre_simple)
    print('Mujer Apellido Simple = ',apellid_simple)
    """