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
        background_image = pygame.image.load("Artwork/Background.jpeg")
        # surface = pygame.Surface((100,100))

        self._screen.fill((255,255,255))
        self._screen.blit(background_image, (0,0))
        pygame.display.update()
    # Funtions related to the cat sprite:
    # Functions related to the ice cream sprites:
    # Function related to the time visual:
    # Function related to the score visual:
    # Function related to the end of the game:
    
    def draw(self):
        """ Draw the current game state to the screen """

        self._screen.fill(pygame.Color(0,0,0))

        pygame.display.set_caption("A Chubby Cat's Adventure")

        #background_image = pygame.image.load("")


class Controller(object):
# what does this class do: takes the user's input from the up, down, left, and right arrows and translates them into motion of the cat sprite.
# will also be used to bring up a 'help' and 'quit game' display.
    def __init__(self,model):
        self.model = model
        self.model._cat.vy = 0
        self.model._cat.vx = 0

    def arrow_keys(self):
        # Functions related to up,down, left, right arrow input:
        self.pressed = pygame.key.get_pressed()
        
        # for vy/vx will need to mention or edit in Model class:
        if self.pressed.pygame.K_UP:
            self.model._cat.vy = 1 # "1" = 1 frame/s
        elif self.pressed.pygame.K_DOWN:
            self.model._cat.vy = -1
        elif self.pressed.pygame.K_RIGHT:
            self.model._cat.vx = 1
        elif self.pressed.pygame.K_LEFT:
            self.model._cat.vx = -1
        else:
            self.model._cat.vy = 0
            self.model._cat.vx = 0

    # Function related to display response with H key (help) --- key name: pygame.K_h
    def help_key(self):
        if self.pressed.pygame.K_h:
            # display help visual
            pass
    # Function related to display response with Q key (quit) --- key name: pygame.k_q 
    # there may be a quick default quit method but would like to include a "are you sure" display
        # may not be in this section could occur in Model or game loop
    def quit_key(self):
        if self.pressed.pygame.K_q:
            pygame.quit() ## TBD based on gameplay -- maybe VS

class Model(object):
# what does this class do: handles the back end of game play with five main sections to take into account:
# 1. the cat sprite, 2. ice creams, 3. Point tracker, 4. Timer, 5. board setup

    # Functions related to the intial board
    def __init__(self, size):
        """
        Create a new game.
        """

        # Set the size of the window.
        self.width = size[0]
        self.height = size[1]

        # Set the size of the grid row and column.
        self._grid_row = 20
        self._grid_col = 20

        # Set the initial position of the character and the number of ice cream. (this might change if we add stage so that the number of ice cream changes.)
        self._cat = [0, 0]
        self._icecream_num = 10

        # Set the initial point in this game.
        self._point = 0

    # Function related to tracking the cat's location, marked with a square ([]) {marker can change}
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
        for i in range(self._grid_row):
            for j in range(self._grid_row):
                grid_list += [[i, j]]
        grid_list.remove([0,0])

        random.shuffle(grid_list)
        self._icecream_list = grid_list[:self._icecream_num]
        return self._icecream_list

    def move_cat(self, x, y):
        """
        Change the coordinate of the character location following the input direction.
        """
        self._cat[0] += x
        self._cat[1] += y

        return self._cat

    # Functions related to tracking points:
        # when cat bumps into ice cream:
            # delete the ice cream sprite image
            # add quantity of points to the total
            # when game ends, display total points in 'End Game' sequence
    def is_icecream(self):
        for items in self._icecream_list:
            if self._cat[0] == items[0] and self._cat[1] == items[1]:
                self._point += 1
                self._icecream_list.remove(items)
                


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
    print(model)

    view = Visual(model, size)
    # controller = Controller(model)
    
    # Open a Window
    # pygame.display.set_mode(size)

    # Set title to the window
    #pygame.display.set_caption("A Chubby Cat's Adventure")

    # Display the Background image
    # background_image = pygame.image.load("").convert()
    
    # screen.fill((255,255,255))
    # screen.blit(background_image, (0,0))
    # pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get(): # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
                running = False # Ends the game loop
            # Should call a controller method that checks what the event is

        #view.draw()


    # If we exit the loop this will execute and close our game
    pygame.quit() 