import numpy as np
from datetime import datetime
import os



def get_rand_matrix(n):
  return(np.array(np.random.randint(0,1000,size = (n,n))))

def numpy_matrix_multipication(a,b):
  return a.dot(b)

def normal_matrix_multiplication(a,b,n):
  temp =0
  for i in range(0,6):
    for j in range(0,6):
      for k in range(0,6):
        temp += a[i,k] * b[k,j]
      c[i,j] = temp
      temp = 0 
  return c


n = 100
test = 100000
c = np.zeros((n,n))
t0 = datetime.now()
for i in range(test): 
  a = get_rand_matrix(n)
  b = get_rand_matrix(n)
  prod = numpy_matrix_multipication(a,b)
time_fast = datetime.now() - t0

print("Numpy finished in ", time_fast)


t0 = datetime.now()
for i in range(test): 
  a = get_rand_matrix(n)
  b = get_rand_matrix(n)
  prod = normal_matrix_multiplication(a,b,n)
time_slow = datetime.now() - t0
print("Normal multiplication took: ", time_slow)
print("Numpy was %.2f times faster" %(time_slow/time_fast))