import csv
import os.path
from dataclasses import dataclass, astuple
from datetime import datetime

import global_variables
from global_variables import datetime_format

filename = "saves/top_score.csv"
max_store = 5


@dataclass
class Score:
    datetime: datetime
    nickname: str
    score: int

    def __int__(self):
        return self.score


def get_scores():
    if not os.path.exists(filename):
        clear_scores()
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for line in reader:
            if len(line) >= 3:
                yield Score(datetime.strptime(line[0], datetime_format), line[1], int(line[2]))
            elif global_variables.debug:
                print(f"[WARNING] Can not parse {filename}:{line}")


def clear_scores():
    open(filename, "w", encoding="utf-8").close()


def store_score(score: int, nickname: str):
    if not os.path.exists(filename):
        clear_scores()
    scores = list(get_scores())[:(max_store - 1)]
    scores.append(Score(datetime.today(), nickname, score))
    scores.sort(key=lambda item: item.score, reverse=True)
    # print(scores)
    with open(filename, "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        for date_and_time, nickname, score in [astuple(score) for score in scores]:
            writer.writerow((date_and_time.strftime("%d.%m.%Y %H:%M:%S"), nickname, score))
