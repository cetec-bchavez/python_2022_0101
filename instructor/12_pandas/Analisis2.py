import pandas as pd
import matplotlib.pyplot as plt

print('--------------- DATOS --------------')

datos1= pd.read_csv('D:\\2022\\python\\01\\data\\data.csv')

#print(datos1.to_string())

#print(datos1.info())
#print(datos1.head(5))
#print(datos1.tail(5))

#datos1["Pulse"].plot()
#plt.show()

datos1.plot(kind='scatter',x='Duration',y='Calories')
plt.show()