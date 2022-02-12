try { 
    let x=100
    let y=-999 //0,-999
    let r= x/ y

    if(y==-999) {
        throw new Exception("Numero negativo")
    }

    console.log("Resultado",r)

} catch(e) {

    console.log('Error Generado, consulte con Administrador')
    //Codigo generar archivo text
}
finally{
    console.log('Siempre Ejecuta')
    //Cerrar Archivos, conexiones a BD
}