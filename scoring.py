import csv


class Score:
    """
    A class for documenting user's scores over time
    Data will be stored inside 'score.csv' file with rows: score, time, won
    """
    def __init__(self):
        self.create_if_not_exists()

    @staticmethod
    def create_if_not_exists() -> None:
        """
        This method is called on class initialization
        to create an empty score.csv file if it doesn't exist
        """
        try:
            with open('score.csv') as _:
                pass
        except FileNotFoundError:
            with open('score.csv', 'w', newline='') as _:
                pass

    @staticmethod
    def get_record():
        """Get current highest score user has reached"""
        with open('score.csv') as f:
            pass

    @staticmethod
    def add_record(score) -> None:
        """If user has a new record score - this method is called"""
        ...

    def get_data(self):
        """Get data from score.csv"""
        ...
