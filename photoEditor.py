from PIL import Image, ImageEnhance, ImageFilter
import os
from sys import argv

base_path = argv[1]
path = '\imgs'
pathOut = '\editedImgs'
fullpath = base_path + path
print(fullpath)

try:
    for filename in os.listdir(fullpath):
        img = Image.open(f"{base_path + path}\{filename}")
    
        edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
    
        factor = 1.5
        enhancer = ImageEnhancer.Contrast(edit)
        edit = enhancer.enhance(factor)
    
        clean_name = os.path.splitext(filename)[0]
    
        edit.save(f"{base_path + pathOut}\{clean_name}_edited.jpg")
except:
    print("File not found, Check whether there is an image in that directory")
    
    