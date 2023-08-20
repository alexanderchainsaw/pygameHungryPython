from settings import Settings
from collections import deque


class Snake:
    def __init__(self):
        self.settings = Settings()
        self.body = self.spawn_snake()

    def spawn_snake(self):
        snake = deque()
        snake += self.settings.base_snake_position
        return snake


