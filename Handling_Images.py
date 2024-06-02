#!/usr/bin/env python3

# Import image module from PIL library to handle images and OS library to handle directorys
from PIL import Image
import os

# Intialize source_folder and destination_folder for storing the respective paths of images that to be handled and saved
source_folder = "./images"  
destination_folder = "./resized_images"  

# Verify that is destination directory exist if not create
os.makedirs(destination_folder, exist_ok=True)

# Iterate over the files located in source_folder
for filename in os.listdir(source_folder):
    # Check for image files that endswith .Jpg, .png, .tiff 
    if filename.endswith(".tiff") or filename.endswith('.jpg') or filename.endswith('.png'):
        # Create complete file path of image file by joining source folder path and filenames.
        file_path = os.path.join(source_folder, filename)
        # Open Image file from source directory
        image = Image.open(file_path)
        # Rotate images in 90 degree clock wise using rotate method
        image = image.rotate(90)
        # Resize image to 420x480 using resize method
        resized_image = image.resize((420, 480))
        # Verify is image mode set to RGB if not convert image to RGB
        if resized_image.mode is not('RGB','L'):
            resized_image.convert('RGB')
        # generate new filename by adding .jpeg extension
        new_filename = os.path.splitext(filename)[0] + ".jpeg"  
        # generate destination path by joining path of destination directory and new filename
        destination_path = os.path.join(destination_folder, new_filename)
        # Save the new image to destination directory in jpeg format
        resized_image.save(destination_path, format="JPEG")
        # Print the statement
        print(f"Converted {filename} to {new_filename} and saved to {destination_folder}")
