import PIL
from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilename()
img = PIL.Image.open(file_path) 
myHeight, mywidth = img.size
img = img.resize((myHeight, mywidth), PIL.Image.ANTIALIAS)
save_path = asksaveasfilename()

img.save(save_path+"_compressed.JPG")