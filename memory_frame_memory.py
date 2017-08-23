#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
from memory_model import MemoryModel
from memory_card import ImageButton

class FrameMemory:
    #controller
    control=None
    frames = None

    #widgets
    buttons = []
    n = 0
    photoImages = None

    def __init__(self, frames, control):
        self.control = control
        self.n = control.n
        self.frames = frames

        self.photoImages = []
        
        for i in range(0, 50):
            ppmFile = "images/hero_%d.ppm" % i
            self.photoImages.append(tk.PhotoImage(file=ppmFile))

        self.photoImages.append(tk.PhotoImage(file="images/hide_card.ppm"))
        
    def initTable(self):
        self.frames[0].pack_forget()

        self.buttons = []
        
        for i in range(0, self.n):
            for j in range(0, self.n):
                self.buttons.append (\
                    ImageButton(self.frames[1], \
                    self.control.model.table[i * self.n + j], \
                    i, j, \
                    self.photoImages, \
                    self.frames, \
                    self.control))

        self.control.buttons = self.buttons
        self.control.clicks = 0
        
        self.frames[1].pack(fill=tk.BOTH, expand=1)
