import random

from assets import Assets
from settings import Settings, spawn_snake
from random import randint
import pygame
import sys


class HungryPython(Settings):
    """Main class"""
    def __init__(self):
        super().__init__()
        self.assets = Assets()
        # Environment variables to handle in-game scenarios:
        # 1. To check if game has started
        self.running = False

        # 2. To allow only one movement button press per game tick
        self.button_pressed = False

        # 3. Track score
        self.score = 0

        # Other dynamic variables
        # 1. Snake direction to manage movement: (-1, 0), (1, 0), (0, -1), (0, 1) = LEFT, RIGHT, UP, DOWN
        self.dir = self.starting_direction

        # 2. Default starting snake
        self.snake = spawn_snake()

        # 3. Random food position
        self.food = self.get_food()

        # 4. Random food image
        self.food_image = random.choice(self.assets.food_images)

        # 5. Snake head image
        self.head_image = self.assets.head_right

    def start(self):
        """Start/restart the game according to current states of the game"""
        self.score = 0
        self.snake = spawn_snake()
        self.button_pressed = False
        self.running = True
        self.food = self.get_food()
        self.food_image = random.choice(self.assets.food_images)
        self.dir = self.starting_direction
        self.head_image = self.assets.head_right

    def get_food(self):
        """Create food (x, y) position outside the snake body and obstacles"""
        x = randint(0, self.sqr_x)
        y = randint(0, self.sqr_y)
        while (x, y) in self.snake:
            x = randint(0, self.sqr_x)
            y = randint(0, self.sqr_y)
        return x, y

    def _handle_input(self):
        """Handling user inputs"""
        for event in pygame.event.get():

            # Allow user to quit the game whenever
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

                # handle game start
                elif event.key == pygame.K_RETURN and not self.running:
                    self.start()

                # handle direction change according to button presses if the game is running
                elif self.running and not self.button_pressed:

                    if event.key in (pygame.K_w, pygame.K_UP) and not self.dir[1]:
                        self.dir = (0, -1)
                        self.head_image = self.assets.head_up
                    elif event.key in (pygame.K_s, pygame.K_DOWN) and not self.dir[1]:
                        self.dir = (0, 1)
                        self.head_image = self.assets.head_down
                    elif event.key in (pygame.K_a, pygame.K_LEFT) and not self.dir[0]:
                        self.dir = (-1, 0)
                        self.head_image = self.assets.head_left
                    elif event.key in (pygame.K_d, pygame.K_RIGHT) and not self.dir[0]:
                        self.dir = (1, 0)
                        self.head_image = self.assets.head_right
                self.button_pressed = True

    def _handle_movement(self):
        """Method for handling snake movement"""

        def limit(x: int, y: int) -> tuple[int, int]:
            """For limiting values according to width and height,
            which will allow the snake to pass through walls"""
            if x > self.sqr_x:
                x = 0
            elif x < 0:
                x = self.sqr_x
            if y > self.sqr_y:
                y = 0
            elif y < 0:
                y = self.sqr_y
            return x, y

        # Variable to store the next snake position according to the snake's direction
        next_pos = limit(self.snake[0][0] + self.dir[0], self.snake[0][1] + self.dir[1])

        if self.running:
            self.button_pressed = False

            if next_pos == self.food:
                self._eat_food()
            elif next_pos in self.snake:
                self.running = False
            else:
                self.snake.appendleft(next_pos), self.snake.pop()

    def _eat_food(self):
        """Handle scenarios when the food is eaten:"""
        if len(self.snake) == self.sqr_y * self.sqr_x - 1:
            pass
            # TODO: victory scenario
        self.score += 1
        self.snake.appendleft(self.food)
        self.food_image = random.choice(self.assets.food_images)
        self.food = self.get_food()

    def _draw_python(self):
        """To paint the snake in 2 classic Python colors"""

        # painting the body
        for i in self.snake[:len(self.snake)//2]:
            self.screen.blit(self.assets.body,
                             (i[0] * self.square_size, i[1] * self.square_size,
                              self.square_size * 2, self.square_size * 2))
        for i in self.snake[len(self.snake)//2:]:
            self.screen.blit(self.assets.body_yellow,
                             (i[0] * self.square_size, i[1] * self.square_size,
                              self.square_size * 2, self.square_size * 2))
        # painting the head
        self.screen.blit(self.head_image,
                         (self.snake[0][0] * self.square_size, self.snake[0][1] * self.square_size,
                          self.square_size * 2, self.square_size * 2))

    def _draw_food(self):
        if self.running:
            self.screen.blit(self.food_image,
                             (self.food[0] * self.square_size, self.food[1] * self.square_size,
                              self.square_size, self.square_size))

    def main(self):
        while True:
            self.screen.fill((255, 255, 255))
            self._handle_input()
            self._handle_movement()
            self._draw_food()
            self._draw_python()
            pygame.display.update()
            self.clock.tick(self.speed)


if __name__ == "__main__":
    game = HungryPython()
    game.main()



