from PIL import Image
import numpy as np
from numpy import asarray
img = Image.open('newimage.jpg')
numpydata = asarray(img)
print(img.format)
print(img.size)
print(img.mode)
# print(numpydata)
data=""
with open("newimage.txt",'a') as f:
  for pixel in np.nditer(numpydata):
    data+=f"{pixel}"
  f.write(str(data))

# formula to calculate file size after calculation
# Image file size = resolution * bit depth