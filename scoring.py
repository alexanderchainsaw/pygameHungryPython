import csv


class Score:
    """
    A class for documenting user's scores over time
    Data will be stored inside 'score.csv' file with rows: score, time, session, won
    * score: int = user's score
    * time: YYYY-MM-DD HH:MM = date when the game was played
    * session: int (seconds) = game duration
    * won: bool = game result (victory=True/defeat=False)
    """
    def __init__(self):
        self.create_if_doesnt_exist()
        self.data: tuple[list, list, list, list] = self.get_data()

    @staticmethod
    def create_if_doesnt_exist() -> None:
        """
        This method is called on class initialization
        to create an empty score.csv file if it doesn't exist
        """
        try:
            with open('score.csv') as _:
                pass
        except FileNotFoundError:
            with open('score.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['score', 'time', 'session', 'won'])
                writer.writeheader()

    @staticmethod
    def get_record() -> int:
        """Get current highest score user has ever reached"""
        with open('score.csv') as file:
            scores = set()
            reader = csv.DictReader(file)
            for row in reader:
                scores.add(int(row['score']))

            return 0 if not scores else max(scores)

    def add_record(self, current_score: int, victory: bool, start_time: str, ses_length: int) -> None:
        """If user has a new record score - this method updates existing csv with new data"""
        score, time, session, won = self.data
        if current_score > self.get_record() or victory:
            with open('score.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['score', 'time', 'session', 'won'])
                writer.writeheader()
                for i in range(len(score)):
                    writer.writerow({'score': score[i], 'time': time[i], 'session': session[i], 'won': won[i]})
                writer.writerow({'score': current_score, 'time': start_time, 'session': ses_length, 'won': victory})

    @staticmethod
    def get_data() -> tuple[list, list, list, list]:
        """Get data from score.csv"""
        score, time, session, won = [], [], [], []
        with open('score.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                score.append(row['score'])
                time.append(row['time'])
                session.append(row['session'])
                won.append(row['won'])
        return score, time, session, won
