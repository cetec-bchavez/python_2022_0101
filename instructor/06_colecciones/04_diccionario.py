provincias={'02':'Pichincha',
            '04':'Guayas',
            '06':'Carchi'
            }

print('---------------- DICCIONARIO ----------------')

print('Crear Provincias -> ',provincias)

print('Primera Provincia -> ',provincias.get('02'))

provincias['02']='PICHINCHA'
print('Cambio Primera Provincia -> ',provincias.get('02'))

provincias['08']='Azuay'
provincias['08']='Azuay'
provincias['0802']='Azuay'
print('Nueva Provincia -> ',provincias)

print('Numero Provincias',len(provincias))

del(provincias['04'])
print('Quitar Provincia')
print('Numero Provincias',len(provincias))
print('Provincias Final -> ',provincias)

print('Recorrer Provincias')
for codigo,provincia in provincias.items() :
    print('Provincia =', codigo,provincia)