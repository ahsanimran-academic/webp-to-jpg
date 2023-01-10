#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:35:59 2022

@author: faceengine
"""

# from PIL import Image

# # Open the WebP image
# image = Image.open("image.webp")

# # Save the image in JPG format
# image.save("image.jpg")

# example
# from PIL import Image
# image = Image.open("/home/faceengine/FaceEngine/webp_images/jason_momoa_04.webp")
# image.save("/home/faceengine/FaceEngine/webp_images/jason_momoa_04.webp".replace(".webp", ".jpg"))

import glob
import os
from PIL import Image


person_names = glob.glob("webp_images/*")
# name_list = []
for name in person_names:
    only_name = name.split("/")[-1]
    # name_list.append(only_name)
    
    for root, dirs, files in os.walk(name):
        # print(files)
       
        for file in files:
            
            # img = Image.open(file)
            # print(img.format)
            # print(file)
            only_format = file.split(".")[-1]
            
            if only_format == "webp":
                string_ = f"/home/faceengine/FaceEngine/webp_images/{only_name}/"+file
                img = Image.open(string_)
                 
                img.save(string_.replace(".webp", ".jpg"))
                
for name in person_names:
    only_name = name.split("/")[-1]
    # name_list.append(only_name)
    
    for root, dirs, files in os.walk(name):
        # print(files)
       
        for file in files:
            
            # img = Image.open(file)
            # print(img.format)
            # print(file)
            only_format = file.split(".")[-1]
            
            if only_format == "webp":
                string_ = f"/home/faceengine/FaceEngine/webp_images/{only_name}/"+file
                # img = Image.open(string_)
                 
                # img.save(string_.replace(".webp", ".jpg"))
                os.remove(string_)
                