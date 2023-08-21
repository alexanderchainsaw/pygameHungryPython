from settings import Settings
from collections import deque


class Snake(Settings):
    """Simple class for creating initial snake"""
    def __init__(self):
        super().__init__()

    def spawn_snake(self):
        snake = deque()
        snake += self.base_snake_position
        return snake

    def manage_direction(self):
        pass





