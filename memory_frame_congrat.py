#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Tkinter as tk

class FrameCongrat:
    frames = None

    def __init__(self, frames, control):
        self.frames = frames
        self.frames[1].pack_forget()
        tk.Label(self.frames[2], \
              text="Congratulations!", \
              font="Helvetica 14  bold").pack(fill=tk.BOTH, expand=1, padx=5, pady=5)
        tk.Label(self.frames[2], \
              text="You've discovered", \
              font="Helvetica 12").pack(fill=tk.BOTH, expand=1, padx=5, pady=5)
        tk.Label(self.frames[2], \
              text="all hidden pairs!", \
              font="Helvetica 12").pack(fill=tk.BOTH, expand=1, padx=5, pady=5)
        tk.Label(self.frames[2], \
              text="Solved %dx%d memory table" % (control.n, control.n), \
              font="Helvetica 12").pack(fill=tk.BOTH, expand=1, padx=5, pady=5)
        tk.Label(self.frames[2], \
              text="using %d clicks." % control.clicks , \
              font="Helvetica 12").pack(fill=tk.BOTH, expand=1, padx=5, pady=5)
         
        self.frames[2].pack(fill=tk.BOTH, expand=1, padx=5, pady=5)
        
