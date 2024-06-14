from PIL import Image, ImageEnhance, ImageFilter
import os
from sys import argv

base_path = argv[1]
path = '\imgs'
pathOut = '\editedImgs'
fullpath = base_path + path
print(fullpath)

try:
    if not os.path.isdir(fullpath):
        print(f"Error: '{fullpath}' is not a valid directory.")
    elif not os.listdir(fullpath):
        print(f"Error: '{fullpath}' is empty or does not contain any image files.")
    else:
        # Create the output directory if it doesn't exist
        output_dir = f"{base_path + pathOut}"
        os.makedirs(output_dir, exist_ok=True)
        for filename in os.listdir(fullpath):
            img = Image.open(f"{base_path + path}\{filename}")
    
            edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
    
            factor = 1.5
            enhancer = ImageEnhance.Contrast(edit)
            edit = enhancer.enhance(factor)
    
            clean_name = os.path.splitext(filename)[0]
    
            output_file = f"{base_path + pathOut}\{clean_name}_edited.jpg"
            print(f"Saving edited image to: {output_file}")
            edit.save(output_file)
except Exception as e:
    print(f"Error: {e}")
    
    