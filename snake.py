import pygame

from settings import Settings
from collections import deque


class Snake(Settings):
    def __init__(self):
        super().__init__()
        self.snake = self.spawn_snake()

    def spawn_snake(self):
        snake = deque()
        snake += self.base_snake_position
        return snake

    def manage_direction(self):
        pass





