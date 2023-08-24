import pygame
from collections import deque
import ctypes
import itertools


class Settings:
    """Lower level class to store constant settings"""
    def __init__(self):
        """Collect user's monitor resolution and initialize constant variables"""

        # for matching user's monitor resolution to predefined square sizes
        self._SCREEN_TO_SIZE = {
            (1280, 1024): 64,
            (1366, 768): 40,
            (1600, 900): 50,
            (1920, 1080): 60,
            (1920, 1200): 60,
            (2560, 1440): 80,
            (2752, 1152): 64,
            (3440, 1440): 80,
            (3840, 2160): 120,
        }

        # Default specs, used if user's monitor resolution did not match predefined dictionary
        self.__DEFAULT = (1000, 720, 40)

        # Collect user's monitor resolution
        user32 = ctypes.windll.user32
        self.width = user32.GetSystemMetrics(0)
        self.height = user32.GetSystemMetrics(1)

        try:
            self.square_size = self._SCREEN_TO_SIZE[(self.width, self.height)]
        except KeyError:
            print("[settings.py] - Screen resolution did not match any of the available values, "
                  "switching to default resolution...")
            self.width, self.height, self.square_size = self.__DEFAULT

        # how many squares of playable area in width
        self.sqr_x: int = self.width // self.square_size - 1

        # how many squares of playable area in height
        self.sqr_y: int = self.height // self.square_size - 1

        # snake speed
        self.speed: int = 10

        # Default snake direction to manage movement: (-1, 0), (1, 0), (0, -1), (0, 1) = LEFT, RIGHT, UP, DOWN
        # Has the form of (x, y), which will be added to the current snake position,
        # thus moving it in a certain direction
        self.starting_direction = (1, 0)

        # General initialization of pygame environment
        pygame.init()
        pygame.display.set_caption('Hungry Python')
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))

        # main text font of the game
        self.main_font = pygame.font.Font('AtariClassic-gry3.ttf', self.square_size//2)


class SliceableDeque(deque):
    """For storing the snake and then painting it in two colors (we will need to slice it)"""

    def __getitem__(self, index):
        if isinstance(index, slice):
            return type(self)(itertools.islice(self, index.start,
                                               index.stop, index.step))
        return deque.__getitem__(self, index)


def spawn_snake():
    """Create initial snake body"""
    snake = SliceableDeque()
    snake.append((3, 7))
    snake.append((2, 7))
    snake.append((1, 7))
    return snake




