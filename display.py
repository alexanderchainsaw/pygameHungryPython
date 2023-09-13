from settings import Settings
from assets import Assets
from collections import deque
from scoring import Score


class Display:
    """Class for handling drawing objects on the screen"""
    def __init__(self):
        self.settings = Settings()
        self.assets = Assets()
        self.scoring = Score()
        self.spacing_h: int = self.settings.height//10
        self.spacing_w: int = self.settings.width//15

    def draw_python(self, snake: deque[tuple], head_image) -> None:
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

    def draw_food(self, food_image, food_pos: tuple, forbidden_food: tuple, score: int, running: bool) -> None:
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

    def print_texts(self, running: bool, won: bool, score: int) -> None:
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
            self._print_score()

        else:
            # print user's current score
            self.settings.screen.blit(score_track,
                                      (self.settings.width//2 - (score_width//2), 0))

    def _print_score(self) -> None:
        """To print score information on main screen"""

        def give_color(s) -> tuple[int, int, int]:
            """Give proper color for displaying session result data
            * If won - give RGB color green
            * If lost - give RGB color red"""
            match s:
                case 'True':
                    return 0, 255, 0
                case 'False':
                    return 255, 0, 0

        if not self.scoring.get_record():
            pass
        else:
            ses_scores, ses_dates, ses_len, ses_results = self.scoring.get_data()

            # render messages
            header_msg = self.settings.main_font.render("Your best result:", True, (100, 100, 100))
            latest_score = self.settings.main_font.render(f"SCORE: {ses_scores[-1]} |", True, (100, 100, 100))
            latest_date = self.settings.main_font.render(f"DATE: {ses_dates[-1]} |", True, (100, 100, 100))
            latest_len = self.settings.main_font.render(f"DURATION: {ses_len[-1]} |", True, (100, 100, 100))
            latest_result = self.settings.main_font.render(f"WON: {ses_results[-1]}", True, give_color(ses_results[0]))

            # collect sizes of messages
            header_w, header_h = self.settings.main_font.size('Your best result:')
            score_w, score_h = self.settings.main_font.size('___')
            date_w, date_h = self.settings.main_font.size('YYYY-MM-DD HH:MM')
            len_w, len_s = self.settings.main_font.size('____')

            self.settings.screen.blit(header_msg,
                                      (self.settings.width // 2 - (header_w // 2),
                                       self.settings.height // 2 + (header_h // 2) + self.spacing_h))
            self.settings.screen.blit(latest_score,
                                      (self.settings.width // 2 - (date_w // 2) - self.spacing_w*4,
                                       self.settings.height // 2 + (date_h // 2) + self.spacing_h*2))
            self.settings.screen.blit(latest_date,
                                      (self.settings.width // 2 - (date_w // 2) - self.spacing_w*2,
                                       self.settings.height // 2 + (date_h // 2) + self.spacing_h * 2))
            self.settings.screen.blit(latest_len,
                                      (self.settings.width // 2 - (date_w // 2) + date_w*0.85,
                                       self.settings.height // 2 + (date_h // 2) + self.spacing_h * 2))
            self.settings.screen.blit(latest_result,
                                      (self.settings.width // 2 - (date_w // 2) + date_w*1.8,
                                       self.settings.height // 2 + (date_h // 2) + self.spacing_h * 2))



