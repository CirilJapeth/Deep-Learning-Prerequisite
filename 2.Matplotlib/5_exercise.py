#creating XOR gate like functionality using python and then plotting them


# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

# Make 1D arrays for x and y axes and spread them around -1 and 1
x1 = (np.random.random(2000)-0.5)*2
x2 = (np.random.random(2000)-0.5)*2

# Make an array for color picking
Y = np.zeros(2000)

for e in range(len(Y)):
  if (x1[e] <= 0 and x2[e] > 0) or (x1[e] > 0 and x2[e] <= 0):
    Y[e] = 1

# Plot it all
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Matplotlib Exercise')
plt.scatter(x1,x2,c=Y)
plt.show()
