let provincias={'02':'Pichincha',
            '04':'Guayas',
            '06':'Carchi'
            }

console.log('---------------- DICCIONARIO ----------------')

console.log('Crear Provincias -> ',provincias)

console.log('Primera Provincia -> ',provincias.get('02'))

provincias['02']='PICHINCHA'
console.log('Cambio Primera Provincia -> ',provincias.get('02'))

provincias['08']='Azuay'
provincias['08']='Azuay'
provincias['0802']='Azuay'
console.log('Nueva Provincia -> ',provincias)

console.log('Numero Provincias',len(provincias))

del(provincias['04'])
console.log('Quitar Provincia')
console.log('Numero Provincias',len(provincias))
console.log('Provincias Final -> ',provincias)

console.log('Recorrer Provincias')
for(codigo,provincia of provincias.items()) 
    console.log('Provincia =', codigo,provincia)