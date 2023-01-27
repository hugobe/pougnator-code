from random import randint
import numpy as np
import pygame as pg
import argparse
import os 
from pathlib import Path
from os import system
import re


        


# pg.init()

# def lecture_fichier(enter_file):
#     '''lit le fichier et le met dans une liste '''
#     map_liste = []
#     with open(enter_file, 'r') as f : 
#         for ligne in f :
#             map_liste.append(list(ligne.strip()))
#     return map_liste


        

pg.init()

# initialisation du grid
def lecture_fichier(enter_file='map/map1.txt'):
    '''lit le fichier et le met dans une liste '''
    map_liste = []
    with open(enter_file, 'r') as f : 
        for ligne in f :
            map_liste.append(list(ligne))
    return map_liste

################### fonctions draw ###########################

def draw_perso(pers):
    rect = pg.Rect(perso['y'] * pixel + 1,
    perso['x'] * pixel + 1,
    pixel - 2, pixel - 2)
    pg.draw.rect(screen, (255, 0, 255), rect)

def draw_point(pos_x, pos_y):
    rect = pg.Rect(pos_y * pixel + 1,
    pos_x * pixel + 1,
    pixel - 2, pixel - 2)
    pg.draw.rect(screen, (199, 208, 0), rect)

def draw_h(pos_x, pos_y):
    rect = pg.Rect(pos_y * pixel + 1,
    pos_x * pixel + 1,
    pixel - 2, pixel - 2)
    pg.draw.rect(screen, (179, 177, 145), rect)

def draw_plus(pos_x, pos_y):
    rect = pg.Rect(pos_y * pixel + 1,
    pos_x * pixel + 1,
    pixel - 2, pixel - 2)
    pg.draw.rect(screen, (158, 253, 56), rect)

def draw_alpha(pos_x, pos_y):
    rect = pg.Rect(pos_y * pixel + 1,
    pos_x * pixel + 1,
    pixel - 2, pixel - 2)
    pg.draw.rect(screen, (255, 0, 127), rect)


def move_perso(deplacement, map_list, pers):
    pos = (pers['x'], pers['y'])
    new_pos = (pos[0] + deplacement[0], pos[1] + deplacement[1])
    if map_list[new_pos[0]][new_pos[1]] in ['.', '+', '#']:
        pers['x'], pers['y'] = new_pos[0], new_pos[1]
        if map_list[pos[0]][pos[1]] == '.':
            draw_point(*pos)
            draw_perso(perso)
        elif map_list[pos[0]][pos[1]] == '#':
            draw_h(*pos)  
            draw_perso(perso)   
        elif map_list[pos[0]][pos[1]] == '+':
            draw_plus(*pos)  
            draw_perso(perso)    
        elif map_list[pos[0]][pos[1]] == '@':
            draw_alpha(*pos)
            draw_perso(perso) 

        
def detect_objects(pers , map):    
    if map[pers['x']][pers['y']] == 'j':
        pers['potion']+=1
    elif map[pers['x']][pers['y']] == '*':
        pers['or']+=1
    elif map[pers['x']][pers['y']] == '!':
        pers['armes']+=1

#chauffe-souris=='c'
#monstre cache == 'K'
#creeper == 'b'
def monstre_autour(pers , map):    
    if map[pers['x']][pers['y']] == 'j':
        pass


def mort_perso(pers ):
    if pers['life']<=0:
        raise ValueError('you have been defeated')
           

def monstres_attaque(monstre, pers):
    pass



# initialisation de l'écran
# longueur ecran

larg_case = 80
long_case = 40
width = 40 # largeur du rectangle en pixels
pixel = 40 # hauteur du rectangle en pixels
long_ecr = long_case*pixel
larg_ecr = larg_case*pixel

pg.init()
screen = pg.display.set_mode((larg_ecr, long_ecr))
running = True

# dessin des trucs
    #dessin des murs

# def draw_wall(position): #position est le couple (i,j)

#         (i,j) = position

        # if map_liste[i][j+1] == '-' and map_liste[i+1][j]  == '|': # coin du haut à gauche
        #     pg.draw.rect(screen, (0,0,0), pg.Rect(i*10, j*10, width, height)) # fond case murs
        #     pg.draw.rect(screen, (153,76,0), pg.Rect(i*(10+1/3), j*(10+1/3), width*(2/3), height/3))
        #     pg.draw.rect(screen, (153,76,0), pg.Rect(i*(10+1/3), j*(10+1/3), width/3, height*(2/3)))

        # else if map_liste[i][j-1] == '-' and map_liste[i+1][j]  == '|': # coin du haut à droite
        #     pg.draw.rect(screen, (0,0,0), pg.Rect(i*10, j*10, width, height)) # fond case murs
        #     pg.draw.rect(screen, (153,76,0), pg.Rect(i*10, j*(10+1/3), width*(2/3), height/3))
        #     pg.draw.rect(screen, (153,76,0), pg.Rect(i*(10+1/3), j*(10+1/3), width/3, height*(2/3)))

        # else if map_liste[i][j+1] == '-' and map_liste[i-1][j]  == '|': # coin en bas à gauche
        # pg.draw.rect(screen, (0,0,0), pg.Rect(i*10, j*10, width, height)) # fond case murs
        # pg.draw.rect(screen, (153,76,0), pg.Rect(i*10, j*(10+1/3), width/3, height*(2/3)))
        # pg.draw.rect(screen, (153,76,0), pg.Rect(i*(10+1/3), j*(10+1/3), width(2/3), height/3))

        # else if map_liste[i][j-1] == '-' and map_liste[i-1][j]  == '|': # coin en bas à droite
        #     pg.draw.rect(screen, (0,0,0), pg.Rect(i*10, j*(10+1/3), width, height)) # fond case murs
        #     pg.draw.rect(screen, (153,76,0), pg.Rect(i*10, j*(10+1/3), width/3, height*(2/3)))
        #     pg.draw.rect(screen, (153,76,0), pg.Rect(i*(10+1/3), j*10, width*(2/3), height/3))

        # else if map_liste[i][j] == '-':
        #     pg.draw.rect(screen, (0,0,0), pg.Rect(i*10, j*10, width, height)) # fond case murs
        #     pg.draw.rect(screen, (153,76,0), pg.Rect(i*(10+1/3), j*(10+1/3), width/3, height)) # interieur des murs (prend 1/3 des murs)

        # else if map_liste[i][j] == '|':
        #     pg.draw.rect(screen, (0,0,0), pg.Rect(i*10, j*10, width, height)) # fond case murs
        #     pg.draw.rect(screen, (153,76,0), pg.Rect(i*(10+1/3), j*(10+1/3), width, height/3)) # interieur des murs (prend 1/3 des murs)











################################### On initialise la map #########################################
# Loop on all tiles
map_list = lecture_fichier()

perso={'x':None, 'y':None,'power':5,'life':10,'or':0,'potion':0,'armes':0}

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
            perso['x'] = i
            perso['y'] = j
            draw_perso(perso)

        elif col == '=':
            rect = pg.Rect(j * pixel + 1,
            i * pixel + 1,
            pixel - 2, pixel - 2)
            pg.draw.rect(screen, (129, 20, 83), rect)


pg.display.update()

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
            if event.key == pg.K_UP:
                move_perso((-1,0), map_list, perso)
            elif event.key == pg.K_DOWN:
                move_perso((1,0), map_list, perso)
            elif event.key == pg.K_RIGHT:
                move_perso((0,1), map_list, perso)
            elif event.key == pg.K_LEFT:
                move_perso((0,-1), map_list, perso)
        
    pg.display.update()



