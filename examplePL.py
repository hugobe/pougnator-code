class Ant:
    '''
    A class to represent the ant
    '''
    def __init__(self, ant_x=0, ant_y=0, direction=(0,-1)): #initial direction UP

        self._ant_x = ant_x
        self._ant_y = ant_y
        self._direction = direction
        

    def getAntX(self):
        return self._ant_x
    
    def getAntY(self):
        return self._ant_y
    
    def getDirection(self):
        return self._direction

    def reDefPosition(self,p): #p is a tuple representing the position
        self._ant_x = p[0]
        self._ant_y = p[1]
    
    def newDirection(self,d):
        self._direction=d
        
    def moveAntForward(self):
        '''
        Moves the ant in the current direction by changing the value of the ant's position
        '''
        self._ant_x = self._ant_x + self._direction[0]
        self._ant_y = self._ant_y + self._direction[1]
  
class GameLangtonAnt:
    '''A class to represent and run the game of Langton
    '''
    def __init__(self, step=0, 
                grid=[[0 for x in range(1)] for y in range(1)]):
        
        self._step = step
        self._grid = grid

    def getGrid(self):
        return self._grid

    def getGridX(self):
        return len(self._grid[0])
    
    def getGridY(self):
        return len(self._grid)
    
    def getStep(self):
        return self._step

    def next(self, at):     #takes an object ant to process the game
        '''
        Computes the next step of the game
        '''
        
        #change the direction using the new position
        if self._grid[at.getAntY()][at.getAntX()] == 0:     
            #we now change the direction of 90 degrees to the right
            if at.getDirection() == (0,1):      #DOWN
                at.newDirection((-1,0))

            elif at.getDirection() == (-1,0):    #LEFT
                at.newDirection((0,-1))

            elif at.getDirection() == (0,-1):     #UP
                at.newDirection((1,0))

            elif at.getDirection() == (1,0):    #RIGHT
                at.newDirection((0,1))
        else:
            
            #we now change the direction of 90 degrees to the left
            if at.getDirection() == (0,1):      #DOWN
                at.newDirection((1,0))

            elif at.getDirection() == (-1,0):    #LEFT
                at.newDirection((0,1))

            elif at.getDirection() == (0,-1):     #UP
                at.newDirection((-1,0))

            elif at.getDirection() == (1,0):    #RIGHT
                at.newDirection((0,-1))
        
        if self._grid[at.getAntY()][at.getAntX()] == 0:
            self._grid[at.getAntY()][at.getAntX()] = 1
        else:
            self._grid[at.getAntY()][at.getAntX()] = 0
        at.moveAntForward()
        self.adaptSize(at)
        
        
        logger.debug("Value at position %s is %d " % (str((at.getAntX(),
                    at.getAntY())),self._grid[at.getAntY()][at.getAntX()]))
        self._step += 1
        logger.debug("Ant's direction is %s." % str(at.getDirection()))
        
        logger.debug("Step %d" % self._step)

    
    def save(self, file, at):
        """Saves the state of this Game of Langton into a file.
        """
        
        # Open the file to write the final state of the game
        with open(file, 'w') as f:
            f.write(f'Step {self._step}')
            f.write("\n")
            dir = at.getDirection()
            if dir == (0,1):
                f_dir='DOWN'
            elif dir == (1,0):
                f_dir='RIGHT'
            elif dir == (0,-1):
                f_dir='UP'
            elif dir == (-1,0):
                f_dir='LEFT'
            f.write(f'{at.getAntY()}, {at.getAntX()}, {f_dir}')

            f.write("\n")
            # Loop on all rows and cols
            for row in range(self.getGridY()):
                for col in range(self.getGridX()):
                    if self._grid[row][col] == 1:
                        f.write('X')
                    else:
                        f.write(' ')
                f.write("\n")
    
    def adaptSize(self, at):
        '''
        Adapts the size of the screen to the ant's path
        '''
        if at.getAntY() < 0 :
            self._grid.insert(0, [0 for x in range(self.getGridX())])
            at.reDefPosition((at.getAntX(),0))
 
        elif at.getAntY()+1 > self.getGridY():
            self._grid.append([0 for x in range(self.getGridX())])
            
        
        elif at.getAntX() < 0 :
            for i in range(self.getGridY()):
                self._grid[i].insert(0,0)
            at.reDefPosition((0,at.getAntY()))

        elif at.getAntX()+1 > self.getGridX():
            for i in range(self.getGridY()):
                self._grid[i].append(0)
            
       

class GameDisplay:
    '''Draws the current state of the game
    '''
    # Quit exception
    class Quit(Exception):
        pass

    def __init__(self, game, an, cell_size = DISPLAY_CELL_SIZE, 
                    fps=FPS, color1 = WHITE, color2 = BLACK, colorAnt = RED):
        self._color1 = color1       #color for background cells
        self._color2 = color2
        self._colorAnt = colorAnt       #color for other cells
        self._game = game
        self._ant = an
        self._cell_size = cell_size
        self._fps = fps


    def displayCells(self, screen):
        '''Paints cells in different colors given their values on
            a screen of the dimensions of the game's grid
        '''
        screen.fill(pg.Color(WHITE))
        # Loop on all tiles
        for row in range(self._game.getGridY()):
            for col in range(self._game.getGridX()):
                if self._game.getGrid()[row][col] == 1:
                    rect = pg.Rect((col) * self._cell_size + 1,
                    (row) * self._cell_size + 1,
                    self._cell_size - 2, self._cell_size - 2)
                    logger.debug("Cell rect = %s" % str(rect))
                    pg.draw.rect(screen, self._color2, rect)

               # else:
                #    rect = pg.Rect(col * self._cell_size ,
                #    row * self._cell_size ,
                 #   self._cell_size , self._cell_size )
                 #   pg.draw.rect(self._screen, self._color1, rect)
    
    def displayAnt(self, screen):
        '''Paints the ant
        '''
        #drawing the ant in order to see its direction
        ant_coord = ((self._ant.getAntX())*self._cell_size, 
                        (self._ant.getAntY())*self._cell_size)
        
        if self._ant.getDirection() == (1,0):       #RIGHT
            pentagon_vertices = ((ant_coord),
                (ant_coord[0], ant_coord[1] + self._cell_size),
                (ant_coord[0] + 0.5*self._cell_size, ant_coord[1] + self._cell_size),
                (ant_coord[0] + self._cell_size, ant_coord[1] + 0.5*self._cell_size),
                (ant_coord[0] + 0.5*self._cell_size, ant_coord[1])
                                    )
        
        elif self._ant.getDirection() == (-1,0):        #LEFT
            pentagon_vertices = ((ant_coord[0] + self._cell_size, ant_coord[1]),
                (ant_coord[0] + 0.5*self._cell_size, ant_coord[1]),
                (ant_coord[0], ant_coord[1] + 0.5*self._cell_size),
                (ant_coord[0] + 0.5*self._cell_size, ant_coord[1] + self._cell_size),
                (ant_coord[0] + self._cell_size, ant_coord[1] + self._cell_size)
                                    )
        
        elif self._ant.getDirection() == (0,1):         #DOWN
            pentagon_vertices = ((ant_coord),
                (ant_coord[0], ant_coord[1] + 0.5*self._cell_size),
                (ant_coord[0] + 0.5*self._cell_size, ant_coord[1] + self._cell_size),
                (ant_coord[0] + self._cell_size, ant_coord[1] + 0.5*self._cell_size),
                (ant_coord[0] + self._cell_size, ant_coord[1])
                                    )

        elif self._ant.getDirection() == (0,-1):        #UP
            pentagon_vertices = ((ant_coord[0], ant_coord[1] + 0.5*self._cell_size),
                (ant_coord[0], ant_coord[1] + self._cell_size),
                (ant_coord[0] + self._cell_size, ant_coord[1] + self._cell_size),
                (ant_coord[0] + self._cell_size, ant_coord[1] + 0.5*self._cell_size),
                (ant_coord[0] + 0.5*self._cell_size, ant_coord[1])
                                    )
        
        pg.draw.polygon(screen, self._colorAnt, pentagon_vertices)
        #use of polygon function from pygame to draw an ant where we see the direction
                    
    
    def _process_events(self):
        """Process new events (keyboard, mouse) in order to quit."""

        
        for event in pg.event.get():
            
            # Catch selection of exit icon (Window "cross" icon)
            if event.type == pg.QUIT:
                raise type(self).Quit()

            # Catch a key press
            elif event.type == pg.KEYDOWN:
                raise type(self).Quit()

    def run(self, max_iteration = MAX_STEPS):
        """Display the Game of Langton, and iterate to the next step until user
        decides to quit.
        """
        
        # Init Pygame
        pg.init()
        clock = pg.time.Clock()
        
        try:
            while self._game.getStep() < max_iteration:
                
                # Wait 1/FPS of a second, starting from last display or now
                clock.tick(self._fps)
                
                # Events
                self._process_events()

                # Update title
                pg.display.set_caption("Game of Langton - step %d"
                        % self._game.getStep())

                # Draw cells and ant
                
                logger.debug("Nb rows = %d" % self._game.getGridY())
                logger.debug("Nb cols = %d" % self._game.getGridX())
                logger.debug("Cell size = %d" % self._cell_size)
                # Next step in the Game of Life
                self._game.next(self._ant)

                screen = pg.display.set_mode(((self._game.getGridX())*self._cell_size,
                                (self._game.getGridY())*self._cell_size))
                self.displayCells(screen)
                self.displayAnt(screen)

                # Update the screen
                pg.display.update()

        except type(self).Quit:
            pass
        
def main():
    """Main function."""

    logger.debug("Start main function.")
    # Read command line arguments
    args = read_args()

    # Enable debug messages
    if args.g:
        logger.setLevel(logging.DEBUG)
    
    # Initiate the game by creating an object
    game = GameLangtonAnt()
    ant = Ant()
    # Display
    if args.d:
        test_hexa(args.cellColor1)
        test_hexa(args.cellColor2) 
        test_hexa(args.antColor)
        GameDisplay(game, an=ant, cell_size=args.s,
                fps=args.f, color1=args.cellColor1 , color2=args.cellColor2 , 
                colorAnt=args.antColor).run(args.m)
    else:
        for s in range(args.m):
            game.next(ant)
            logger.debug("Computed step %d" % game.getStep())
        
    # Save
    game.save(args.o, at=ant)


if __name__ == "__main__":

    import sys

    # Setup the logger
    handler = logging.StreamHandler(sys.stderr)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # Call main function
    main()
    
pg.quit()