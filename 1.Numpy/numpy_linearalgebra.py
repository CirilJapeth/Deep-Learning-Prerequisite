import numpy as np 

x = np.array([1,2,3])
y = np.array([4,5,6])
print(x,"\n", y)

#Different ways to get the dot product

#1
import numpy as np

x = np.array([1,2,3])
y = np.array([4,5,6])
dot_Product = 0

for i in range (3): 
  dot_Product += x[i]*y[i]
print(dot_Product)


#2
dot = 0
for i , j in zip(x,y): 
  dot += (i*j)
print("\nDot Product = ", dot)


#3
print("\nDot Product = ", sum(x*y))

#4
print("\nDot Product = ", np.dot(x,y))


#calculating The angle between two vectors: 

# dot product = magnitue * magnitude * cos of angle


#2
cosangle = np.dot(x,y) / (np.linalg.norm(x) * np.linalg.norm(y))
print("\nangle =",np.arccos(cosangle))

#Creating an ideneity Matrix
print(np.eye((3)))
