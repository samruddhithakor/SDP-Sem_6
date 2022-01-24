
import PIL
from PIL import Image

mywidth = 2200

img = Image.open(r'C:\Users\Dhruv j Patel\Desktop\sdp_project\image1.jpg')
wpercent = (mywidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
img.save(r'C:\Users\Dhruv j Patel\Desktop\sdp_project\resized2.jpg')