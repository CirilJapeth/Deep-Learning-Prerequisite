import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm
from scipy.signal import convolve2d
from PIL import Image
import os

os.system("wget https://stat.overdrive.in/wp-content/odgallery/2020/06/57263_2020_Mercedes_Benz_GLS.jpg")
os.system("mv 57263_2020_Mercedes_Benz_GLS.jpg car.jpg")
os.system("clear")

im = Image.open('car.jpg')

#convert into greyscale
gray = np.mean(im, axis = 2)

#apply 2d gausian filter
x = np.linspace(-6,6,50)
fx = norm.pdf(x,loc=0,scale=1)
filt = np.outer(fx,fx)
# plt.imshow(filt,cmap='gray')
out=convolve2d(gray,filt)

# Plotting both images side by side
plt.subplot(1,2,1)
plt.imshow(gray,cmap = 'gray')
plt.subplot(1,2,2)
plt.imshow(out,cmap='gray')
plt.show()


#cleaning up
os.system("rm car.jpg")