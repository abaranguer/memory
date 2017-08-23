#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from memory_model import MemoryModel

class MemoryController:
    model = None
    buttons = None
    clicks = 0
    n = 0
    state = 0   # 0 - shows no cards
                # 1 - shows 1 card
                # 2 - shows 2 cards
                # 3 - waits 3 seconds
    card1 = -1
    cell1 = []
    card2 = -1
    cell2 = []

    def __init__(self, model):
        self.model = model
    
    def newGame(self, n):
        self.n = n
        self.clicks = 0
        self.buttons = None
        self.model.initTable(self.n)

    def isEndGame(self):
        endGame = True
        for i in range(0, self.n * self.n):
            endGame = endGame and (not self.buttons[i].hide)
    
        # true: end game
        # false: continue game
        return endGame
    
    def analyzeState(self):
        if self.state==2:
            if self.card1 == self.card2:   # pair discovered
                if self.isEndGame():
                    self.reset()
                    return "end game"
                else:
                    self.state = 0
                    self.card1 = -1
                    self.card2 = -1
                    self.cell1 = []
                    self.cell2 = []
            else:
                self.state = 3
                time.sleep(3)
                self.card1 = -1
                self.card2 = -1
                self.buttons[self.cellToIndex(self.cell1)].hide = True
                self.buttons[self.cellToIndex(self.cell2)].hide = True
                self.buttons[self.cellToIndex(self.cell1)].hideCard()
                self.buttons[self.cellToIndex(self.cell2)].hideCard()
                self.cell1 = []
                self.cell2 = []
                self.state = 0
        return "continue"
                    
    def cellToIndex(self, cell):
        return cell[0] * self.n + cell[1]

    def reset(self):
        for i in range(0, len(self.buttons)):
            self.buttons[i].reset()
