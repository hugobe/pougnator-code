from random import randint
import numpy as np
import pygame as pg
import argparse
import os 
from pathlib import Path
from os import system

pg.init()

# initialisation du grid
def lecture_fichier(enter_file='map/map1.txt'):
    '''lit le fichier et le met dans une liste '''
    map_liste = []
    with open(enter_file, 'r') as f : 
        for ligne in f :
            map_liste.append(list(ligne))
    return map_liste

map_list = lecture_fichier()

perso={'x':2, 'y':2,'power':2,'life':10,'or':0,'potion':0,
        'armes':0, 'shield':0}

        
def detect_objects(pers = perso, map = map_list):    
    if map[pers['x']][pers['y']] == 'j':
        pers['potion']+=1
    elif map[pers['x']][pers['y']] == '*':
        pers['or']+=1
    elif map[pers['x']][pers['y']] == '!':
        pers['armes']+=1
    elif map[pers['x']][pers['y']] == 's':
        pers['armures']+=1

#chauffe-souris=='c'
#monstre cache == 'K'
#creeper == 'b'
def monstre_autour(pers = perso, map = map_list):
    dir=[(1,0),(-1,0),(0,1),(0,-1),
        (1,1),(-1,-1),(-1,1),(1,-1)] 
    clock = pg.time.Clock()
        
    for d in dir:
        if map[pers['x']+d[0]][pers['y']+d[1]] == 'c':
            c_life=3
            
            while c_life>0:
                pers['life']+=-2
                clock.tick(1)
                if
                    c_life += -pers['power']
                
            pers['life'] += 1





# initialisation de l'écran
# longueur ecran

larg_case = len(map_list[0])
long_case = len(map_list)

pixel = 40 # hauteur du rectangle en pixels
long_ecr = long_case*pixel
larg_ecr = larg_case*pixel

screen = pg.display.set_mode((larg_ecr, long_ecr))
running = True

# On initialise la map
# Loop on all tiles

for i, row in enumerate(map_list) :
    for j, col in enumerate(row):
        if col == '-' or col == '|':
            rect = pg.Rect(j * pixel + 1,
            i *  pixel + 1,
            pixel - 2, pixel - 2)
            pg.draw.rect(screen, (220, 85, 0), rect)

        elif col == '.':
            rect = pg.Rect(j * pixel + 1,
            i * pixel + 1,
            pixel - 2, pixel - 2)
            pg.draw.rect(screen, (199, 208, 0), rect)
        
        elif col == '#':
            rect = pg.Rect(j * pixel + 1,
            i * pixel + 1,
            pixel - 2, pixel - 2)
            pg.draw.rect(screen, (179, 177, 145), rect)

        elif col == '+':
            rect = pg.Rect(j * pixel + 1,
            i * pixel + 1,
            pixel - 2, pixel - 2)
            pg.draw.rect(screen, (158, 253, 56), rect)
        
        elif col == '@':
            rect = pg.Rect(j * pixel + 1,
            i * pixel + 1,
            pixel - 2, pixel - 2)
            pg.draw.rect(screen, (253, 108, 158), rect)

        elif col == '=':
            rect = pg.Rect(j * pixel + 1,
            i * pixel + 1,
            pixel - 2, pixel - 2)
            pg.draw.rect(screen, (129, 20, 83), rect)

if perso['life']<=0:
    running = False
    
while running:

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            pass
            # si la touche est "Q" on veut quitter le programme
        
    pg.display.update()
raise ValueError('you have been defeated')


