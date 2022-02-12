let nombre_mayus = ''
let nombre = 'Centro de Capacitacion'

nombre_mayus = nombre.toUpperCase()

console.log(nombre_mayus)


console.log('--------------------- ANONIMAMENTE -------------------------')

nombre = 'Centro de Capacitacion'

console.log('Centro de Capacitacion'.toUpperCase())
console.log(nombre.toUpperCase())

console.log('--------------------- OTROS -------------------------')

console.log(nombre.replace('Centro','Universidad'))
//nombre = nombre.replace('Centro','Universidad')
console.log(nombre)

let nombre2='Maria,Ana,Veronica,Luizana,Luis,Carlos'

let palabras = nombre.split(' ')
let palabras_nombres = nombre2.split(',')

console.log(palabras)
console.log(palabras_nombres)

for(palabra of palabras_nombres) 
    console.log('Mujer Actual = ',palabra)    


console.log('--------------------- Ejercicio 1 Pregunta -------------------------')

for(palabra in palabras_nombres) {
    if(palabra != 'Luis' && palabra != 'Carlos')
        console.log('Mujer Actual = ',palabra)
    else
        console.log('Hombre Actual = ',palabra)
}

console.log('--------------------- Ejercicio 2 Nombre Completo -------------------------')

nombres3='Maria Perez,Ana Sanchez,Veronica Gutierrez,Luizana Perez,Luis Perez'
palabras_nombres3 = nombres3.split(',')

for(palabra of palabras_nombres3) {
    console.log('Mujer Completo = ',palabra)
    console.log('Mujer Nombre Simple = ',palabra.split(' ')[0])
    console.log('Mujer Apellido Simple = ',palabra.split(' ')[1])
    /*
    nombre_simple = palabra.split(' ')[0]
    apellid_simple = palabra.split(' ')[1]

    console.log('Mujer Nombre Simple = ',nombre_simple)
    console.log('Mujer Apellido Simple = ',apellid_simple)
    */
}