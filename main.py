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

class Perso:
    '''
    A class to represent the person
    '''
    def __init__(self, perso_x=0, perso_y=0, direction=(0,-1),objects={}, 
                pdv=20, puissance=1): #initial direction UP

        self._perso_x = perso_x
        self._perso_y = perso_y
        self._direction = direction
        self._objects = objects
        self._pdv = pdv
        self._puissance = puissance
        

    def getPersoX(self):
        return self._perso_x
    
    def getPersoY(self):
        return self._perso_y
    
    def getDirection(self):
        return self._direction

    def reDefPosition(self,p): #p is a tuple representing the position
        self._ant_x = p[0]
        self._ant_y = p[1]
    
    def newDirection(self,d):
        self._direction=d
        
    def movePersoForward(self):
        '''
        Moves the ant in the current direction by changing the value of the ant's position
        '''
        self._perso_x = self._perso_x + self._direction[0]
        self._perso_y = self._perso_y + self._direction[1]
    
    def getObjects(self):
        return self._objects

    def detect_objects(self,fru,object,sco):    
        pass

    def mort_perso(self,object):
        pass


#     def moves(self):
#         for event in pg.event.get():  #renvoie none si pas event
#             if event.type == pg.QUIT:
#                 self._running = False
#         # un type de pg.KEYDOWN signifie que l'on a appuye une touche du clavier
#             elif event.type == pg.KEYDOWN:
#             # si la touche est "Q" on veut quitter le programme
#                 if event.key == pg.K_q:
#                     self._running = False
#                 if event.key == pg.K_UP:
#                     self._direction = (0,-1)
#                 if event.key == pg.K_DOWN:
#                     self._direction=(0,1)
#                 if event.key == pg.K_LEFT:
#                     self._direction=(-1,0)
#                 if event.key == pg.K_RIGHT:
#                     self._direction=(1,0)







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



# initialisation du grid
def lecture_fichier(enter_file='map/map1.txt'):
    '''lit le fichier et le met dans une liste '''
    map_liste = []
    with open(enter_file, 'r') as f : 
        for ligne in f :
            map_liste.append(list(ligne))
    return map_liste

map_list = lecture_fichier()


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



