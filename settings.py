import pygame
from collections import deque


class Settings:
    """Lower level class to store constant settings"""
    def __init__(self):
        """Initialize lower level settings for the game which are not to be altered"""

        # !Changing the following might lead to bugs and unintended behaviour!
        self.width: int = 1000
        self.height: int = 700
        self.sqr_size: int = 40  # = 40x40 size of one movement unit
        self.sqr_x: int = int(self.width // self.sqr_size - 1)  # == 24 (25 squares in width)
        self.sqr_y: int = int(self.height // self.sqr_size - 1)  # == 17 (18 squares in height)
        self.base_snake_position = ((3, 7), (2, 7), (1, 7))

        # !Changing the following might affect intended game-design rules!
        self.initial_snake = deque([(3, 7), (2, 7), (1, 7)])
        self.points_for_lvlup: int = 10
        self.base_speed: int = 10
        self.speed_incr: int = 2
        # Default snake direction to manage movement: (-1, 0), (1, 0), (0, -1), (0, 1) = LEFT, RIGHT, UP, DOWN
        # Has the form of (x, y), which will be added to the current snake position,
        # thus moving it in a certain direction
        self.starting_direction = (1, 0)

        # General initialization of pygame environment
        pygame.init()
        pygame.display.set_caption('Hungry Python')
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Tuples of ((x, y), ...) data to be used to generate obstacles for in-game levels
        self.levels: tuple = (
            (),

            ((4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0),
             (11, 0), (12, 0), (13, 0), (14, 0), (15, 0),
             (16, 0), (17, 0), (18, 0), (19, 0), (20, 0),
             (4, 17), (5, 17), (6, 17), (7, 17), (8, 17), (9, 17), (10, 17),
             (11, 17), (12, 17), (13, 17), (14, 17), (15, 17),
             (16, 17), (17, 17), (18, 17), (19, 17), (20, 17),
             (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10),
             (0, 11), (0, 12), (0, 13),
             (24, 4), (24, 5), (24, 6), (24, 7), (24, 8), (24, 9), (24, 10),
             (24, 11), (24, 12), (24, 13)),

            ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0),
             (11, 0), (12, 0), (13, 0), (14, 0), (15, 0), (16, 0), (17, 0), (18, 0), (19, 0), (20, 0),
             (21, 0), (22, 0), (23, 0), (24, 0), (0, 17), (1, 17), (2, 17), (3, 17), (4, 17), (5, 17),
             (6, 17), (7, 17), (8, 17), (9, 17), (10, 17), (11, 17), (12, 17), (13, 17), (14, 17),
             (15, 17), (16, 17), (17, 17), (18, 17), (19, 17), (20, 17), (21, 17), (22, 17), (23, 17),
             (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10),
             (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17), (24, 0), (24, 1), (24, 2),
             (24, 3), (24, 4), (24, 5), (24, 6), (24, 7), (24, 8), (24, 9), (24, 10), (24, 11), (24, 12),
             (24, 13), (24, 14), (24, 15), (24, 16), (24, 17), (24, 18)),

            ((0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8),
             (11, 8), (12, 8), (13, 8), (14, 8), (15, 8), (16, 8), (17, 8), (18, 8), (19, 8), (20, 8),
             (21, 8), (22, 8), (23, 8), (24, 8), (12, 0), (12, 1), (12, 2), (12, 3), (12, 4), (12, 5),
             (12, 6), (12, 7), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15),
             (12, 16), (12, 17)),

            ((0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
             (6, 0), (7, 0), (8, 0), (15, 0), (16, 0), (17, 0), (18, 0), (19, 0), (20, 0), (21, 0), (22, 0),
             (23, 0), (24, 0), (24, 1), (24, 2), (24, 3), (24, 4), (24, 5), (24, 6), (24, 11), (24, 12),
             (24, 13), (24, 14), (24, 15), (24, 16), (24, 17), (23, 17), (22, 17), (21, 17), (20, 17),
             (19, 17), (18, 17), (17, 17), (16, 17), (15, 17), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15),
             (0, 16), (0, 17), (1, 17), (2, 17), (3, 17), (4, 17), (5, 17), (6, 17), (7, 17), (8, 17),
             (5, 6), (6, 6), (7, 6), (8, 6), (8, 5), (8, 4), (8, 3), (15, 6), (16, 6), (17, 6), (18, 6),
             (19, 6), (15, 5), (15, 4), (15, 3), (5, 11), (6, 11), (7, 11), (8, 11), (8, 12), (8, 13), (8, 14),
             (15, 11), (16, 11), (17, 11), (18, 11), (19, 11), (15, 12), (15, 13), (15, 14)),

        )
