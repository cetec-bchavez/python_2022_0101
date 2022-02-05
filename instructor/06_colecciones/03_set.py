provincias={'Pichincha','Guayas'}
print('Crear Provincias -> ',provincias)

#print('Primera Provincia -> ',provincias[0])

#provincias[0]='PICHINCHA'

"""
for provincia in provincias :
    if provincia=='Pichincha':
        print('Cambio Nombre')
        provincia='PICHINCHA1'    
"""

#print('Cambio Primera Provincia -> ',provincias[0])

provincias.add('Azuay')
provincias.add('Azuay')
provincias.add('Azuay')
print('Nueva Provincia -> ',provincias)

print('Numero Provincias',len(provincias))

provincias.remove('Guayas')
print('Quitar Provincia')
print('Numero Provincias',len(provincias))
print('Provincias Final -> ',provincias)

print('Recorrer Provincias')
for provincia in provincias :
    print('Provincia =', provincia)