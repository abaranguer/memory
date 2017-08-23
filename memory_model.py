#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class MemoryModel:
    table = None
    
    def initTable(self, n):
        self.table = [-1 for i in range(0, n * n)]
        usedCards = []
        for i in range(0, n * n / 2):
            while True:
                while True:
                    hero = random.randint(0, 49)
                    if not hero in usedCards:
                        break
                pos1 = random.randint(0, n * n - 1)
                pos2 = random.randint(0, n * n - 1)
                if (self.table[pos1] == -1) and \
                   (self.table[pos2] == -1) and \
                   (pos1 != pos2):
                    self.table[pos1] = hero
                    self.table[pos2] = hero
                    usedCards.append(hero)
                    break;
