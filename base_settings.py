import pygame


class BaseSettings:
    """Lower level class to store basic configuration settings"""
    def __init__(self):
        """Initialize lower level settings for the game"""

        self.width: int = 1000
        self.height: int = 700
        self.sqr_size: int = 40  # 40x40 size of one movement unit
        self.sqr_x: int = self.width // self.sqr_size - 1  # 24 squares in width
        self.sqr_y: int = self.height // self.sqr_size - 1  # 17 squares in height

        self.points_for_lvlup = 10
        self.base_speed = 10
        self.speed_incr = 2

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.levels = ()
