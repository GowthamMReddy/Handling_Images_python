#!/usr/bin/env python3
from PIL import Image

import os

source_folder = "."  
destination_folder = "/opt/icons"  


for filename in os.listdir(source_folder):
    if filename.endswith(".tiff"):
      
        image = Image.open(os.path.join(source_folder, filename))

        
        image = image.rotate(90)

       
        resized_image = image.resize((128, 128), Image.ANTIALIAS)

        new_filename = os.path.splitext(filename)[0] + ".jpeg"  
        destination_path = os.path.join(destination_folder, new_filename)
        resized_image.save(destination_path, format="JPEG")

        print(f"Converted {filename} to {new_filename} and saved to {destination_folder}")
