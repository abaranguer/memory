#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
from PIL import Image, ImageTk


# 450 293
xdim = 45
ydim = int(293.0 / 5.0)
cropDimensions= (xdim, ydim)

images = []

imageFace = Image.open("marvel-heros-villains-reduced.3.jpg")
imageHide = Image.open("diamond-shaped-texture-background.jpg")
       
for i in range(0, 50):
    y = i / 10
    x = i % 10
    x1 = x * xdim 
    x2 = x1 + xdim
    y1 = int(y * (293.0 / 5.0))
    y2 = y1 + ydim
    
    images.append(imageFace.crop((x1, y1, x2, y2)))

images.append(imageHide.crop((0, 0, xdim, ydim)))

print "working!"

for i in range(0, len(images)):
    print "file %d " % i
    images[i].save("hero_%d.ppm" % i)

print "done!"
