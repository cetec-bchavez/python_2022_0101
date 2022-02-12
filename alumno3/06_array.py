provincias=['Pichincha','Guayas']
print('Crear Provincias -> ',provincias)

print('Primera Provincia -> ',provincias[0])

provincias[0]='PICHINCHA'
print('Cambio Primera Provincia -> ',provincias[0])

provincias.append('Azuay')
print('Nueva Provincia -> ',provincias)

print('Numero Provincias',len(provincias))

provincias.remove('Guayas')
print('Quitar Provincia')
print('Numero Provincias',len(provincias))
print('Provincias Final -> ',provincias)
