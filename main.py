import pygame as pg

def lecture_fichier(enter_file):
    '''lit le fichier et le met dans une liste '''
    map_liste = []
    with open(enter_file, 'r') as f : 
        for ligne in f :
            map_liste.append(list(ligne.strip()))
    return map_liste









