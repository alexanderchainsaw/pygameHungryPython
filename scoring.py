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
    def give_score_data() -> {}:
        """Return data from the score.csv file in dict format"""
        with open('score.csv') as f:
            pass

    @staticmethod
    def update_score_data(score) -> None:
        """Called everytime a game ends to update the top score if user has set a new record"""
        pass
