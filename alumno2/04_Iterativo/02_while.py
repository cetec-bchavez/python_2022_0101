print("---Ecuacion de While---")
y=0
x=5
while x<=50:
    print(x)
    print(f"x= {x}, y = {y}")
    x= x+5

print("---While Ecuacion---")

#hacer que no se imprima x=30
x=5
while x<=50:

    if x==30:
        x=x+5
        continue

    y = 5 * x + 30 
    print(f"x= {x}, y = {y}")
    x= x+5

print("---While Ecuacion(Break)---")

#hacer que no se imprima x=30
x=5
while x<=50:

    if x==30:
        break

    y = 5 * x + 30 
    print(f"x= {x}, y = {y}")
    x= x+5

