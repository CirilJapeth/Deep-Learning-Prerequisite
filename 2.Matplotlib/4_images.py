import numpy as np 
import matplotlib.pyplot as plt 
import os 
from PIL import Image
#Getting the image
os.system("wget https://stat.overdrive.in/wp-content/odgallery/2020/06/57263_2020_Mercedes_Benz_GLS.jpg")
os.system("mv 57263_2020_Mercedes_Benz_GLS.jpg car.jpg")
os.system("clear")

im = Image.open('car.jpg')
array = np.array(im)
#print(array.shape) shows res, color

#basic plot
plt.imshow(array)
plt.show()

#convert it into grey by taking mean across color channels

grey = array.mean(axis =2)
plt.imshow(grey)
plt.show()
print(grey.shape)
# This did not create a b/w rather a heat map becuase it gives a number between 0 and 255 and matplotlib decides which color to use
#hence, we use cmap argument to select our color

plt.imshow(grey,cmap = 'gray')
plt.show()

os.system("rm car.jpg")
