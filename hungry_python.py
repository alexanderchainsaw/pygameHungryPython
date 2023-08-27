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
        self.food = self._get_food()

        # 4. Random forbidden food position
        self.forbidden_food = self._get_forbidden_food()

        # 5. Random food image
        self.food_image = random.choice(self.assets.food_images)

        # 6. Snake head image
        self.head_image = self.assets.head_right

        # 7. For printing proper message in case player won
        self.won = False

    def _start(self):
        """Start/restart the game according to current states of the game"""
        self.score = 0
        self.snake = spawn_snake()
        self.button_pressed = False
        self.running = True
        self.food = self._get_food()
        self.food_image = random.choice(self.assets.food_images)
        self.dir = self.starting_direction
        self.head_image = self.assets.head_right
        self.won = False

    def _get_food(self):
        """Create food (x, y) position outside the snake body"""
        x = randint(0, self.sqr_x)
        y = randint(0, self.sqr_y)
        while (x, y) in self.snake:
            x = randint(0, self.sqr_x)
            y = randint(0, self.sqr_y)
        return x, y

    def _get_forbidden_food(self):
        """Create forbidden food (x, y) position outside snake body and regular food"""
        x = randint(0, self.sqr_x)
        y = randint(0, self.sqr_y)
        while (x, y) in self.snake or (x, y) == self.food:
            x = randint(0, self.sqr_x)
            y = randint(0, self.sqr_y)
        return x, y

    def _handle_input(self):
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

    def _eat_food(self):
        """Handle scenarios when the food is eaten:"""

        # check if player won
        if len(self.snake) == self.sqr_y * self.sqr_x - 1:
            self.won = True

        self.score += 1
        self.snake.appendleft(self.food)
        self.food_image = random.choice(self.assets.food_images)
        self.food = self._get_food()

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
        """To paint food images at the food position"""
        if self.running:
            self.screen.blit(self.food_image,
                             (self.food[0] * self.square_size, self.food[1] * self.square_size,
                              self.square_size, self.square_size))

        # Draw forbidden food if score % 5 == 0 and score != 0
            if not self.score % 10 and self.score:
                self.screen.blit(self.assets.forbidden_food_image,
                                 (self.forbidden_food[0] * self.square_size, self.forbidden_food[1] * self.square_size,
                                  self.square_size, self.square_size))

    def _print_text(self):
        """To print messages on screen"""
        self.victory_msg = self.main_font.render('YOU WON!', True, (0, 0, 0))
        self.static_msg = self.main_font.render('Press ENTER to start or ESC to quit', True, (0, 0, 0))
        self.score_track = self.main_font.render(f'Score: {self.score}', True, (0, 0, 0))

        # Collecting sizes of messages to properly display them on the screen
        self.v_width, self.v_height = self.main_font.size('YOU WON!')
        self.score_width, self.score_height = self.main_font.size(f"Score: {self.score}")
        self.static_width, self.static_height = self.main_font.size("Press ENTER to start or ESC to quit")

        if not self.running:
            self.screen.blit(self.static_msg, (self.width//2 - (self.static_width//2),
                                               self.height//2 - (self.static_height//2)))
            if self.won:
                self.screen.blit(self.victory_msg, (self.width//2 - self.v_width//2,
                                 self.height//2 - self.v_height//2 - self.static_height*2))
        else:
            self.screen.blit(self.score_track, (self.width//2 - (self.score_width//2), 0))

    def main(self):
        while True:
            self.screen.fill((255, 255, 255))
            self._handle_input()
            self._handle_movement()
            self._draw_food()
            self._draw_python()
            self._print_text()
            pygame.display.update()
            self.clock.tick(self.speed)


if __name__ == "__main__":
    game = HungryPython()
    game.main()



