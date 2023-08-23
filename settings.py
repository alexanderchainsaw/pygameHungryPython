import pygame
from collections import deque
from configuration import Configuration


class Settings(Configuration):
    """Lower level class to store constant settings"""
    def __init__(self):
        super().__init__()
        """Initialize lower level settings according to inherited configuration data,
        the following settings are not recommended to be altered"""

        # !Changing the following might lead to bugs and unintended behaviour!
        self.width: int = self._screen_width
        self.height: int = self._screen_height
        self.sqr_size: int = self._square_size
        self.sqr_x: int = self._sqr_x  # how many squares of playable area in width
        self.sqr_y: int = self._sqr_y  # how many squares of playable area in height
        self.initial_snake = deque([((3, 7), (2, 7), (1, 7))])  # initial snake body

        # !Changing the following might affect intended game-design rules!
        self.speed: int = 10

        # Default snake direction to manage movement: (-1, 0), (1, 0), (0, -1), (0, 1) = LEFT, RIGHT, UP, DOWN
        # Has the form of (x, y), which will be added to the current snake position,
        # thus moving it in a certain direction
        self.starting_direction = (1, 0)

        # General initialization of pygame environment
        pygame.init()
        pygame.display.set_caption('Hungry Python')
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
