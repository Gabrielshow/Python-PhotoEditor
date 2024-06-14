from PIL import Image, ImageEnhance, ImageFilter
import os
from pathlib import Path
from sys import argv

base_path = Path(argv[1]) if len(argv) > 1 else Path.cwd()

input_dir = base_path/'imgs'
output_dir = base_path/'editedImgs'
output_dir.mkdir(parents=True, exist_ok=True)
# fullpath = base_path + path
# print(fullpath)

try:
    if not os.path.isdir(input_dir):
        print(f"Error: '{input_dir}' is not a valid directory.")
    elif not os.listdir(input_dir):
        print(f"Error: '{input_dir}' is empty or does not contain any image files.")
    else:
        # Create the output directory if it doesn't exist
#         output_dir = f"{base_path + pathOut}"
#         os.makedirs(output_dir, exist_ok=True)
        for filename in os.listdir(input_dir):
            img_path = input_dir/filename
            with Image.open(img_path) as img:
                edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
    
                factor = 1.5
                enhancer = ImageEnhance.Contrast(edit)
                edit = enhancer.enhance(factor)
    
                clean_name = os.path.splitext(filename)[0]
    
                output_file = output_dir/f"{clean_name}_edited.jpg"
                print(f"Saving edited image to: {output_file}")
                edit.save(output_file)
except Exception as e:
    print(f"Error: {e}")
    
    