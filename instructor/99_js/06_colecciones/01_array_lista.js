let provincias=['Pichincha','Guayas']
console.log('Crear Provincias -> ',provincias)

console.log('Primera Provincia -> ',provincias[0])

provincias[0]='PICHINCHA'
console.log('Cambio Primera Provincia -> ',provincias[0])

provincias.push('Azuay')
provincias.push('Azuay')
console.log('Nueva Provincia -> ',provincias)

console.log('Numero Provincias',provincias.length)

provincias.pop('Guayas')
console.log('Quitar Provincia')
console.log('Numero Provincias',provincias.length)
console.log('Provincias Final -> ',provincias)

console.log('Recorrer Provincias')
for(provincia of provincias)
    console.log('Provincia =', provincia)