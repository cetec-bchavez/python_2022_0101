let y=0

for(let x=5;x<=50;x+=5) {
    y = 5*x + 30

    console.log(`x=${x},  y=${y}`)
}

console.log('------------------- 2da Forma ---------------')

for(x of [5,10,15,20,25,30,35,40,45,50]) {
    y = 5*x + 30

    console.log(`x=${x},  y=${y}`)
}

