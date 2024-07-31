import cv2
from matplotlib import pyplot as plt 
import numpy as np
image = cv2.imread('D:\Panda.jpg')
height, width, channels = image.shape
print("Panda")
print("Height:", height)
print("Width:", width )
print("No. of channels:", channels)
