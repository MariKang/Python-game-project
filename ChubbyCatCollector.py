import itertools
import random
import sys
import pygame
from pygame.locals import *
import time

class Visual(object):
# what does this class do: this class ocuses on what the user will see; the constantly updating game play, location of the various sprites,
# the background and surroundings.

    # Init:
    def __init__(self, model, size):

        """
        Initialize the view with a reference to the model and the specified game
        screen dimensions (represented as a tuple containing the width and height
        """

        self._model = model
        self._screen = pygame.display.set_mode(size)
        self.background_set()

    # Function related to game display with background:
    def background_set(self):
        self.background_image = pygame.image.load("Artwork/Background.jpeg")
        # surface = pygame.Surface((100,100))

        self._screen.fill((255,255,255)) # fill screen with white --- may move to the init
        self._screen.blit(self.background_image, (0,0))
        # pygame.display.update()

    # Functions related to the cat sprite:
    # Functions related to the ice cream sprites:
    # Function related to the time visual:
    # Function related to the score visual:
    # Function related to the end of the game:
    
    def draw(self): # have access to everything that needs to be visible , update screen once!
        """ Draw the current game state to the screen """

        # self._screen.fill(pygame.Color(0,0,0))
        pygame.display.set_caption("A Chubby Cat's Adventure") # -- could be done in the init

    def draw_winner_page(self):
        """ Draw the winner page to the screen """
        self._screen.fill((255,255,255))


class Controller(object):
# what does this class do: takes the user's input from the up, down, left, and right arrows and translates them into motion of the cat sprite.
# will also be used to bring up a 'help' and 'quit game' display.
    def __init__(self, model):
        self.cat = model.cat
        self.model = model

    def arrow_keys(self):
        # Functions related to up,down, left, right arrow input:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_UP:
                    self.cat.vx = 0
                    self.cat.vy = -1 # "1" = 1 frame/s
                elif event.key == pygame.K_DOWN:
                    self.cat.vx = 0
                    self.cat.vy = 1
                elif event.key == pygame.K_RIGHT:
                    self.cat.vx = 1
                    self.cat.vy = 0
                elif event.key == pygame.K_LEFT:
                    self.cat.vx = -1
                    self.cat.vy = 0
                elif event.key == pygame.K_h:
                    # help function/screen switch
                    pass
                elif event.key == pygame.K_q:
                    pygame.quit() # quit function needs editing
                else:
                    self.cat.vy = 0
                    self.cat.vx = 0


class Model():
    def __init__(self, size):
        # Set the size of the window.
        self.width = size[0]
        self.height = size[1]

        # Set the size of the grid row and column.
        self._grid_row = 20
        self._grid_col = 20

        # Set the initial point in this game.
        # self._point = 0

        self.cat = Cat(size)
        self.icecream = Icecream(size)
        self._icecream_list = self.icecream._icecream_list


    # generate ice creams
    # cat touch ice creams
    # update score
        # when cat bumps into ice cream:
            # delete the ice cream sprite image
            # add quantity of points to the total
            # when game ends, display total points in 'End Game' sequence
    def is_icecream(self):
        
        for items in self._icecream_list:
            dist = self.distance(self.cat._pos, items)
            if dist <= 25:
                # self._point += 1
                self._icecream_list.remove(items)

    def distance(self, point_a, point_b):
        a = point_b[0] - point_a[0]
        b = point_b[1] - point_a[1]
        c = (a**2 + b**2)**(1/2)
        return c
    
    def get_icecreamlist(self):
        return self._icecream_list

class Cat(object):
# what does this class do: handles the back end of game play with five main sections to take into account:
# 1. the cat sprite, 2. ice creams, 3. Point tracker, 4. Timer, 5. board setup

    # Functions related to the intial board
    def __init__(self, size):

        # Set the initial position of the character and the number of ice cream. (this might change if we add stage so that the number of ice cream changes.)
        self._pos = [300, 300]
        self.vx = 0
        self.vy = 0

        self.width = size[0]
        self.height = size[1]

    # Function related to tracking the cat's location, marked with a square ([]) {marker can change}:
    def draw_cat_loc(self, screen):
        
        rect = pygame.Rect(self._pos[0], self._pos[1],25,25)
        pygame.draw.rect(screen, (255,255,255), rect)

    def move_cat(self):
        """
        Change the coordinate of the character location following the input direction.
        """
        new_posx = self._pos[0] + self.vx
        new_posy = self._pos[1] + self.vy
        if new_posx > 2 and new_posx < self.width-2:
            self._pos[0] = new_posx
        if new_posy > 2 and new_posy < self.height-2:
            self._pos[1] = new_posy
        
        return self._pos


                
# need help with icecream class
class Icecream():
    def __init__(self,size):
        self._icecream_num = 10
        self._grid_row = size[0]
        self.generate_icecream()
    # Function related to the ice creams:
        # input how many ice creams are involved
        # calculate the randomized locations per ice cream
        # mark each location with a X {marker can change}
    def generate_icecream(self):
        """
        Generate and return the position of the ice creams.
        """
        # This method can be used in visual to show the initial position of the ice cream.
        grid_list = []
        for i in range(0, self._grid_row, 25):
            for j in range(0, self._grid_row, 25):
                grid_list += [[i, j]]
        grid_list.remove([0,0])

        random.shuffle(grid_list)
        self._icecream_list = grid_list[:self._icecream_num]


    def draw_icecream_loc(self, screen):
        for pair in self._icecream_list:
            rect = pygame.Rect(pair[0], pair[1],25,25)
            pygame.draw.rect(screen, (0,0,0), rect)



    # Functions related to the timer counting down:
        # per round each timer will be set at less and less time

if __name__ == '__main__':
    # Start a pygame
    pygame.init()

    size = (600, 600) # originally 600,480
    # screen = pygame.display.set_mode(size)
    # background_image = pygame.image.load("Background.jpeg")
    # surface = pygame.Surface((100,100))
    model = Model(size)
    
    # print(cat)
    # icecream = Icecream(size)

    view = Visual(model, size)
    controller = Controller(model)
    
    # Open a Window
    # pygame.display.set_mode(size)

    # Set title to the window
    pygame.display.set_caption("A Chubby Cat's Adventure")

    running = True
    while running:
        
        # for event in pygame.event.get(): # This will loop through a list of any keyboard or mouse events.
        #     if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
        #         running = False # Ends the game loop
            # Should call a controller method that checks what the event is       
        controller.arrow_keys()
        model.cat.move_cat()
        model.is_icecream()
        view.background_set() 
        model.cat.draw_cat_loc(view._screen)
        model.icecream.draw_icecream_loc(view._screen)
        if len(model.get_icecreamlist()) == 0:
            view.draw_winner_page()
        pygame.display.flip()# this renders/updates to screen

    # If we exit the loop this will execute and close our game
    pygame.quit() 