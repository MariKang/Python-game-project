import random
import pygame
from pygame.locals import *
import time


class Visual(object):
    """
    Representation of a visual of the game.

    Attributes:

        _model: An instance of a Model class.
        screen: A display surface created representing the screen of the game.
        _background_image: A surface object representing the image of the
            background of the game.
        _help_image: A surface object representing the image of the
            help page of the game.
        _win_image: A surface object representing the image of the
            win page of the game.
        _lose_image: A surface object representing the image of the
            lose page of the game.
        _font: A font object loaded from the system font.
    """

    def __init__(self, model, size):
        """
        Initialize the view with a reference to the model and the specified game
        screen dimensions.

        Args:
            model: An instance of a Model class.
            size: A tuple representing the size of the screen for the game.
        """

        self._model = model

        # Create a display surface with the given size of the screen.
        self.screen = pygame.display.set_mode(size)

        # Load the images of the background, help page, win page, and the
        # lose page.
        self._background_image = pygame.image.load("Artwork/Background.jpeg")
        self._help_image = pygame.image.load("Artwork/RedoneHelp.png")
        self._win_image = pygame.image.load("Artwork/Winner.png")
        self._lose_image = pygame.image.load("Artwork/Loser.png")

        # Call the method that sets the background.
        self.background_set()

        # Create a font object loaded from the system font.
        self._font = pygame.font.SysFont(None, 100)

    def background_set(self):
        """
        Set the background of the game using the background image
        loaded in the init method.
        """

        # Fill the screen with white.
        self.screen.fill((255, 255, 255))

        # Draw a background image on the white screen with coordinate
        # representing the position of the upper left of the image on the
        # screen.
        self.screen.blit(self._background_image, (0, 0))

    def draw_end(self):
        """
        Draw the ending page to the screen if the game ends.
        """

        # If the game ended because the player lost, it draws the loser
        # page. If time is zero, it means that the player has lost.
        if model.time == 0:
            self.screen.fill((255, 255, 255))
            self.screen.blit(self._lose_image, (0, 0))
        # If the game ended because the player won, it draws the winner
        # page.
        else:
            self.screen.fill((255, 255, 255))
            self.screen.blit(self._win_image, (0, 0))

    def draw_help_page(self):
        """
        Draw the help page to the screen if the player asks for help.
        """
        self.screen.fill((255, 255, 255))
        self.screen.blit(self._help_image, (0, 0))

    def draw_timer(self):
        """
        Draw the timer to the screen when game is played.
        """

        # Render a text of the leftover time.
        text = self._font.render(str(model.time), True, (0, 128, 0))

        # Create a rectangle for the text at the center of the screen.
        text_rect = text.get_rect(center=self.screen.get_rect().center)

        # Draw the text on the screen.
        self.screen.blit(text, text_rect)


class Controller(object):
    """
    Representation of a controller of the game.

    Controller class takes the user's arrow key input and translate into
    the motion of the cat sprite, or change the state of the game
    (quit of help).

    Attributes:
        cat: An instance of a Cat class.
        model: An instance of a Model class.
    """
    def __init__(self, model):
        """
        Initialize the controller of the game by creating model instance
        and the cat instance from that model class.

        Args:
            model: An instance of a Model class.
        """
        self.cat = model.cat
        self.model = model

    def arrow_keys(self):
        """
        Translate input received from the keyboard of the player to move
        the cat, display a help screen, or quit the game and from the
        timer event.
        """
        # Loop through a list of any keyboard or mouse events.
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                # If up key in the keyboard is pressed, move the cat
                # upward in a given velocity.
                if event.key == pygame.K_UP:
                    self.cat.vx = 0
                    self.cat.vy = -3  # "1" = 1 frame/s
                # If down key in the keyboard is pressed, move the cat
                # downward in a given velocity.
                elif event.key == pygame.K_DOWN:
                    self.cat.vx = 0
                    self.cat.vy = 3
                # If right key in the keyboard is pressed, move the cat
                # right in a given velocity.
                elif event.key == pygame.K_RIGHT:
                    self.cat.vy = 0
                    self.cat.vx = 3
                # If left key in the keyboard is pressed, move the cat
                # left in a given velocity.
                elif event.key == pygame.K_LEFT:
                    self.cat.vy = 0
                    self.cat.vx = -3
                # If 'h' in the keyboard is pressed, indicate that it
                # is help state of the game.
                elif event.key == pygame.K_h:
                    model.help = True
                # If 'escape' key in the keyboard is pressed and it is
                # the help state of the game, indicate that help state
                # is ended.
                elif event.key == pygame.K_ESCAPE and model.help is True:
                    model.help = False
                # If 'q' in the keyboard is pressed, quit the game.
                elif event.key == pygame.K_q:
                    pygame.quit()
                else:
                    self.cat.vy = 0
                    self.cat.vx = 0
            # In every timer event, if it's not the help state and the
            # game didn't end, reduce the time. And if the there's no
            # leftover time, stop the timer and indicate that the game
            # is over.
            elif event.type == model.timer_event:
                if model.help is False and model.gameover is False:
                    model.time -= 1

                if model.time == 0:
                    pygame.time.set_timer(model.timer_event, 0)
                    model.gameover = True


class Model(object):
    """
    Representation of a model of the game.

    Attributes:
        cat: An instance of a Cat class.
        icecream: An instance of a Icecream class.
        _icecream_list: A list representing the location of the ice cream.
        view: An instance of a Visual class.
        controller: An instance of a Controller class.
        help: A boolean representing whether it's help status of the game
            or not.
        gameover: A boolean representing whether the game is over or not.
        time: An integer representing the total time in the timer of
            a game.
        timer_event: A custom event representing the timer.
    """
    def __init__(self, size):
        """
        Initialize the model of the game by setting the board and classes.

        Call Cat, Icecream, Visual and Controller class instances to use them
        in the model. Also, set the timer, size of the window, and game status.

        Args:
            size: A tuple representing the size of the window.
        """
        self.cat = Cat(size)
        self.icecream = Icecream(size)

        # Get the ice cream list from the ice cream class instance.
        self._icecream_list = self.icecream._icecream_list

        self.view = Visual(self, size)
        self.controller = Controller(self)

        # Set the boolean of help and gameover to false when game starts.
        self.help = False
        self.gameover = False

        # Set the total time given for a single game.
        self.time = 20

        # Set the time interval to one second and set the timer.
        timer_interval = 1000
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, timer_interval)

    def _is_icecream(self):
        """
        Remove the ice cream if the cat position reaches the ice cream
        position.
        """
        # For all ice cream in the list, check if the distance between
        # the cat and the ice cream is in the range of collision. If it
        # is, remove the ice cream from the list.
        for items in self._icecream_list:
            dist = self.distance(self.cat._pos, items)
            if dist <= 25:
                self._icecream_list.remove(items)

    def distance(self, point_a, point_b):
        """
        Return the distance between the two points using pythagorean
        theorem.

        Args:
            point_a: A list representing the position of the first point.
            point_b: A list representing the position of the second point.

        Returns:
            An integer of the distance between two points.
        """
        # Get the difference in x position and y position of two points.
        a = point_b[0] - point_a[0]
        b = point_b[1] - point_a[1]

        # Using pythagorean theorem, get the distance between the points.
        c = (a**2 + b**2)**(1 / 2)
        return c

    def get_icecreamlist(self):
        """
        Return the list of the ice cream positions.

        Returns:
            A list representing the ice cream positions.
        """
        return self._icecream_list

    def play_loop(self):
        """
        Play the game loop.

        After getting the input of the player, this method moves the cat,
        check if it collected the ice cream and remove the ice cream if it
        did, and update the display. Also, it checks if the game has ended
        or has paused for help and display them.
        """
        # If the game is not over and not in a help page, play the game loop.
        if self.help is False and self.gameover is False:
            # Move the cat and check if the new position collides the ice cream.
            self.cat.move_cat()
            self._is_icecream()

            # Update the display with new cat locations.
            self.view.background_set()
            self.view.draw_timer()
            self.cat.draw_cat_loc(self.view.screen)
            self.icecream.draw_icecream_loc(self.view.screen)

            # If the length of the ice cream list is 0, indicate that the
            # game has ended.
            if len(self.get_icecreamlist()) == 0:
                self.gameover = True

        # If the game is over, draw the ending screen.
        elif self.gameover is True:
            self.view.draw_end()
        # If is in the help page, draw the help screen.
        else:
            self.view.draw_help_page()

        # Update the display.
        pygame.display.flip()


class Cat(object):
    """
    Representation of a cat model of the game.

    Attributes:
        _pos: A list representing the position of the cat.
        vx: An integer representing the x velocity  of the cat.
        vy: An integer representing the y velocity  of the cat.
        _width: An integer representing the width of the window.
        _height: An integer representing the height of the window.
        _cat_image: A surface object representing the image of the cat.
    """
    def __init__(self, size):
        """
        Initialize the cat model of the game by setting the position, velocity,
        and the image of the cat.

        Args:
            size: A tuple representing the size of the window.
        """
        # Set the initial position of the cat and the initial velocity.
        self._pos = [300, 300]
        self.vx = 0
        self.vy = 0

        # Set the width and the height of the window with given size.
        self._width = size[0]
        self._height = size[1]

        # Load the image of the cat.
        self._cat_image = pygame.image.load("Artwork/Cat for animation 1.png")

    def draw_cat_loc(self, screen):
        """
        Draw the character to the screen on a correct position.

        Args:
            screen: A display surface created representing the screen of
                the game.
        """

        # Display the cat in its position. The coordinate is adjusted based
        # on the size and the white space of the image.
        screen.blit(self._cat_image, (self._pos[0] - 80, self._pos[1] - 70))

    def move_cat(self):
        """
        Change the coordinate of the character location following the input
        direction.

        Returns:
            A list representing the position of the cat.
        """
        # Set the new position of the cat using the input velocity.
        new_posx = self._pos[0] + self.vx
        new_posy = self._pos[1] + self.vy

        # If the new position doesn't exceed the boundary of the screen,
        # change the position of the cat to the new position.
        if new_posx > 60 and new_posx < self._width - 60:
            self._pos[0] = new_posx
        if new_posy > 60 and new_posy < self._height - 60:
            self._pos[1] = new_posy

        return self._pos


class Icecream():
    """
    Representation of a ice cream model of the game.

    Attributes:
        _icecream_num: An integer representing the number of ice cream.
        _grid_row: An integer representing the width of the screen.
        _grid_col: An integer representing the height of the screen.
        _icecream_image: A surface object representing the image of the ice
        cream.
    """
    def __init__(self, size):
        """
        Initialize the ice cream model of the game by setting the number and
        image of the ice cream and generate their random position.

        Args:
            size: A tuple representing the size of the window.
        """
        # Set the number of the ice cream and the width/height of the screen.
        self.icecream_num = 20
        self._grid_row = size[0]
        self._grid_col = size[1]

        # Generate the random ice cream position.
        self.generate_icecream()

        # Load the image of the ice cream.
        self._icecream_image = pygame.image.load(
            "Artwork/Ice cream for gameplay.png")

    def generate_icecream(self):
        """
        Generate a list that represents the positions of the ice cream
        initially.
        """
        grid_list = []

        # Create a list containing the coordinates of the possible position of
        # the ice cream in the window.
        for i in range(70, self._grid_row - 70, 25):
            for j in range(70, self._grid_col - 70, 25):
                grid_list += [[i, j]]

        # Randomly shuffle the list and get these random coordinates. The number
        # of the coordinate we are getting is the initial number of the ice
        # cream.
        random.shuffle(grid_list)
        self._icecream_list = grid_list[:self.icecream_num]

    def draw_icecream_loc(self, screen):
        """
        Draw the ice cream to the screen on correct positions.

        Args:
            screen: A display surface created representing the screen of
                the game.
        """
        # Display the ice creams in their positions. The coordinates are
        # adjusted based on the size and the white space of the image.
        for pair in self._icecream_list:
            screen.blit(self._icecream_image, (pair[0] - 45, pair[1] - 62))


if __name__ == '__main__':
    # Start a pygame.
    pygame.init()

    # Set the size of the screen.
    size = (600, 600)

    # Create a model instance.
    model = Model(size)

    # Set title to the window
    pygame.display.set_caption("A Chubby Cat's Adventure")

    running = True

    while running:
        # Call a controller method that checks what the
        # input is and play the game loop.

        model.controller.arrow_keys()
        model.play_loop()

        time.sleep(.01)

    # Close the game if it exits the loop.
    pygame.quit()
