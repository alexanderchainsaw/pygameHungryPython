from base_settings import BaseSettings


class Settings(BaseSettings):
    """A class to store settings and variables"""
    def __init__(self):
        """Gather lower level settings from the parent class"""
        super().__init__()

        # variables to handle in-game scenarios:
        self.running, self.won, self.lost = False, False, False

        # to allow only one movement button press per game tick:
        self.button_pressed = False

