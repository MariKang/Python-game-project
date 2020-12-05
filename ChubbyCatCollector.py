import itertools
import random
import sys

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


class Controller:
# what does this class do: takes the user's input from the up, down, left, and right arrows and translates them into motion of the cat sprite.
# will also be used to bring up a 'help' and 'quit game' display.

    # Functions related to up,down, left, right arrow input:
    # Function related to display response with H key (help)
    # Funtion related to display response with Q key (quit)


class Model:
# what does this class do: handles the back end of game play with five main sections to take into account:
# 1. the cat sprite, 2. ice creams, 3. Point tracker, 4. Timer, 5. board setup

    # Functions related to the intial board
    # Function related to tracking the cat's location, marked with a square ([]) {marker can change}
    # Function related to the ice creams:
        # input how many ice creams are involved
        # calculate the randomized locations per ice cream
        # mark each location with a X {marker can change}

    # Functions related to tracking points:
        # when cat bumps into ice cream:
            # delete the ice cream sprite image
            # add quantity of points to the total
            # when game ends, display total points in 'End Game' sequence

    # Functions related to the timer counting down:
        # per round each timer will be set at less and less time