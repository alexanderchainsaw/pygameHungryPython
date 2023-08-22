from screeninfo import get_monitors
import math


class Configuration:
    """A class to collect user monitor's specs for adjusting the formulas"""
    def __init__(self):

        # Default specs, used if user monitor's specs are not collected
        self.__DEFAULT = (1000, 600)

        self._screen_width, self._screen_height = None, None

        for monitor in get_monitors():
            if monitor.is_primary:
                self._screen_width, self._screen_height = monitor.width, monitor.height
                break

        if not self._screen_width or not self._screen_height:
            self._screen_width, self._screen_height = self.__DEFAULT

        # Initialize configuration variables according to collected data
        self._square_size = math.sqrt(math.sqrt(self._screen_width * self._screen_height))
        self._sqr_x = self._screen_width // self._square_size - 1
        self._sqr_y = self._screen_height // self._square_size - 1

        self._levels = [(), ()]

    def generate_levels(self):
        """Generate obstacle positions for in-game levels according to  collected configuration data"""
        def two():
            pass

        def three():
            pass

        def four():
            pass

        def five():
            pass



