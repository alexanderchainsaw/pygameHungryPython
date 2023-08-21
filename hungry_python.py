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
        self.dir = self.starting_direction

        # 4. Default starting snake
        self.snake = self.spawn_snake()

        # 5. Random food position
        self.food = self.get_food()

    def start(self):
        """Start/restart the game according to current states of the game"""
        if self.lost:
            self.score, self.lvl, self.streak = 0, 0, 0
            self.speed = self.base_speed
        self.won = False
        self.snake = self.spawn_snake()
        self.button_pressed = False
        self.running = True
        # reset head img

    def get_food(self):
        """Create food (x, y) position outside the snake body and obstacles"""
        x = randint(0, self.sqr_x)
        y = randint(0, self.sqr_y)
        while (x, y) in self.snake or (x, y) in self.obstacles:
            x = randint(0, self.sqr_x)
            y = randint(0, self.sqr_y)
        return x, y

    def handle_input(self):
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
                        # change head image
                    elif event.key in (pygame.K_s, pygame.K_DOWN) and not self.dir[1]:
                        self.dir = (0, 1)
                        # change head image
                    elif event.key in (pygame.K_a, pygame.K_LEFT) and not self.dir[0]:
                        self.dir = (-1, 0)
                        # change head image
                    elif event.key in (pygame.K_d, pygame.K_RIGHT) and not self.dir[0]:
                        self.dir = (1, 0)
                        # change head image
                self.button_pressed = True

    def handle_movement(self):
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
                self.eat_food()
            elif next_pos in self.snake or next_pos in self.obstacles:
                self.running = False
                self.lost = True
            else:
                self.snake.appendleft(next_pos), self.snake.pop()

    def eat_food(self):
        """Handle scenarios when the food is eaten:
            1. Increment score
            2. LvlUp if enough points
            3. Increment streak and speed if won"""
        self.score += 1
        if self.score == self.points_for_lvlup:
            self.lvl += 1
            if self.lvl > len(self.levels)-1:
                self.won = True
                self.lvl = 0
            self.running = False
            self.lost = False
            self.score = 0
            # change head
            # this reminds of the start() method, integrate it
        else:
            self.snake.appendleft(self.food), self.snake.pop()
        self.food = self.get_food()



