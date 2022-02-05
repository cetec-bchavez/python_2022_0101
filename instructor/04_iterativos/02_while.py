print('------------------ WHILE ECUASION -----------------')

x=5
y=0

while x <= 50 :
    y = 5*x + 30

    print(f'x={x},  y={y}')

    x+=5 # Ciclo Infinito

print('------------------ WHILE ECUASION (continue) -----------------')

x=5

while x <= 50 :

    if x==30 :
        x+=5
        continue

    y = 5*x + 30

    print(f'x={x},  y={y}')
    
    x+=5

print('------------------ WHILE ECUASION (break) -----------------')

x=5

while x <= 50 :

    if x==30 :
        break

    y = 5*x + 30

    print(f'x={x},  y={y}')
    
    x+=5