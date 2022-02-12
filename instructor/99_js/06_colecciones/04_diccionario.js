let provincias=new Map([
            ['02','Pichincha'],
            ['04','Guayas'],
            ['06','Carchi']
            ])

console.log('---------------- DICCIONARIO ----------------')

console.log('Crear Provincias -> ',provincias)

console.log('Primera Provincia -> ',provincias.get('02'))

provincias.set('02','PICHINCHA')
console.log('Cambio Primera Provincia -> ',provincias.get('02'))

provincias.set('08','Azuay')
provincias.set('08','Azuay')
console.log('Nueva Provincia -> ',provincias)

console.log('Numero Provincias',provincias.size)

delete provincias.delete('04')
console.log('Quitar Provincia')
console.log('Numero Provincias',provincias.size)
console.log('Provincias Final -> ',provincias)

console.log('Recorrer Provincias')
for(let [codigo,provincia] of provincias.entries()) 
    console.log('Provincia =', codigo,provincia)