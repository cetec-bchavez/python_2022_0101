provincias=['Pichincha','Guayas']
print('Provincias -> ',provincias)

print('Primera provincia -> ', provincias[0])

provincias[0]='Pichincha'
print('cambio primera provincia -> ',provincias[0])

provincias.append('Azuay')
print('Nueva provincia -> ',provincias)

print('Numero provincias',len(provincias))

provincias.remove('Guayas')
print('quitar provincia')
print('numero provincias',len(provincias))
print('Provincia Final -> ', provincias[0])
