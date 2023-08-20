from base_settings import BaseSettings
import pygame


class Settings(BaseSettings):
    """A class to store volatile in-game variables and states"""
    def __init__(self):
        """Gather lower level settings from the parent class"""
        super().__init__()

        # Variables to handle in-game scenarios:
        # 1. Overall states of the game
        self.running, self.won, self.lost = False, False, False

        # 2. To allow only one movement button press per game tick
        self.button_pressed = False

        # 3. Level-up related variables
        self.score, self.lvl, self.streak = 0, 0, 0

        # Other variables:
        # 1. Current set of obstacles according to current lvl
        self.obstacles = self.levels[self.lvl]

        # 2. Current speed
        self.speed = self.base_speed

        # 3. Snake direction to manage movement: (-1, 0), (1, 0), (0, -1), (0, 1) = LEFT, RIGHT, UP, DOWN
        self.direction = (1, 0)

    def reset(self):
        """Reset environment according to current states"""
        pass
