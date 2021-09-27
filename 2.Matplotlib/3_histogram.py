import numpy as np
import matplotlib.pyplot as plt 

x = np.random.randn(10000)
#plt.hist(x)
#Get more bars with bins argument
plt.hist(x,bins = 50)
plt.show() 