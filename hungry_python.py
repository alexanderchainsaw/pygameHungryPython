import random
from time import localtime, strftime, time
from collections import deque
from assets import Assets
from settings import Settings
from random import randint
import pygame
import sys

from display import Display
from scoring import Score


class HungryPython(Settings):
    """Main class"""
    def __init__(self):
        super().__init__()
        self.assets = Assets()
        self.display = Display()
        # Environment variables to handle in-game scenarios:
        # 1. To check if game has started
        self.running: bool = False

        # 2. To allow only one movement button press per game tick
        self.button_pressed: bool = False

        # 3. Track score
        self.score: int = 0

        # Other dynamic variables
        # 1. Snake direction to manage movement: (-1, 0), (1, 0), (0, -1), (0, 1) = LEFT, RIGHT, UP, DOWN
        self.dir: tuple[int, int] = self.starting_direction

        # 2. Default starting snake
        self.snake: deque[tuple[int, ...]] = self.spawn_snake()

        # 3. Random food position
        self.food: tuple[int, int] = self._get_food()

        # 4. Random forbidden food position
        self.forbidden_food: tuple[int, int] = self._get_forbidden_food()

        # 5. Random food image
        self.food_image = random.choice(self.assets.food_images)

        # 6. Snake head image
        self.head_image = self.assets.head_right

        # 7. For printing proper message in case player won
        self.won: bool = False

        # 8. For recording accurate date and time of each session
        self.start_date_time = None

        # 9. For tracking session length
        self.session_length = None

    def _start(self) -> None:
        """Start/restart the game according to current states of the game"""
        self.start_date_time = None
        self.session_length = None
        self.score = 0
        self.snake = self.spawn_snake()
        self.button_pressed = False
        self.running = True
        self.food = self._get_food()
        self.food_image = random.choice(self.assets.food_images)
        self.dir = self.starting_direction
        self.head_image = self.assets.head_right
        self.won = False

        # Scoring class for storing user's scores over time, will be reinitialized after every loss/win
        self.scoring = Score()

    def _get_food(self) -> tuple[int, int]:
        """Create food (x, y) position outside the snake body"""
        x = randint(0, self.sqr_x)
        y = randint(0, self.sqr_y)
        while (x, y) in self.snake:
            x = randint(0, self.sqr_x)
            y = randint(0, self.sqr_y)
        return x, y

    def _get_forbidden_food(self) -> tuple[int, int]:
        """Create forbidden food (x, y) position outside snake body and regular food"""
        x = randint(0, self.sqr_x)
        y = randint(0, self.sqr_y)
        while (x, y) in self.snake or (x, y) == self.food:
            x = randint(0, self.sqr_x)
            y = randint(0, self.sqr_y)
        return x, y

    def _handle_input(self) -> None:
        """Handling user inputs"""
        for event in pygame.event.get():

            # Allow user to quit the game whenever
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # handle game start
                elif event.key == pygame.K_RETURN and not self.running:
                    self._start()

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

    def _handle_movement(self) -> None:
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

            # Handle eating food
            if next_pos == self.food:
                self._eat_food()

            # Handle snake colliding with itself
            elif next_pos in self.snake:
                self.snake.appendleft(next_pos), self.snake.pop()
                self.running = False

            # Handle eating forbidden food (only appears when score % 10 == 0)
            elif next_pos == self.forbidden_food and not self.score % 10 and self.score:
                self.snake.appendleft(next_pos), self.snake.pop()
                self.running = False

            # Append next square and discard last square to simulate movement
            else:
                self.snake.appendleft(next_pos), self.snake.pop()

    def _eat_food(self) -> None:
        """Handle scenarios when the food is eaten:"""

        # check if player won
        if len(self.snake) == self.sqr_y * self.sqr_x - 1:
            self.won = True

        self.score += 1
        self.snake.appendleft(self.food)
        self.food_image = random.choice(self.assets.food_images)
        self.food = self._get_food()

    def _track_data(self):
        if not self.session_length:
            self.session_length = time()
        if not self.start_date_time and self.running:
            self.start_date_time = strftime("%Y-%m-%d %H:%M", localtime())
        elif self.start_date_time and not self.running:
            self.scoring.add_record(current_score=self.score, victory=self.won, start_time=self.start_date_time,
                                    ses_length=round(time() - self.session_length))

    def run(self) -> None:
        """Main loop"""
        while True:
            self.screen.fill((255, 255, 255))
            self._track_data()
            self._handle_input()
            self._handle_movement()
            self.display.draw_food(self.food_image, self.food, self.forbidden_food, self.score, self.running)
            self.display.draw_python(self.snake, self.head_image)
            self.display.print_texts(self.running, self.won, self.score)
            pygame.display.update()
            self.clock.tick(self.speed)


if __name__ == "__main__":
    game = HungryPython()
    game.run()



