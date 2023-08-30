from settings import Settings
from assets import Assets


class Display:
    """Class for handling drawing objects on the screen"""
    def __init__(self):
        self.settings = Settings()
        self.assets = Assets()

    def draw_python(self, snake: tuple[tuple], head_image):
        """Draw the snake in two pythonic colors"""

        # draw first half blue
        for i in snake[:len(snake)//2]:
            self.settings.screen.blit(
                self.assets.body,
                (i[0] * self.settings.square_size, i[1] * self.settings.square_size,
                 self.settings.square_size * 2, self.settings.square_size * 2))

        # draw second half yellow
        for i in snake[len(snake)//2:]:
            self.settings.screen.blit(self.assets.body_yellow,
                             (i[0] * self.settings.square_size, i[1] * self.settings.square_size,
                              self.settings.square_size * 2, self.settings.square_size * 2))

        # draw the head
        self.settings.screen.blit(head_image,
                                  (snake[0][0] * self.settings.square_size, snake[0][1] * self.settings.square_size,
                                   self.settings.square_size * 2, self.settings.square_size * 2))

    def draw_food(self, food_image, food_pos: tuple, forbidden_food: tuple, score: int, running: bool):
        """Draw food and (if conditions are met) forbidden food at their positions"""

        if running:
            self.settings.screen.blit(food_image,
                                      (food_pos[0] * self.settings.square_size, food_pos[1] * self.settings.square_size,
                                       self.settings.square_size, self.settings.square_size))

            if score and score % 10 == 0:
                self.settings.screen.blit(self.assets.forbidden_food_image,
                                          (forbidden_food[0] * self.settings.square_size,
                                           forbidden_food[1] * self.settings.square_size,
                                           self.settings.square_size, self.settings.square_size))

    def print_texts(self, running: bool, won: bool, score: int):
        """To output text messages on screen"""

        # render all messages
        victory_msg = self.settings.main_font.render('YOU WON!', True, (0, 0, 0))
        static_msg = self.settings.main_font.render('Press ENTER to start or ESC to quit', True, (0, 0, 0))
        score_track = self.settings.main_font.render(f'Score: {score}', True, (0, 0, 0))

        # collect sizes of the messages
        v_width, v_height = self.settings.main_font.size('YOU WON!')
        score_width, score_height = self.settings.main_font.size(f"Score: {score}")
        static_width, static_height = self.settings.main_font.size("Press ENTER to start or ESC to quit")

        # print default message when the game is not running
        if not running:
            self.settings.screen.blit(static_msg,
                                      (self.settings.width // 2 - (static_width // 2),
                                       self.settings.height // 2 - (static_height // 2)))
            # along with the default message, announce that the user has won (if the user won)
            if won:
                self.settings.screen.blit(victory_msg,
                                          (self.settings.width // 2 - v_width // 2,
                                           self.settings.height // 2 - v_height // 2 - static_height * 2))

        else:
            # print user's current score
            self.settings.screen.blit(score_track,
                                      (self.settings.width//2 - (score_width//2), 0))
