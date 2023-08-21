from settings import Settings
from snake import Snake
from random import randint
import pygame
import sys

class HungryPython(Settings, Snake):
    """Main class"""
    def __init__(self):
        super().__init__()

        # Environment variables to handle in-game scenarios:
        # 1. Overall states of the game
        self.running, self.won, self.lost = False, False, False

        # 2. To allow only one movement button press per game tick
        self.button_pressed = False

        # 3. Level-up related variables
        self.score, self.lvl, self.streak = 0, 0, 0

        # Other dynamic variables:
        # 1. Current set of obstacles according to current lvl
        self.obstacles = self.levels[self.lvl]

        # 2. Current speed
        self.speed = self.base_speed

        # 3. Snake direction to manage movement: (-1, 0), (1, 0), (0, -1), (0, 1) = LEFT, RIGHT, UP, DOWN
        self.direction = self.starting_direction

    def reset(self):
        """Reset variables according to current states"""
        pass

    def get_food(self):
        x = randint(0, self.sqr_x)
        y = randint(0, self.sqr_y)
        while (x, y) in self.snake or (x, y) in self.obstacles:
            x = randint(0, self.sqr_x)
            y = randint(0, self.sqr_y)
        return x, y

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_RETURN and not self.running:
                    self.reset()
                elif event.key in (pygame.K_w, pygame.K_UP) and self.running:
                    if not self.button_pressed and not self.direction[1]:
                        self.direction = (0, -1)
                        # change head image
                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    if not self.button_pressed and not self.direction[1]:
                        self.direction = (0, 1)




