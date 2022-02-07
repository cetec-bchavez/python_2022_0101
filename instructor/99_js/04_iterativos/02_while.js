console.log('------------------ WHILE ECUASION -----------------')

let x=5
let y=0

while(x <= 50) {
    y = 5*x + 30

    console.log(`x=${x},  y=${y}`)

    x+=5 // Ciclo Infinito
}

console.log('------------------ WHILE ECUASION (continue) -----------------')

x=5

while(x <= 50) {

    if(x==30) {
        x+=5
        continue
    }

    y = 5*x + 30

    console.log(`x=${x},  y=${y}`)
    
    x+=5
}

console.log('------------------ WHILE ECUASION (break) -----------------')

x=5

while(x <= 50) {

    if(x==30)
        break

    y = 5*x + 30

    console.log(`x=${x},  y=${y}`)
    
    x+=5
}