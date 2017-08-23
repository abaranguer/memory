#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from Tkinter import *
from memory_frame_congrat import FrameCongrat

class ImageButton:
    cell = None
    num = -1
    hide =True
    indexHide = -1
    control = None
    frames = None
    master = None
    imgButton = None
    photoImages = None
    xdim = 45
    ydim = int(293.0 / 5.0)
                            
    # num 0..49
    def __init__(self, master, num, rowButton, columnButton, photoImages, frames, control):
        self.control = control
        self.cell = [rowButton, columnButton]
        self.photoImages = photoImages
        self.frames = frames
        self.num = num
        self.indexHide = len(self.photoImages) - 1
        self.master = master
        self.imgButton = Button(self.master, image=self.photoImages[self.indexHide], \
                              height=self.ydim, width=self.xdim, \
                              command=self.flip)        
        self.imgButton.grid(row=self.cell[0], column=self.cell[1], padx=1, pady=1)

    def flip(self):
        self.control.clicks = self.control.clicks + 1
        if self.control.state == 0 and self.hide:
            self.imgButton.config(image=self.photoImages[self.num], \
                                  height=self.ydim, width=self.xdim, \
                                  command=self.flip)
            self.imgButton.update()
            
            self.hide = False
            self.control.state = 1
            self.control.card1 = self.num
            self.control.cell1 = self.cell
            if self.control.analyzeState() == "end game":
                self.congrats()
        else:
            if self.control.state == 1 and self.hide:
                self.imgButton.config(image=self.photoImages[self.num], \
                                      height=self.ydim, width=self.xdim, \
                                      command=self.flip)
                self.imgButton.update()
                
                self.hide = False
                self.control.state = 2
                self.control.card2 = self.num
                self.control.cell2 = self.cell
                if self.control.analyzeState() == "end game":
                    self.congrats()
                
    def hideCard(self):
        self.imgButton.config(image=self.photoImages[self.indexHide], \
                              height=self.ydim, width=self.xdim, \
                              command=self.flip)
        self.imgButton.update()
        self.hide = True

    def congrats(self):
        FrameCongrat(self.frames, self.control)
        
    def reset(self):
        self.master = None
        self.photoImages[0] = None
        self.photoImages[1] = None
        self.imgButton.pack_forget()
        self.imgButton.destroy()
