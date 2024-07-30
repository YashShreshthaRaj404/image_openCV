import cv2
from matplotlib import pyplot as plt 
import numpy as np 
img = cv2.imread('D:\Buddy.jpg')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('My Dog-Buddy')
plt.axis('off')
plt.show()
