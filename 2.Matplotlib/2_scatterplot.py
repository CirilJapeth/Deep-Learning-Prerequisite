import numpy as np
import matplotlib.pyplot as plt

#getting some random numbers 
#x = np.array(np.random.randint(0,10,size = (100,2)))
x = np.random.randn(200,2)
#To center this at 3, we add 3 too all elements up to 50
x[:50] += 3
#Crating 1d array for color
y = np.zeros(200)
y[:50] = 1
plt.scatter(x[:,0], x[:,1],c =y)
plt.show()
