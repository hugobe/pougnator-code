from random import randint
import numpy as np
import pygame as pg
import argparse
import os 
from pathlib import Path
from os import system
import re


pg.init()

def lecture_fichier(enter_file):
    '''lit le fichier et le met dans une liste '''
    map_liste = []
    with open(enter_file, 'r') as f : 
        for ligne in f :
            map_liste.append(list(ligne.strip()))
    return map_liste

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

class Game:
    '''
    A class to run the game
    '''
    def __init__(self, perso, file):
        self._running = True #it will turn False if @ dies
        self._direction = None
        self._grid = self.lecture_fichier(file)

    def lecture_fichier(enter_file='map/map1.txt'):
        '''lit le fichier et le met dans une liste '''
        map_liste = []
        with open(enter_file, 'r') as f : 
            for ligne in f :
                map_liste.append(list(ligne.strip()))
        return map_liste
    
    def test(self):
        return self._running

    def moves(self):
        for event in pg.event.get():  #renvoie none si pas event
            if event.type == pg.QUIT:
                self._running = False
        # un type de pg.KEYDOWN signifie que l'on a appuye une touche du clavier
            elif event.type == pg.KEYDOWN:
            # si la touche est "Q" on veut quitter le programme
                if event.key == pg.K_q:
                    self._running = False
                if event.key == pg.K_UP:
                    self._direction = (0,-1)
                if event.key == pg.K_DOWN:
                    self._direction=(0,1)
                if event.key == pg.K_LEFT:
                    self._direction=(-1,0)
                if event.key == pg.K_RIGHT:
                    self._direction=(1,0)

class Display: #on definit l'objet damier
    class Quit(Exception):
        pass

    def __init__(self, game, height=400, width=400, pixel=20):
        self._height = height
        self._width = width
        self._pixel = pixel
    
    def screen(self):       #creates screen with pygame
        return pg.display.set_mode((self._width,self._height))
    
    def displayMap(self, screen):
        screen.fill(pg.Color((0,0,0)))
        # Loop on all tiles
        for row in range(self._game.getGridY()):
            for col in range(self._game.getGridX()):
                if self._game.getGrid()[row][col] == '-' or self._game.getGrid()[row][col] == '|':
                    rect = pg.Rect((col) * self._cell_size + 1,
                    (row) * self._cell_size + 1,
                    self._cell_size - 2, self._cell_size - 2)
                    
                    pg.draw.rect(screen, (220, 85, 0), rect)

                elif self._game.getGrid()[row][col] == '.':
                    rect = pg.Rect((col) * self._cell_size + 1,
                    (row) * self._cell_size + 1,
                    self._cell_size - 2, self._cell_size - 2)
                    pg.draw.rect(screen, (199, 208, 0), rect)
                
                elif self._game.getGrid()[row][col] == '#':
                    rect = pg.Rect((col) * self._cell_size + 1,
                    (row) * self._cell_size + 1,
                    self._cell_size - 2, self._cell_size - 2)
                    pg.draw.rect(screen, (179, 177, 145), rect)

                elif self._game.getGrid()[row][col] == '+':
                    rect = pg.Rect((col) * self._cell_size + 1,
                    (row) * self._cell_size + 1,
                    self._cell_size - 2, self._cell_size - 2)
                    pg.draw.rect(screen, (231, 61, 1), rect)

    
    def displayPerso(self, screen, perso):
        '''Paints the perso
        '''
        rect = pg.Rect((perso.getPersoX()) * self._cell_size + 1,
                    (perso.getPersoY()) * self._cell_size + 1,
                    self._cell_size - 2, self._cell_size - 2)
        pg.draw.rect(screen, (252, 108, 156), rect)

    def _process_events(self):
        """Process new events (keyboard, mouse) in order to quit."""
        
        for event in pg.event.get():
            
            # Catch selection of exit icon (Window "cross" icon)
            if event.type == pg.QUIT:
                raise type(self).Quit()

            # Catch a key press
            elif event.type == pg.KEYDOWN:
                raise type(self).Quit()

    def run(self):
        
        # Init Pygame
        pg.init()
        screen=self.screen()
        try:
            while game.test():
                
                self._process_events()

            #self._game.next(self._ant)

                self.displayMap(screen)
                self.displayPerso(screen)

            # Update the screen
                pg.display.update()

        except type(self).Quit:
            pass


#definition of the objects
perso=Perso()

game=Game(perso, 'map/map1.txt')

screen=Display(game).screen()


pg.quit()












