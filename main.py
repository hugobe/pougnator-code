# dictionnaire des couleurs

color = {
    '@' : (1,2,3)

}


import pygame as pg

def lecture_fichier(enter_file):
    '''lit le fichier et le met dans une liste '''
    map_liste = []
    with open(enter_file, 'r') as f : 
        for ligne in f :
            map_liste.append(list(ligne.strip()))
    return map_liste


# initialisation de l'écran
# longueur ecran

larg_case = 130
long_case = 80
width = 10 # largeur du rectangle en pixels
height = 10 # hauteur du rectangle en pixels
long_ecr = long_case*height
larg_ecr = larg_case*height

pg.init()
screen = pg.display.set_mode((larg_ecr, long_ecr))

# dessin des trucs
    #dessin des murs

def draw_wall(position): #position est le couple (i,j)

        (i,j) = position

        if map_liste[i][j+1] == '-' and map_liste[i+1][j]  == '|': # coin du haut à gauche
            pg.draw.rect(screen, (0,0,0), pg.Rect(i*10, j*10, width, height)) # fond case murs
            pg.draw.rect(screen, (153,76,0), pg.Rect(i*(10+1/3), j*(10+1/3), width*(2/3), height/3))
            pg.draw.rect(screen, (153,76,0), pg.Rect(i*(10+1/3), j*(10+1/3), width/3, height*(2/3)))

        else if map_liste[i][j-1] == '-' and map_liste[i+1][j]  == '|': # coin du haut à droite
            pg.draw.rect(screen, (0,0,0), pg.Rect(i*10, j*10, width, height)) # fond case murs
            pg.draw.rect(screen, (153,76,0), pg.Rect(i*10, j*(10+1/3), width*(2/3), height/3))
            pg.draw.rect(screen, (153,76,0), pg.Rect(i*(10+1/3), j*(10+1/3), width/3, height*(2/3)))

        else if map_liste[i][j+1] == '-' and map_liste[i-1][j]  == '|': # coin en bas à gauche
        pg.draw.rect(screen, (0,0,0), pg.Rect(i*10, j*10, width, height)) # fond case murs
        pg.draw.rect(screen, (153,76,0), pg.Rect(i*10, j*(10+1/3), width/3, height*(2/3)))
        pg.draw.rect(screen, (153,76,0), pg.Rect(i*(10+1/3), j*(10+1/3), width(2/3), height/3))

        else if map_liste[i][j-1] == '-' and map_liste[i-1][j]  == '|': # coin en bas à droite
            pg.draw.rect(screen, (0,0,0), pg.Rect(i*10, j*(10+1/3), width, height)) # fond case murs
            pg.draw.rect(screen, (153,76,0), pg.Rect(i*10, j*(10+1/3), width/3, height*(2/3)))
            pg.draw.rect(screen, (153,76,0), pg.Rect(i*(10+1/3), j*10, width*(2/3), height/3))

        else if map_liste[i][j] == '-':
            pg.draw.rect(screen, (0,0,0), pg.Rect(i*10, j*10, width, height)) # fond case murs
            pg.draw.rect(screen, (153,76,0), pg.Rect(i*(10+1/3), j*(10+1/3), width/3, height)) # interieur des murs (prend 1/3 des murs)

        else if map_liste[i][j] == '|':
            pg.draw.rect(screen, (0,0,0), pg.Rect(i*10, j*10, width, height)) # fond case murs
            pg.draw.rect(screen, (153,76,0), pg.Rect(i*(10+1/3), j*(10+1/3), width, height/3)) # interieur des murs (prend 1/3 des murs)




rect = pg.Rect(0,0,width,height)
pg.draw.rect(screen, (23,254,4), rect)


running = True


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



