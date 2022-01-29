from re import X


x = 5
y = 0


while x <= 50 :
    
    if x == 30:
        x+=5
        #continue
        break
  
    y+=5*x+30
  
    print (f'x={x}, y={y}')
    
    x+=5

