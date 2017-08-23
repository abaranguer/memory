#!/usr/bin/python
# -*- coding: utf-8 -*-

import gc
from Tkinter import *
from memory_controller import MemoryController
from memory_model import MemoryModel
from memory_card import ImageButton
from memory_frame_new_game import FrameNewGame


class MemoryAppWindow:
    control = None
    root = None
    buttons = []
    frames = []
    n = 0

    def __init__(self):
        self.model = MemoryModel()
        self.control = MemoryController(self.model)
        self.initializeRoot()
        self.initializeMenu()
        self.initializeFrames()
        self.initializeGame()
        self.root.mainloop()

    def initializeRoot(self):
        self.root = Tk()
        self.root.title("Memory")
        self.root.geometry("300x300+20+20")
        self.root.resizable(False, False)

    def initializeMenu(self):
        menubar = Menu(self.root)
        menubar.add_command(label="new game", command=self.newGame)
        menubar.add_command(label="quit", command=self.quitGame)
        self.root.config(menu=menubar)

    def initializeFrames(self):
        frameNewGame = Frame(self.root)
        frameMemory = Frame(self.root)
        frameCongrat = Frame(self.root)
        self.frames = [frameNewGame, frameMemory, frameCongrat]
        FrameNewGame(self.root, self.frames, self.control)
        
    def initializeGame(self):
        self.frames[0].pack(fill=BOTH, expand=1, padx=50, pady=50)

    def newGame(self):
        self.control = None
        self.buttons = []
        self.frames[0].pack_forget()
        self.frames[1].pack_forget()
        self.frames[2].pack_forget()
        self.frames = []
        self.n = 0
        self.model = MemoryModel()
        self.control = MemoryController(self.model)        
        self.initializeFrames()
        self.initializeGame()
        
    def quitGame(self):
        self.root.destroy()
        exit(0)
