let provincias=new Set(['Pichincha','Guayas'])
console.log('Crear Provincias -> ',provincias)

//console.log('Primera Provincia -> ',provincias[0])

//provincias[0]='PICHINCHA'

/*
for provincia in provincias :
    if provincia=='Pichincha':
        console.log('Cambio Nombre')
        provincia='PICHINCHA1'    
*/

//console.log('Cambio Primera Provincia -> ',provincias[0])

provincias.add('Azuay')
provincias.add('Azuay')
provincias.add('Azuay')
console.log('Nueva Provincia -> ',provincias)

console.log('Numero Provincias',provincias.lenght)

provincias.delete('Guayas')
console.log('Quitar Provincia')
console.log('Numero Provincias',provincias.lenght)
console.log('Provincias Final -> ',provincias)

console.log('Recorrer Provincias')
for(provincia of provincias)
    console.log('Provincia =', provincia)