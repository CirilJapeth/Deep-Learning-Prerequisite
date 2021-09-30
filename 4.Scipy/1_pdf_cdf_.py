#Calculating Probability Density Function and Cumulative distribution Function

import numpy as np 
import matplotlib.pyplot as plt
from scipy.stats import norm 

x = np.linspace(-6,6,1000)

fx = norm.pdf(x, loc=0,scale =1)
# loc: mean scale: sd, use cdf instad of pdf for cdf and logpdf, logcdf

plt.plot(x,fx)
plt.show()
