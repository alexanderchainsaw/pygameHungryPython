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
