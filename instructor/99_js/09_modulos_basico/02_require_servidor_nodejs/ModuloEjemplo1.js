function saludar(nombre){
    console.log('Buenos Dias',nombre)
}

let persona1=new Map([
    ["nombre","Ana"],
    ["apellido","Perez"],
    ["edad",25]
])

module.exports = {
    saludar: saludar,
    persona1: persona1
}

//module.exports.saludar = saludar
//module.exports.persona1 = persona1