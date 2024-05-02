from math import inf

class BatPop(object):

    def __init__(self, function):
        self.bat_pop = []
        self.function = function
        self.average_volume = 0
        self.best_bat_score = inf
        self.best_bat_coordinates = []

    def append_bat(self, bat):
        if bat.score < self.best_bat_score:
            self.best_bat_score = bat.score
            self.best_bat_coordinates = bat.coordinates
        self.bat_pop.append(bat)

    def get_average(self):
        result = 0
        for bat in self.bat_pop:
            result += bat.volume
        return result / len(self.bat_pop)
