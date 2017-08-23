#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os
import time

instructions = '''
Memory
------
Memory és el joc clàssic de recordar parelles.
Tenim un tauler de NxN (amb N 4,6 o 8) caselles. 
Cada casella es correspon amb un número.
Cada casella amaga el nom d'un objecte. Hi han 8 (al tauler de 4x4), 18 (al tauler de 6x6)  o 
32 (al tauler de 8x8) objectes diferents.
Cada objecte apareix dues vegades.
En cada torn, el jugador ha de destapar dues caselles. 
Si a ambdues caselles hi ha el mateix objecte, les caselles queden destapades.
Si no, després d'un temps de 3 segons, les caselles tornen a tapar-se
El cicle es repeteix fins que el jugador ha destapat totes les caselles
'''

class Card:
    nom = ""
    tapada = True

def initGame(n):
    cards = initCards()
    table = initTable(cards, n)
    return {"table":table, "cards":cards}
    
def initCards():
    cards = [Card() for i in range(0, 32)]
    cards[0].nom = 'Wolverine'
    cards[1].nom = 'Psylocke'    
    cards[2].nom = 'Storm'
    cards[3].nom = 'Jubilee'    
    cards[4].nom = 'X-23'
    cards[5].nom = 'Jean Grey'    
    cards[6].nom = 'Dark Fenix'
    cards[7].nom = 'Cyclops'    
    cards[8].nom = 'Gambit'
    cards[9].nom = 'Angel'    
    cards[10].nom = 'Beast'
    cards[11].nom = 'Nightcrawler'    
    cards[12].nom = 'Mystique'
    cards[13].nom = 'Professor X'    
    cards[14].nom = 'Magneto'
    cards[15].nom = 'Rogue'    
    cards[16].nom = 'Deadpool'
    cards[17].nom = 'Captain America'    
    cards[18].nom = 'Thor'
    cards[19].nom = 'Iron Man'    
    cards[20].nom = 'Spiderman'
    cards[21].nom = 'Black Widow'    
    cards[22].nom = 'Scarlet Witch'
    cards[23].nom = 'Ant Man'    
    cards[24].nom = 'Hulk'
    cards[25].nom = 'Colossus'    
    cards[26].nom = 'Venom'
    cards[27].nom = 'Doctor Strange'    
    cards[28].nom = 'Green Goblin'
    cards[29].nom = 'Ultron'    
    cards[30].nom = 'Vision'
    cards[31].nom = 'Black Panther'    
    return cards

def clrscr():
    os.system("clear")

def initTable(cards, n):
    table = [None for i in range(0, n * n)]
    for i in range(0, n * n / 2):
        while True:
            pos1 = random.randint(0, n * n - 1)
            pos2 = random.randint(0, n * n - 1)
            if (table[pos1] == None) and \
               (table[pos2] == None) and \
               (pos1 != pos2):
                table[pos1] = cards[i]
                table[pos2] = cards[i]
                break;
    return table

def showTable(table, n):
    for i in range(0, n * n):
        if not table[i].tapada:
            print "casella %d : %s" % (i + 1), table[i].nom

def getCells(table, n):
    while True:
        try:
            p1 = int(raw_input('\nguess cell 1 : '))
            p2 = int(raw_input('guess cell 2 : '))
            if not (p1 in range(1, n * n + 1)) or \
               not (p2 in range(1, n * n + 1)):
                print "Only numbers 1 to %d " % n * n
                continue
            if (not table[p1-1].tapada) or (not table[p2-1].tapada):
                print "Only closed cells"
                continue
            break
        except:
            print "Only integer values 1 to %d" % n * n
    return [p1-1, p2-1]

def analyzeCells(table, cells, n):
    endGame = True
    pos1 = cells[0]
    pos2 = cells[1]
    nom1 = table[pos1].nom 
    nom2 = table[pos2].nom 
    
    print "cell %d : %s" % (pos1 + 1, nom1)
    print "cell %d : %s" % (pos2 + 1, nom2)

    if (nom1 == nom2):
        table[pos1].tapada = False 
        table[pos2].tapada = False

    time.sleep(3)
    clrscr()
    
    for i in range(0, n * n):
        endGame = endGame and (not table[i].tapada)
          
    return not endGame

def showTable(table, n):
    for i in range(0, n * n):
        if not table[i].tapada:
            print "Posició %d : %s" % ((i + 1), table[i].nom)
        
def gameLoop(gameObjects, n):
    table = gameObjects.get("table")
    showTable(table, n)
    cells = getCells(table, n)
    continueGame = analyzeCells(table, cells, n)
    return continueGame

if __name__ == "__main__":
    continueGame = True
    showInstructions(instructions)
    
    while True:
        n = raw_input("dimension NxN (4,6,8) ? ")
        if n in ['4','6','8']:
            break

    n = int(n)
    
    gameObjects = initGame(n)
    while continueGame:
        continueGame = gameLoop(gameObjects, n)

    print "Well done!"
