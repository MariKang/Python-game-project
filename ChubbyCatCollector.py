import itertools
import random
import sys
import pygame
from pygame.locals import *
import time

class Visual:
# what does this class do: this class ocuses on what the user will see; the constantly updating game play, location of the various sprites,
# the background and surroundings.

    # Init:
    # Function related to game display with background:
    # Funtions related to the cat sprite:
    # Functions related to the ice cream sprites:
    # Function related to the time visual:
    # Function related to the score visual:
    # Function related to the end of the game:
    pass


class Controller:
# what does this class do: takes the user's input from the up, down, left, and right arrows and translates them into motion of the cat sprite.
# will also be used to bring up a 'help' and 'quit game' display.
    def __init__(self,model):
        self.model = model
        self.model._cat.vy = vy
        self.model._cat.vx = vx

    def arrow_keys():
        # Functions related to up,down, left, right arrow input:
        pressed = pygame.key.get_pressed()
        
        # for vy/vx will need to mention or edit in Model class:
        if pressed[pygame.K_UP]:
            self.model._cat.vy = 1 
        elif pressed[pygame.K_DOWN]:
            self.model._cat.vy = -1
        elif presssed[pygame.K_RIGHT]:
            self.model._cat.vx = 1
        elif presssed[pygame.K_LEFT]:
            self.model._cat.vx = -1
        else:
            self.model._cat.vy = 0
            self.model._cat.vx = 0

    # Function related to display response with H key (help) --- key name: pygame.K_h
    def help_key():
        if pressed[pygame.K_h]:
            # display help visual

    # Function related to display response with Q key (quit) --- key name: pygame.k_q 
    # there may be a quick default quit method but would like to include a "are you sure" display
        # may not be in this section could occur in Model or game loop
    def quit_key():
        if pressed[pygame.K_q]:
            pygame.quit()

class Model:
# what does this class do: handles the back end of game play with five main sections to take into account:
# 1. the cat sprite, 2. ice creams, 3. Point tracker, 4. Timer, 5. board setup

    # Functions related to the intial board
    def __init__(self):
        """
        Create a new game.
        """
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
        icecream_list = grid_list[:10]
        return icecream_list

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
        pass

    # Functions related to the timer counting down:
        # per round each timer will be set at less and less time