#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk
from memory_frame_memory import FrameMemory 

class FrameNewGame:
    control = None
    frames = None
    root = None
    
    def __init__(self, root, frames, control):
        self.control = control
        self.frames = frames
        self.root = root

        tk.Button(self.frames[0], text=" Memory 4 x 4", \
               command=lambda: self.newGame(4)).pack(fill=tk.X, expand=1)
        tk.Button(self.frames[0], text=" Memory 6 x 6", \
               command=lambda: self.newGame(6)).pack(fill=tk.X, expand=1)
        tk.Button(self.frames[0], text=" Memory 8 x 8", \
               command=lambda: self.newGame(8)).pack(fill=tk.X, expand=1)
        tk.Button(self.frames[0], text=" Memory 10 x 10", \
               command=lambda: self.newGame(10)).pack(fill=tk.X, expand=1)

    def newGame(self, value):
        if value == 10:
            self.root.geometry("531x661+20+20")
        if value == 8:
            self.root.geometry("425x529+20+20")
        if value == 6:
            self.root.geometry("320x398+20+20")
        if value == 4:
            self.root.geometry("214x265+20+20")
            
        self.control.newGame(value)
        
        FrameMemory(self.frames, self.control).initTable()

