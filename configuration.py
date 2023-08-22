from screeninfo import get_monitors


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

