#edge detection using scipy.signal

from PIL import Image
import numpy as np
import scipy.signal as sg
import matplotlib.pyplot as plt
import os

os.system("wget https://stat.overdrive.in/wp-content/odgallery/2020/06/57263_2020_Mercedes_Benz_GLS.jpg")
os.system("mv 57263_2020_Mercedes_Benz_GLS.jpg car.jpg")
os.system("clear")

im = Image.open('car.jpg')
img = np.array(Image.open('car.jpg'))
img = img[:, :, 0]
img = img.astype(np.int16)

edge = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
results = sg.convolve(img, edge, mode='same')
results[results > 255] = 255
results[results < 0] = 0

results = results.astype(np.uint8)
plt.imshow(results,cmap='gray')
plt.show()

os.system("rm car.jpg")