import matplotlib.pyplot as plt
import numpy as np

xs1= np.array([0,10])
ys1= np.array([0,200])

#plt.plot(xs1,ys1)
#plt.plot(xs1,ys1,'o')



ys1= np.array([100,200,300])
#plt.plot(ys1)
#plt.plot(ys1,marker='o')

titulos=["Teclados","Mouses","Monitores"]

plt.pie(ys1,labels=titulos)
plt.legend(title="Ventas de Productos")
plt.show()