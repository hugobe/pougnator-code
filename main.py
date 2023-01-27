from random import randint
import numpy as np
import pygame as pg
import argparse
import os 
from pathlib import Path
from os import system
import re


pg.init()

class Perso:
    '''
    A class to represent the ant
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
    def __init__(self, perso):
        self._running = True #it will turn False if @ dies
        self._direction = None
    
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


#definition of the objects
snake=Snake()
fruit=Fruit()
game=Game()
score=Score()
damier=Damier()

screen=damier.screen()
clock=game.clock()

while game.test(): #tant qu'on a pas de mort du serpent

    clock.tick(5) # regarde le temps entre 2 boucles et attend 1/5s sinon bloque
  
    damier.affiche_damier() 
    score.displayScore()
  
    game.moves()
    snake.NewDirection(game.Getdirection())
    snake.avance_snake()  #on fait avancer le snake en rajoutant un rectangle a sa liste et enlevant le dernier
    damier.affiche_fruit(fruit.getposition())
    snake.manger_fruit(fruit,damier,score)
    
    damier.affiche_snake(snake.getliste_snake())
    pg.display.update()
    snake.mort_snake(game)
    
pg.quit()
score.write_score(score)

system("cat highscore.txt")

if __name__=='__main__':
    print('launched from the original file')
else:
    print('lauched with another file')